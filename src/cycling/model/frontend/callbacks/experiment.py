import dash_core_components as dcc
import pandas as pd
import dash_table
from dash_table.Format import Format, Scheme, Symbol
from dash.dependencies import Input, Output, State
from cycling.model.frontend.app import app
from cycling.model.frontend.plots.results import simulation_results_plot
import numpy as np
from cycling.model.core.bike import Bike
from cycling.model.core.environment import Environment
from cycling.model.core.rider import Rider
from cycling.model.core.stage import Stage
from cycling.model.core.simulation import Simulation
from cycling.model.core.critical_power import CriticalPowerModel
from cycling.model.etl.utils import interpolate
from cycling.model.frontend.app import rider_data, bike_data

callback_suffix = 'experiment'


@app.callback(
    Output(f"collapse_bike_{callback_suffix}", "is_open"),
    [Input(f"collapse_button_bike_{callback_suffix}", "n_clicks")],
    [State(f"collapse_bike_{callback_suffix}", "is_open")],
)
def toggle_collapse_bike(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output(f"collapse_{callback_suffix}", "is_open"),
    [Input(f"collapse_button_{callback_suffix}", "n_clicks")],
    [State(f"collapse_{callback_suffix}", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    [
        Output(f"rider_weight_{callback_suffix}", "value"),
        Output(f"rider_cp_{callback_suffix}", "value"),
        Output(f"rider_w_prime_{callback_suffix}", "value")
    ],
    [
        Input(f"rider_select_{callback_suffix}", "value"),
    ],
)
def on_rider_select(rider_name):
    if rider_name in rider_data.keys():
        return rider_data[rider_name].mass, rider_data[rider_name].cp, rider_data[rider_name].w_prime
    else:
        return None, None, None


@app.callback(
    [
        Output(f"bike_weight_{callback_suffix}", "value"),
        Output(f"bike_cda_{callback_suffix}", "value"),
        Output(f"bike_cda_climbing_{callback_suffix}", "value"),
        Output(f"bike_gradient_climbing_{callback_suffix}", "value"),
        Output(f"bike_crr_{callback_suffix}", "value")
    ],
    [
        Input(f"bike_select_{callback_suffix}", "value"),
    ],
)
def on_bike_select(bike_name):
    if bike_name in bike_data.keys():
        return bike_data[bike_name].mass, bike_data[bike_name].cda, bike_data[
            bike_name].cda_climbing, bike_data[bike_name].gradient_climbing, bike_data[bike_name].crr
    else:
        return None, None, None, None, None


@app.callback(
    Output(f"power_target_{callback_suffix}", "value"),
    [
        Input(f"power_select_{callback_suffix}", "value"),
    ],
)
def on_power_select(power_type):
    if power_type == "Constant":
        return 370
    else:
        return None


@app.callback(
    [
        Output("btn_experiment", "disabled"),
        Output("btn_experiment_nestor", "disabled"),
    ],
    [
        Input(f"rider_weight_{callback_suffix}", "value"),
        Input(f"bike_weight_{callback_suffix}", "value"),
        Input(f"bike_cda_{callback_suffix}", "value"),
        Input(f"bike_crr_{callback_suffix}", "value"),
        Input(f"power_target_{callback_suffix}", "value")
    ],
)
def check_validity(*args):
    if all(args):
        return False, False
    return True, True


@app.callback(
    [
        Output("plot_experiment", "children"),
        Output("hidden_data_experiment", "value")
    ],
    [
        Input("btn_experiment", "n_clicks_timestamp")
    ],
    [
        State(f"rider_select_{callback_suffix}", "value"),
        State(f"rider_weight_{callback_suffix}", "value"),
        State(f"rider_cp_{callback_suffix}", "value"),
        State(f"rider_w_prime_{callback_suffix}", "value"),
        State(f"bike_select_{callback_suffix}", "value"),
        State(f"bike_weight_{callback_suffix}", "value"),
        State(f"bike_cda_{callback_suffix}", "value"),
        State(f"bike_cda_climbing_{callback_suffix}", "value"),
        State(f"bike_gradient_climbing_{callback_suffix}", "value"),
        State(f"bike_crr_{callback_suffix}", "value"),
        State(f"power_target_{callback_suffix}", "value"),
        State("experiment_name", "value"),
        State("hidden_data", "value"),
        State("hidden_data_stage", "value")
    ]
)
def generate_experiment(
        n_clicks_time,
        rider_name,
        rider_weight,
        rider_cp,
        rider_w_prime,
        bike_name,
        bike_weight,
        bike_cda,
        bike_cda_climbing,
        bike_gradient_climbing,
        bike_crr,
        power_target,
        experiment_name,
        baseline_data,
        selected_stage):

    # Run simulation
    env = Environment()
    rider = Rider(name=rider_name, mass=rider_weight, cda=0)
    bike = Bike(
        name=bike_name,
        mass=bike_weight,
        cda=bike_cda,
        cda_climb=bike_cda_climbing,
        r_gradient_switch=bike_gradient_climbing /
        100,
        crr=bike_crr)

    stage = Stage(name='Stage', file_name=f'{selected_stage}.csv', s_step=50)
    simulation = Simulation(
        rider=rider,
        bike_1=bike,
        stage=stage,
        environment=env)

    power = power_target * np.ones(len(stage.distance))
    velocity, time, _, _ = simulation.solve_velocity_and_time(
        s=stage.distance, power=power, v0=0.1, t0=0)
    seconds = np.arange(0, int(time[-1] + 1))
    power_per_second = power_target * np.ones(len(seconds))
    cpm = CriticalPowerModel(cp=rider_cp, w_prime=rider_w_prime)
    w_prime_balance_per_second = cpm.w_prime_balance(power=power_per_second)
    w_prime_balance = interpolate(seconds, w_prime_balance_per_second, time)
    experiment_data = dict()
    experiment_data['time'] = time.tolist()
    experiment_data['distance'] = stage.distance.tolist()
    experiment_data['velocity'] = velocity.tolist()
    experiment_data['elevation'] = stage.elevation.tolist()
    experiment_data['w_prime_balance'] = w_prime_balance
    experiment_data['rider_name'] = rider_name
    experiment_data['bike_name'] = bike_name
    experiment_data['experiment_name'] = experiment_name

    figure = simulation_results_plot(baseline_data, experiment_data)
    return dcc.Graph(figure=figure), experiment_data


@app.callback(
    Output('log-table', 'children'),
    [Input("hidden_data", "value"),
     Input("hidden_data_experiment", "value")],
    [State("hidden_data_merged", "value")])
def update_table(baseline_data, experiment_data, data):
    baseline_data = pd.DataFrame(baseline_data)
    baseline_data = baseline_data[[
        'experiment_name', 'rider_name', 'bike_name', 'time', 'w_prime_balance']]

    if data is None:
        data = baseline_data.tail(1)

    if experiment_data is not None:
        experiment_data = pd.DataFrame(experiment_data)
        experiment_data = experiment_data[[
            'experiment_name', 'rider_name', 'bike_name', 'time', 'w_prime_balance']]
        experiment_data = experiment_data.tail(1)
        data = data.append(experiment_data, ignore_index=True)
        baseline_time = data['time'].iloc[0]
        baseline_pb = data['w_prime_balance'].iloc[0]
        style_data_conditional = [
            {
                'if': {
                    'column_id': 'time',
                    'filter_query': '{time} < ' + str(baseline_time)
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'w_prime_balance',
                    'filter_query': '{w_prime_balance} >' + str(baseline_pb)
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'time',
                    'filter_query': '{time} > ' + str(baseline_time)
                },
                'backgroundColor': '#e0001c',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'w_prime_balance',
                    'filter_query': '{w_prime_balance} < ' + str(baseline_pb)
                },
                'backgroundColor': '#e0001c',
                'color': 'white',
            }
        ]
    else:
        style_data_conditional = []

    unit = ['', '', '', u's', u'J']
    table = dash_table.DataTable(
        columns=[{"name": name,
                  "id": name,
                  "type": "numeric",
                  "format": Format(precision=1,
                                   scheme=Scheme.fixed,
                                   symbol=Symbol.yes,
                                   symbol_suffix=u
                                   )
                  } for name, u in zip(data.columns, unit)
                 ],
        data=data.to_dict('records'),
        editable=True,
        style_as_list_view=True,
        style_header={'fontWeight': 'bold'},
        style_data_conditional=style_data_conditional
    )

    return table  # , data TODO: still needs to be fixed
