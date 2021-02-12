import pytest

from cycling.model.core.rider import Rider


@pytest.fixture
def setup_rider():
    name = 'Mikel Landa'
    mass = 70
    cda = 0.2
    cp = 380
    w_prime = 19800
    rider = Rider(name=name, mass=mass, cda=cda, cp=cp, w_prime=w_prime)
    return rider


def test_rider_representation(setup_rider):
    assert setup_rider.__repr__() == '<Rider: {}>'.format(setup_rider.name)
