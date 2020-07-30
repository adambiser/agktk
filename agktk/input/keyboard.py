"""
Raw keyboard functionality.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input-Raw > Existence
    get_keyboard_exists as _get_keyboard_exists,
    # Input > Text Input
    get_last_char,
    # Input-Raw > Keyboard
    get_char_buffer,
    get_char_buffer_length,
    get_raw_key_pressed as is_key_pressed,
    get_raw_key_released as is_key_released,
    get_raw_key_state as _get_raw_key_state,
    get_raw_last_key as get_last_key,
)
# noinspection PyUnresolvedReferences
from ..constants import (
    STATE_UP as _STATE_UP,
    STATE_DOWN as _STATE_DOWN,
    KEYBOARD_NONE as _KEYBOARD_NONE,
    KEYBOARD_FULL_SIZE as _KEYBOARD_FULL_SIZE,
    KEYBOARD_VIRTUAL as _KEYBOARD_VIRTUAL,
)


def exists() -> bool:
    return _get_keyboard_exists() != _KEYBOARD_NONE


def is_full_size() -> bool:
    return _get_keyboard_exists() == _KEYBOARD_FULL_SIZE


def is_virtual() -> bool:
    return _get_keyboard_exists() == _KEYBOARD_VIRTUAL


def is_key_down(key: int) -> bool:
    """Returns True if the key is currently down."""
    return _get_raw_key_state(key) == _STATE_DOWN


def is_key_up(key: int) -> bool:
    """Returns True if the key is currently up."""
    return _get_raw_key_state(key) == _STATE_UP
