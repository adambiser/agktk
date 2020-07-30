"""
Contains video functions.
"""

# noinspection PyUnresolvedReferences
from appgamekit import (
    # Video > Youtube
    play_youtube_video as _play_youtube_video,
    # Video > Recording
    # is_screen_recording as _is_screen_recording,  # iOS and Android only
    # start_screen_recording as _start_screen_recording,  # iOS and Android only
    # stop_screen_recording as _stop_screen_recording,  # iOS and Android only
    # Video > General
    delete_video as delete,
    get_video_duration as get_duration,
    get_video_height as get_height,
    get_video_playing as is_playing,
    get_video_position as get_position,
    get_video_width as get_width,
    load_video as _load_video,
    pause_video as pause,
    play_video as _play_video,
    play_video_to_image as _play_video_to_image,
    set_video_dimensions as set_dimensions,
    set_video_position as set_position,
    set_video_volume as set_volume,
    stop_video as stop,
)
from .enums import VideoLoadResult
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .image import Image


def play_youtube_video(video_id: str, start_time: float = 0):
    _play_youtube_video("", video_id, start_time)


def load(filename: str) -> VideoLoadResult:
    return VideoLoadResult(_load_video(filename))


def play(image: "Image" = None):
    if image:
        _play_video_to_image(image.id)
    else:
        _play_video()

