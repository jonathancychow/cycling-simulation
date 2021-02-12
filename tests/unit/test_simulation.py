import pytest
import numpy as np

from cycling.model.core.bike import Bike
from cycling.model.core.rider import Rider
from cycling.model.core.stage import Stage
from cycling.model.core.environment import Environment
from cycling.model.core.simulation import Simulation


@pytest.fixture
def sim_setup():
    bike = Bike(name='test_bike', mass=0, cda=0, crr=0)
    rider = Rider(name='test_rider', mass=70, cda=0.2, cp=380, w_prime=20000)
    stage = Stage(name='default', s_step=50)
    environment = Environment()
    simulation = Simulation(rider=rider, stage=stage, environment=environment, bike_1=bike)
    return simulation


def test_simulation_solve(sim_setup):
    v0 = 0.1
    t0 = 0
    s = sim_setup.stage.distance
    power = 440 * np.ones(len(s))
    velocity, time, _, _= sim_setup.solve_velocity_and_time(s=s, power=power, v0=v0, t0=t0)
    assert len(velocity) == len(s)
    assert len(s) == len(power)
    assert len(power) == len(time)


if __name__ == '__main__':
    pytest.main()
