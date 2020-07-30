"""
Raw mouse functionality.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input-Raw > Existence
    get_multi_touch_exists as exists,
    # Input-Raw > Multitouch
    get_raw_first_touch_event as _get_raw_first_touch_event,
    get_raw_next_touch_event as _get_raw_next_touch_event,
    get_raw_touch_count as _get_raw_touch_count,
    get_raw_touch_current_x as _get_raw_touch_current_x,
    get_raw_touch_current_y as _get_raw_touch_current_y,
    get_raw_touch_last_x as _get_raw_touch_last_x,
    get_raw_touch_last_y as _get_raw_touch_last_y,
    get_raw_touch_released as _get_raw_touch_released,
    get_raw_touch_start_x as _get_raw_touch_start_x,
    get_raw_touch_start_y as _get_raw_touch_start_y,
    get_raw_touch_time as _get_raw_touch_time,
    get_raw_touch_type as _get_raw_touch_type,
    get_raw_touch_value as _get_raw_touch_value,
    set_raw_touch_move_sensitivity as set_move_sensitivity,
    set_raw_touch_value as _set_raw_touch_value,
)
# noinspection PyUnresolvedReferences
from .._constants import (
    TOUCH_UNKNOWN,
    TOUCH_SHORT,
    TOUCH_HOLD,
    TOUCH_DRAG,
)
from typing import Optional, Generator, Any


class TouchEvent(object):
    """A touch event."""
    def __init__(self, index: int):
        self.__id = index

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def x(self) -> float:
        return _get_raw_touch_current_x(self.__id)

    @property
    def y(self) -> float:
        return _get_raw_touch_current_y(self.__id)

    @property
    def last_x(self) -> float:
        return _get_raw_touch_last_x(self.__id)

    @property
    def last_y(self) -> float:
        return _get_raw_touch_last_y(self.__id)

    @property
    def start_x(self) -> float:
        return _get_raw_touch_start_x(self.__id)

    @property
    def start_y(self) -> float:
        return _get_raw_touch_start_y(self.__id)

    @property
    def is_released(self) -> bool:
        return _get_raw_touch_released(self.__id)

    @property
    def touch_time(self) -> float:
        return _get_raw_touch_time(self.__id)

    @property
    def touch_type(self) -> int:
        return _get_raw_touch_type(self.__id)

    @property
    def is_unknown_touch(self) -> bool:
        return _get_raw_touch_type(self.__id) == TOUCH_UNKNOWN

    @property
    def is_short_touch(self) -> bool:
        return _get_raw_touch_type(self.__id) == TOUCH_SHORT

    @property
    def is_hold_touch(self) -> bool:
        return _get_raw_touch_type(self.__id) == TOUCH_HOLD

    @property
    def is_drag_touch(self) -> bool:
        return _get_raw_touch_type(self.__id) == TOUCH_DRAG

    @property
    def value(self) -> int:
        return _get_raw_touch_value(self.__id)

    @value.setter
    def value(self, value: int):
        _set_raw_touch_value(self.__id, value)


# def get_event_count(include_unknown: bool = False) -> int:
#     return _get_raw_touch_count(include_unknown)
#
#
# def get_first_event(include_unknown: bool = False) -> Optional[TouchEvent]:
#     index = _get_raw_first_touch_event(include_unknown)
#     if index:
#         return TouchEvent(index)
#     return None
#
#
# def get_next_event() -> Optional[TouchEvent]:
#     index = _get_raw_next_touch_event()
#     if index:
#         return TouchEvent(index)
#     return None


def events(include_unknown: bool = False) -> Generator[TouchEvent, Any, None]:
    index = _get_raw_first_touch_event(include_unknown)
    while index > 0:
        yield TouchEvent(index)
        index = _get_raw_next_touch_event()
