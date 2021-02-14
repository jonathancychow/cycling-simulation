import math


class Environment:
    def __init__(self, gravity=9.81, air_density=1.225):
        self.gravity = gravity
        self.air_density = air_density

    def __repr__(self):
        return f'<{self.__class__.__name__}: gravity={self.gravity}, air_density={self.air_density}>'


def compute_air_density(temperature_degc, relative_humidity, air_pressure_mb):
    zero_degc_in_k = 273.15
    temperature_k = temperature_degc + zero_degc_in_k
    eso = 6.11  # saturation vapor pressure at 273.15K (0 degC) [mb]
    lv = 2.5e6  # Latent heat of vaporization [J/kg]
    rv = 461.5  # [J/kg/K]
    rd = 287  # [J/kg-K]

    es = eso * math.exp((lv/rv)*(1/zero_degc_in_k-1/temperature_k))  # saturation vapor pressure [mb]
    e = relative_humidity*es  # vapor pressure [mb]
    q = 0.622*(e/air_pressure_mb)  # specific humidity [-]
    temperature_virtual_k = temperature_k*(1+0.61*q)  # Virtual temperature [K]

    air_pressure_pa = air_pressure_mb * 100  # air pressure [Pa]
    density = air_pressure_pa/(rd*temperature_virtual_k)  # air density [kg/m^3]
    return density
