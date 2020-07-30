from appgamekit import (
    # Skeleton > 2D
    create_skeleton_2d as _create_skeleton_2d,
    delete_skeleton_2d as _delete_skeleton_2d,
    fix_skeleton_2d_to_screen as _fix_skeleton_2d_to_screen,
    fix_sprite_to_skeleton_2d as _fix_sprite_to_skeleton_2d,
    get_skeleton_2d_angle as _get_skeleton_2d_angle,
    get_skeleton_2d_animation_time as _get_skeleton_2d_animation_time,
    get_skeleton_2d_bone as _get_skeleton_2d_bone,
    get_skeleton_2d_bone_angle as _get_skeleton_2d_bone_angle,
    get_skeleton_2d_bone_curr_angle as _get_skeleton_2d_bone_curr_angle,
    get_skeleton_2d_bone_curr_x as _get_skeleton_2d_bone_curr_x,
    get_skeleton_2d_bone_curr_y as _get_skeleton_2d_bone_curr_y,
    get_skeleton_2d_bone_parent as _get_skeleton_2d_bone_parent,
    get_skeleton_2d_bone_x as _get_skeleton_2d_bone_x,
    get_skeleton_2d_bone_y as _get_skeleton_2d_bone_y,
    get_skeleton_2d_current_time as _get_skeleton_2d_current_time,
    get_skeleton_2d_depth as _get_skeleton_2d_depth,
    # get_skeleton_2d_exists,  # Not needed
    get_skeleton_2d_is_animating as _get_skeleton_2d_is_animating,
    get_skeleton_2d_is_tweening as _get_skeleton_2d_is_tweening,
    get_skeleton_2d_x as _get_skeleton_2d_x,
    get_skeleton_2d_y as _get_skeleton_2d_y,
    load_skeleton_2d_from_spine_file as _load_skeleton_2d_from_spine_file,
    load_skeleton_2d_from_spriter_file as _load_skeleton_2d_from_spriter_file,
    play_skeleton_2d_animation as _play_skeleton_2d_animation,
    set_skeleton_2d_animation_frame as _set_skeleton_2d_animation_frame,
    set_skeleton_2d_animation_speed as _set_skeleton_2d_animation_speed,
    set_skeleton_2d_bone_angle as _set_skeleton_2d_bone_angle,
    set_skeleton_2d_bone_mode as _set_skeleton_2d_bone_mode,
    set_skeleton_2d_bone_position as _set_skeleton_2d_bone_position,
    set_skeleton_2d_bone_scale as _set_skeleton_2d_bone_scale,
    set_skeleton_2d_depth as _set_skeleton_2d_depth,
    set_skeleton_2d_flip as _set_skeleton_2d_flip,
    set_skeleton_2d_position as _set_skeleton_2d_position,
    set_skeleton_2d_rotation as _set_skeleton_2d_rotation,
    set_skeleton_2d_visible as _set_skeleton_2d_visible,
    stop_skeleton_2d_animation as _stop_skeleton_2d_animation,
)
from enum import IntEnum as _IntEnum, auto as _auto
from ._image import Image
from ._sprite import Sprite
import weakref


class Skeleton2DFileType(_IntEnum):
    SPINE = _auto()
    SPRITER = _auto()


class Bone(object):
    def __init__(self, skeleton: "Skeleton2D", bone_id: int):
        self.__skeleton = skeleton
        self.__skeleton_id = skeleton.id
        self.__id = bone_id

    def __repr__(self):
        return f"<{self.__class__.__name__}, skeleton_id: {self.__skeleton_id}, bone_id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def skeleton_id(self) -> int:
        """The internal ID for this object."""
        return self.__skeleton_id

    @property
    def parent(self) -> "Bone":
        # return self.__skeleton.bones[_get_skeleton_2d_bone_parent(self.__skeleton_id, self.__id)]
        return self.__skeleton.get_bone(_get_skeleton_2d_bone_parent(self.__skeleton_id, self.__id))

    def attach_sprite(self, sprite: Sprite, zorder: int = 0):
        # Use Sprite.detach_from_skeleton() to remove.
        _fix_sprite_to_skeleton_2d(sprite.id, self.__skeleton_id, self.__id, zorder)

    @property
    def angle(self) -> float:
        return _get_skeleton_2d_bone_angle(self.__skeleton_id, self.__id)

    @angle.setter
    def angle(self, value: float):
        _set_skeleton_2d_bone_angle(self.__skeleton_id, self.__id, value)

    @property
    def x(self) -> float:
        return _get_skeleton_2d_bone_x(self.__skeleton_id, self.__id)

    @property
    def y(self) -> float:
        return _get_skeleton_2d_bone_y(self.__skeleton_id, self.__id)

    def set_position(self, x: float, y: float):
        _set_skeleton_2d_bone_position(self.__skeleton_id, self.__id, x, y)

    def set_scale(self, x: float, y: float):
        _set_skeleton_2d_bone_scale(self.__skeleton_id, self.__id, x, y)

    def set_animate(self, enabled: bool):
        _set_skeleton_2d_bone_mode(self.__skeleton_id, self.__id, enabled)

    @property
    def current_angle(self) -> float:
        return _get_skeleton_2d_bone_curr_angle(self.__skeleton_id, self.__id)

    @property
    def current_x(self) -> float:
        return _get_skeleton_2d_bone_curr_x(self.__skeleton_id, self.__id)

    @property
    def current_y(self) -> float:
        return _get_skeleton_2d_bone_curr_y(self.__skeleton_id, self.__id)


# class _BoneList(object):
#     def __init__(self, skeleton: "Skeleton2D"):
#         self.__skeleton = weakref.proxy(skeleton)
#         self.__skeleton_id = skeleton.id
#
#     def __getitem__(self, item):
#         try:
#             index = _get_skeleton_2d_bone(self.__skeleton_id, item)
#         except TypeError:
#             index = item
#         if index < 0:
#             return None
#         return Bone(self.__skeleton, index)


class Skeleton2D(object):
    """
    Wraps AppGameKit skeleton 2d methods.
    """
    class FileType(_IntEnum):
        test = 0

    def __init__(self, filename: str, file_type: Skeleton2DFileType,
                 scale: float = 1.0, atlas_image: Image = None, load_animation: bool = True):
        if file_type == Skeleton2DFileType.SPINE:
            if not atlas_image:
                raise ValueError("Spine files require an atlas_image.")
            self.__id = _load_skeleton_2d_from_spine_file(filename, scale, atlas_image.id, load_animation)
        elif file_type == Skeleton2DFileType.SPRITER:
            self.__id = _load_skeleton_2d_from_spriter_file(filename, scale, 0)
        else:
            self.__id = _create_skeleton_2d()
        self.__fixed_to_screen = False
        self.__atlas_image = atlas_image
        self.__visible = True
        # self.__bones = _BoneList(self)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_skeleton_2d(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    # @property
    # def bones(self):
    #     return self.__bones

    def get_bone(self, item):
        try:
            index = _get_skeleton_2d_bone(self.__id, item)
        except TypeError:
            index = item
        if index < 0:
            return None
        return Bone(weakref.proxy(self), index)

    # @classmethod
    # def _from_id(cls, skeleton_id, atlas_image: Image = None):
    #     s = cls.__new__(cls)
    #     s.__id = skeleton_id
    #     s.__fixed_to_screen = False
    #     s.__atlas_image = atlas_image
    #     s.__visible = True
    #     s.__bones = _BoneList(s)
    #     return s
    #
    # @classmethod
    # def from_spine_file(cls, filename: str, scale: float, atlas_image: Image, load_animation: bool) -> "Skeleton2D":
    #     return cls._from_id(_load_skeleton_2d_from_spine_file(filename, scale, atlas_image.id, load_animation),
    #                         atlas_image)
    #
    # @classmethod
    # def from_spriter_file(cls, filename: str, scale: float) -> "Skeleton2D":
    #     return cls._from_id(_load_skeleton_2d_from_spriter_file(filename, scale))

    @property
    def fixed_to_screen(self) -> bool:
        """Returns or sets whether the sprite is fixed to screen coordinates rather than world coordinates."""
        return self.__fixed_to_screen

    @fixed_to_screen.setter
    def fixed_to_screen(self, value: bool):
        self.__fixed_to_screen = value
        _fix_skeleton_2d_to_screen(self.__id, value)

    @property
    def angle(self) -> float:
        return _get_skeleton_2d_angle(self.__id)

    @angle.setter
    def angle(self, value: float):
        _set_skeleton_2d_rotation(self.__id, value)

    def get_animation_time(self, name: str) -> float:
        return _get_skeleton_2d_animation_time(self.__id, name)

    @property
    def current_time(self) -> float:
        return _get_skeleton_2d_current_time(self.__id)

    @property
    def depth(self) -> int:
        return _get_skeleton_2d_depth(self.__id)

    @depth.setter
    def depth(self, value: int):
        _set_skeleton_2d_depth(self.__id, value)

    @property
    def is_animating(self) -> bool:
        return _get_skeleton_2d_is_animating(self.__id)

    @property
    def is_tweening(self) -> bool:
        return _get_skeleton_2d_is_tweening(self.__id)

    @property
    def x(self) -> float:
        return _get_skeleton_2d_x(self.__id)

    @property
    def y(self) -> float:
        return _get_skeleton_2d_y(self.__id)

    def set_position(self, x: float, y: float):
        _set_skeleton_2d_position(self.__id, x, y)

    def play_animation(self, name: str, start_time: float = 0, loop: int = 0, tween_time: float = 0):
        _play_skeleton_2d_animation(self.__id, name, start_time, loop, tween_time)

    def stop_animation(self):
        _stop_skeleton_2d_animation(self.__id)

    def set_animation_frame(self, name: str, time: float, tween_time: float):
        _set_skeleton_2d_animation_frame(self.__id, name, time, tween_time)

    def set_animation_speed(self, speed: float):
        _set_skeleton_2d_animation_speed(self.__id, speed)

    def set_flip(self, horizontal: bool, vertical: bool):
        _set_skeleton_2d_flip(self.__id, horizontal, vertical)

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, value: bool):
        self.__visible = value
        _set_skeleton_2d_visible(self.__id, value)

    # fix_sprite_to_skeleton_2d as _fix_sprite_to_skeleton_2d,
    # get_skeleton_2d_bone as _get_skeleton_2d_bone,
    # get_skeleton_2d_bone_angle as _get_skeleton_2d_bone_angle,
    # get_skeleton_2d_bone_curr_angle as _get_skeleton_2d_bone_curr_angle,
    # get_skeleton_2d_bone_curr_x as _get_skeleton_2d_bone_curr_x,
    # get_skeleton_2d_bone_curr_y as _get_skeleton_2d_bone_curr_y,
    # get_skeleton_2d_bone_parent as _get_skeleton_2d_bone_parent,
    # get_skeleton_2d_bone_x as _get_skeleton_2d_bone_x,
    # get_skeleton_2d_bone_y as _get_skeleton_2d_bone_y,
    #
    # set_skeleton_2d_bone_angle as _set_skeleton_2d_bone_angle,
    # set_skeleton_2d_bone_mode as _set_skeleton_2d_bone_mode,
    # set_skeleton_2d_bone_position as _set_skeleton_2d_bone_position,
    # set_skeleton_2d_bone_scale as _set_skeleton_2d_bone_scale,
