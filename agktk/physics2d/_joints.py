# TODO These should probably move into the Sprite class.
from appgamekit import (
    # 2DPhysics > Joints
    create_distance_joint as _create_distance_joint,
    # create_distance_joint_id,  # Not needed
    create_gear_joint as _create_gear_joint,
    # create_gear_joint_id,  # Not needed
    create_line_joint as _create_line_joint,
    # create_line_joint_id,  # Not needed
    create_mouse_joint as _create_mouse_joint,
    # create_mouse_joint_id,  # Not needed
    create_prismatic_joint as _create_prismatic_joint,
    # create_prismatic_joint_id,  # Not needed
    # create_pulley_joint,  # Not needed
    create_pulley_joint2 as _create_pulley_joint2,
    create_revolute_joint as _create_revolute_joint,
    # create_revolute_joint_id,  # Not needed
    create_rope_joint as _create_rope_joint,
    # create_rope_joint_id,  # Not needed
    create_weld_joint as _create_weld_joint,
    # create_weld_joint_id,  # Not needed
    delete_joint as _delete_joint,
    finish_pulley_joint as _finish_pulley_joint,
    # get_joint_exists,  # Not needed
    get_joint_reaction_force_x as _get_joint_reaction_force_x,
    get_joint_reaction_force_y as _get_joint_reaction_force_y,
    get_joint_reaction_torque as _get_joint_reaction_torque,
    set_joint_damping as _set_joint_damping,
    set_joint_limit_off as _set_joint_limit_off,
    set_joint_limit_on as _set_joint_limit_on,
    set_joint_motor_off as _set_joint_motor_off,
    set_joint_motor_on as _set_joint_motor_on,
    set_joint_mouse_max_force as _set_joint_mouse_max_force,
    set_joint_mouse_target as _set_joint_mouse_target,
)
from .._grfx import Sprite


class _BaseJoint2D(object):
    def __init__(self, joint_id):
        self.__id = joint_id

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_joint(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def reaction_force_x(self) -> float:
        return _get_joint_reaction_force_x(self.__id)

    @property
    def reaction_force_y(self) -> float:
        return _get_joint_reaction_force_y(self.__id)


class DistanceJoint(_BaseJoint2D):
    def __init__(self, sprite1: Sprite, sprite2: Sprite, x1: float, y1: float, x2: float, y2: float,
                 can_collide: bool):
        super().__init__(_create_distance_joint(sprite1.id, sprite2.id, x1, y1, x2, y2, can_collide))
        self.__refs = (sprite1, sprite2)

    def set_damping(self, damping: float, frequency: float):
        _set_joint_damping(self.id, damping, frequency)


class GearJoint(_BaseJoint2D):
    def __init__(self, joint1, joint2, ratio: float):
        super().__init__(_create_gear_joint(joint1.id, joint2.id, ratio))
        self.__refs = (joint1, joint2)

    @property
    def reaction_torque(self) -> float:
        return _get_joint_reaction_torque(self.id)


class LineJoint(_BaseJoint2D):
    def __init__(self, sprite1: Sprite, sprite2: Sprite, anchor_x: float, anchor_y: float,
                 axis_x: float, axis_y: float, can_collide: bool):
        super().__init__(_create_line_joint(sprite1.id, sprite2.id, anchor_x, anchor_y, axis_x, axis_y, can_collide))
        self.__refs = (sprite1, sprite2)

    @property
    def reaction_torque(self) -> float:
        return _get_joint_reaction_torque(self.id)

    def set_damping(self, damping: float, frequency: float):
        _set_joint_damping(self.id, damping, frequency)

    def set_motor_off(self):
        _set_joint_motor_off(self.id)

    def set_motor_on(self, speed: float, max_force: float):
        _set_joint_motor_on(self.id, speed, max_force)


class MouseJoint(_BaseJoint2D):
    def __init__(self, sprite: Sprite, anchor_x: float, anchor_y: float, max_force: float):
        super().__init__(_create_mouse_joint(sprite.id, anchor_x, anchor_y, max_force))
        self.__refs = (sprite,)

    def set_max_force(self, value: float):
        _set_joint_mouse_max_force(self.id, value)

    def set_target(self, x: float, y: float):
        _set_joint_mouse_target(self.id, x, y)

    def set_damping(self, damping: float, frequency: float):
        _set_joint_damping(self.id, damping, frequency)


class PrismaticJoint(_BaseJoint2D):
    def __init__(self, sprite1: Sprite, sprite2: Sprite, anchor_x: float, anchor_y: float,
                 axis_x: float, axis_y: float, can_collide: bool):
        super().__init__(_create_prismatic_joint(sprite1.id, sprite2.id, anchor_x, anchor_y, axis_x, axis_y,
                                                 can_collide))
        self.__refs = (sprite1, sprite2)

    @property
    def reaction_torque(self) -> float:
        return _get_joint_reaction_torque(self.id)

    def set_limit_off(self):
        _set_joint_limit_off(self.id)

    def set_limit_on(self, minimum: float, maximum: float):
        _set_joint_limit_on(self.id, minimum, maximum)

    def set_motor_off(self):
        _set_joint_motor_off(self.id)

    def set_motor_on(self, speed: float, max_force: float):
        _set_joint_motor_on(self.id, speed, max_force)


class PulleyJoint(_BaseJoint2D):
    def __init__(self, sprite1: Sprite, sprite2: Sprite,
                 ground_x1: float, ground_y1: float, ground_x2: float, ground_y2: float,
                 anchor_x1: float, anchor_y1: float,  anchor_x2: float, anchor_y2: float,
                 ratio: float, can_collide: bool):
        _create_pulley_joint2(sprite1.id, sprite2.id, ratio, can_collide)
        super().__init__(_finish_pulley_joint(ground_x1, ground_y1, ground_x2, ground_y2,
                                              anchor_x1, anchor_y1, anchor_x2, anchor_y2))
        self.__refs = (sprite1, sprite2)


class RevoluteJoint(_BaseJoint2D):
    def __init__(self, sprite1: Sprite, sprite2: Sprite, x: float, y: float, can_collide: bool):
        super().__init__(_create_revolute_joint(sprite1.id, sprite2.id, x, y, can_collide))
        self.__refs = (sprite1, sprite2)

    @property
    def reaction_torque(self) -> float:
        return _get_joint_reaction_torque(self.id)

    def set_limit_off(self):
        _set_joint_limit_off(self.id)

    def set_limit_on(self, minimum: float, maximum: float):
        _set_joint_limit_on(self.id, minimum, maximum)

    def set_motor_off(self):
        _set_joint_motor_off(self.id)

    def set_motor_on(self, speed: float, max_force: float):
        _set_joint_motor_on(self.id, speed, max_force)


class RopeJoint(_BaseJoint2D):
    def __init__(self, sprite1: Sprite, sprite2: Sprite, x1: float, y1: float, x2: float, y2: float,
                 max_length: float, can_collide: bool):
        super().__init__(_create_rope_joint(sprite1.id, sprite2.id, x1, y1, x2, y2, max_length, can_collide))
        self.__refs = (sprite1, sprite2)


class WeldJoint(_BaseJoint2D):
    def __init__(self, sprite1: Sprite, sprite2: Sprite, x: float, y: float, can_collide: bool):
        super().__init__(_create_weld_joint(sprite1.id, sprite2.id, x, y, can_collide))
        self.__refs = (sprite1, sprite2)

    @property
    def reaction_torque(self) -> float:
        return _get_joint_reaction_torque(self.id)

    def set_damping(self, damping: float, frequency: float):
        _set_joint_damping(self.id, damping, frequency)
