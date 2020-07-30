"""
Raw gyro sensor functions.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input-Raw > Existence
    get_gyro_sensor_exists as exists,
    # Input-Raw > Sensors
    get_raw_gyro_velocity_x as get_x,
    get_raw_gyro_velocity_y as get_y,
    get_raw_gyro_velocity_z as get_z,
)
