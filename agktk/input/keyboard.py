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
    get_raw_key_pressed as _get_raw_key_pressed,
    get_raw_key_released as _get_raw_key_released,
    get_raw_key_state as _get_raw_key_state,
    get_raw_last_key as _get_raw_last_key,
)
# noinspection PyUnresolvedReferences
from .._constants import (
    STATE_UP as _STATE_UP,
    STATE_DOWN as _STATE_DOWN,
    KEYBOARD_NONE as _KEYBOARD_NONE,
    KEYBOARD_FULL_SIZE as _KEYBOARD_FULL_SIZE,
    KEYBOARD_VIRTUAL as _KEYBOARD_VIRTUAL,
)
from .._enums import Key


def exists() -> bool:
    return _get_keyboard_exists() != _KEYBOARD_NONE


def is_full_size() -> bool:
    return _get_keyboard_exists() == _KEYBOARD_FULL_SIZE


def is_virtual() -> bool:
    return _get_keyboard_exists() == _KEYBOARD_VIRTUAL


def is_key_pressed(key: Key) -> bool:
    return _get_raw_key_pressed(key)


def is_key_released(key: Key) -> bool:
    return _get_raw_key_released(key)


def is_key_down(key: Key) -> bool:
    """Returns True if the key is currently down."""
    return _get_raw_key_state(key) == _STATE_DOWN


def is_key_up(key: Key) -> bool:
    """Returns True if the key is currently up."""
    return _get_raw_key_state(key) == _STATE_UP


def get_last_key() -> Key:
    return Key(_get_raw_last_key())
