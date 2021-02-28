import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

logo_image = '/assets/img/bike.svg'

nav_links = dbc.Row(
    children=[],
    id='nav-items',
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    children=[
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=logo_image, height="30px", className='ml-2'))
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(nav_links, id="navbar-collapse", navbar=True),
    ],
    color='#c0c0c0',#"#7a7a7a"
)

main_layout = html.Div(
    children=[
        dcc.Location(
            id='url',
            refresh=False
        ),
        navbar,
        dbc.Container(
            children=[],
            id='page_content',
            className="mt-4",
        ),
        html.Div(
            id='hidden_data',
            style={'display': 'none'}
        ),
        html.Div(
            id='hidden_data_experiment',
            style={'display': 'none'}
        ),
        html.Div(
            id='hidden_data_merged',
            style={'display': 'none'}
        ),
        html.Div(
            id='hidden_data_stage',
            style={'display': 'none'}
        )
    ]
)
