import pytest

from cycling.model.core.bike import Bike


@pytest.fixture
def setup_bike():
    name = 'test_bike'
    mass = 0
    cda = 0
    crr = 0
    bike = Bike(name=name, mass=mass, cda=cda, crr=crr)
    return bike


def test_bike_representation(setup_bike):
    assert setup_bike.__repr__() == '<Bike: {}>'.format(setup_bike.name)
