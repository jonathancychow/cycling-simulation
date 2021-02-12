import pytest
import numpy as np
import os

from cycling.model.etl.reader import StageData
from cycling.model.core.stage import Stage


@pytest.fixture
def setup_stage():
    name = 'test_stage'
    file_name = 'test_stage.csv'
    s_step = 10
    stage = Stage(name=name, file_name=file_name, file_path=os.path.dirname(__file__), s_step=s_step)
    return stage


@pytest.fixture
def setup_default():
    name = 'default'
    stage = Stage(name=name)
    return stage


def test_stage_representation(setup_stage):
    assert setup_stage.__repr__() == '<Stage: {} with distance step of {}m>'.format(setup_stage.name,
                                                                                    setup_stage.s_step)


def test_raw_data_properties(setup_stage):
    assert isinstance(setup_stage.raw_data, tuple)
    for field in StageData._fields:
        assert field in setup_stage.raw_data._fields


def test_distance_is_equal_step_size(setup_stage):
    assert np.all(np.diff(setup_stage.distance) == setup_stage.s_step)


def test_attributes_have_equal_length(setup_stage):
    assert len(setup_stage.distance) == len(setup_stage.elevation)
    assert len(setup_stage.elevation) == len(setup_stage.latitude)
    assert len(setup_stage.latitude) == len(setup_stage.longitude)
    assert len(setup_stage.longitude) == len(setup_stage.gradient)


def test_raw_data_properties_default(setup_default):
    assert isinstance(setup_default.raw_data, tuple)
    for field in StageData._fields:
        assert field in setup_default.raw_data._fields


def test_distance_is_equal_step_size_default(setup_default):
    assert np.all(np.diff(setup_default.distance) == setup_default.s_step)


def test_attributes_have_equal_length_default(setup_default):
    assert len(setup_default.distance) == len(setup_default.elevation)
    assert len(setup_default.elevation) == len(setup_default.latitude)
    assert len(setup_default.latitude) == len(setup_default.longitude)
    assert len(setup_default.longitude) == len(setup_default.gradient)


if __name__ == '__main__':
    pytest.main()
