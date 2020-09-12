"""
Sprites
"""
from appgamekit import (
    # 2DPhysics > Contacts
    get_contact_sprite_id1 as _get_contact_sprite_id1,
    get_contact_sprite_id2 as _get_contact_sprite_id2,
    get_contact_world_x as _get_contact_world_x,
    get_contact_world_y as _get_contact_world_y,
    get_sprite_contact_sprite_id2 as _get_sprite_contact_sprite_id2,
    get_sprite_contact_world_x as _get_sprite_contact_world_x,
    get_sprite_contact_world_y as _get_sprite_contact_world_y,
    get_sprite_first_contact as _get_sprite_first_contact,
    get_sprite_next_contact as _get_sprite_next_contact,
    # Sprite > Animation
    add_sprite_animation_frame as _add_sprite_animation_frame,
    clear_sprite_animation_frames as _clear_sprite_animation_frames,
    get_sprite_current_frame as _get_sprite_current_frame,
    get_sprite_frame_count as _get_sprite_frame_count,
    get_sprite_playing as _get_sprite_playing,
    play_sprite as _play_sprite,
    resume_sprite as _resume_sprite,
    set_sprite_animation as _set_sprite_animation,
    set_sprite_frame as _set_sprite_frame,
    set_sprite_speed as _set_sprite_speed,
    stop_sprite as _stop_sprite,
    # Sprite > Physics
    add_sprite_shape_box as _add_sprite_shape_box,
    add_sprite_shape_chain as _add_sprite_shape_chain,
    add_sprite_shape_circle as _add_sprite_shape_circle,
    add_sprite_shape_polygon as _add_sprite_shape_polygon,
    calculate_sprite_physics_com as _calculate_sprite_physics_com,
    clear_sprite_shapes as _clear_sprite_shapes,
    get_physics_collision as _get_physics_collision,
    get_physics_collision_world_x as _get_physics_collision_world_x,
    get_physics_collision_world_y as _get_physics_collision_world_y,
    get_physics_collision_x as _get_physics_collision_x,
    get_physics_collision_y as _get_physics_collision_y,
    get_sprite_num_shapes as _get_sprite_num_shapes,
    get_sprite_physics_angular_velocity as _get_sprite_physics_angular_velocity,
    get_sprite_physics_com_x as _get_sprite_physics_com_x,
    get_sprite_physics_com_y as _get_sprite_physics_com_y,
    get_sprite_physics_mass as _get_sprite_physics_mass,
    get_sprite_physics_velocity_x as _get_sprite_physics_velocity_x,
    get_sprite_physics_velocity_y as _get_sprite_physics_velocity_y,
    get_sprite_shape_num_vertices as _get_sprite_shape_num_vertices,
    get_sprite_shape_vertex_x as _get_sprite_shape_vertex_x,
    get_sprite_shape_vertex_y as _get_sprite_shape_vertex_y,
    set_sprite_category_bit as _set_sprite_category_bit,
    set_sprite_category_bits as _set_sprite_category_bits,
    set_sprite_collide_bit as _set_sprite_collide_bit,
    set_sprite_collide_bits as _set_sprite_collide_bits,
    set_sprite_group as _set_sprite_group,
    set_sprite_physics_angular_damping as _set_sprite_physics_angular_damping,
    set_sprite_physics_angular_impulse as _set_sprite_physics_angular_impulse,
    set_sprite_physics_angular_velocity as _set_sprite_physics_angular_velocity,
    set_sprite_physics_com as _set_sprite_physics_com,
    set_sprite_physics_can_rotate as _set_sprite_physics_can_rotate,
    set_sprite_physics_damping as _set_sprite_physics_damping,
    set_sprite_physics_delete as _set_sprite_physics_delete,
    set_sprite_physics_density as _set_sprite_physics_density,
    set_sprite_physics_force as _set_sprite_physics_force,
    set_sprite_physics_friction as _set_sprite_physics_friction,
    set_sprite_physics_impulse as _set_sprite_physics_impulse,
    set_sprite_physics_is_bullet as _set_sprite_physics_is_bullet,
    set_sprite_physics_is_sensor as _set_sprite_physics_is_sensor,
    set_sprite_physics_mass as _set_sprite_physics_mass,
    set_sprite_physics_off as _set_sprite_physics_off,
    set_sprite_physics_on as _set_sprite_physics_on,
    set_sprite_physics_restitution as _set_sprite_physics_restitution,
    set_sprite_physics_torque as _set_sprite_physics_torque,
    set_sprite_physics_velocity as _set_sprite_physics_velocity,
    # set_sprite_shape,  # Is this really needed?  Why not just use the other set_sprite_shape_ methods?
    set_sprite_shape_box as _set_sprite_shape_box,
    set_sprite_shape_chain as _set_sprite_shape_chain,
    set_sprite_shape_circle as _set_sprite_shape_circle,
    set_sprite_shape_polygon as _set_sprite_shape_polygon,
    # Sprite > Collision
    get_sprite_collision as _get_sprite_collision,
    get_sprite_distance as _get_sprite_distance,
    get_sprite_distance_point1_x as _get_sprite_distance_point1_x,
    get_sprite_distance_point1_y as _get_sprite_distance_point1_y,
    get_sprite_distance_point2_x as _get_sprite_distance_point2_x,
    get_sprite_distance_point2_y as _get_sprite_distance_point2_y,
    get_sprite_in_box as _get_sprite_in_box,
    get_sprite_in_circle as _get_sprite_in_circle,
    # Sprite > Properties
    draw_sprite as _draw_sprite,
    fix_sprite_to_screen as _fix_sprite_to_screen,
    get_sprite_active as _get_sprite_active,
    get_sprite_angle as _get_sprite_angle,
    get_sprite_angle_rad as _get_sprite_angle_rad,
    get_sprite_color_alpha as _get_sprite_color_alpha,
    get_sprite_color_blue as _get_sprite_color_blue,
    get_sprite_color_green as _get_sprite_color_green,
    get_sprite_color_red as _get_sprite_color_red,
    get_sprite_depth as _get_sprite_depth,
    # get_sprite_exists,  # Not needed
    get_sprite_flipped_h as _get_sprite_flipped_h,
    get_sprite_flipped_v as _get_sprite_flipped_v,
    get_sprite_group as _get_sprite_group,
    get_sprite_height as _get_sprite_height,
    get_sprite_hit as _get_sprite_hit,
    get_sprite_hit_category as _get_sprite_hit_category,
    get_sprite_hit_group as _get_sprite_hit_group,
    get_sprite_hit_test as _get_sprite_hit_test,
    # get_sprite_image_id,  # Not needed.
    get_sprite_in_screen as _get_sprite_in_screen,
    get_sprite_offset_x as _get_sprite_offset_x,
    get_sprite_offset_y as _get_sprite_offset_y,
    get_sprite_pixel_from_x as _get_sprite_pixel_from_x,
    get_sprite_pixel_from_y as _get_sprite_pixel_from_y,
    get_sprite_scale_x as _get_sprite_scale_x,
    get_sprite_scale_y as _get_sprite_scale_y,
    get_sprite_transparency as _get_sprite_transparency,
    get_sprite_visible as _get_sprite_visible,
    get_sprite_width as _get_sprite_width,
    get_sprite_x as _get_sprite_x,
    get_sprite_x_by_offset as _get_sprite_x_by_offset,
    get_sprite_x_from_pixel as _get_sprite_x_from_pixel,
    get_sprite_x_from_world as _get_sprite_x_from_world,
    get_sprite_y as _get_sprite_y,
    get_sprite_y_by_offset as _get_sprite_y_by_offset,
    get_sprite_y_from_pixel as _get_sprite_y_from_pixel,
    get_sprite_y_from_world as _get_sprite_y_from_world,
    get_world_x_from_sprite as _get_world_x_from_sprite,
    get_world_y_from_sprite as _get_world_y_from_sprite,
    reset_sprite_uv as _reset_sprite_uv,
    set_sprite_active as _set_sprite_active,
    set_sprite_additional_image as _set_sprite_additional_image,
    set_sprite_angle as _set_sprite_angle,
    set_sprite_angle_rad as _set_sprite_angle_rad,
    set_sprite_color as _set_sprite_color,
    set_sprite_color_alpha as _set_sprite_color_alpha,
    set_sprite_color_blue as _set_sprite_color_blue,
    set_sprite_color_green as _set_sprite_color_green,
    set_sprite_color_red as _set_sprite_color_red,
    set_sprite_depth as _set_sprite_depth,
    set_sprite_flip as _set_sprite_flip,
    set_sprite_image as _set_sprite_image,
    set_sprite_offset as _set_sprite_offset,
    set_sprite_position as _set_sprite_position,
    set_sprite_position_by_offset as _set_sprite_position_by_offset,
    set_sprite_scale as _set_sprite_scale,
    set_sprite_scale_by_offset as _set_sprite_scale_by_offset,
    set_sprite_scissor as _set_sprite_scissor,
    set_sprite_shader as _set_sprite_shader,
    set_sprite_size as _set_sprite_size,
    set_sprite_snap as _set_sprite_snap,
    set_sprite_transparency as _set_sprite_transparency,
    set_sprite_uv as _set_sprite_uv,
    set_sprite_uv_border as _set_sprite_uv_border,
    set_sprite_uv_offset as _set_sprite_uv_offset,
    set_sprite_uv_scale as _set_sprite_uv_scale,
    set_sprite_visible as _set_sprite_visible,
    set_sprite_x as _set_sprite_x,
    set_sprite_y as _set_sprite_y,
    # Sprite > Creation
    clone_sprite as _clone_sprite,  # Not needed.
    # clone_sprite_to,  # Not needed.
    create_dummy_sprite as _create_dummy_sprite,
    # create_dummy_sprite_id,  # Not needed.
    create_sprite as _create_sprite,
    # create_sprite_id,  # Not needed.
    # delete_all_sprites,  # Not needed.
    # delete_all_text,  # why is this in here?
    delete_sprite as _delete_sprite,
    # load_sprite,  # Not needed.  Don't allow this usage.  Must use an Image.
    # load_sprite_id,  # Not needed.  Don't allow this usage.  Must use an Image.
    # Skeleton > 2D
    fix_sprite_to_skeleton_2d as _fix_sprite_to_skeleton_2d,
)
from agktk._enums import (
    PhysicsMode,
    # SpriteShape,
    TransparencyMode,
)
from .image import Image
from .._grfx3d import Shader
from typing import List, Optional, Sequence, Tuple, Union
from copy import deepcopy as _deepcopy
import weakref as _weakref


class SpriteContact(object):
    def __init__(self, for_sprite: "Sprite" = None):
        # Load everything now.
        if for_sprite:
            # Use the sprite-specific functions
            self.__sprite1 = for_sprite
            # noinspection PyProtectedMember
            self.__sprite2 = Sprite._from_id(_get_sprite_contact_sprite_id2())
            self.__world_x = _get_sprite_contact_world_x()
            self.__world_y = _get_sprite_contact_world_y()
        else:
            # noinspection PyProtectedMember
            self.__sprite1 = Sprite._from_id(_get_contact_sprite_id1())
            # noinspection PyProtectedMember
            self.__sprite2 = Sprite._from_id(_get_contact_sprite_id2())
            self.__world_x = _get_contact_world_x()
            self.__world_y = _get_contact_world_y()

    @property
    def sprite1(self) -> "Sprite":
        return self.__sprite1

    @property
    def sprite2(self) -> "Sprite":
        return self.__sprite2

    @property
    def world_x(self) -> float:
        return self.__world_x

    @property
    def world_y(self) -> float:
        return self.__world_y


class Sprite(object):
    """
    Wraps AppGameKit sprite object methods.
    """
    __instances = _weakref.WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        _id = kwargs.get("_id")
        # If an ID is given and it is 0, don't create an instance.
        if _id == 0:
            return None
        o = super().__new__(cls)
        return o

    def __init__(self, image: Image = None, x: float = 0, y: float = 0, width: float = None, height: float = None,
                 dummy: bool = False, **kwargs):
        _id = kwargs.get("_id")
        if _id is None:
            _id = _create_dummy_sprite() if dummy else _create_sprite(image.id if image else 0)
        self.__id = _id
        Sprite.__instances[_id] = self
        # Sprites have an image plus up to 7 additional images.  See set_sprite_additional_image.
        self.__images = [image] + [None] * 7
        self.__fixed_to_screen = False
        self.__animation_images = []
        self.__shader = None
        _set_sprite_position(_id, x, y)
        if width or height:
            width = width or _get_sprite_width(_id)
            height = height or _get_sprite_height(_id)
            _set_sprite_size(_id, width, height)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_sprite(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @classmethod
    def _from_id(cls, sprite_id: int):
        """Internal use only."""
        if not sprite_id:
            return None
        if sprite_id in cls.__instances:
            return cls.__instances.get(sprite_id)
        return Sprite(_id=sprite_id)

    def clone(self) -> "Sprite":
        # Don't call __init__.
        # c = Sprite.__new__(Sprite)
        c = _deepcopy(self)
        c.__id = _clone_sprite(self.__id)
        # c.__images = self.__images
        # c.__fixed_to_screen = self.__fixed_to_screen
        return c

    @classmethod
    def get_sprite_hit(cls, x: float, y: float, category: int = None, group: int = None) -> "Sprite":
        if category is not None and group is not None:
            raise ValueError("If either 'category' or 'group' is specified, only one may be specified.")
        if category is not None:
            _id = _get_sprite_hit_category(category, x, y)
        elif group is not None:
            _id = _get_sprite_hit_group(group, x, y)
        else:
            _id = _get_sprite_hit(x, y)
        return Sprite._from_id(_id)

    # Sprite > Properties
    def draw(self):
        _draw_sprite(self.__id)

    @property
    def fixed_to_screen(self) -> bool:
        """Returns or sets whether the sprite is fixed to screen coordinates rather than world coordinates."""
        return self.__fixed_to_screen

    @fixed_to_screen.setter
    def fixed_to_screen(self, value: bool):
        self.__fixed_to_screen = value
        _fix_sprite_to_screen(self.__id, value)

    @property
    def is_active(self) -> bool:
        return _get_sprite_active(self.__id)

    @is_active.setter
    def is_active(self, value: bool):
        _set_sprite_active(self.__id, value)

    @property
    def angle(self) -> float:
        return _get_sprite_angle(self.__id)

    @angle.setter
    def angle(self, value: float):
        _set_sprite_angle(self.__id, value)

    @property
    def angle_rad(self) -> float:
        return _get_sprite_angle_rad(self.__id)

    @angle_rad.setter
    def angle_rad(self, value: float):
        _set_sprite_angle_rad(self.__id, value)

    @property
    def color_alpha(self) -> int:
        return _get_sprite_color_alpha(self.__id)

    @color_alpha.setter
    def color_alpha(self, value: int):
        _set_sprite_color_alpha(self.__id, value)

    @property
    def color_blue(self) -> int:
        return _get_sprite_color_blue(self.__id)

    @color_blue.setter
    def color_blue(self, value: int):
        _set_sprite_color_blue(self.__id, value)

    @property
    def color_green(self) -> int:
        return _get_sprite_color_green(self.__id)

    @color_green.setter
    def color_green(self, value: int):
        _set_sprite_color_green(self.__id, value)

    @property
    def color_red(self) -> int:
        return _get_sprite_color_red(self.__id)

    @color_red.setter
    def color_red(self, value: int):
        _set_sprite_color_red(self.__id, value)

    def set_color(self, red: int, green: int, blue: int, alpha: int = 255):
        _set_sprite_color(self.__id, red, green, blue, alpha)

    @property
    def depth(self) -> int:
        return _get_sprite_depth(self.__id)

    @depth.setter
    def depth(self, value: int):
        _set_sprite_depth(self.__id, value)

    @property
    def is_flipped_horizontal(self) -> bool:
        return _get_sprite_flipped_h(self.__id)

    @property
    def is_flipped_vertical(self) -> bool:
        return _get_sprite_flipped_v(self.__id)

    def set_flip(self, horizontal: bool, vertical: bool):
        _set_sprite_flip(self.__id, horizontal, vertical)

    @property
    def group(self) -> int:
        return _get_sprite_group(self.__id)

    def set_group(self, group: int, shape_id: int = 0):
        _set_sprite_group(self.__id, group, shape_id)

    @property
    def height(self) -> float:
        return _get_sprite_height(self.__id)

    @property
    def width(self) -> float:
        return _get_sprite_width(self.__id)

    def set_size(self, width: float, height: float):
        _set_sprite_size(self.__id, width, height)

    def hit_test(self, x: float, y: float) -> bool:
        return _get_sprite_hit_test(self.__id, x, y)

    @property
    def image(self) -> Image:
        return self.__images[0]

    @image.setter
    def image(self, value: Image):
        self.__images[0] = value
        _set_sprite_image(self.__id, value.id if value else 0)

    def set_additional_image(self, image: Image, stage: int):
        self.__images[stage] = image
        _set_sprite_additional_image(self.__id, image.id if image else 0, stage)

    @property
    def is_in_screen(self) -> bool:
        return _get_sprite_in_screen(self.__id)

    @property
    def offset_x(self) -> float:
        return _get_sprite_offset_x(self.__id)

    @property
    def offset_y(self) -> float:
        return _get_sprite_offset_y(self.__id)

    def set_offset(self, x: float, y: float):
        _set_sprite_offset(self.__id, x, y)

    def get_pixel_from_x(self, x: float):
        return _get_sprite_pixel_from_x(self.__id, x)

    def get_pixel_from_y(self, x: float):
        return _get_sprite_pixel_from_y(self.__id, x)

    @property
    def scale_x(self) -> float:
        return _get_sprite_scale_x(self.__id)

    @property
    def scale_y(self) -> float:
        return _get_sprite_scale_y(self.__id)

    def set_scale(self, x: float, y: float):
        _set_sprite_scale(self.__id, x, y)

    def set_scale_by_offset(self, x: float, y: float):
        _set_sprite_scale_by_offset(self.__id, x, y)

    @property
    def transparency_mode(self) -> TransparencyMode:
        return TransparencyMode(_get_sprite_transparency(self.__id))

    @transparency_mode.setter
    def transparency_mode(self, value: TransparencyMode):
        _set_sprite_transparency(self.__id, value)

    @property
    def is_visible(self) -> bool:
        return _get_sprite_visible(self.__id)

    @is_visible.setter
    def is_visible(self, value: bool):
        _set_sprite_visible(self.__id, value)

    @property
    def x(self) -> float:
        return _get_sprite_x(self.__id)

    @x.setter
    def x(self, value: float):
        _set_sprite_x(self.__id, value)

    @property
    def y(self) -> float:
        return _get_sprite_y(self.__id)

    @y.setter
    def y(self, value: float):
        _set_sprite_y(self.__id, value)

    def set_position(self, x: float, y: float):
        _set_sprite_position(self.__id, x, y)

    @property
    def x_by_offset(self) -> float:
        return _get_sprite_x_by_offset(self.__id)

    @property
    def y_by_offset(self) -> float:
        return _get_sprite_y_by_offset(self.__id)

    def set_position_by_offset(self, x: float, y: float):
        _set_sprite_position_by_offset(self.__id, x, y)

    def get_point_from_pixel(self, x: int, y: int) -> Tuple[float, float]:
        return _get_sprite_x_from_pixel(self.__id, x), _get_sprite_y_from_pixel(self.__id, y)

    def get_point_from_world(self, x: float, y: float) -> Tuple[float, float]:
        return _get_sprite_x_from_world(self.__id, x, y), _get_sprite_y_from_world(self.__id, x, y)

    def get_world_from_point(self, x: float, y: float) -> Tuple[float, float]:
        return _get_world_x_from_sprite(self.__id, x, y), _get_world_y_from_sprite(self.__id, x, y)

    def reset_uv(self):
        _reset_sprite_uv(self.__id)

    def set_scissor(self, x1: float, y1: float, x2: float, y2: float):
        _set_sprite_scissor(self.__id, x1, y1, x2, y2)

    def set_shader(self, shader: Shader):
        self.__shader = shader
        _set_sprite_shader(self.__id, shader.id if shader else 0)

    def set_snap_enabled(self, enabled: bool):
        _set_sprite_snap(self.__id, enabled)

    def set_uv(self, u1: float, v1: float, u2: float, v2: float, u3: float, v3: float, u4: float, v4: float):
        _set_sprite_uv(self.__id, u1, v1, u2, v2, u3, v3, u4, v4)

    def set_uv_border(self, border_size: float):
        _set_sprite_uv_border(self.__id, border_size)

    def set_uv_offset(self, u: float, v: float):
        _set_sprite_uv_offset(self.__id, u, v)

    def set_uv_scale(self, u: float, v: float):
        _set_sprite_uv_scale(self.__id, u, v)

    # Sprite > Animation
    def add_animation_frame(self, image: Image):
        self.__animation_images.append(image)
        _add_sprite_animation_frame(self.__id, image.id if image else 0)

    def clear_animation_frames(self):
        self.__animation_images.clear()
        _clear_sprite_animation_frames(self.__id)

    @property
    def current_frame(self) -> int:
        return _get_sprite_current_frame(self.__id)

    @current_frame.setter
    def current_frame(self, value: int):
        _set_sprite_frame(self.__id, value)

    @property
    def frame_count(self) -> int:
        return _get_sprite_frame_count(self.__id)

    @property
    def is_playing(self) -> bool:
        return _get_sprite_playing(self.__id)

    def play(self, fps: Union[float, int] = 10, loop: Union[bool, int] = True,
             from_frame: int = -1, to_frame: int = -1):
        _play_sprite(self.__id, fps, loop, from_frame, to_frame)

    def resume(self):
        _resume_sprite(self.__id)

    def set_animation(self, width: int, height: int, count: int):
        # # If count isn't given, calculate the count from the entire image.
        # if count is None:
        #     count = (self.image.width // width) * (self.image.height // height)
        _set_sprite_animation(self.__id, width, height, count)

    def set_speed(self, value: float):
        _set_sprite_speed(self.__id, value)

    def stop(self):
        _stop_sprite(self.__id)

    # Sprite > Collision
    def has_collision_with(self, other: "Sprite") -> bool:
        return _get_sprite_collision(self.__id, other.__id if other else 0)

    def get_distance_to(self, other: "Sprite") -> float:
        return _get_sprite_distance(self.__id, other.__id if other else 0)

    # noinspection PyMethodMayBeStatic
    def get_distance_point1(self) -> Tuple[float, float]:
        return _get_sprite_distance_point1_x(), _get_sprite_distance_point1_y()

    # noinspection PyMethodMayBeStatic
    def get_distance_point2(self) -> Tuple[float, float]:
        return _get_sprite_distance_point2_x(), _get_sprite_distance_point2_y()

    def is_in_box(self, x1: float, y1: float, x2: float, y2: float) -> bool:
        return _get_sprite_in_box(self.__id, x1, y1, x2, y2)

    def is_in_circle(self, x: float, y: float, radius: float) -> bool:
        return _get_sprite_in_circle(self.__id, x, y, radius)

    # Sprite > Physics
    def add_shape_box(self, x1: float, y1: float, x2: float, y2: float, angle: float):
        _add_sprite_shape_box(self.__id, x1, y1, x2, y2, angle)

    def add_shape_chain(self, points: Sequence[Tuple[float, float]], loop: bool):
        count = len(points)
        for index in range(count):
            _add_sprite_shape_chain(self.__id, count, index, loop, *points[index])

    def add_shape_circle(self, x: float, y: float, radius: float):
        _add_sprite_shape_circle(self.__id, x, y, radius)

    def add_shape_polygon(self, points: Sequence[Tuple[float, float]]):
        count = len(points)
        for index in range(count):
            _add_sprite_shape_polygon(self.__id, count, index, *points[index])

    def clear_shapes(self):
        _clear_sprite_shapes(self.__id)

    @property
    def shape_count(self) -> int:
        return _get_sprite_num_shapes(self.__id)

    def get_shape_vertices(self, shape_id: int) -> Sequence[Tuple[float, float]]:
        _id = self.__id
        return [(_get_sprite_shape_vertex_x(_id, shape_id, vertex_index),
                 _get_sprite_shape_vertex_y(_id, shape_id, vertex_index))
                for vertex_index in range(1, _get_sprite_shape_num_vertices(_id, shape_id) + 1)]

    # def get_shape_vertices_count(self, shape_id: int) -> int:
    #     return get_sprite_shape_num_vertices(self.__id, shape_id)
    #
    # def get_shape_vertex_x(self, shape_id: int, vertex_index: int) -> float:
    #     return get_sprite_shape_vertex_x(self.__id, shape_id, vertex_index)
    #
    # def get_shape_vertex_y(self, shape_id: int, vertex_index: int) -> float:
    #     return get_sprite_shape_vertex_y(self.__id, shape_id, vertex_index)

    # def set_shape(self, shape: SpriteShape, shape_id: int = 0):
    #     set_sprite_shape(self.__id, shape, shape_id)

    def set_shape_box(self, x1: float, y1: float, x2: float, y2: float, angle: float, shape_id: int = 0):
        _set_sprite_shape_box(self.__id, x1, y1, x2, y2, angle, shape_id)

    def set_shape_chain(self, points: Sequence[Tuple[float, float]], loop: bool, shape_id: int = 0):
        count = len(points)
        for index in range(count):
            _set_sprite_shape_chain(self.__id, count, index, loop, *points[index], shape_id)

    def set_shape_circle(self, x: float, y: float, radius: float, shape_id: int = 0):
        _set_sprite_shape_circle(self.__id, x, y, radius, shape_id)

    def set_shape_polygon(self, points: Sequence[Tuple[float, float]], shape_id: int = 0):
        count = len(points)
        for index in range(count):
            _set_sprite_shape_polygon(self.__id, count, index, *points[index], shape_id)

    def set_category_bit(self, category: int, enabled: Union[bool, int], shape_id: Optional[int] = 0):
        _set_sprite_category_bit(self.__id, category, enabled, shape_id)

    def set_category_bits(self, categories: int, shape_id: Optional[int] = 0):
        _set_sprite_category_bits(self.__id, categories, shape_id)

    def set_collide_bit(self, category: int, enabled: Union[bool, int], shape_id: Optional[int] = 0):
        _set_sprite_collide_bit(self.__id, category, enabled, shape_id)

    def set_collide_bits(self, categories: int, shape_id: Optional[int] = 0):
        _set_sprite_collide_bits(self.__id, categories, shape_id)

    def has_physics_collision_with(self, other: "Sprite") -> bool:
        return _get_physics_collision(self.__id, other.__id if other else 0)

    # noinspection PyMethodMayBeStatic
    def get_physics_collision_world_point(self) -> Tuple[float, float]:
        return _get_physics_collision_world_x(), _get_physics_collision_world_y()

    # noinspection PyMethodMayBeStatic
    def get_physics_collision_point(self) -> Tuple[float, float]:
        return _get_physics_collision_x(), _get_physics_collision_y()

    @property
    def physics_angular_velocity(self) -> float:
        return _get_sprite_physics_angular_velocity(self.__id)

    @physics_angular_velocity.setter
    def physics_angular_velocity(self, value: float):
        _set_sprite_physics_angular_velocity(self.__id, value)

    def calculate_physics_com(self):
        _calculate_sprite_physics_com(self.__id)

    @property
    def physics_com_x(self) -> float:
        return _get_sprite_physics_com_x(self.__id)

    @property
    def physics_com_y(self) -> float:
        return _get_sprite_physics_com_y(self.__id)

    def set_physics_com(self, x: float, y: float):
        _set_sprite_physics_com(self.__id, x, y)

    @property
    def physics_mass(self) -> float:
        return _get_sprite_physics_mass(self.__id)

    @physics_mass.setter
    def physics_mass(self, value: float):
        _set_sprite_physics_mass(self.__id, value)

    @property
    def physics_velocity_x(self) -> float:
        return _get_sprite_physics_velocity_x(self.__id)

    @property
    def physics_velocity_y(self) -> float:
        return _get_sprite_physics_velocity_y(self.__id)

    def set_physics_velocity(self, x: float, y: float):
        _set_sprite_physics_velocity(self.__id, x, y)

    def set_physics_angular_damping(self, damping: float):
        _set_sprite_physics_angular_damping(self.__id, damping)

    def set_physics_angular_impulse(self, impulse: float):
        _set_sprite_physics_angular_impulse(self.__id, impulse)

    def set_physics_can_rotate(self, enabled: bool):
        _set_sprite_physics_can_rotate(self.__id, enabled)

    def set_physics_damping(self, damping: float):
        _set_sprite_physics_damping(self.__id, damping)

    def delete_physics(self):
        _set_sprite_physics_delete(self.__id)

    def set_physics_density(self, density: float, shape_id: int = 0):
        _set_sprite_physics_density(self.__id, density, shape_id)

    def set_physics_force(self, x: float, y: float, force_x: float, force_y: float):
        _set_sprite_physics_force(self.__id, x, y, force_x, force_y)

    def set_physics_friction(self, friction: float, shape_id: int = 0):
        _set_sprite_physics_friction(self.__id, friction, shape_id)

    def set_physics_impulse(self, x: float, y: float, impulse_x: float, impulse_y: float):
        _set_sprite_physics_impulse(self.__id, x, y, impulse_x, impulse_y)

    def set_physics_is_bullet(self, enabled: bool):
        _set_sprite_physics_is_bullet(self.__id, enabled)

    def set_physics_is_sensor(self, enabled: bool, shape_id: int = 0):
        _set_sprite_physics_is_sensor(self.__id, enabled, shape_id)

    def set_physics_off(self):
        _set_sprite_physics_off(self.__id)

    def set_physics_on(self, mode: PhysicsMode):
        _set_sprite_physics_on(self.__id, mode)

    # def set_physics_mode(self, mode: PhysicsMode):
    #     if mode == PhysicsMode.DISABLED:
    #         set_sprite_physics_off(self.__id)
    #     else:
    #         set_sprite_physics_on(self.__id, mode)

    def set_physics_restitution(self, restitution: float, shape_id: int = 0):
        _set_sprite_physics_restitution(self.__id, restitution, shape_id)

    def set_physics_torque(self, torque: float):
        _set_sprite_physics_torque(self.__id, torque)

    def detach_from_skeleton(self):
        _fix_sprite_to_skeleton_2d(self.__id, 0, 0, 0)

    def get_contacts(self) -> List[SpriteContact]:
        _id = self.__id

        def _get_contacts():
            if _get_sprite_first_contact(_id):
                yield SpriteContact(self)
                while _get_sprite_next_contact():
                    yield SpriteContact(self)
        return list(_get_contacts())
