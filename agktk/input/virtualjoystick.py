"""
On-screen virtual joysticks.
"""
from appgamekit import (
    # Input > Virtual Joystick
    add_virtual_joystick as _add_virtual_joystick,
    delete_virtual_joystick as _delete_virtual_joystick,
    get_virtual_joystick_exists as _get_virtual_joystick_exists,
    get_virtual_joystick_x as _get_virtual_joystick_x,
    get_virtual_joystick_y as _get_virtual_joystick_y,
    set_virtual_joystick_active as _set_virtual_joystick_active,
    set_virtual_joystick_alpha as _set_virtual_joystick_alpha,
    set_virtual_joystick_dead_zone as _set_virtual_joystick_dead_zone,
    set_virtual_joystick_image_inner as _set_virtual_joystick_image_inner,
    set_virtual_joystick_image_outer as _set_virtual_joystick_image_outer,
    set_virtual_joystick_position as _set_virtual_joystick_position,
    set_virtual_joystick_size as _set_virtual_joystick_size,
    set_virtual_joystick_visible as _set_virtual_joystick_visible,
)
from agktk._image import Image
from typing import Optional, Tuple


class _VirtualJoystickMeta(type):
    def __init__(cls, name, bases, nmspc):
        super().__init__(name, bases, nmspc)
        cls.__dead_zone = 0.15

    @property
    def dead_zone(cls) -> float:
        """Returns and sets the dead zone for all virtual joysticks."""
        return cls.__dead_zone

    @dead_zone.setter
    def dead_zone(cls, value: float):
        cls.__dead_zone = value
        _set_virtual_joystick_dead_zone(value)


class VirtualJoystick(object, metaclass=_VirtualJoystickMeta):
    """
    An on-screen joystick that can be controlled by a touch screen, mouse, or other pointer device.

    A maximum of 4 virtual joysticks can be created at the same time.
    """
    __FIRST_ID = 1
    __LAST_ID = 4

    def __init__(self, x: float, y: float, size: float):
        """
        Creates an on-screen virtual joystick.

        :param float x: The x-coordinate of the center of the joystick.
        :param float y: The y-coordinate of the center of the joystick.
        :param float size: The diameter of the joystick in screen coordinates.
        """
        # noinspection PyShadowingBuiltins
        id = next((i for i in range(VirtualJoystick.__FIRST_ID, VirtualJoystick.__LAST_ID + 1)
                   if not _get_virtual_joystick_exists(i)), None)
        self.__id = id
        if id is None:
            raise RuntimeError("Could not find an available virtual joystick index.")
        # Store the properties that aren't accessible via AppGameKit commands.
        self.__is_active = True
        self.__image_inner = None  # type: Optional[Image]
        self.__image_outer = None  # type: Optional[Image]
        self.__position = (x, y)
        self.__size = size
        self.__text = None
        self.__is_visible = True
        _add_virtual_joystick(id, x, y, size)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_virtual_joystick(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def x(self) -> float:
        """Returns the X value of the virtual joystick."""
        return _get_virtual_joystick_x(self.__id)

    @property
    def y(self) -> float:
        """Returns the X value of the virtual joystick."""
        return _get_virtual_joystick_y(self.__id)

    @property
    def is_active(self) -> bool:
        """Returns or sets whether the virtual joystick will capture mouse and touch events."""
        return self.__is_active

    @is_active.setter
    def is_active(self, value: bool):
        self.__is_active = value
        _set_virtual_joystick_active(self.__id, value)

    def set_alpha(self, outer: int, inner: int):
        """Sets the transparency of the virtual joystick on screen."""
        _set_virtual_joystick_alpha(self.__id, outer, inner)

    @property
    def image_inner(self) -> Image:
        return self.__image_inner

    @image_inner.setter
    def image_inner(self, value: Image):
        self.__image_inner = value
        _set_virtual_joystick_image_inner(self.__id, value.id)

    @property
    def image_outer(self) -> Image:
        return self.__image_outer

    @image_outer.setter
    def image_outer(self, value: Image):
        self.__image_outer = value
        _set_virtual_joystick_image_outer(self.__id, value.id)

    @property
    def position(self) -> Tuple[float, float]:
        """Returns or sets the screen coordinates of the virtual joystick."""
        return self.__position

    @position.setter
    def position(self, value: Tuple[float, float]):
        self.__position = value
        _set_virtual_joystick_position(self.__id, *value)

    @property
    def size(self) -> float:
        """Returns or sets the size of the virtual joystick."""
        return self.__size

    @size.setter
    def size(self, value: float):
        self.__size = value
        _set_virtual_joystick_size(self.__id, value)

    @property
    def is_visible(self) -> bool:
        """Returns or sets the visibility of the virtual joystick."""
        return self.__is_visible

    @is_visible.setter
    def is_visible(self, value: bool):
        self.__is_visible = value
        _set_virtual_joystick_visible(self.__id, value)
