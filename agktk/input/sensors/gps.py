"""
Raw gps sensor functions.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input-Raw > Existence
    get_gps_sensor_exists as exists,
    # Input-Raw > Sensors
    get_raw_gps_altitude as get_altitude,
    get_raw_gps_latitude as get_latitude,
    get_raw_gps_longitude as get_longitude,
    start_gps_tracking as start_tracking,
    stop_gps_tracking as stop_tracking,
)
