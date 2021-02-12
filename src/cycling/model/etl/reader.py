import os
import pandas as pd

from collections import namedtuple

data_root = os.path.join(os.path.dirname(__file__), '..', 'data')
StageData = namedtuple('StageData', ['latitude', 'longitude', 'elevation', 'distance'])


def read_csv(file_path, file_name):
    if file_path:
        data = pd.read_csv(os.path.join(file_path, file_name))
    else:
        data = pd.read_csv(os.path.join(data_root, file_name))
    return StageData(latitude=data.latitude.values,
                     longitude=data.longitude.values,
                     distance=data.distance.values,
                     elevation=data.elevation.values)
