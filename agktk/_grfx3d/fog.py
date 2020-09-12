# noinspection PyUnresolvedReferences
from appgamekit import (
    # 3D > Fog
    get_fog_mode as _get_fog_mode,
    set_fog_color as set_color,
    set_fog_mode as _set_fog_mode,
    set_fog_range as set_range,
    set_fog_sun_color as set_sun_color,
)


def is_active() -> bool:
    return _get_fog_mode()


def set_active(active: bool = True):
    _set_fog_mode(active)
