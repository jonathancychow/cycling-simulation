import dash_core_components as dcc
import dash_bootstrap_components as dbc
from cycling.model.frontend.layout.forms import rider_data_form

callback_suffix = 'baseline'

rider_form = rider_data_form(callback_suffix)
generate_baseline = [
    dbc.Row(
        children=[
            dbc.Col(
                dbc.Button("Let's see how fast you can go!", id="btn_baseline", color="primary", size="lg",
                           block=True, disabled=True),
                md=12
            ),
        ],
        className='mt-3 mb-3'
    ),
    dbc.Row(
        dbc.Col(children=[
            dcc.Loading(id="plot_baseline"),
        ],
            md=12
        )
    ),
    dbc.Row(
        children=[
            dbc.Col(dbc.Button("Go to Experiment", id="btn_to_experiment", color="primary", size="lg", block=True,
                               href="experiment", disabled=True)
                    )
        ],
        className='mt-3 mb-3'),
]

baseline_page_layout = rider_form + generate_baseline
