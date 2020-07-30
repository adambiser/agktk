"""
Raw mouse functionality.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input-Raw > Existence
    get_mouse_exists as exists,
    # Input-Raw > Mouse
    get_raw_mouse_fifth_pressed as is_fifth_button_pressed,
    get_raw_mouse_fifth_released as is_fifth_button_released,
    get_raw_mouse_fifth_state as _get_raw_mouse_fifth_state,
    get_raw_mouse_fourth_pressed as is_fourth_button_pressed,
    get_raw_mouse_fourth_released as is_fourth_button_released,
    get_raw_mouse_fourth_state as _get_raw_mouse_fourth_state,
    get_raw_mouse_left_pressed as is_left_button_pressed,
    get_raw_mouse_left_released as is_left_button_released,
    get_raw_mouse_left_state as _get_raw_mouse_left_state,
    get_raw_mouse_middle_pressed as is_middle_button_pressed,
    get_raw_mouse_middle_released as is_middle_button_released,
    get_raw_mouse_middle_state as _get_raw_mouse_middle_state,
    get_raw_mouse_right_pressed as is_right_button_pressed,
    get_raw_mouse_right_released as is_right_button_released,
    get_raw_mouse_right_state as _get_raw_mouse_right_state,
    get_raw_mouse_wheel as get_mouse_wheel,
    get_raw_mouse_wheel_delta as get_mouse_wheel_delta,
    get_raw_mouse_x as get_x,
    get_raw_mouse_y as get_y,
    set_raw_mouse_position as set_position,
    set_raw_mouse_visible as set_visible,
)
from .._constants import (
    STATE_UP as _STATE_UP,
    STATE_DOWN as _STATE_DOWN,
)


def get_position():
    return get_x(), get_y()


def is_fifth_button_down() -> bool:
    return _get_raw_mouse_fifth_state() == _STATE_DOWN


def is_fifth_button_up() -> bool:
    return _get_raw_mouse_fifth_state() == _STATE_UP


def is_fourth_button_down() -> bool:
    return _get_raw_mouse_fourth_state() == _STATE_DOWN


def is_fourth_button_up() -> bool:
    return _get_raw_mouse_fourth_state() == _STATE_UP


def is_left_button_down() -> bool:
    return _get_raw_mouse_left_state() == _STATE_DOWN


def is_left_button_up() -> bool:
    return _get_raw_mouse_left_state() == _STATE_UP


def is_middle_button_down() -> bool:
    return _get_raw_mouse_middle_state() == _STATE_DOWN


def is_middle_button_up() -> bool:
    return _get_raw_mouse_middle_state() == _STATE_UP


def is_right_button_down() -> bool:
    return _get_raw_mouse_right_state() == _STATE_DOWN


def is_right_button_up() -> bool:
    return _get_raw_mouse_right_state() == _STATE_UP
