"""
Contains classes to use for music playback.
"""
from appgamekit import (
    # Music > OGG
    delete_music_ogg as _delete_music_ogg,
    get_music_duration_ogg as _get_music_duration_ogg,
    # get_music_exists_ogg,  # Not needed
    get_music_loop_count_ogg as _get_music_loop_count_ogg,
    get_music_playing_ogg as _get_music_playing_ogg,
    get_music_position_ogg as _get_music_position_ogg,
    load_music_ogg as _load_music_ogg,
    pause_music_ogg as _pause_music_ogg,
    play_music_ogg as _play_music_ogg,
    resume_music_ogg as _resume_music_ogg,
    seek_music_ogg as _seek_music_ogg,
    set_music_loop_count_ogg as _set_music_loop_count_ogg,
    set_music_loop_times_ogg as _set_music_loop_times_ogg,
    # set_music_system_volume_ogg,  # See mixer.
    set_music_volume_ogg as _set_music_volume_ogg,
    stop_music_ogg as _stop_music_ogg,
)
from . import mixer
# noinspection PyUnresolvedReferences
from ._constants import (
    SEEK_ABSOLUTE,
    SEEK_RELATIVE,
)


class Music(object):
    """Wraps OGG music functionality."""
    __is_first_instance = True

    def __init__(self, filename: str):
        self.__id = _load_music_ogg(filename)
        self.__volume = 100
        # Hack because calling set_music_system_volume_ogg before loading any music doesn't work.
        # if Music.__is_first_instance and MusicSystem.volume != 100:
        #     Music.__is_first_instance = False
        #     MusicSystem.volume = MusicSystem.volume
        if Music.__is_first_instance:
            mixer.refresh()

    def __del__(self):
        """Delete the object."""
        try:
            _delete_music_ogg(self.__id)
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
        """The duration of the song in seconds."""
        return _get_music_duration_ogg(self.__id)

    # GetMusicExistsOGG

    @property
    def loop_count(self) -> int:
        """Returns the number of times this music file has looped."""
        return _get_music_loop_count_ogg(self.__id)

    @loop_count.setter
    def loop_count(self, loop: int) -> None:
        """Changes the number of times the music file will loop.
        1 to loop indefinitely.
        0 to stop after current playback.
        """
        _set_music_loop_count_ogg(self.__id, loop)

    @property
    def is_playing(self) -> bool:
        """Returns True if the music file is playing; otherwise False."""
        return _get_music_playing_ogg(self.__id)

    @property
    def position(self) -> float:
        """Returns the current position in the music file."""
        return _get_music_position_ogg(self.__id)

    def pause(self) -> None:
        """Pauses the music playback (is_playing will still report True)."""
        _pause_music_ogg(self.__id)

    def play(self, loop: int = 1) -> None:
        """Plays the music file with an optional loop count.  A loop count of 1 loops indefinitely."""
        _play_music_ogg(self.__id, loop)

    def resume(self) -> None:
        """Resumes the music file if paused."""
        _resume_music_ogg(self.__id)

    def seek(self, seconds: float, mode: int = SEEK_ABSOLUTE) -> None:
        """Seeks to the position in the music file."""
        _seek_music_ogg(self.__id, seconds, mode)

    def set_loop_times(self, start_time: float, end_time: float) -> None:
        """Sets the start and end times of the music loop."""
        _set_music_loop_times_ogg(self.__id, start_time, end_time)

    # @staticmethod
    # def set_system_volume(volume: int) -> None:
    #     """Sets the master volume for all OGG music files."""
    #     set_music_system_volume_ogg(volume)

    @property
    def volume(self) -> int:
        return self.__volume

    @volume.setter
    def volume(self, value: int) -> None:
        """Sets the volume for this music files."""
        self.__volume = value
        _set_music_volume_ogg(self.__id, value)

    def stop(self) -> None:
        """Stops the music file and resets its position to the beginning of the file."""
        _stop_music_ogg(self.__id)
