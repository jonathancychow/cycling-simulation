import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

splash_layout =[
    dbc.Jumbotron(
    children=[
        html.H1("Cycling Simulation", className="display-3", style={"text-align": "left"}),
        html.P("Model to simulate performance for cycling time trial", className="lead", style={"text-align": "left"}),
        html.Hr(className="my-2"),

    ]
    ),
    dbc.Row(
        children=[
            dbc.Col(dbc.Button("Get Started!", id="itt", color="primary", size="lg", block=True)),
        ]
    ),
    dbc.Row(
        children=[
            html.Br(),
            html.P([
                "Welcome! A simulation is like running an experiment, but inside a computer program. In a simulation, we can control everything, including the bike and rider we use, and even the weather! With a good setup, it can solve very difficult problems quickly, and we can run it again and again!",
                html.Br(),
                html.Br(),
                "Behind the scenes, the computer model solves acceleration by balancing all the forces on the bike. It may takes the computer a few seconds to finish the calculation, so just be patient and wait. "
                "It is worth waiting as it would take a lot longer if we do these calculations by hand!",
                html.Br(),
                html.Img(src="https://www.harriswestminstersixthform.org.uk/uploads/asset_image/2_259_l.jpg",
                         className="lead",
                         style={'margin-left': 'auto',
                                'margin-right': 'auto',
                                'display': 'block'}
                         ),
                html.Br(),
                "If you are keen to try some advanced features, like customising your own bike or track, click the following and explore the world of Python in a Jupyter Notebook.",
                html.Br()
            ],
                className="lead",
                style={"text-align": "left",
                       'word-wrap': 'break-word',
                       }
            ),
        ]
    ),
    dbc.Row(
        children=[
            dbc.Col(dbc.Button("Advanced - Explore with Python", id="notebook", color="primary", size="lg", block=True,
                               href='https://mybinder.org/v2/gh/jonathancychow/cycling-simulation/main?filepath=notebooks%2Fcycling_simulation.ipynb')),
        ]
    ),
    html.Div(dcc.Markdown('''
            &nbsp;  
            &nbsp;  
            Documention [here](https://github.com/jonathancychow/cycling-simulation)  
            '''),
             style={
                 'textAlign': 'left',
                 'color': '#BEBEBE',
                 'width': '100%',
                 'float': 'center',
                 'display': 'inline-block'}
             )
]
