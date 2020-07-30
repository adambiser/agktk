"""
Emulated pointer functions.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input > Pointer
    get_pointer_pressed as is_pressed,
    get_pointer_released as is_released,
    get_pointer_state as _get_pointer_state,
    get_pointer_x as get_x,
    get_pointer_y as get_y,
)
from ...constants import (
    STATE_UP as _STATE_UP,
    STATE_DOWN as _STATE_DOWN,
)


def is_down() -> bool:
    """Returns True if the pointer is currently down."""
    return _get_pointer_state() == _STATE_DOWN


def is_up() -> bool:
    """Returns True if the pointer is currently up."""
    return _get_pointer_state() == _STATE_UP

