from appgamekit import (
    # 3DPhysics > RayCast
    create_3d_physics_ray as _create_3d_physics_ray,
    delete_3d_physics_ray as _delete_3d_physics_ray,
    get_3d_physics_ray_cast_closest_contact_position as _get_3d_physics_ray_cast_closest_contact_position,
    get_3d_physics_ray_cast_closest_object_hit as _get_3d_physics_ray_cast_closest_object_hit,
    get_3d_physics_ray_cast_contact_position as _get_3d_physics_ray_cast_contact_position,
    get_3d_physics_ray_cast_fraction as _get_3d_physics_ray_cast_fraction,
    get_3d_physics_ray_cast_normal_vector as _get_3d_physics_ray_cast_normal_vector,
    get_3d_physics_ray_cast_num_hits as _get_3d_physics_ray_cast_num_hits,
    get_3d_physics_ray_cast_object_hit as _get_3d_physics_ray_cast_object_hit,
    # ray_3d_physics_exist,  # Not needed.
    ray_cast_3d_physics as _ray_cast_3d_physics,
    ray_cast_3d_physics_object as _ray_cast_3d_physics_object,
    sphere_cast_3d_physics as _sphere_cast_3d_physics,
    sphere_cast_3d_physics_object as _sphere_cast_3d_physics_object,
)
from .._grfx3d import Object3D
from .. import Vector3
from .._enums import RayCastMode
from typing import Tuple


class Ray(object):
    def __init__(self):
        self.__id = _create_3d_physics_ray()

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_3d_physics_ray(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def get_closest_contact_position(self, out_vector: Vector3) -> bool:
        return _get_3d_physics_ray_cast_closest_contact_position(self.__id, out_vector.id)

    @property
    def closest_object_hit(self) -> Object3D:
        # noinspection PyProtectedMember
        return Object3D._from_id(_get_3d_physics_ray_cast_closest_object_hit(self.__id))

    def closest_contact_fraction(self) -> float:
        return _get_3d_physics_ray_cast_fraction(self.__id)

    def get_normal_vector(self, out_vector: Vector3):
        _get_3d_physics_ray_cast_normal_vector(self.__id, out_vector.id)

    # @property
    # def contact_count(self) -> int:
    #     return _get_3d_physics_ray_cast_num_hits(self.__id)
    #
    # def get_contact_position(self, hit_index: int, out_vector: Vector3) -> bool:
    #     return _get_3d_physics_ray_cast_contact_position(self.__id, hit_index, out_vector.id)
    #
    # def get_contact_object(self, hit_index: int) -> Object3D:
    #     # noinspection PyProtectedMember
    #     return Object3D._from_id(_get_3d_physics_ray_cast_object_hit(self.__id, hit_index))

    def contacts(self):
        _id = self.__id
        temp_vector = Vector3()
        for index in range(_get_3d_physics_ray_cast_num_hits(_id)):
            # Note: There's no bounds checking in get_3d_physics_ray_cast_contact_position.
            #   As long as the object and vector ids are valid, it returns True even if the fraction_index is invalid.
            _get_3d_physics_ray_cast_contact_position(self.__id, index, temp_vector.id)
            # noinspection PyProtectedMember
            obj = Object3D._from_id(_get_3d_physics_ray_cast_object_hit(self.__id, index))
            yield (temp_vector.x, temp_vector.y, temp_vector.z), obj


def vector_cast(from_vector: Vector3, to_vector: Vector3,
                mode: RayCastMode = RayCastMode.CLOSEST, radius: float = 0) -> Ray:
    """
    Casts a ray from the starting point to the ending point to determine contacts.
    When a radius is given, sphere casting is used.

    :param from_vector: The starting vector.
    :param to_vector: The ending vector
    :param mode: The ray cast mode.
    :param radius: When > 0, sphere casting is used and the ray cast mode is always CLOSEST.
    :return: The ray result.
    """
    ray = Ray()
    if radius > 0:
        _sphere_cast_3d_physics(ray.id, from_vector.id, to_vector.id, radius)
    else:
        _ray_cast_3d_physics(ray.id, from_vector.id, to_vector.id, mode)
    return ray


def cast(from_xyz: Tuple[float, float, float], to_xyz: Tuple[float, float, float],
         mode: RayCastMode = RayCastMode.CLOSEST, radius: float = 0) -> Ray:
    return vector_cast(Vector3(*from_xyz), Vector3(*to_xyz), mode, radius)


def vector_intersects(test_object: Object3D, from_vector: Vector3, to_vector: Vector3,
                      mode: RayCastMode = RayCastMode.CLOSEST, radius: float = 0) -> Ray:
    """
    Tests whether a ray from the starting point to the ending point intersects the given object.
    When a radius is given, sphere casting is used.

    :param test_object: The object to test for intersection.
    :param from_vector: The starting vector.
    :param to_vector: The ending vector
    :param mode: The ray cast mode.
    :param radius: When > 0, sphere casting is used and the ray cast mode is always CLOSEST.
    :return: The ray result.
    """
    ray = Ray()
    if radius > 0:
        _sphere_cast_3d_physics_object(test_object.id, ray.id, from_vector.id, to_vector.id, radius)
    else:
        _ray_cast_3d_physics_object(test_object.id, ray.id, from_vector.id, to_vector.id, mode)
    return ray


def intersects(test_object: Object3D, from_xyz: Tuple[float, float, float], to_xyz: Tuple[float, float, float],
               mode: RayCastMode = RayCastMode.CLOSEST, radius: float = 0) -> Ray:
    return vector_intersects(test_object, Vector3(*from_xyz), Vector3(*to_xyz), mode, radius)
