# noinspection PyUnresolvedReferences
from appgamekit import (
    # 2DPhysics > Debug
    get_physics_island_count as get_island_count,
    get_physics_solve_time as get_solve_time,
    set_physics_ccd as _set_physics_ccd,
    set_physics_debug_off as _set_physics_debug_off,
    set_physics_debug_on as _set_physics_debug_on,
    set_physics_sleeping as _set_physics_sleeping,
    set_physics_threading as set_threading,
    # 2DPhysics > Forces
    create_physics_force as _create_physics_force,
    delete_physics_force as _delete_physics_force,
    set_physics_force_position as _set_physics_force_position,
    set_physics_force_power as _set_physics_force_power,
    set_physics_force_range as _set_physics_force_range,
    # 2DPhysics > General
    set_physics_gravity as set_gravity,
    set_physics_max_polygon_points as set_max_polygon_points,
    set_physics_scale as set_scale,
    set_physics_wall_bottom as _set_physics_wall_bottom,
    set_physics_wall_left as _set_physics_wall_left,
    set_physics_wall_right as _set_physics_wall_right,
    set_physics_wall_top as _set_physics_wall_top,
    # 2DPhysics > Contacts
    # get_contact_sprite_id1,  # See sprite
    # get_contact_sprite_id2,  # See sprite
    # get_contact_world_x,  # See sprite
    # get_contact_world_y,  # See sprite
    get_first_contact as _get_first_contact,
    get_next_contact as _get_next_contact,
    # get_sprite_contact_sprite_id2,  # See sprite
    # get_sprite_contact_world_x,  # See sprite
    # get_sprite_contact_world_y,  # See sprite
    # get_sprite_first_contact,  # See sprite
    # get_sprite_next_contact,  # See sprite
    # 2DPhysics > RayCast
    # See raycaster
    # 2DPhysics > Joints
    # See _joints
)
from .._grfx import SpriteContact
from ._joints import (
    DistanceJoint,
    GearJoint,
    LineJoint,
    MouseJoint,
    PrismaticJoint,
    PulleyJoint,
    RevoluteJoint,
    RopeJoint,
    WeldJoint
)


def enable_ccd(enabled: bool = True):
    _set_physics_ccd(enabled)


def enable_debug(enabled: bool = True):
    if enabled:
        _set_physics_debug_on()
    else:
        _set_physics_debug_off()


def enable_sleeping(enabled: bool = True):
    _set_physics_sleeping(enabled)


def enable_wall(top: bool = None, right: bool = None, bottom: bool = None, left: bool = None):
    if top is not None:
        _set_physics_wall_top(top)
    if right is not None:
        _set_physics_wall_right(right)
    if bottom is not None:
        _set_physics_wall_bottom(bottom)
    if left is not None:
        _set_physics_wall_left(left)


class Physics2DForce(object):
    # noinspection PyShadowingBuiltins
    def __init__(self, x: float, y: float, power: float, limit: float, range: float, fade: bool):
        self.__id = _create_physics_force(x, y, power, limit, range, fade)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_physics_force(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def set_position(self, x: float, y: float):
        _set_physics_force_position(self.__id, x, y)

    def set_power(self, power: float):
        _set_physics_force_power(self.__id, power)

    # noinspection PyShadowingBuiltins
    def set_range(self, range: float):
        _set_physics_force_range(self.__id, range)


def get_contacts() -> SpriteContact:
    """Note: Finish using all of the results before using this generator again."""
    has_contact = _get_first_contact()
    while has_contact:
        yield SpriteContact()
        has_contact = _get_next_contact()
