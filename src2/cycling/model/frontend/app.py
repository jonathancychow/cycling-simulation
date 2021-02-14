import dash

import dash_bootstrap_components as dbc

from collections import namedtuple

THEME = 'Light'
if THEME == 'Dark':
    bootswatch_theme = dbc.themes.DARKLY
else:
    bootswatch_theme = dbc.themes.BOOTSTRAP

# Mock rider database
RiderData = namedtuple(
    'RiderData', [
        'mass', 'cda', 'cp', 'w_prime', 'seat_to_ground'])  # schema
rider_data = {
    "Sam": RiderData(
        mass=64,
        cda=None,
        cp=360,
        w_prime=19800,
        seat_to_ground=1.03)}

# Mock bike database
BikeData = namedtuple('BikeData',
                      ['mass',
                       'cda',
                       'cda_climbing',
                       'gradient_climbing',
                       'crr',
                       'track_mu',
                       'eff_drive'])  # schema
bike_data = {
    "Light Bike": BikeData(
        mass=6.47,
        cda=0.3,
        cda_climbing=0.3,
        gradient_climbing=5,
        crr=0.003,
        track_mu=0.0025,
        eff_drive=0.974),
    "Slim bike": BikeData(
        mass=8.20,
        cda=0.22,
        cda_climbing=0.3,
        gradient_climbing=5,
        crr=0.003,
        track_mu=0.0025,
        eff_drive=0.974)}

rider_options = sorted([{"label": key, "value": key}
                        for key in rider_data.keys()], key=lambda x: x['value'])
bike_options = sorted([{"label": key, "value": key}
                       for key in bike_data.keys()], key=lambda x: x['value'])
power_options = [{"label": "Constant", "value": "Constant"}]

app = dash.Dash(__name__, external_stylesheets=[bootswatch_theme])

app.title = 'Cycling Simulation'

app.config.suppress_callback_exceptions = True

server = app.server
