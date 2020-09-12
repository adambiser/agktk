from appgamekit import (
    # Particles > Creation
    create_particles as _create_particles,
    # create_particles_id,  # Not needed.
    delete_particles as _delete_particles,
    # Particles > Properties
    add_particles_color_key_frame as _add_particles_color_key_frame,
    add_particles_force as _add_particles_force,
    add_particles_scale_key_frame as _add_particles_scale_key_frame,
    clear_particles_colors as _clear_particles_colors,
    clear_particles_forces as _clear_particles_forces,
    clear_particles_scales as _clear_particles_scales,
    draw_particles as _draw_particles,
    fix_particles_to_screen as _fix_particles_to_screen,
    get_particles_active as _get_particles_active,
    get_particles_angle as _get_particles_angle,
    get_particles_angle_rad as _get_particles_angle_rad,
    get_particles_depth as _get_particles_depth,
    get_particles_direction_x as _get_particles_direction_x,
    get_particles_direction_y as _get_particles_direction_y,
    # get_particles_exists as _get_particles_exists,  # Not needed
    get_particles_frequency as _get_particles_frequency,
    get_particles_life as _get_particles_life,
    get_particles_max_reached as _get_particles_max_reached,
    get_particles_size as _get_particles_size,
    get_particles_visible as _get_particles_visible,
    get_particles_x as _get_particles_x,
    get_particles_y as _get_particles_y,
    offset_particles as _offset_particles,
    reset_particle_count as _reset_particle_count,
    set_particles_active as _set_particles_active,
    set_particles_angle as _set_particles_angle,
    set_particles_angle_rad as _set_particles_angle_rad,
    set_particles_color_interpolation as _set_particles_color_interpolation,
    set_particles_depth as _set_particles_depth,
    set_particles_direction as _set_particles_direction,
    set_particles_face_direction as _set_particles_face_direction,
    set_particles_frequency as _set_particles_frequency,
    set_particles_image as _set_particles_image,
    set_particles_life as _set_particles_life,
    set_particles_max as _set_particles_max,
    set_particles_position as _set_particles_position,
    set_particles_rotation_range as _set_particles_rotation_range,
    set_particles_rotation_range_rad as _set_particles_rotation_range_rad,
    set_particles_size as _set_particles_size,
    set_particles_start_zone as _set_particles_start_zone,
    set_particles_transparency as _set_particles_transparency,
    set_particles_velocity_range as _set_particles_velocity_range,
    set_particles_visible as _set_particles_visible,
    update_particles as _update_particles,
)
from agktk._enums import (
    InterpolationMode,
    RotationMode,
    TransparencyMode,
)
from .image import Image
from typing import Optional


class ParticleEmitter(object):
    """
    Wraps AppGameKit particles methods.
    """
    def __init__(self, x: float, y: float):
        self.__id = _create_particles(x, y)
        self.__image = None  # type: Optional[Image]
        self.__fixed_to_screen = False
        # self.__max = -1

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_particles(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def draw(self):
        _draw_particles(self.__id)

    @property
    def fixed_to_screen(self) -> bool:
        """Returns or sets whether the particle emitter is fixed to screen coordinates rather than world coordinates."""
        return self.__fixed_to_screen

    @fixed_to_screen.setter
    def fixed_to_screen(self, value: bool):
        self.__fixed_to_screen = value
        _fix_particles_to_screen(self.__id, value)

    def offset(self, x: float, y: float):
        _offset_particles(self.__id, x, y)

    def update(self, time: float):
        _update_particles(self.__id, time)

    def add_color_key_frame(self, time: float, red: int, green: int, blue: int, alpha: int):
        _add_particles_color_key_frame(self.__id, time, red, green, blue, alpha)

    def clear_colors(self):
        _clear_particles_colors(self.__id)

    def add_force(self, start_time: float, end_time: float, x: float, y: float):
        _add_particles_force(self.__id, start_time, end_time, x, y)

    def clear_forces(self):
        _clear_particles_forces(self.__id)

    def add_scale_key_frame(self, time: float, scale: float):
        _add_particles_scale_key_frame(self.__id, time, scale)

    def clear_scales(self):
        _clear_particles_scales(self.__id)

    # @property
    # def max(self) -> int:
    #     return self.__max

    # @max.setter
    def set_max(self, value: int):
        # self.__max = value
        _set_particles_max(self.__id, value)

    @property
    def max_reached(self) -> bool:
        return _get_particles_max_reached(self.__id)

    def reset_count(self):
        _reset_particle_count(self.__id)

    @property
    def active(self) -> bool:
        return _get_particles_active(self.__id)

    @active.setter
    def active(self, value: bool):
        _set_particles_active(self.__id, value)

    @property
    def angle(self) -> float:
        return _get_particles_angle(self.__id)

    @angle.setter
    def angle(self, value: float):
        _set_particles_angle(self.__id, value)

    @property
    def angle_rad(self) -> float:
        return _get_particles_angle_rad(self.__id)

    @angle_rad.setter
    def angle_rad(self, value: float):
        _set_particles_angle_rad(self.__id, value)

    @property
    def depth(self) -> int:
        return _get_particles_depth(self.__id)

    @depth.setter
    def depth(self, value: int):
        _set_particles_depth(self.__id, value)

    @property
    def direction_x(self) -> float:
        return _get_particles_direction_x(self.__id)

    @property
    def direction_y(self) -> float:
        return _get_particles_direction_y(self.__id)

    def set_direction(self, x: float, y: float):
        return _set_particles_direction(self.__id, x, y)

    def set_face_direction(self, mode: RotationMode):
        return _set_particles_face_direction(self.__id, mode)

    @property
    def frequency(self) -> float:
        return _get_particles_frequency(self.__id)

    @frequency.setter
    def frequency(self, value: float):
        _set_particles_frequency(self.__id, value)

    @property
    def image(self) -> Image:
        return self.__image

    @image.setter
    def image(self, value: Image):
        self.__image = value
        _set_particles_image(self.__id, value.id if value else 0)

    @property
    def life(self) -> float:
        return _get_particles_life(self.__id)

    @life.setter
    def life(self, value: float):
        _set_particles_life(self.__id, value)

    @property
    def size(self) -> float:
        return _get_particles_size(self.__id)

    @size.setter
    def size(self, value: float):
        _set_particles_size(self.__id, value)

    @property
    def visible(self) -> bool:
        return _get_particles_visible(self.__id)

    @visible.setter
    def visible(self, value: bool):
        _set_particles_visible(self.__id, value)

    @property
    def x(self) -> float:
        return _get_particles_x(self.__id)

    @property
    def y(self) -> float:
        return _get_particles_y(self.__id)

    def set_position(self, x: float, y: float):
        return _set_particles_position(self.__id, x, y)

    def set_color_interpolation(self, mode: InterpolationMode):
        _set_particles_color_interpolation(self.__id, mode)

    def set_rotation_range(self, minimum: float, maximum: float):
        _set_particles_rotation_range(self.__id, minimum, maximum)

    def set_rotation_range_rad(self, minimum: float, maximum: float):
        _set_particles_rotation_range_rad(self.__id, minimum, maximum)

    def set_start_zone(self, x1: float, y1: float, x2: float, y2: float):
        _set_particles_start_zone(self.__id, x1, y1, x2, y2)

    def set_transparency(self, mode: TransparencyMode):
        _set_particles_transparency(self.__id, mode)

    def set_velocity_range(self, minimum: float, maximum: float):
        _set_particles_velocity_range(self.__id, minimum, maximum)
