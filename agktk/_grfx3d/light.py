# noinspection PyUnresolvedReferences
from appgamekit import (
    # clear_point_lights,  # Not needed
    create_point_light as _create_point_light,
    delete_point_light as _delete_point_light,
    # get_point_light_exists,  # Not needed
    set_ambient_color,
    set_point_light_color as _set_point_light_color,
    set_point_light_mode as _set_point_light_mode,
    set_point_light_position as _set_point_light_position,
    set_point_light_radius as _set_point_light_radius,
    set_sun_active,
    set_sun_color,
    set_sun_direction,
)
from .._enums import PointLightMode
from .._utils import iter_id as _iter_id


class PointLight(object):
    """
    Wraps AppGameKit point light methods.
    """
    __iter_id = _iter_id(1)

    def __init__(self, x: float, y: float, z: float, radius: float, red: int, green: int, blue: int):
        _id = next(PointLight.__iter_id)
        self.__id = _id
        _create_point_light(_id, x, y, z, radius, red, green, blue)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_point_light(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def set_color(self, red: int, green: int, blue: int):
        _set_point_light_color(self.__id, red, green, blue)

    def set_mode(self, mode: PointLightMode):
        _set_point_light_mode(self.__id, mode)

    def set_position(self, x: float, y: float, z: float):
        _set_point_light_position(self.__id, x, y, z)

    def set_radius(self, radius: float):
        _set_point_light_radius(self.__id, radius)
