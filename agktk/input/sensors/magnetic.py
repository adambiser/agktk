"""
Raw magnetic sensor functions.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input-Raw > Existence
    get_magnetic_sensor_exists as exists,
    # Input-Raw > Sensors
    get_raw_magnetic_x as get_x,
    get_raw_magnetic_y as get_y,
    get_raw_magnetic_z as get_z,
)
