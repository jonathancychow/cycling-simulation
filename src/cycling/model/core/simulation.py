import logging

import numpy as np
from scipy.integrate import solve_ivp

from cycling.model.etl.utils import interpolate

logger = logging.getLogger()


class Simulation:
    """
    Implementation of an ODE based on Newtons second law. Given power and distance, solve for velocity and time.

    Newtons second law
    dvdt = a = F/m
    dsdt = v

    ODE to solve for velocity and time
    dvds = dvdt * dtds
    dtds = 1 / dsdt

    """

    def __init__(self, rider, stage, environment, bike_1):
        self.rider = rider
        self.bike_1 = bike_1

        self.stage = stage
        self.environment = environment

        self.bike_1_total_mass = self.rider.mass + self.bike_1.mass
        self.bike_1_total_cda = self.rider.cda + self.bike_1.cda
        self.bike_1_total_cda_climb = self.rider.cda + self.bike_1.cda_climb

    def velocity_and_time_ode(self, s, x, power):
        v = x[0]
        p = interpolate(self.stage.distance, power, s)
        fx_tyre = p / v
        r_gradient = interpolate(self.stage.distance, self.stage.gradient, s)

        if r_gradient > self.bike_1.r_gradient_switch:  # FIXME
            logger.debug('Increasing cda: gradient = %s', r_gradient)
            f_drag = 0.5 * self.environment.air_density * self.bike_1_total_cda_climb * v ** 2
        else:
            f_drag = 0.5 * self.environment.air_density * self.bike_1_total_cda * v ** 2

        f_gravity = self.bike_1_total_mass * self.environment.gravity * np.sin(np.arctan(r_gradient))
        f_rolling = (self.bike_1.crr_front * self.bike_1_total_mass / 2
                     + self.bike_1.crr_rear * self.bike_1_total_mass / 2
                     ) * self.environment.gravity * np.cos(np.arctan(r_gradient))
        g_long = 1 / self.bike_1_total_mass * (fx_tyre - f_drag - f_gravity - f_rolling)
        dvds = g_long / v
        dtds = 1 / v
        return np.array([dvds, dtds])

    def solve_velocity_and_time(self, s, power, v0, t0):
        sol = solve_ivp(self.velocity_and_time_ode, t_span=(s[0], s[-1]), y0=np.array([v0, t0]), args=(power,),
                        max_step=100)
        sim_v = interpolate(sol.t, sol.y[0, :], s)
        sim_t = interpolate(sol.t, sol.y[1, :], s)
        return sim_v, sim_t, None, None
