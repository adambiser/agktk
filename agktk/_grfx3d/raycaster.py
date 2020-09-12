# Note:
#   object_ray_cast, object_sphere_cast, and object_sphere_slide return the ID of the hit object when performed against
#   all objects.  When a specific object ID is passed into the method, the return value acts as a boolean instead.
# Also:
#   The methods with an index parameter should only have a value > 0 when object_sphere_slide is used.
#   Only index 0 need be checked when using object_ray_cast or object_sphere_cast.

from appgamekit import (
    # 3D > Objects
    get_object_ray_cast_bounce_x as _get_object_ray_cast_bounce_x,
    get_object_ray_cast_bounce_y as _get_object_ray_cast_bounce_y,
    get_object_ray_cast_bounce_z as _get_object_ray_cast_bounce_z,
    get_object_ray_cast_distance as _get_object_ray_cast_distance,
    get_object_ray_cast_hit_id as _get_object_ray_cast_hit_id,
    get_object_ray_cast_normal_x as _get_object_ray_cast_normal_x,
    get_object_ray_cast_normal_y as _get_object_ray_cast_normal_y,
    get_object_ray_cast_normal_z as _get_object_ray_cast_normal_z,
    get_object_ray_cast_num_hits as _get_object_ray_cast_num_hits,
    get_object_ray_cast_slide_x as _get_object_ray_cast_slide_x,
    get_object_ray_cast_slide_y as _get_object_ray_cast_slide_y,
    get_object_ray_cast_slide_z as _get_object_ray_cast_slide_z,
    get_object_ray_cast_x as _get_object_ray_cast_x,
    get_object_ray_cast_y as _get_object_ray_cast_y,
    get_object_ray_cast_z as _get_object_ray_cast_z,
    object_ray_cast as _object_ray_cast,
    object_sphere_cast as _object_sphere_cast,
    object_sphere_slide as _object_sphere_slide,
)
from .object3d import Object3D
from typing import Tuple, Union


def cast(start_x: float, start_y: float, start_z: float,
         end_x: float, end_y: float, end_z: float, radius: float = 0) -> Union[Object3D, None]:
    """
    Casts a ray from the starting point to the ending point to find the first object hit.
    When a radius is given, sphere casting is used.

    :param float start_x: The X component of the start position.
    :param float start_y: The Y component of the start position.
    :param float start_z: The Z component of the start position.
    :param float end_x: The X component of the end position.
    :param float end_y: The Y component of the end position.
    :param float end_z: The Z component of the end position.
    :param float radius: The radius of the sphere to cast when sphere casting.
    :return: The object hit, or None.
    """
    if radius > 0:
        object_id = _object_sphere_cast(0, start_x, start_y, start_z, end_x, end_y, end_z, radius)
    else:
        object_id = _object_ray_cast(0, start_x, start_y, start_z, end_x, end_y, end_z)
    # noinspection PyProtectedMember
    return Object3D._from_id(object_id)


def intersects(test_object: Object3D,
               start_x: float, start_y: float, start_z: float,
               end_x: float, end_y: float, end_z: float, radius: float = 0) -> bool:
    """
    Tests whether a ray from the starting point to the ending point intersects the given object.
    When a radius is given, sphere casting is used.

    :param test_object: The object to test for intersection.
    :param float start_x: The X component of the start position.
    :param float start_y: The Y component of the start position.
    :param float start_z: The Z component of the start position.
    :param float end_x: The X component of the end position.
    :param float end_y: The Y component of the end position.
    :param float end_z: The Z component of the end position.
    :param float radius: The radius of the sphere to cast when sphere casting.
    :return: True when the ray intersects `test_object`; otherwise, False.
    """
    if radius > 0:
        result = _object_sphere_cast(test_object.id, start_x, start_y, start_z, end_x, end_y, end_z, radius)
    else:
        result = _object_ray_cast(test_object.id, start_x, start_y, start_z, end_x, end_y, end_z)
    return bool(result)


def slide_cast(start_x: float, start_y: float, start_z: float,
               end_x: float, end_y: float, end_z: float, radius: float) -> Union[Object3D, None]:
    """
    Performs sphere sliding from the starting point to the ending point to find the slide position.

    :param float start_x: The X component of the start position.
    :param float start_y: The Y component of the start position.
    :param float start_z: The Z component of the start position.
    :param float end_x: The X component of the end position.
    :param float end_y: The Y component of the end position.
    :param float end_z: The Z component of the end position.
    :param float radius: The radius of the sphere to cast.
    :return: The object hit, or None.
    """
    object_id = _object_sphere_slide(0, start_x, start_y, start_z, end_x, end_y, end_z, radius)
    # noinspection PyProtectedMember
    return Object3D._from_id(object_id)


def slide_against(test_object: Object3D,
                  start_x: float, start_y: float, start_z: float,
                  end_x: float, end_y: float, end_z: float, radius: float) -> bool:
    """
    Performs sphere sliding from the starting point to the ending point to find the slide position against the given
    object.

    :param Object3D test_object: The object to slide against.
    :param float start_x: The X component of the start position.
    :param float start_y: The Y component of the start position.
    :param float start_z: The Z component of the start position.
    :param float end_x: The X component of the end position.
    :param float end_y: The Y component of the end position.
    :param float end_z: The Z component of the end position.
    :param float radius: The radius of the sphere to cast.
    :return: True when the ray intersects `test_object`; otherwise, False.
    """
    return bool(_object_sphere_slide(test_object.id, start_x, start_y, start_z, end_x, end_y, end_z, radius))


def get_hit_count() -> int:
    return _get_object_ray_cast_num_hits()


def get_distance(index: int = 0) -> float:
    return _get_object_ray_cast_distance(index)


def get_hit_object(index: int = 0) -> Object3D:
    # noinspection PyProtectedMember
    return Object3D._from_id(_get_object_ray_cast_hit_id(index))


def get_hit_x(index: int = 0) -> float:
    return _get_object_ray_cast_x(index)


def get_hit_y(index: int = 0) -> float:
    return _get_object_ray_cast_y(index)


def get_hit_z(index: int = 0) -> float:
    return _get_object_ray_cast_z(index)


def get_hit_position(index: int = 0) -> Tuple[float, float, float]:
    return _get_object_ray_cast_x(index), _get_object_ray_cast_y(index), _get_object_ray_cast_z(index)


def get_normal_x(index: int = 0) -> float:
    return _get_object_ray_cast_normal_x(index)


def get_normal_y(index: int = 0) -> float:
    return _get_object_ray_cast_normal_y(index)


def get_normal_z(index: int = 0) -> float:
    return _get_object_ray_cast_normal_z(index)


def get_normal(index: int = 0) -> Tuple[float, float, float]:
    return _get_object_ray_cast_normal_x(index), \
           _get_object_ray_cast_normal_y(index), \
           _get_object_ray_cast_normal_z(index)


def get_bounce_x(index: int = 0) -> float:
    return _get_object_ray_cast_bounce_x(index)


def get_bounce_y(index: int = 0) -> float:
    return _get_object_ray_cast_bounce_y(index)


def get_bounce_z(index: int = 0) -> float:
    return _get_object_ray_cast_bounce_z(index)


def get_bounce_position(index: int = 0) -> Tuple[float, float, float]:
    return _get_object_ray_cast_bounce_x(index), \
           _get_object_ray_cast_bounce_y(index), \
           _get_object_ray_cast_bounce_z(index)


def get_slide_x(index: int = 0) -> float:
    return _get_object_ray_cast_slide_x(index)


def get_slide_y(index: int = 0) -> float:
    return _get_object_ray_cast_slide_y(index)


def get_slide_z(index: int = 0) -> float:
    return _get_object_ray_cast_slide_z(index)


def get_slide_position(index: int = 0) -> Tuple[float, float, float]:
    return _get_object_ray_cast_slide_x(index), \
           _get_object_ray_cast_slide_y(index), \
           _get_object_ray_cast_slide_z(index)
