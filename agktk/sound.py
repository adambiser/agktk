"""
Contains classes for sound playback.
"""
from appgamekit import (
    # Sound > Creation
    delete_sound as _delete_sound,
    load_sound as _load_sound,
    load_sound_ogg as _load_sound_ogg,
    play_sound as _play_sound,
    save_sound as _save_sound,
    stop_sound as _stop_sound,
    # Sound > Properties
    # get_sound_exists, - not needed
    get_sound_instance_loop_count as _get_sound_instance_loop_count,
    get_sound_instance_playing as _get_sound_instance_playing,
    get_sound_instance_rate as _get_sound_instance_rate,
    get_sound_instance_volume as _get_sound_instance_volume,
    get_sound_instances as _get_sound_instances,
    # get_sound_max_rate as _get_sound_max_rate,  # see mixer
    # get_sound_min_rate as _get_sound_min_rate,  # see mixer
    # get_sounds_playing, - same as get_sound_instances
    set_sound_instance_balance as _set_sound_instance_balance,
    set_sound_instance_rate as _set_sound_instance_rate,
    set_sound_instance_volume as _set_sound_instance_volume,
    # set_sound_system_volume as _set_sound_system_volume,  # see mixer
    stop_sound_instance as _stop_sound_instance,
    # Memblock > Sound
    create_sound_from_memblock as _create_sound_from_memblock,
)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .memblock import Memblock


class SoundInstance(object):
    """Wraps sound instance functionality."""
    def __init__(self, instance_id: int):
        self.__id = instance_id
        self.__balance = 0.0

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def loop_count(self) -> int:
        return _get_sound_instance_loop_count(self.__id)

    @property
    def is_playing(self) -> bool:
        return _get_sound_instance_playing(self.__id)

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        self.__balance = value
        _set_sound_instance_balance(self.__id, value)

    @property
    def rate(self) -> float:
        return _get_sound_instance_rate(self.__id)

    @rate.setter
    def rate(self, value: float):
        _set_sound_instance_rate(self.__id, value)

    @property
    def volume(self) -> int:
        return _get_sound_instance_volume(self.__id)

    @volume.setter
    def volume(self, value: int):
        _set_sound_instance_volume(self.__id, value)

    def stop(self):
        _stop_sound_instance(self.__id)


class Sound(object):
    """Wraps sound functionality."""
    def __init__(self, filename: str, is_ogg: bool = False):
        self.__id = _load_sound_ogg(filename) if is_ogg else _load_sound(filename)

    def __del__(self):
        """Delete the object."""
        try:
            _delete_sound(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self):
        return self.__id

    @property
    def instance_count(self):
        return _get_sound_instances(self.__id)  # same as get_sounds_playing

    def play(self, volume: int = 100, loop: int = 0, priority: int = 0) -> SoundInstance:
        return SoundInstance(_play_sound(self.__id, volume, loop, priority))

    def save(self, filename: str):
        _save_sound(self.__id, filename)

    def stop(self):
        _stop_sound(self.__id)

    @classmethod
    def from_memblock(cls, memblock: "Memblock") -> "Sound":
        sound = Sound.__new__(Sound)
        sound.__id = _create_sound_from_memblock(memblock.id)
        return sound
