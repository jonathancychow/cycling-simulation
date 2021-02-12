import datetime
from plotly.subplots import make_subplots
import plotly.graph_objects as go

experiment_color = '#28A745'


def simulation_results_plot(baseline_data, experiment_data=None):
    baseline_race_time = str(datetime.timedelta(seconds=baseline_data['time'][-1])).split('.')[0]
    figure = make_subplots(rows=3, cols=1,
                           shared_xaxes=True,
                           vertical_spacing=0.02,
                           row_heights=[0.2, 0.6, 0.2])
    figure.add_trace(
        go.Scatter(x=baseline_data['distance'], y=baseline_data['elevation'], fill='tozeroy', showlegend=False), row=1,
        col=1)
    figure.add_trace(go.Scatter(x=baseline_data['distance'], y=baseline_data['velocity'],
                                name="Baseline: {}".format(baseline_race_time),
                                opacity=0.5, line={'color': '#e31d1a'}),
                     row=2, col=1)
    figure.add_trace(
        go.Scatter(x=baseline_data['distance'], y=baseline_data['w_prime_balance'], opacity=0.5,
                   line={'color': '#e31d1a'},
                   showlegend=False),
        row=3, col=1)
    max_w_prime = max(baseline_data['w_prime_balance'])
    min_w_prime = min(baseline_data['w_prime_balance'])
    if experiment_data:
        experiment_race_time = str(datetime.timedelta(seconds=experiment_data['time'][-1])).split('.')[0]
        figure.add_trace(go.Scatter(x=experiment_data['distance'], y=experiment_data['velocity'],
                                    name="Experiment: {}".format(experiment_race_time), opacity=0.5,
                                    line={'color': experiment_color}),
                         row=2, col=1)
        figure.add_trace(
            go.Scatter(x=experiment_data['distance'], y=experiment_data['w_prime_balance'], opacity=0.5,
                       line={'color': experiment_color},
                       showlegend=False), row=3, col=1)

        max_w_prime = max(max_w_prime, max(experiment_data['w_prime_balance']))
        min_w_prime = min(min_w_prime, min(experiment_data['w_prime_balance']))

    figure.update_yaxes(title_text="elevation (m)", row=1, col=1)
    figure.update_xaxes(title_text="distance (m)", row=3, col=1)
    figure.update_yaxes(title_text="velocity (m/s)", row=2, col=1)
    figure.update_yaxes(title_text="W' balance (J)", range=[min(0, min_w_prime) - 1000, max_w_prime + 1000], row=3,
                        col=1)
    figure.update_layout(height=700)

    return figure
