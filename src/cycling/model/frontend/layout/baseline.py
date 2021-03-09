import dash_core_components as dcc
import dash_bootstrap_components as dbc
from cycling.model.frontend.layout.forms import rider_data_form
import dash_html_components as html

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
header = [
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Label("Step 2 - Configure you bike and rider ", className="bold"),
                    html.P("Click on 'More' to see more variables you could change. "
                           "Once you have generated a baseline, click on 'Go to Experiment'.", className="lead"),
                ],
                width="auto",
            ),
        ],
        className='mb-3'
    ),
]

baseline_page_layout = header + rider_form + generate_baseline
