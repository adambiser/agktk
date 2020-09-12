from appgamekit import (
    # 3D > Cameras
    fix_camera_to_object as _fix_camera_to_object,  # See also Object3D.attach_camera
    get_camera_angle_x as _get_camera_angle_x,
    get_camera_angle_y as _get_camera_angle_y,
    get_camera_angle_z as _get_camera_angle_z,
    get_camera_fov as _get_camera_fov,
    get_camera_quat_w as _get_camera_quat_w,
    get_camera_quat_x as _get_camera_quat_x,
    get_camera_quat_y as _get_camera_quat_y,
    get_camera_quat_z as _get_camera_quat_z,
    get_camera_world_x as _get_camera_world_x,
    get_camera_world_y as _get_camera_world_y,
    get_camera_world_z as _get_camera_world_z,
    get_camera_x as _get_camera_x,
    get_camera_y as _get_camera_y,
    get_camera_z as _get_camera_z,
    move_camera_local_x as _move_camera_local_x,
    move_camera_local_y as _move_camera_local_y,
    move_camera_local_z as _move_camera_local_z,
    rotate_camera_global_x as _rotate_camera_global_x,
    rotate_camera_global_y as _rotate_camera_global_y,
    rotate_camera_global_z as _rotate_camera_global_z,
    rotate_camera_local_x as _rotate_camera_local_x,
    rotate_camera_local_y as _rotate_camera_local_y,
    rotate_camera_local_z as _rotate_camera_local_z,
    set_camera_aspect as _set_camera_aspect,
    set_camera_bounds as _set_camera_bounds,
    set_camera_fov as _set_camera_fov,
    set_camera_look_at as _set_camera_look_at,
    set_camera_off_center as _set_camera_off_center,
    set_camera_ortho_width as _set_camera_ortho_width,
    set_camera_position as _set_camera_position,
    set_camera_range as _set_camera_range,
    set_camera_rotation as _set_camera_rotation,
    set_camera_rotation_quat as _set_camera_rotation_quat,
)


class Camera3D(object):
    """
    Wraps AppGameKit 3d camera methods.
    """

    def __init__(self, camera_id: int = 1):
        self.__id = camera_id

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def detach_from_object(self):
        _fix_camera_to_object(self.__id, 0)

    @property
    def angle_x(self) -> float:
        return _get_camera_angle_x(self.__id)

    @property
    def angle_y(self) -> float:
        return _get_camera_angle_y(self.__id)

    @property
    def angle_z(self) -> float:
        return _get_camera_angle_z(self.__id)

    @property
    def fov(self) -> float:
        return _get_camera_fov(self.__id)

    @fov.setter
    def fov(self, value: float):
        _set_camera_fov(self.__id, value)

    @property
    def quat_w(self) -> float:
        return _get_camera_quat_w(self.__id)

    @property
    def quat_x(self) -> float:
        return _get_camera_quat_x(self.__id)

    @property
    def quat_y(self) -> float:
        return _get_camera_quat_y(self.__id)

    @property
    def quat_z(self) -> float:
        return _get_camera_quat_z(self.__id)

    @property
    def world_x(self) -> float:
        return _get_camera_world_x(self.__id)

    @property
    def world_y(self) -> float:
        return _get_camera_world_y(self.__id)

    @property
    def world_z(self) -> float:
        return _get_camera_world_z(self.__id)

    @property
    def x(self) -> float:
        return _get_camera_x(self.__id)

    @property
    def y(self) -> float:
        return _get_camera_y(self.__id)

    @property
    def z(self) -> float:
        return _get_camera_z(self.__id)

    def move_local_x(self, distance: float):
        _move_camera_local_x(self.__id, distance)

    def move_local_y(self, distance: float):
        _move_camera_local_y(self.__id, distance)

    def move_local_z(self, distance: float):
        _move_camera_local_z(self.__id, distance)

    def rotate_global_x(self, angle: float):
        _rotate_camera_global_x(self.__id, angle)

    def rotate_global_y(self, angle: float):
        _rotate_camera_global_y(self.__id, angle)

    def rotate_global_z(self, angle: float):
        _rotate_camera_global_z(self.__id, angle)

    def rotate_local_x(self, angle: float):
        _rotate_camera_local_x(self.__id, angle)

    def rotate_local_y(self, angle: float):
        _rotate_camera_local_y(self.__id, angle)

    def rotate_local_z(self, angle: float):
        _rotate_camera_local_z(self.__id, angle)

    def set_aspect(self, aspect: float):
        _set_camera_aspect(self.__id, aspect)

    def set_bounds(self, left: float, right: float, top: float, bottom: float):
        _set_camera_bounds(self.__id, left, right, top, bottom)

    def look_at(self, x: float, y: float, z: float, roll: float):
        _set_camera_look_at(self.__id, x, y, z, roll)

    def set_off_center(self, active: bool):
        _set_camera_off_center(self.__id, active)

    def set_ortho_width(self, width: float):
        _set_camera_ortho_width(self.__id, width)

    def set_position(self, x: float, y: float, z: float):
        _set_camera_position(self.__id, x, y, z)

    def set_range(self, near: float, far: float):
        _set_camera_range(self.__id, near, far)

    def set_rotation(self, x: float, y: float, z: float):
        _set_camera_rotation(self.__id, x, y, z)

    def set_rotation_quat(self, w: float, x: float, y: float, z: float):
        _set_camera_rotation_quat(self.__id, w, x, y, z)
