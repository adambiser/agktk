from appgamekit import (
    # Tweening > Chains
    add_tween_chain_camera as _add_tween_chain_camera,
    add_tween_chain_char as _add_tween_chain_char,
    add_tween_chain_custom as _add_tween_chain_custom,
    add_tween_chain_object as _add_tween_chain_object,
    add_tween_chain_sprite as _add_tween_chain_sprite,
    add_tween_chain_text as _add_tween_chain_text,
    clear_tween_chain as _clear_tween_chain,
    create_tween_chain as _create_tween_chain,
    delete_tween_chain as _delete_tween_chain,
    get_tween_chain_end_time as _get_tween_chain_end_time,
    get_tween_chain_playing as _get_tween_chain_playing,
    pause_tween_chain as _pause_tween_chain,
    play_tween_chain as _play_tween_chain,
    set_tween_chain_time as _set_tween_chain_time,
    stop_tween_chain as _stop_tween_chain,
    # Tweening > Objects
    create_tween_object as _create_tween_object,
    # get_tween_object_exists,  # not needed
    get_tween_object_playing as _get_tween_object_playing,
    pause_tween_object as _pause_tween_object,
    play_tween_object as _play_tween_object,
    resume_tween_object as _resume_tween_object,
    set_tween_object_alpha as _set_tween_object_alpha,
    set_tween_object_angle_x as _set_tween_object_angle_x,
    set_tween_object_angle_y as _set_tween_object_angle_y,
    set_tween_object_angle_z as _set_tween_object_angle_z,
    set_tween_object_blue as _set_tween_object_blue,
    set_tween_object_green as _set_tween_object_green,
    set_tween_object_red as _set_tween_object_red,
    set_tween_object_scale_x as _set_tween_object_scale_x,
    set_tween_object_scale_y as _set_tween_object_scale_y,
    set_tween_object_scale_z as _set_tween_object_scale_z,
    set_tween_object_x as _set_tween_object_x,
    set_tween_object_y as _set_tween_object_y,
    set_tween_object_z as _set_tween_object_z,
    stop_tween_object as _stop_tween_object,
    # Tweening > Char
    create_tween_char as _create_tween_char,
    # get_tween_char_exists,  # not needed
    get_tween_char_playing as _get_tween_char_playing,
    pause_tween_char as _pause_tween_char,
    play_tween_char as _play_tween_char,
    resume_tween_char as _resume_tween_char,
    set_tween_char_alpha as _set_tween_char_alpha,
    set_tween_char_angle as _set_tween_char_angle,
    set_tween_char_blue as _set_tween_char_blue,
    set_tween_char_green as _set_tween_char_green,
    set_tween_char_red as _set_tween_char_red,
    set_tween_char_x as _set_tween_char_x,
    set_tween_char_y as _set_tween_char_y,
    stop_tween_char as _stop_tween_char,
    # Tweening > General
    delete_tween as _delete_tween,
    # get_tween_exists,  # not needed
    set_tween_duration as _set_tween_duration,
    update_all_tweens,  # as _update_all_tweens,
    update_tween_camera as _update_tween_camera,
    update_tween_chain as _update_tween_chain,
    update_tween_char as _update_tween_char,
    update_tween_custom as _update_tween_custom,
    update_tween_object as _update_tween_object,
    update_tween_sprite as _update_tween_sprite,
    update_tween_text as _update_tween_text,
    # Tweening > Cameras
    create_tween_camera as _create_tween_camera,
    # get_tween_camera_exists,  # not needed
    get_tween_camera_playing as _get_tween_camera_playing,
    pause_tween_camera as _pause_tween_camera,
    play_tween_camera as _play_tween_camera,
    resume_tween_camera as _resume_tween_camera,
    set_tween_camera_angle_x as _set_tween_camera_angle_x,
    set_tween_camera_angle_y as _set_tween_camera_angle_y,
    set_tween_camera_angle_z as _set_tween_camera_angle_z,
    set_tween_camera_fov as _set_tween_camera_fov,
    set_tween_camera_x as _set_tween_camera_x,
    set_tween_camera_y as _set_tween_camera_y,
    set_tween_camera_z as _set_tween_camera_z,
    stop_tween_camera as _stop_tween_camera,
    # Tweening > Custom
    create_tween_custom as _create_tween_custom,
    # get_tween_custom_exists,  # not needed
    get_tween_custom_float1 as _get_tween_custom_float1,
    get_tween_custom_float2 as _get_tween_custom_float2,
    get_tween_custom_float3 as _get_tween_custom_float3,
    get_tween_custom_float4 as _get_tween_custom_float4,
    get_tween_custom_integer1 as _get_tween_custom_integer1,
    get_tween_custom_integer2 as _get_tween_custom_integer2,
    get_tween_custom_integer3 as _get_tween_custom_integer3,
    get_tween_custom_integer4 as _get_tween_custom_integer4,
    get_tween_custom_playing as _get_tween_custom_playing,
    pause_tween_custom as _pause_tween_custom,
    play_tween_custom as _play_tween_custom,
    resume_tween_custom as _resume_tween_custom,
    set_tween_custom_float1 as _set_tween_custom_float1,
    set_tween_custom_float2 as _set_tween_custom_float2,
    set_tween_custom_float3 as _set_tween_custom_float3,
    set_tween_custom_float4 as _set_tween_custom_float4,
    set_tween_custom_integer1 as _set_tween_custom_integer1,
    set_tween_custom_integer2 as _set_tween_custom_integer2,
    set_tween_custom_integer3 as _set_tween_custom_integer3,
    set_tween_custom_integer4 as _set_tween_custom_integer4,
    stop_tween_custom as _stop_tween_custom,
    # Tweening > Text
    create_tween_text as _create_tween_text,
    # get_tween_text_exists,  # not needed
    get_tween_text_playing as _get_tween_text_playing,
    pause_tween_text as _pause_tween_text,
    play_tween_text as _play_tween_text,
    resume_tween_text as _resume_tween_text,
    set_tween_text_alpha as _set_tween_text_alpha,
    set_tween_text_angle as _set_tween_text_angle,
    set_tween_text_blue as _set_tween_text_blue,
    set_tween_text_green as _set_tween_text_green,
    set_tween_text_line_spacing as _set_tween_text_line_spacing,
    set_tween_text_red as _set_tween_text_red,
    set_tween_text_size as _set_tween_text_size,
    set_tween_text_spacing as _set_tween_text_spacing,
    set_tween_text_x as _set_tween_text_x,
    set_tween_text_y as _set_tween_text_y,
    stop_tween_text as _stop_tween_text,
    # Tweening > Sprites
    create_tween_sprite as _create_tween_sprite,
    # get_tween_sprite_exists,  # not needed
    get_tween_sprite_playing as _get_tween_sprite_playing,
    pause_tween_sprite as _pause_tween_sprite,
    play_tween_sprite as _play_tween_sprite,
    resume_tween_sprite as _resume_tween_sprite,
    set_tween_sprite_alpha as _set_tween_sprite_alpha,
    set_tween_sprite_angle as _set_tween_sprite_angle,
    set_tween_sprite_blue as _set_tween_sprite_blue,
    set_tween_sprite_green as _set_tween_sprite_green,
    set_tween_sprite_red as _set_tween_sprite_red,
    set_tween_sprite_size_x as _set_tween_sprite_size_x,
    set_tween_sprite_size_y as _set_tween_sprite_size_y,
    set_tween_sprite_x as _set_tween_sprite_x,
    set_tween_sprite_x_by_offset as _set_tween_sprite_x_by_offset,
    set_tween_sprite_y as _set_tween_sprite_y,
    set_tween_sprite_y_by_offset as _set_tween_sprite_y_by_offset,
    stop_tween_sprite as _stop_tween_sprite,
)
from ._sprite import Sprite
from ._text import Text
# from .constants import (
#     # Tweening > Interpolation
#     TWEEN_BOUNCE,
#     TWEEN_EASE_IN1,
#     TWEEN_EASE_IN2,
#     TWEEN_EASE_OUT1,
#     TWEEN_EASE_OUT2,
#     TWEEN_LINEAR,
#     TWEEN_OVERSHOOT,
#     TWEEN_SMOOTH1,
#     TWEEN_SMOOTH2,
# )
from ._enums import TweenInterpolation


# TODO Implement
# class CameraTween(object):
#     """
#     A tween for manipulating cameras.
#     """
#     def __init__(self, duration: float):
#         self.__id = _create_tween_camera(duration)
#         self.__duration = duration
#
#     def __del__(self):
#         """Deletes the object."""
#         try:
#             _delete_tween(self.__id)
#         except TypeError:
#             pass
#
#     def __repr__(self):
#         return f"<{self.__class__.__name__}, id: {self.__id}>"
#
#     @property
#     def id(self) -> int:
#         """The internal ID for this object."""
#         return self.__id
#
#     @property
#     def duration(self) -> float:
#         return self.__duration
#
#     @duration.setter
#     def duration(self, value: float):
#         self.__duration = value
#         _set_tween_duration(self.__id, value)
#
#     def is_playing(self, camera: Camera) -> bool:
#         return _get_tween_camera_playing(self.__id, obj.id)
#
#     def pause(self, camera: Camera):
#         _pause_tween_camera(self.__id, camera.id)
#
#     def play(self, camera: Camera, delay: float = 0):
#         _play_tween_camera(self.__id, camera.id, delay)
#
#     def resume(self, camera: Camera):
#         _resume_tween_camera(self.__id, camera.id)
#
#     def stop(self, camera: Camera):
#         _stop_tween_camera(self.__id, camera.id)
#
#     def update(self, camera: Camera, time: float):
#         _update_tween_camera(self.__id, camera.id, time)
#
#     def set_angle_x(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_camera_angle_x(self.__id, begin, end, interpolation)
#
#     def set_angle_y(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_camera_angle_y(self.__id, begin, end, interpolation)
#
#     def set_angle_z(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_camera_angle_z(self.__id, begin, end, interpolation)
#
#     def set_fov(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_camera_fov(self.__id, begin, end, interpolation)
#
#     def set_x(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_camera_x(self.__id, begin, end, interpolation)
#
#     def set_y(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_camera_y(self.__id, begin, end, interpolation)
#
#     def set_z(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_camera_z(self.__id, begin, end, interpolation)


# TODO Implement
# class ObjectTween(object):
#     """
#     A tween for manipulating object models.
#     """
#     def __init__(self, duration: float):
#         self.__id = _create_tween_object(duration)
#         self.__duration = duration
#
#     def __del__(self):
#         """Deletes the object."""
#         try:
#             _delete_tween(self.__id)
#         except TypeError:
#             pass
#
#     def __repr__(self):
#         return f"<{self.__class__.__name__}, id: {self.__id}>"
#
#     @property
#     def id(self) -> int:
#         """The internal ID for this object."""
#         return self.__id
#
#     @property
#     def duration(self) -> float:
#         return self.__duration
#
#     @duration.setter
#     def duration(self, value: float):
#         self.__duration = value
#         _set_tween_duration(self.__id, value)
#
#     def is_playing(self, obj: ObjectModel) -> bool:
#         return _get_tween_object_playing(self.__id, obj.id)
#
#     def pause(self, obj: ObjectModel):
#         _pause_tween_object(self.__id, obj.id)
#
#     def play(self, obj: ObjectModel, delay: float = 0):
#         _play_tween_object(self.__id, obj.id, delay)
#
#     def resume(self, obj: ObjectModel):
#         _resume_tween_object(self.__id, obj.id)
#
#     def stop(self, obj: ObjectModel):
#         _stop_tween_object(self.__id, obj.id)
#
#     def update(self, obj: ObjectModel, time: float):
#         _update_tween_object(self.__id, obj.id, time)
#
#     def set_alpha(self, begin: int, end: int, interpolation: TweenInterpolation):
#         _set_tween_object_alpha(self.__id, begin, end, interpolation)
#
#     def set_blue(self, begin: int, end: int, interpolation: TweenInterpolation):
#         _set_tween_object_blue(self.__id, begin, end, interpolation)
#
#     def set_green(self, begin: int, end: int, interpolation: TweenInterpolation):
#         _set_tween_object_green(self.__id, begin, end, interpolation)
#
#     def set_red(self, begin: int, end: int, interpolation: TweenInterpolation):
#         _set_tween_object_red(self.__id, begin, end, interpolation)
#
#     def set_angle_x(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_angle_x(self.__id, begin, end, interpolation)
#
#     def set_angle_y(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_angle_y(self.__id, begin, end, interpolation)
#
#     def set_angle_z(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_angle_z(self.__id, begin, end, interpolation)
#
#     def set_scale_x(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_scale_x(self.__id, begin, end, interpolation)
#
#     def set_scale_y(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_scale_y(self.__id, begin, end, interpolation)
#
#     def set_scale_z(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_scale_z(self.__id, begin, end, interpolation)
#
#     def set_x(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_x(self.__id, begin, end, interpolation)
#
#     def set_y(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_y(self.__id, begin, end, interpolation)
#
#     def set_z(self, begin: float, end: float, interpolation: TweenInterpolation):
#         _set_tween_object_z(self.__id, begin, end, interpolation)


class CharTween(object):
    """
    A tween for manipulating text object characters.
    """
    def __init__(self, duration: float):
        self.__id = _create_tween_char(duration)
        self.__duration = duration

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_tween(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, value: float):
        self.__duration = value
        _set_tween_duration(self.__id, value)

    def is_playing(self, text: Text, char_index: int) -> bool:
        return _get_tween_char_playing(self.__id, text.id, char_index)

    def pause(self, text: Text, char_index: int):
        _pause_tween_char(self.__id, text.id, char_index)

    def play(self, text: Text, char_index: int, delay: float = 0):
        _play_tween_char(self.__id, text.id, char_index, delay)

    def resume(self, text: Text, char_index: int):
        _resume_tween_char(self.__id, text.id, char_index)

    def stop(self, text: Text, char_index: int):
        _stop_tween_char(self.__id, text.id, char_index)

    def update(self, text: Text, char_index: int, time: float):
        _update_tween_char(self.__id, text.id, char_index, time)

    def set_alpha(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_char_alpha(self.__id, begin, end, interpolation)

    def set_blue(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_char_blue(self.__id, begin, end, interpolation)

    def set_green(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_char_green(self.__id, begin, end, interpolation)

    def set_red(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_char_red(self.__id, begin, end, interpolation)

    def set_angle(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_char_angle(self.__id, begin, end, interpolation)

    def set_x(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_char_x(self.__id, begin, end, interpolation)

    def set_y(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_char_y(self.__id, begin, end, interpolation)


class CustomTween(object):
    """
    A tween for manipulating custom numeric values.
    """
    def __init__(self, duration: float):
        self.__id = _create_tween_custom(duration)
        self.__duration = duration

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_tween(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, value: float):
        self.__duration = value
        _set_tween_duration(self.__id, value)

    # Not a @property so it matches other tween classes.
    def is_playing(self) -> bool:
        return _get_tween_custom_playing(self.__id)

    def pause(self):
        _pause_tween_custom(self.__id)

    def play(self, delay: float = 0):
        _play_tween_custom(self.__id, delay)

    def resume(self):
        _resume_tween_custom(self.__id)

    def stop(self):
        _stop_tween_custom(self.__id)

    def update(self, time: float):
        _update_tween_custom(self.__id, time)

    @property
    def float1(self) -> float:
        return _get_tween_custom_float1(self.__id)

    def set_float1(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_custom_float1(self.__id, begin, end, interpolation)

    @property
    def float2(self) -> float:
        return _get_tween_custom_float2(self.__id)

    def set_float2(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_custom_float2(self.__id, begin, end, interpolation)

    @property
    def float3(self) -> float:
        return _get_tween_custom_float3(self.__id)

    def set_float3(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_custom_float3(self.__id, begin, end, interpolation)

    @property
    def float4(self) -> float:
        return _get_tween_custom_float4(self.__id)

    def set_float4(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_custom_float4(self.__id, begin, end, interpolation)

    @property
    def integer1(self) -> int:
        return _get_tween_custom_integer1(self.__id)

    def set_integer1(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_custom_integer1(self.__id, begin, end, interpolation)

    @property
    def integer2(self) -> int:
        return _get_tween_custom_integer2(self.__id)

    def set_integer2(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_custom_integer2(self.__id, begin, end, interpolation)

    @property
    def integer3(self) -> int:
        return _get_tween_custom_integer3(self.__id)

    def set_integer3(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_custom_integer3(self.__id, begin, end, interpolation)

    @property
    def integer4(self) -> int:
        return _get_tween_custom_integer4(self.__id)

    def set_integer4(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_custom_integer4(self.__id, begin, end, interpolation)


class TextTween(object):
    """
    A tween for manipulating text objects.
    """
    def __init__(self, duration: float):
        self.__id = _create_tween_text(duration)
        self.__duration = duration

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_tween(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, value: float):
        self.__duration = value
        _set_tween_duration(self.__id, value)

    def is_playing(self, text: Text) -> bool:
        return _get_tween_text_playing(self.__id, text.id)

    def pause(self, text: Text):
        _pause_tween_text(self.__id, text.id)

    def play(self, text: Text, delay: float = 0):
        _play_tween_text(self.__id, text.id, delay)

    def resume(self, text: Text):
        _resume_tween_text(self.__id, text.id)

    def stop(self, text: Text):
        _stop_tween_text(self.__id, text.id)

    def update(self, text: Text, time: float):
        _update_tween_text(self.__id, text.id, time)

    def set_alpha(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_text_alpha(self.__id, begin, end, interpolation)

    def set_blue(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_text_blue(self.__id, begin, end, interpolation)

    def set_green(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_text_green(self.__id, begin, end, interpolation)

    def set_red(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_text_red(self.__id, begin, end, interpolation)

    def set_angle(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_text_angle(self.__id, begin, end, interpolation)

    def set_line_spacing(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_text_line_spacing(self.__id, begin, end, interpolation)

    def set_size(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_text_size(self.__id, begin, end, interpolation)

    def set_spacing(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_text_spacing(self.__id, begin, end, interpolation)

    def set_x(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_text_x(self.__id, begin, end, interpolation)

    def set_y(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_text_y(self.__id, begin, end, interpolation)


class SpriteTween(object):
    """
    A tween for manipulating sprites.
    """
    def __init__(self, duration: float):
        self.__id = _create_tween_sprite(duration)
        self.__duration = duration

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_tween(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, value: float):
        self.__duration = value
        _set_tween_duration(self.__id, value)

    def is_playing(self, sprite: Sprite) -> bool:
        return _get_tween_sprite_playing(self.__id, sprite.id)

    def pause(self, sprite: Sprite):
        _pause_tween_sprite(self.__id, sprite.id)

    def play(self, sprite: Sprite, delay: float = 0):
        _play_tween_sprite(self.__id, sprite.id, delay)

    def resume(self, sprite: Sprite):
        _resume_tween_sprite(self.__id, sprite.id)

    def stop(self, sprite: Sprite):
        _stop_tween_sprite(self.__id, sprite.id)

    def update(self, sprite: Sprite, time: float):
        _update_tween_sprite(self.__id, sprite.id, time)

    def set_alpha(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_sprite_alpha(self.__id, begin, end, interpolation)

    def set_blue(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_sprite_blue(self.__id, begin, end, interpolation)

    def set_green(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_sprite_green(self.__id, begin, end, interpolation)

    def set_red(self, begin: int, end: int, interpolation: TweenInterpolation):
        _set_tween_sprite_red(self.__id, begin, end, interpolation)

    def set_angle(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_sprite_angle(self.__id, begin, end, interpolation)

    def set_size_x(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_sprite_size_x(self.__id, begin, end, interpolation)

    def set_size_y(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_sprite_size_y(self.__id, begin, end, interpolation)

    def set_x(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_sprite_x(self.__id, begin, end, interpolation)

    def set_y(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_sprite_y(self.__id, begin, end, interpolation)

    def set_x_by_offset(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_sprite_x_by_offset(self.__id, begin, end, interpolation)

    def set_y_by_offset(self, begin: float, end: float, interpolation: TweenInterpolation):
        _set_tween_sprite_y_by_offset(self.__id, begin, end, interpolation)


class TweenChain(object):
    """
    Chains tweens together.
    """
    def __init__(self):
        self.__id = _create_tween_chain()
        self.__tweens = []  # Stores tween refs.

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_tween_chain(self.__id)
            self.__tweens.clear()
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def is_playing(self) -> bool:
        return _get_tween_chain_playing(self.__id)

    def pause(self):
        _pause_tween_chain(self.__id)

    def play(self):
        _play_tween_chain(self.__id)

    def stop(self):
        _stop_tween_chain(self.__id)

    def update(self, time: float):
        _update_tween_chain(self.__id, time)

    def clear(self):
        _clear_tween_chain(self.__id)
        self.__tweens.clear()

    @property
    def end_time(self) -> float:
        return _get_tween_chain_end_time(self.__id)

    def set_time(self, time: float):
        _set_tween_chain_time(self.__id, time)

    # TODO Implement
    # def add_camera_tween(self, tween: CameraTween, camera: Camera, delay: float = 0):
    #     self.__tweens.append(tween)
    #     _add_tween_chain_camera(self.__id, tween.id, camera.id, delay)

    def add_char_tween(self, tween: CharTween, text: Text, char_index: int, delay: float = 0):
        self.__tweens.append(tween)
        _add_tween_chain_char(self.__id, tween.id, text.id, char_index, delay)

    def add_custom_tween(self, tween: CustomTween, delay: float = 0):
        self.__tweens.append(tween)
        _add_tween_chain_custom(self.__id, tween.id, delay)

    # TODO Implement
    # def add_object_tween(self, tween: ObjectTween, object_model: ObjectModel, delay: float = 0):
    #     self.__tweens.append(tween)
    #     _add_tween_chain_object(self.__id, tween.id, object_model.id, delay)

    def add_sprite_tween(self, tween: SpriteTween, sprite: Sprite, delay: float = 0):
        self.__tweens.append(tween)
        _add_tween_chain_sprite(self.__id, tween.id, sprite.id, delay)

    def add_text_tween(self, tween: TextTween, text: Text, delay: float = 0):
        self.__tweens.append(tween)
        _add_tween_chain_text(self.__id, tween.id, text.id, delay)
