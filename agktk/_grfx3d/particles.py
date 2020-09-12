from appgamekit import (
    # 3DParticles > Properties
    add_3d_particles_color_key_frame as _add_3d_particles_color_key_frame,
    add_3d_particles_force as _add_3d_particles_force,
    add_3d_particles_scale_key_frame as _add_3d_particles_scale_key_frame,
    clear_3d_particles_colors as _clear_3d_particles_colors,
    clear_3d_particles_forces as _clear_3d_particles_forces,
    clear_3d_particles_scales as _clear_3d_particles_scales,
    draw_3d_particles as _draw_3d_particles,
    get_3d_particles_active as _get_3d_particles_active,
    get_3d_particles_direction_range1 as _get_3d_particles_direction_range1,
    get_3d_particles_direction_range2 as _get_3d_particles_direction_range2,
    get_3d_particles_direction_x as _get_3d_particles_direction_x,
    get_3d_particles_direction_y as _get_3d_particles_direction_y,
    get_3d_particles_direction_z as _get_3d_particles_direction_z,
    # get_3d_particles_exists,  # not needed
    get_3d_particles_frequency as _get_3d_particles_frequency,
    get_3d_particles_life as _get_3d_particles_life,
    get_3d_particles_max_reached as _get_3d_particles_max_reached,
    get_3d_particles_size as _get_3d_particles_size,
    get_3d_particles_visible as _get_3d_particles_visible,
    get_3d_particles_x as _get_3d_particles_x,
    get_3d_particles_y as _get_3d_particles_y,
    get_3d_particles_z as _get_3d_particles_z,
    offset_3d_particles as _offset_3d_particles,
    reset_3d_particle_count as _reset_3d_particle_count,
    set_3d_particles_active as _set_3d_particles_active,
    set_3d_particles_color_interpolation as _set_3d_particles_color_interpolation,
    set_3d_particles_direction as _set_3d_particles_direction,
    set_3d_particles_direction_range as _set_3d_particles_direction_range,
    set_3d_particles_frequency as _set_3d_particles_frequency,
    set_3d_particles_image as _set_3d_particles_image,
    set_3d_particles_life as _set_3d_particles_life,
    set_3d_particles_max as _set_3d_particles_max,
    set_3d_particles_position as _set_3d_particles_position,
    set_3d_particles_size as _set_3d_particles_size,
    set_3d_particles_start_zone as _set_3d_particles_start_zone,
    set_3d_particles_transparency as _set_3d_particles_transparency,
    set_3d_particles_velocity_range as _set_3d_particles_velocity_range,
    set_3d_particles_visible as _set_3d_particles_visible,
    update_3d_particles as _update_3d_particles,
    # 3DParticles > Creation
    create_3d_particles as _create_3d_particles,
    delete_3d_particles as _delete_3d_particles,
)
from agktk._enums import (
    InterpolationMode,
    TransparencyMode,
)
from .._grfx.image import Image
from typing import Optional


class ParticleEmitter3D(object):
    """
    Wraps AppGameKit 3d particles methods.
    """
    def __init__(self, x: float, y: float, z: float):
        self.__id = _create_3d_particles(x, y, z)
        self.__image = None  # type: Optional[Image]

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_3d_particles(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def draw(self):
        _draw_3d_particles(self.__id)

    def offset(self, x: float, y: float, z: float):
        _offset_3d_particles(self.__id, x, y, z)

    def update(self, time: float):
        _update_3d_particles(self.__id, time)

    def add_color_key_frame(self, time: float, red: int, green: int, blue: int, alpha: int):
        _add_3d_particles_color_key_frame(self.__id, time, red, green, blue, alpha)

    def clear_colors(self):
        _clear_3d_particles_colors(self.__id)

    def add_force(self, start_time: float, end_time: float, x: float, y: float, z: float):
        _add_3d_particles_force(self.__id, start_time, end_time, x, y, z)

    def clear_forces(self):
        _clear_3d_particles_forces(self.__id)

    def add_scale_key_frame(self, time: float, scale: float):
        _add_3d_particles_scale_key_frame(self.__id, time, scale)

    def clear_scales(self):
        _clear_3d_particles_scales(self.__id)

    def set_max(self, value: int):
        _set_3d_particles_max(self.__id, value)

    @property
    def max_reached(self) -> bool:
        return _get_3d_particles_max_reached(self.__id)

    def reset_count(self):
        _reset_3d_particle_count(self.__id)

    @property
    def active(self) -> bool:
        return _get_3d_particles_active(self.__id)

    @active.setter
    def active(self, value: bool):
        _set_3d_particles_active(self.__id, value)

    @property
    def direction_range1(self) -> float:
        return _get_3d_particles_direction_range1(self.__id)

    @property
    def direction_range2(self) -> float:
        return _get_3d_particles_direction_range2(self.__id)

    def set_direction_range(self, angle1: float, angle2: float):
        return _set_3d_particles_direction_range(self.__id, angle1, angle2)

    @property
    def direction_x(self) -> float:
        return _get_3d_particles_direction_x(self.__id)

    @property
    def direction_y(self) -> float:
        return _get_3d_particles_direction_y(self.__id)

    @property
    def direction_z(self) -> float:
        return _get_3d_particles_direction_z(self.__id)

    def set_direction(self, x: float, y: float, z: float, roll: float):
        return _set_3d_particles_direction(self.__id, x, y, z, roll)

    @property
    def frequency(self) -> float:
        return _get_3d_particles_frequency(self.__id)

    @frequency.setter
    def frequency(self, value: float):
        _set_3d_particles_frequency(self.__id, value)

    @property
    def image(self) -> Image:
        return self.__image

    @image.setter
    def image(self, value: Image):
        self.__image = value
        _set_3d_particles_image(self.__id, value.id if value else 0)

    @property
    def life(self) -> float:
        return _get_3d_particles_life(self.__id)

    @life.setter
    def life(self, value: float):
        _set_3d_particles_life(self.__id, value)

    @property
    def size(self) -> float:
        return _get_3d_particles_size(self.__id)

    @size.setter
    def size(self, value: float):
        _set_3d_particles_size(self.__id, value)

    @property
    def visible(self) -> bool:
        return _get_3d_particles_visible(self.__id)

    @visible.setter
    def visible(self, value: bool):
        _set_3d_particles_visible(self.__id, value)

    @property
    def x(self) -> float:
        return _get_3d_particles_x(self.__id)

    @property
    def y(self) -> float:
        return _get_3d_particles_y(self.__id)

    @property
    def z(self) -> float:
        return _get_3d_particles_z(self.__id)

    def set_position(self, x: float, y: float, z: float):
        return _set_3d_particles_position(self.__id, x, y, z)

    def set_color_interpolation(self, mode: InterpolationMode):
        _set_3d_particles_color_interpolation(self.__id, mode)

    def set_start_zone(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):
        _set_3d_particles_start_zone(self.__id, x1, y1, z1, x2, y2, z2)

    def set_transparency(self, mode: TransparencyMode):
        _set_3d_particles_transparency(self.__id, mode)

    def set_velocity_range(self, minimum: float, maximum: float):
        _set_3d_particles_velocity_range(self.__id, minimum, maximum)
