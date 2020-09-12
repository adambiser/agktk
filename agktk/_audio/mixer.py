"""
The device sound and music mixer.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Music > OGG
    set_music_system_volume_ogg as _set_music_system_volume_ogg,
    # Sound > Properties
    get_sound_max_rate,
    get_sound_min_rate,
    set_sound_system_volume as _set_sound_system_volume,
)

# Hack because calling set_music_system_volume_ogg before loading any music doesn't work.
__music_volume = 100  # type: int
__sound_volume = 100  # type: int


def get_music_volume():
    return __music_volume


def set_music_volume(volume: int):
    global __music_volume
    __music_volume = volume
    _set_music_system_volume_ogg(volume)


def get_sound_volume():
    return __sound_volume


def set_sound_volume(volume: int):
    global __sound_volume
    __sound_volume = volume
    _set_sound_system_volume(volume)


def refresh():
    """Generally not needed.  Only used by the hack in Music.__init__."""
    _set_music_system_volume_ogg(__music_volume)
