import dash_html_components as html
import dash_bootstrap_components as dbc

splash_layout = dbc.Jumbotron(
    children=[
        html.H1("Cycling Simulation", className="display-3", style={"text-align": "center"}),
        html.P("Motion and Forces", className="lead", style={"text-align": "center"}),
        html.Hr(className="my-2"),
        dbc.Row(
            children=[
                dbc.Col(dbc.Button("See how fast you can go!", id="itt", color="primary", size="lg", block=True)),
                # dbc.Col(dbc.Button("CdA Calculator", id="track", color="primary", size="lg", block=True))
            ]
        )
    ]
)
