# TODO These should probably move into the Object3D class.
from appgamekit import (
    # 3DPhysics > Joints
    create_3d_physics_6d_of_joint as _create_3d_physics_6dof_joint,
    create_3d_physics_cone_twist_joint as _create_3d_physics_cone_twist_joint,
    create_3d_physics_fixed_joint as _create_3d_physics_fixed_joint,
    create_3d_physics_hinge_joint as _create_3d_physics_hinge_joint,
    create_3d_physics_pick_joint as _create_3d_physics_pick_joint,
    create_3d_physics_slider_joint as _create_3d_physics_slider_joint,
    delete_3d_physics_joint as _delete_3d_physics_joint,
    delete_3d_physics_pick_joint as _delete_3d_physics_pick_joint,
    get_3d_physics_joint_enabled as _get_3d_physics_joint_enabled,
    get_3d_physics_joint_position_vector as _get_3d_physics_joint_position_vector,
    get_3d_physics_joint_rotation_vector as _get_3d_physics_joint_rotation_vector,
    set_3d_physics_hinge_joint_max_motor_impulse as _set_3d_physics_hinge_joint_max_motor_impulse,
    set_3d_physics_hinge_joint_motor_is_enabled as _set_3d_physics_hinge_joint_motor_is_enabled,
    set_3d_physics_hinge_joint_motor_velocity as _set_3d_physics_hinge_joint_motor_velocity,
    set_3d_physics_joint_breaking_threshold as _set_3d_physics_joint_breaking_threshold,
    set_3d_physics_joint_cone_twist_limits as _set_3d_physics_joint_cone_twist_limits,
    set_3d_physics_joint_enabled as _set_3d_physics_joint_enabled,
    set_3d_physics_joint_hinge_limits as _set_3d_physics_joint_hinge_limits,
    set_3d_physics_joint_slider_angular_limits as _set_3d_physics_joint_slider_angular_limits,
    set_3d_physics_joint_slider_linear_limits as _set_3d_physics_joint_slider_linear_limits,
    set_3d_physics_slider_joint_max_linear_motor_force as _set_3d_physics_slider_joint_max_linear_motor_force,
    set_3d_physics_slider_joint_powered_linear_motor_is_enabled as
    _set_3d_physics_slider_joint_powered_linear_motor_is_enabled,
    set_3d_physics_slider_joint_target_linear_motor_velocity as
    _set_3d_physics_slider_joint_target_linear_motor_velocity,
    set_3d_physics_twist_joint_max_motor_impulse as _set_3d_physics_twist_joint_max_motor_impulse,
    set_3d_physics_twist_joint_motor_is_enabled as _set_3d_physics_twist_joint_motor_is_enabled,
    set_3d_physics_twist_joint_motor_rotation_target as _set_3d_physics_twist_joint_motor_rotation_target,
    update_3d_physics_pick_joint as _update_3d_physics_pick_joint,
)
from .. import Vector3
from .._grfx3d import Object3D


class _BaseJoint3D(object):
    def __init__(self, joint_id):
        self.__id = joint_id

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_3d_physics_joint(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def enabled(self) -> bool:
        return _get_3d_physics_joint_enabled(self.__id)

    @enabled.setter
    def enabled(self, value: bool):
        _set_3d_physics_joint_enabled(self.__id, value)

    def get_position_vector(self):
        # noinspection PyProtectedMember
        return Vector3._from_id(_get_3d_physics_joint_position_vector(self.__id))

    def get_rotation_vector(self):
        # noinspection PyProtectedMember
        return Vector3._from_id(_get_3d_physics_joint_rotation_vector(self.__id))

    def set_breaking_threshold(self, threshold: float):
        _set_3d_physics_joint_breaking_threshold(self.__id, threshold)


class SixDOFJoint(_BaseJoint3D):
    def __init__(self, object1: Object3D, object2: Object3D, position_vector: Vector3, rotation_vector: Vector3):
        _id = _create_3d_physics_6dof_joint(object1.id, object2.id, position_vector.id, rotation_vector.id)
        super().__init__(_id)
        self.__id = _id


class ConeTwistJoint(_BaseJoint3D):
    def __init__(self, object1: Object3D, object2: Object3D, position_vector: Vector3, rotation_vector: Vector3,
                 disable_collisions: bool):
        _id = _create_3d_physics_cone_twist_joint(object1.id, object2.id, position_vector.id, rotation_vector.id,
                                                  disable_collisions)
        super().__init__(_id)
        self.__id = _id

    def set_limits(self, swing_span1: float, swing_span2: float, twist_span: float):
        _set_3d_physics_joint_cone_twist_limits(self.__id, swing_span1, swing_span2, twist_span)

    def set_max_motor_impulse(self, impulse: float):
        _set_3d_physics_twist_joint_max_motor_impulse(self.__id, impulse)

    def enable_motor(self, enabled: bool = True):
        _set_3d_physics_twist_joint_motor_is_enabled(self.__id, enabled)

    def set_motor_target_rotation(self, rotation_vector: Vector3):
        _set_3d_physics_twist_joint_motor_rotation_target(self.__id, rotation_vector.id)


class FixedJoint(_BaseJoint3D):
    def __init__(self, object1: Object3D, object2: Object3D, position_vector: Vector3):
        _id = _create_3d_physics_fixed_joint(object1.id, object2.id, position_vector.id)
        super().__init__(_id)
        self.__id = _id


class HingeJoint(_BaseJoint3D):
    def __init__(self, object1: Object3D, object2: Object3D, position_vector: Vector3, rotation_vector: Vector3,
                 disable_collisions: bool):
        _id = _create_3d_physics_hinge_joint(object1.id, object2.id, position_vector.id, rotation_vector.id,
                                             disable_collisions)
        super().__init__(_id)
        self.__id = _id

    def set_limits(self, minimum: float, maximum: float):
        _set_3d_physics_joint_hinge_limits(self.__id, minimum, maximum)

    def set_max_motor_impulse(self, impulse: float):
        _set_3d_physics_hinge_joint_max_motor_impulse(self.__id, impulse)

    def enable_motor(self, enabled: bool = True):
        _set_3d_physics_hinge_joint_motor_is_enabled(self.__id, enabled)

    def set_motor_target_velocity(self, velocity: float):
        _set_3d_physics_hinge_joint_motor_velocity(self.__id, velocity)


class SliderJoint(_BaseJoint3D):
    def __init__(self, object1: Object3D, object2: Object3D, position_vector: Vector3, rotation_vector: Vector3):
        _id = _create_3d_physics_slider_joint(object1.id, object2.id, position_vector.id, rotation_vector.id)
        super().__init__(_id)
        self.__id = _id

    def set_angular_limits(self, minimum: float, maximum: float):
        _set_3d_physics_joint_slider_angular_limits(self.__id, minimum, maximum)

    def set_linear_limits(self, minimum: float, maximum: float):
        _set_3d_physics_joint_slider_linear_limits(self.__id, minimum, maximum)

    def set_max_linear_motor_force(self, force: float):
        _set_3d_physics_slider_joint_max_linear_motor_force(self.__id, force)

    def enable_motor(self, enabled: bool = True):
        _set_3d_physics_slider_joint_powered_linear_motor_is_enabled(self.__id, enabled)

    def set_motor_target_velocity(self, velocity: float):
        _set_3d_physics_slider_joint_target_linear_motor_velocity(self.__id, velocity)


class PickJoint(_BaseJoint3D):
    def __init__(self, object3d: Object3D, position_vector: Vector3):
        _id = _create_3d_physics_pick_joint(object3d.id, position_vector.id)
        super().__init__(_id)
        self.__id = _id

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_3d_physics_pick_joint(self.__id)
        except TypeError:
            pass

    def update(self, position_vector: Vector3):
        _update_3d_physics_pick_joint(self.__id, position_vector.id)
