import pytest

from cycling.model.core.environment import Environment, compute_air_density


@pytest.fixture
def setup_env():
    gravity = 10
    air_density = 1.2
    env = Environment(gravity=gravity, air_density=air_density)
    return env


def test_env_representation(setup_env):
    assert setup_env.__repr__() == '<Environment: gravity={}, air_density={}>'.format(setup_env.gravity,
                                                                                      setup_env.air_density)


def test_env_defaults():
    env = Environment()
    assert env.__repr__() == '<Environment: gravity={}, air_density={}>'.format(env.gravity,
                                                                                env.air_density)


def test_compute_air_density():
    air_density = compute_air_density(temperature_degc=20.2,
                                      relative_humidity=.684,
                                      air_pressure_mb=1002)
    exp_air_density = 1.18281045779043

    assert abs(air_density - exp_air_density) <= 1e-14
