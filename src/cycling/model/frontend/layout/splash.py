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
                "Welcome! A simulation is an experiment done in computer, it could solve complex problems if it is set up correctly, and we could do repeatable controlled experiments in the virtual world.",
                html.Br(),
                html.Br(),
                "Behind the scenes, the computer model solves acceleration by balancing all the forces on the bike, it may takes the computer a few seconds to finish the calculation, just be patient and wait,",
                "it is worth waiting for it as it will take a lot longer if we do those calculations by hand!",
                html.Br(),
                html.Img(src="https://www.harriswestminstersixthform.org.uk/uploads/asset_image/2_259_l.jpg",
                         className="lead",
                         style={'margin-left': 'auto',
                                'margin-right': 'auto',
                                'display': 'block'}
                         ),
                html.Br(),
                "If you are keen to do more experiments, for example make up your own bike or own track, click the following and explore the world of python in Jupyter Notebook.",
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
