"""
Raw joystick/controller functionality.

Call get_existing to detect and return all existing joysticks/controllers.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Input-Raw > Existence
    get_joystick_exists as _get_joystick_exists,
    # Input-Raw > Joystick
    complete_raw_joystick_detection as _complete_raw_joystick_detection,
    get_raw_joystick_button_pressed as _get_raw_joystick_button_pressed,
    get_raw_joystick_button_released as _get_raw_joystick_button_released,
    get_raw_joystick_button_state as _get_raw_joystick_button_state,
    get_raw_joystick_connected as _get_raw_joystick_connected,
    get_raw_joystick_exists as _get_raw_joystick_exists,
    get_raw_joystick_name as _get_raw_joystick_name,
    get_raw_joystick_pov as _get_raw_joystick_pov,
    get_raw_joystick_rx as _get_raw_joystick_rx,
    get_raw_joystick_ry as _get_raw_joystick_ry,
    get_raw_joystick_rz as _get_raw_joystick_rz,
    get_raw_joystick_slider as _get_raw_joystick_slider,
    get_raw_joystick_x as _get_raw_joystick_x,
    get_raw_joystick_y as _get_raw_joystick_y,
    get_raw_joystick_z as _get_raw_joystick_z,
    set_raw_joystick_dead_zone as set_dead_zone,
)
from .._constants import (
    STATE_UP as _STATE_UP,
    STATE_DOWN as _STATE_DOWN,
)

__FIRST_ID = 1
__LAST_ID = 8


# class _JoystickMeta(type):
#     def __init__(cls, name, bases, nmspc):
#         super().__init__(name, bases, nmspc)
#         cls.__dead_zone = 0.15
#
#     @property
#     def dead_zone(cls) -> float:
#         """Returns and sets the dead zone for all virtual joysticks."""
#         return cls.__dead_zone
#
#     @dead_zone.setter
#     def dead_zone(cls, value: float):
#         cls.__dead_zone = value
#         _set_raw_joystick_dead_zone(value)


class Joystick(object):  # , metaclass=_JoystickMeta):
    def __new__(cls, index, *args, **kwargs):
        # Pass None if the raw joystick doesn't exist.
        if not _get_raw_joystick_exists(index):
            return None
        return super().__new__(cls)

    def __init__(self, index: int):
        """Creates a joystick instance for the given index."""
        self.__id = index

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}, name: {self.name}>"

    @property
    def id(self):
        return self.__id

    def is_button_pressed(self, button: int) -> bool:
        return _get_raw_joystick_button_pressed(self.__id, button)

    def is_button_released(self, button: int) -> bool:
        return _get_raw_joystick_button_released(self.__id, button)

    def is_button_down(self, button: int) -> bool:
        return _get_raw_joystick_button_state(self.__id, button) == _STATE_DOWN

    def is_button_up(self, button: int) -> bool:
        return _get_raw_joystick_button_state(self.__id, button) == _STATE_UP

    @property
    def is_connected(self) -> bool:
        return _get_raw_joystick_connected(self.__id)

    # @property
    # def exists(self) -> bool:
    #     return _get_raw_joystick_exists(self.__id)

    @property
    def name(self) -> str:
        return _get_raw_joystick_name(self.__id)

    def get_pov(self, pov: int):
        return _get_raw_joystick_pov(self.__id, pov)

    @property
    def rx(self) -> float:
        return _get_raw_joystick_rx(self.__id)

    @property
    def ry(self) -> float:
        return _get_raw_joystick_ry(self.__id)

    @property
    def rz(self) -> float:
        return _get_raw_joystick_rz(self.__id)

    def get_slider(self, slider: int):
        return _get_raw_joystick_slider(self.__id, slider)

    @property
    def x(self) -> float:
        return _get_raw_joystick_x(self.__id)

    @property
    def y(self) -> float:
        return _get_raw_joystick_y(self.__id)

    @property
    def z(self) -> float:
        return _get_raw_joystick_z(self.__id)


def _detect():
    # noinspection PyGlobalUndefined
    global _complete_raw_joystick_detection
    try:
        _complete_raw_joystick_detection()
    except AttributeError:
        del _complete_raw_joystick_detection


def exist() -> bool:
    _detect()
    return _get_joystick_exists()


def get_existing():
    _detect()
    return [Joystick(index) for index in range(__FIRST_ID, __LAST_ID + 1) if _get_raw_joystick_exists(index)]


def find(name: str):
    return next((j for j in get_existing() if j.name == name), None)
