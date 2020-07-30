from appgamekit import (
    # Maths > Vectors
    create_vector3 as _create_vector3,
    delete_vector3 as _delete_vector3,
    get_vector3_add as _get_vector3_add,
    get_vector3_cross as _get_vector3_cross,
    get_vector3_distance as _get_vector3_distance,
    get_vector3_dot as _get_vector3_dot,
    get_vector3_length as _get_vector3_length,
    get_vector3_multiply as _get_vector3_multiply,
    get_vector3_x as _get_vector3_x,
    get_vector3_y as _get_vector3_y,
    get_vector3_z as _get_vector3_z,
    set_vector3 as _set_vector3,
)


class Vector3(object):
    """
    Wraps AGK vector3 methods.

    Function chaining is supported.
    """
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.__id = _create_vector3(x, y, z)

    def __del__(self):
        """Delete the image."""
        try:
            _delete_vector3(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def set(self, x: float, y: float, z: float):
        _set_vector3(self.__id, x, y, z)
        return self

    def add(self, add_vector: "Vector3") -> "Vector3":
        _get_vector3_add(self.__id, add_vector.__id)
        return self

    # def add_xyz(self, x: float, y: float, z: float) -> "Vector3":
    #     return self.add(Vector3(x, y, z))

    def cross(self, vector1: "Vector3", vector2: "Vector3") -> "Vector3":
        _get_vector3_cross(self.__id, vector1.__id, vector2.__id)
        return self

    def multiply(self, multiplier: float) -> "Vector3":
        _get_vector3_multiply(self.__id, multiplier)
        return self

    def dot(self, other: "Vector3") -> float:
        return _get_vector3_dot(self.__id, other.__id)

    def distance_to(self, other: "Vector3") -> float:
        return _get_vector3_distance(self.__id, other.__id)

    @property
    def length(self) -> float:
        return _get_vector3_length(self.__id)

    @property
    def x(self) -> float:
        return _get_vector3_x(self.__id)

    @property
    def y(self) -> float:
        return _get_vector3_y(self.__id)

    @property
    def z(self) -> float:
        return _get_vector3_z(self.__id)
