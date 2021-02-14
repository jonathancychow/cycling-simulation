import numpy as np
from cycling.model.etl.reader import read_csv, StageData
from cycling.model.etl.utils import interpolate, low_pass_filter, compute_gradient, elevation_filter_config


class Stage:
    def __init__(self, name, file_name=None, file_path=None, s_step=5, s_switchover=1e6):
        self.name = name
        self.s_step = s_step
        if file_name:
            if file_name.split('.')[1] == 'csv':
                stage_data = read_csv(file_path, file_name)
            else:
                raise NotImplementedError
        else:
            # default track
            distance = np.arange(0, 55000, s_step)
            elevation_gain = 0
            elevation = np.linspace(0, elevation_gain, len(distance))
            latitude = np.linspace(0, 0, len(distance))
            longitude = np.linspace(0, 0, len(distance))
            stage_data = StageData(latitude=latitude,
                                   longitude=longitude,
                                   distance=distance,
                                   elevation=elevation)

        self.raw_data = stage_data
        self.distance = np.arange(stage_data.distance[0], stage_data.distance[-1], s_step)
        self.elevation = low_pass_filter(stage_data.distance, stage_data.elevation, self.distance, s_step,
                                         config=elevation_filter_config)
        self.latitude = interpolate(stage_data.distance, stage_data.latitude, self.distance)
        self.longitude = interpolate(stage_data.distance, stage_data.longitude, self.distance)
        self.gradient = compute_gradient(self.distance, self.elevation)

        self.s_switchover = s_switchover

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.name} with distance step of {self.s_step}m>'
