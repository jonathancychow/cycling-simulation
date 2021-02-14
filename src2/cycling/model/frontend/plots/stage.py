import plotly.graph_objects as go
from cycling.model.core.stage import Stage
from cycling.model.frontend.app import THEME

if THEME == 'Dark':
    mapbox_style = "carto-darkmatter"
    template = "plotly_dark"
else:
    mapbox_style = "stamen-terrain"
    template = "seaborn"


def stage_profile_plot(selected_stage):
    stage = Stage(name='stage', file_name=f'{selected_stage}.csv')
    data = [
        go.Scattermapbox(
            mode="markers+lines",
            lon=stage.longitude[::10],
            lat=stage.latitude[::10],
            line=dict(color='black'),
            marker=dict(
                color=stage.elevation[::10],
                colorscale='plasma'
            ),
            showlegend=False
        ),
        go.Scattermapbox(
            lon=[],
            lat=[],
            mode='markers',
            name='highlight',
            marker=dict(
                color='white',
                size=10
            ),
            showlegend=False
        )
    ]

    layout = go.Layout(
        mapbox_style=mapbox_style,
        mapbox=dict(zoom=10.7,
                    center=dict(
                        lat=stage.latitude[len(stage.latitude)//2],
                        lon=stage.longitude[len(stage.longitude)//2]),  # zooming on the famous city: Belonchamp
                    ),
        margin=dict(l=20, r=20, t=20, b=20),  # noqa
    )

    return {'data': data, 'layout': layout}


def stage_elevation_plot(selected_stage):
    stage = Stage(name='stage', file_name=f'{selected_stage}.csv')
    data = [
        go.Scatter(
            x=stage.distance[::10],
            y=stage.elevation[::10],
            mode='lines+markers',
            name='elevation',
            marker=dict(
                color='#3553db',
                opacity=0.9,
                size=3
            ),
            line=dict(width=2),
            fill='tozeroy',
            showlegend=False),
        go.Scatter(
            x=[],
            y=[],
            mode='markers',
            name='highlight',
            marker=dict(
                color='white',
                size=10
            ),
            showlegend=False
        )
    ]

    layout = go.Layout(
        autosize=True,
        hovermode="closest",
        template=template,
        margin=dict(l=20, r=20, t=20, b=20),  # noqa
        yaxis_title="elevation (m)",
        xaxis_title="distance (m)",
        height=700 * 0.3,
    )

    return {'data': data, 'layout': layout}
