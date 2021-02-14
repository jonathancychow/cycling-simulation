import dash_core_components as dcc
import dash_bootstrap_components as dbc

stage_option = [{"label": "Tour-de-France-2020---Stage-20-ITT", "value": "Tour-de-France-2020---Stage-20-ITT"},
                {"label": "Vuelta-España-2020---Stage-13", "value": "Vuelta-España-2020---Stage-13"}]

stage_page_layout = [
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Label("Stage:", className="bold"),
                    dbc.Select(
                        id="stage_select",
                        options=stage_option,
                        value="Tour-de-France-2020---Stage-20-ITT"
                    )
                ],
                width="auto",
            ),
        ],
        className='mb-3'
    ),
    dbc.Row([
        dbc.Col(
            [
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(
                            id='stage_elevation',
                            hoverData=None,
                            clear_on_unhover=True
                        )
                    ),
                ),
                dbc.Row(
                    dbc.Col(
                        dcc.Graph(
                            id='stage_profile',
                            hoverData=None,
                            clear_on_unhover=True
                        )
                    )
                )
            ]
        ),
    ]
    ),
    dbc.Row(
        children=[
            dbc.Col(dbc.Button("Go to Baseline", id="btn_to_baseline", color="primary", size="lg", block=True,
                               href="baseline")
                    )
        ],
        className='mt-3 mb-3'),
]
