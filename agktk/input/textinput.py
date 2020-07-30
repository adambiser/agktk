"""
Text entry.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input > Text Input
    # get_last_char,  # Moved to keyboard.
    get_text_input as get_text,
    get_text_input_cancelled as is_cancelled,
    get_text_input_completed as is_completed,
    get_text_input_state as _get_text_input_state,
    set_cursor_blink_time,
    set_text_input_max_chars as set_max_chars,
    start_text_input as start,
    stop_text_input as stop,
    sync as _sync,
)
from ..constants import (
    INPUT_TEXT_ACTIVE as _INPUT_TEXT_ACTIVE,
    # INPUT_TEXT_DONE as _INPUT_TEXT_DONE,
)
from typing import Optional

STATE_INACTIVE = 0
STATE_ACTIVE = 1  # User is inputting text.
STATE_COMPLETED = 2  # User
STATE_CANCELLED = 3


def is_active() -> bool:
    return _get_text_input_state() == 0  # 0 if the user is currently inputting text, 1 if not.


def get_result() -> int:
    if is_completed():
        return STATE_CANCELLED if is_cancelled() else STATE_COMPLETED
    return STATE_ACTIVE if _get_text_input_state() == _INPUT_TEXT_ACTIVE else STATE_INACTIVE


def get_user_input(initial_text: str = None, sync_function: callable = None) -> Optional[str]:
    """
    A function that performs all text input functionality and returns the result.

    :param initial_text: The initial text for the input.
    :param sync_function: The function to call each frame (should call `sync`).  If not given, `sync` is called.
    :returns: The inputted text from the user or None if cancelled.
    """
    if not sync_function:
        sync_function = _sync
    start(initial_text)
    while not is_completed():
        sync_function()
    cancelled = is_cancelled()
    # Sync again to clear frame state values.
    sync_function()
    return None if cancelled else get_text()
