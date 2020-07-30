"""
Emulated joystick functions.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input > Joystick
    get_joystick_x as get_x,
    get_joystick_y as get_y,
    set_joystick_dead_zone as set_dead_zone,
    set_joystick_screen_position as set_screen_position,
    # Input > Button
    get_button_pressed as is_button_pressed,
    get_button_released as is_button_released,
    get_button_state as _get_button_state,
    set_button_screen_position,
)
from ...constants import (
    STATE_UP as _STATE_UP,
    STATE_DOWN as _STATE_DOWN,
)


def is_button_down(button_id: int) -> bool:
    """Returns True if the button is currently down."""
    return _get_button_state(button_id) == _STATE_DOWN


def is_button_up(button_id: int) -> bool:
    """Returns True if the button is currently up."""
    return _get_button_state(button_id) == _STATE_UP
