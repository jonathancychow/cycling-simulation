import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from cycling.model.frontend.app import app
from cycling.model.frontend.layout.main import main_layout
from cycling.model.frontend.layout.splash import splash_layout
from cycling.model.frontend.layout.baseline import baseline_page_layout
from cycling.model.frontend.layout.stage import stage_page_layout
from cycling.model.frontend.layout.experiment import experiment_page_layout
from cycling.model.frontend.callbacks import splash  # noqa
from cycling.model.frontend.callbacks import stage  # noqa
from cycling.model.frontend.callbacks import baseline  # noqa
from cycling.model.frontend.callbacks import experiment  # noqa

app.layout = main_layout
server = app.server

# update page based on url
@app.callback(
    Output('page_content', 'children'),
    [Input('url', 'pathname')])
def display_page(pathname):  # noqa
    if pathname == '/':
        return splash_layout
    elif pathname == '/stage':
        return stage_page_layout
    elif pathname == '/baseline':
        return baseline_page_layout
    elif pathname == '/experiment':
        return experiment_page_layout


# update navbar items based on page
@app.callback(
    Output('nav-items', 'children'),
    [Input('url', 'pathname')])
def change_navbar(pathname):  # noqa
    if pathname == '/stage':
        navbar_items = [
            dbc.Col(
                dbc.NavLink(
                    "Stage",
                    id='stage-link',
                    href="stage",
                    className='nav_link active')),
            dbc.Col(
                dbc.NavLink(
                    "Baseline",
                    id='baseline-link',
                    href="baseline",
                    className='nav_link')),
        ]
    elif pathname == '/baseline':
        navbar_items = [
            dbc.Col(
                dbc.NavLink(
                    "Stage",
                    id='stage-link',
                    href="stage",
                    className='nav_link')),
            dbc.Col(
                dbc.NavLink(
                    "Baseline",
                    id='baseline-link',
                    href="baseline",
                    className='nav_link active')),
        ]
    elif pathname == '/experiment':
        navbar_items = [
            dbc.Col(
                dbc.NavLink(
                    "Stage",
                    id='stage-link',
                    href="stage",
                    className='nav_link')),
            dbc.Col(
                dbc.NavLink(
                    "Baseline",
                    id='baseline-link',
                    href="baseline",
                    className='nav_link')),
            dbc.Col(
                dbc.NavLink(
                    "Experiment",
                    id='experiment-link',
                    href="experiment",
                    className='nav_link active')),
        ]
    else:
        navbar_items = []
    return navbar_items


# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=True, port=8055)
