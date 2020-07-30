"""
On-screen virtual buttons.
"""
from appgamekit import (
    # Input > Virtual Button
    add_virtual_button as _add_virtual_button,
    delete_virtual_button as _delete_virtual_button,
    get_virtual_button_exists as _get_virtual_button_exists,
    get_virtual_button_pressed as _get_virtual_button_pressed,
    get_virtual_button_released as _get_virtual_button_released,
    get_virtual_button_state as _get_virtual_button_state,
    set_virtual_button_active as _set_virtual_button_active,
    set_virtual_button_alpha as _set_virtual_button_alpha,
    set_virtual_button_color as _set_virtual_button_color,
    set_virtual_button_image_down as _set_virtual_button_image_down,
    set_virtual_button_image_up as _set_virtual_button_image_up,
    set_virtual_button_position as _set_virtual_button_position,
    set_virtual_button_size as _set_virtual_button_size,
    set_virtual_button_text as _set_virtual_button_text,
    set_virtual_button_visible as _set_virtual_button_visible,
)
from agktk.constants import (
    STATE_UP as _STATE_UP,
    STATE_DOWN as _STATE_DOWN,
)
from agktk.image import Image
from typing import Optional, Tuple, Union


class VirtualButton(object):
    """
    An on-screen button that can be controlled by a touch screen, mouse, or other pointer device.

    A maximum of 100 virtual buttons can be created at the same time.
    """
    __FIRST_ID = 1
    __LAST_ID = 100

    def __init__(self, x: float, y: float, width: float, height: float = None, text: str = None):
        """
        Creates an on-screen virtual button.

        :param float x: The x-coordinate of the center of the button.
        :param float y: The y-coordinate of the center of the button.
        :param float width: The width of the button.
        :param float height: The height of the button.  When not provided, the width will be used.
        :param str text: The text for the button.
        """
        # noinspection PyShadowingBuiltins
        id = next((i for i in range(VirtualButton.__FIRST_ID, VirtualButton.__LAST_ID + 1)
                   if not _get_virtual_button_exists(i)), None)
        self.__id = id
        if id is None:
            raise RuntimeError("Could not find an available virtual button index.")
        if height is None:
            height = width
        # Store the properties that aren't accessible via AppGameKit commands.
        self.__is_active = True
        self.__alpha = 255
        self.__color = (255, 255, 255)
        self.__image_up = None  # type: Optional[Image]
        self.__image_down = None  # type: Optional[Image]
        self.__position = (x, y)
        self.__size = (width, height)
        self.__text = None
        self.__is_visible = True
        _add_virtual_button(id, x, y, width)
        if height != width:
            _set_virtual_button_size(id, width, height)
        self.text = text

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_virtual_button(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def is_pressed(self) -> bool:
        """Returns True if the virtual button was pressed this frame."""
        return _get_virtual_button_pressed(self.__id)

    @property
    def is_released(self) -> bool:
        """Returns True if the virtual button was released this frame."""
        return _get_virtual_button_released(self.__id)

    @property
    def is_down(self) -> bool:
        """Returns True if the virtual button is currently down."""
        return _get_virtual_button_state(self.__id) == _STATE_DOWN

    @property
    def is_up(self) -> bool:
        """Returns True if the virtual button is currently up."""
        return _get_virtual_button_state(self.__id) == _STATE_UP

    @property
    def is_active(self) -> bool:
        """Returns or sets whether the virtual button will capture mouse and touch events."""
        return self.__is_active

    @is_active.setter
    def is_active(self, value: bool):
        self.__is_active = value
        _set_virtual_button_active(self.__id, value)

    @property
    def alpha(self) -> int:
        """Returns or sets the transparency of the virtual button, from 0 to 255."""
        return self.__alpha

    @alpha.setter
    def alpha(self, value: int):
        self.__alpha = value
        _set_virtual_button_alpha(self.__id, value)

    @property
    def color(self) -> Tuple[int, int, int]:
        """Returns or sets the color of the virtual button."""
        return self.__color

    @color.setter
    def color(self, value: Tuple[int, int, int]):
        self.__color = value
        _set_virtual_button_color(self.__id, *value)

    @property
    def image_down(self) -> Image:
        return self.__image_down

    @image_down.setter
    def image_down(self, value: Image):
        self.__image_down = value
        _set_virtual_button_image_down(self.__id, value.id if value else 0)

    @property
    def image_up(self) -> Image:
        return self.__image_up

    @image_up.setter
    def image_up(self, value: Image):
        self.__image_up = value
        _set_virtual_button_image_up(self.__id, value.id if value else 0)

    @property
    def position(self) -> Tuple[float, float]:
        """Returns or sets the screen coordinates of the virtual button."""
        return self.__position

    @position.setter
    def position(self, value: Tuple[float, float]):
        self.__position = value
        _set_virtual_button_position(self.__id, *value)

    @property
    def size(self) -> Tuple[float, float]:
        """Returns or sets the size of the virtual button."""
        return self.__size

    @size.setter
    def size(self, value: Union[float, Tuple[float, float]]):
        if isinstance(value, (float, int)):
            value = (value, value)
        _set_virtual_button_size(self.__id, *value)

    @property
    def text(self) -> str:
        """Returns or sets the text of the virtual button."""
        return self.__text

    @text.setter
    def text(self, value: str):
        self.__text = value
        _set_virtual_button_text(self.__id, value or "")

    @property
    def is_visible(self) -> bool:
        """Returns or sets the visibility of the virtual button."""
        return self.__is_visible

    @is_visible.setter
    def is_visible(self, value: bool):
        self.__is_visible = value
        _set_virtual_button_visible(self.__id, value)
