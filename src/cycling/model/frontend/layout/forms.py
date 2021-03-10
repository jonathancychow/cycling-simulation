import dash_bootstrap_components as dbc
from cycling.model.frontend.app import rider_options, bike_options, power_options
import dash_html_components as html


def rider_data_form(callback_suffix):
    # rider fields
    rider_select = dbc.Select(
        id=f"rider_select_{callback_suffix}",
        options=rider_options,
        value="Sam"
    )
    rider_data = [
        dbc.FormGroup(
            children=[
                dbc.Label("Weight (30 - 100 kg):"),
                dbc.Input(
                    id=f"rider_weight_{callback_suffix}",
                    type="number",
                    min=30,
                    max=100,
                    step=0.1),
            ]),
        dbc.FormGroup(
            children=[
                dbc.Button(
                    "More",
                    id=f"collapse_button_{callback_suffix}",
                    className="mb-3",
                    color="primary",
                ),
                dbc.Collapse(
                    dbc.Card(
                        dbc.FormGroup(
                            children=[
                                dbc.Label("Critical power (W):"),
                                dbc.Input(
                                    id=f"rider_cp_{callback_suffix}",
                                    type="number",
                                    min=50,
                                    max=500,
                                    step=1),
                                html.Div([
                                    html.A('Learn more',
                                           href='https://sporttracks.mobi/blog/critical-power-training',
                                           target='_blank')]),
                                dbc.Label("Anaerobic work capacity - W' (J):"),
                                dbc.Input(
                                    id=f"rider_w_prime_{callback_suffix}",
                                    type="number",
                                    min=10000,
                                    max=30000,
                                    step=10),
                                html.Div([
                                    html.A('Learn more',
                                           href="https://pezcyclingnews.com/toolbox/the-anaerobic-w/",
                                           target='_blank')]),
                            ]),
                    ),
                    id=f"collapse_{callback_suffix}",
                ),
            ]),
    ]
    rider_data_form = dbc.Form(rider_data)

    # bike fields
    def get_bike_select(suffix, transition=False):
        if transition:
            suffix = suffix + '_transition'
        bike_select = dbc.Select(
            id=f"bike_select_{suffix}",
            options=bike_options,
            value="Light Bike"
        )
        return bike_select

    def get_bike_data_form(suffix, transition=False):
        if transition:
            suffix = suffix + '_transition'

        bike_data = [
            dbc.FormGroup(
                children=[
                    dbc.Label("Weight (5 - 20 kg):"),
                    dbc.Input(
                        id=f"bike_weight_{suffix}",
                        type="number",
                        min=5,
                        max=20,
                        step=0.01),
                ]),
            dbc.FormGroup(
                children=[
                    dbc.Button(
                        "More",
                        id=f"collapse_button_bike_{callback_suffix}",
                        className="mb-3",
                        color="primary",
                    ),
                    dbc.Collapse(
                        dbc.Card(
                            dbc.FormGroup(
                                children=[
                                    dbc.Label("Rolling resistance (-):"),
                                    dbc.Input(
                                        id=f"bike_crr_{suffix}",
                                        type="number",
                                        min=0,
                                        max=0.1,
                                        step=0.0001),
                                    html.Div([
                                        html.A('Learn more',
                                                href='https://ridefar.info/bike/cycling-speed/rolling-resistance/',
                                                target='_blank')]),
                                    dbc.Label("Aerodynamics drag - CdA:"),
                                    dbc.Input(
                                        id=f"bike_cda_{suffix}",
                                        type="number",
                                        min=0,
                                        max=1,
                                        step=0.01),
                                    html.Div([
                                        html.A('Learn more',
                                                href='https://notio.ai/blogs/blog/what-is-cda-and-why-is-it-important-as-a-cyclist-to-measure-it',
                                                target='_blank')]),
                                    dbc.Label("Aerodynamics drag at climbing position - CdA:"),
                                    dbc.Input(
                                        id=f"bike_cda_climbing_{suffix}",
                                        type="number",
                                        min=0,
                                        max=1,
                                        step=0.01),
                                    dbc.Label("Climbing position gradient (%):"),
                                    dbc.Input(
                                        id=f"bike_gradient_climbing_{suffix}",
                                        type="number",
                                        min=0,
                                        max=100,
                                        step=0.1),
                                ]),
                        ),
                        id=f"collapse_bike_{callback_suffix}",
                    ),
                ]),
        ]
        return dbc.Form(bike_data)

    # power fields
    power_select = dbc.Select(
        id=f"power_select_{callback_suffix}",
        options=power_options,
        value="Constant"
    )
    power_data = [
        dbc.FormGroup(
            children=[
                dbc.Label("Target power (W):"),
                dbc.Input(
                    id=f"power_target_{callback_suffix}",
                    type="number",
                    min=50,
                    max=800,
                    step=1),
            ])]
    power_data_form = dbc.Form(power_data)

    rider_form = [
        # rider
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Label("Rider:"),
                        rider_select
                    ],
                    md=3
                ),
                dbc.Col(
                    children=[rider_data_form],
                    md=9
                )
            ],
        ),
        # bike
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Label("Bike:"),
                        get_bike_select(callback_suffix)
                    ],
                    md=3
                ),
                dbc.Col(
                    children=[get_bike_data_form(callback_suffix)],
                    md=9
                )
            ],
        ),
        # power
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dbc.Label("Power profile:"),
                        power_select
                    ],
                    md=3
                ),
                dbc.Col(
                    children=[power_data_form],
                    md=9
                )
            ],
        ),
    ]
    return rider_form
