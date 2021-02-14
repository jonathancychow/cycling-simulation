import numpy as np

from collections import namedtuple
from scipy.signal import butter
from scipy.signal import filtfilt
from scipy.interpolate import interp1d

FilterConfigData = namedtuple('FilterConfigData', ['gain', 'offset', 'frequency'])

elevation_filter_config = FilterConfigData(gain=1, offset=0, frequency=0.005)


def interpolate(x, y, xi):
    y_interp = interp1d(x, y, kind='cubic', fill_value="extrapolate")
    return y_interp(xi)


def low_pass_filter(x, y, xi, s_step, config):
    [b, a] = butter(2, 2 * config.frequency * s_step)
    yi = interpolate(x, y * config.gain + config.offset, xi)
    y_mod = filtfilt(b, a, yi)
    return y_mod


def compute_gradient(x, y):
    return np.gradient(y, x)
