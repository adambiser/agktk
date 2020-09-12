from appgamekit import (
    # 2DPhysics > RayCast
    get_ray_cast_fraction as _get_ray_cast_fraction,
    get_ray_cast_normal_x as _get_ray_cast_normal_x,
    get_ray_cast_normal_y as _get_ray_cast_normal_y,
    get_ray_cast_sprite_id as _get_ray_cast_sprite_id,
    get_ray_cast_x as _get_ray_cast_x,
    get_ray_cast_y as _get_ray_cast_y,
    physics_ray_cast as _physics_ray_cast,
    physics_ray_cast_category as _physics_ray_cast_category,
    physics_ray_cast_group as _physics_ray_cast_group,
    sprite_ray_cast as _sprite_ray_cast,
    sprite_ray_cast_category as _sprite_ray_cast_category,
    sprite_ray_cast_group as _sprite_ray_cast_group,
    sprite_ray_cast_single as _sprite_ray_cast_single,
)
from .._grfx import Sprite


def physics_cast(x1: float, y1: float, x2: float, y2: float, category: int = None, group: int = None) -> bool:
    if category is not None and group is not None:
        raise ValueError("If either 'category' or 'group' is specified, only one may be specified.")
    if category is not None:
        return _physics_ray_cast_category(category, x1, y1, x2, y2)
    if group is not None:
        return _physics_ray_cast_group(group, x1, y1, x2, y2)
    return _physics_ray_cast(x1, y1, x2, y2)


def sprite_cast(x1: float, y1: float, x2: float, y2: float, category: int = None, group: int = None) -> bool:
    if category is not None and group is not None:
        raise ValueError("If either 'category' or 'group' is specified, only one may be specified.")
    if category is not None:
        return _sprite_ray_cast_category(category, x1, y1, x2, y2)
    if group is not None:
        return _sprite_ray_cast_group(group, x1, y1, x2, y2)
    return _sprite_ray_cast(x1, y1, x2, y2)


def intersects(test_sprite: Sprite, x1: float, y1: float, x2: float, y2: float) -> bool:
    return _sprite_ray_cast_single(test_sprite.id, x1, y1, x2, y2)


def get_fraction() -> float:
    return _get_ray_cast_fraction()


def get_normal_x() -> float:
    return _get_ray_cast_normal_x()


def get_normal_y() -> float:
    return _get_ray_cast_normal_y()


def get_hit_sprite() -> Sprite:
    # noinspection PyProtectedMember
    return Sprite._from_id(_get_ray_cast_sprite_id())


def get_hit_x() -> float:
    return _get_ray_cast_x()


def get_hit_y() -> float:
    return _get_ray_cast_y()
