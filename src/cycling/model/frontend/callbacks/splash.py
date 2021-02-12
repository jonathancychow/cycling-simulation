from dash.dependencies import Input, Output
from cycling.model.frontend.app import app


@app.callback(
    Output('url', 'pathname'),
    [Input('itt', 'n_clicks'),
     ])
def change_page(n_clicks_itt, n_clicks_track=0):  # noqa
    if n_clicks_itt:
        return '/stage'
    elif n_clicks_track:
        return '/track'
