from dash.dependencies import Input, Output
from cycling.model.frontend.app import app
from cycling.model.frontend.plots.stage import stage_profile_plot, stage_elevation_plot


@app.callback(
    [
        Output("stage_profile", "figure"),
        Output("hidden_data_stage", "value")
    ],
    [
        Input("stage_elevation", "hoverData"),
        Input("stage_select", "value")
    ]
)
def update_stage_profile(hover, selected_stage):
    print(selected_stage)
    if selected_stage:
        stage_profile_figure = stage_profile_plot(selected_stage)
        if hover:
            hover_curve_idx = hover['points'][0]['curveNumber']
            hover_pt_idx = hover['points'][0]['pointIndex']
            data_to_highlight = stage_profile_figure['data'][hover_curve_idx]
            # change the last curve which is reserved for highlight
            stage_profile_figure['data'][-1]['lon'] = [data_to_highlight['lon'][hover_pt_idx]]
            stage_profile_figure['data'][-1]['lat'] = [data_to_highlight['lat'][hover_pt_idx]]
        else:
            stage_profile_figure['data'][-1]['lon'] = []
            stage_profile_figure['data'][-1]['lat'] = []
    return stage_profile_figure, selected_stage


@app.callback(
    Output("stage_elevation", "figure"),
    [
        Input("stage_profile", "hoverData"),
        Input("stage_select", "value")
    ]
)
def update_stage_elevation(hover, selected_stage):
    if selected_stage:
        stage_elevation_figure = stage_elevation_plot(selected_stage)
        if hover:
            hover_curve_idx = hover['points'][0]['curveNumber']
            hover_pt_idx = hover['points'][0]['pointIndex']
            data_to_highlight = stage_elevation_figure['data'][hover_curve_idx]
            # change the last curve which is reserved for highlight
            stage_elevation_figure['data'][-1]['x'] = [data_to_highlight['x'][hover_pt_idx]]
            stage_elevation_figure['data'][-1]['y'] = [data_to_highlight['y'][hover_pt_idx]]
        else:
            stage_elevation_figure['data'][-1]['x'] = []
            stage_elevation_figure['data'][-1]['y'] = []
    return stage_elevation_figure
