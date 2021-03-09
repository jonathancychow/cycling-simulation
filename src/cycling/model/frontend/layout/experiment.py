import dash_core_components as dcc
import dash_bootstrap_components as dbc
from cycling.model.frontend.layout.forms import rider_data_form
import dash_html_components as html

table = None

callback_suffix = 'experiment'

rider_form = rider_data_form(callback_suffix)

experiment_naming = [
    dbc.FormGroup(
        children=[
            dbc.Label("Experiment name:"),
            dbc.Input(id="experiment_name", placeholder="Give your experiment a name...")
        ]
    )
]

generate_experiment = [
    dbc.Row(
        children=[
            dbc.Col(
                dbc.Button("Generate experiment", id="btn_experiment", color="primary", size="lg",
                           block=True, disabled=True),
                md=12
            )

        ], className='mt-3 mb-3'
    ),
    dbc.Row(
        dbc.Col(
            html.Div(
                id='log-table',
                style={'margin': '10px'}
            ),
            md=12
        )
    ),
    dbc.Row(
        dbc.Col(
            children=[
                dcc.Loading(id="plot_experiment")
            ],
            md=12
        ),
    )

]

header = [
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Label("Step 3 - Change a variable ", className="bold"),
                    html.P("Change a variable, click on 'Generate experiment' and see if the result changes. "
                           "If so, by how much? Is it expected? ", className="lead"),
                ],
                width="auto",
            ),
        ],
        className='mb-3'
    ),
]

experiment_page_layout = header + experiment_naming + rider_form + generate_experiment
