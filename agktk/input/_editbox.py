"""
An on-screen edit box.
"""
from appgamekit import (
    # Input > Edit Box
    create_edit_box as _create_edit_box,
    # create_edit_box_id,  # Not needed.
    delete_edit_box as _delete_edit_box,
    fix_edit_box_to_screen as _fix_edit_box_to_screen,
    get_current_edit_box as _get_current_edit_box,
    get_edit_box_active as _get_edit_box_active,
    get_edit_box_changed as _get_edit_box_changed,
    get_edit_box_cursor_position as _get_edit_box_cursor_position,
    get_edit_box_depth as _get_edit_box_depth,
    # get_edit_box_exists as _get_edit_box_exists,  # not needed
    get_edit_box_has_focus as _get_edit_box_has_focus,
    get_edit_box_height as _get_edit_box_height,
    get_edit_box_lines as _get_edit_box_lines,
    get_edit_box_text as _get_edit_box_text,
    get_edit_box_visible as _get_edit_box_visible,
    get_edit_box_width as _get_edit_box_width,
    get_edit_box_x as _get_edit_box_x,
    get_edit_box_y as _get_edit_box_y,
    set_edit_box_active as _set_edit_box_active,
    set_edit_box_background_color as _set_edit_box_background_color,
    set_edit_box_background_image as _set_edit_box_background_image,
    set_edit_box_border_color as _set_edit_box_border_color,
    set_edit_box_border_image as _set_edit_box_border_image,
    set_edit_box_border_size as _set_edit_box_border_size,
    set_edit_box_cursor_blink_time as _set_edit_box_cursor_blink_time,
    set_edit_box_cursor_color as _set_edit_box_cursor_color,
    set_edit_box_cursor_position as _set_edit_box_cursor_position,
    set_edit_box_cursor_width as _set_edit_box_cursor_width,
    set_edit_box_depth as _set_edit_box_depth,
    set_edit_box_extended_font_image as _set_edit_box_extended_font_image,
    set_edit_box_focus as _set_edit_box_focus,
    set_edit_box_font as _set_edit_box_font,
    set_edit_box_font_image as _set_edit_box_font_image,
    # set_edit_box_input_type,  # Not needed.  Mobile only
    set_edit_box_max_chars as _set_edit_box_max_chars,
    set_edit_box_max_lines as _set_edit_box_max_lines,
    set_edit_box_multiline as _set_edit_box_multiline,
    set_edit_box_password_mode as _set_edit_box_password_mode,
    set_edit_box_position as _set_edit_box_position,
    set_edit_box_scissor as _set_edit_box_scissor,
    set_edit_box_size as _set_edit_box_size,
    set_edit_box_text as _set_edit_box_text,
    set_edit_box_text_color as _set_edit_box_text_color,
    set_edit_box_text_size as _set_edit_box_text_size,
    # set_edit_box_use_alternate_input,  # Not needed.  Mobile only
    set_edit_box_visible as _set_edit_box_visible,
    set_edit_box_wrap_mode as _set_edit_box_wrap_mode,
)
# noinspection PyUnresolvedReferences
from .._constants import (
    EDIT_BOX_WRAP_SCROLL as _EDIT_BOX_WRAP_SCROLL,
    EDIT_BOX_WRAP_NEW_LINE as _EDIT_BOX_WRAP_NEW_LINE,
)
from .._grfx.font import Font
from .._grfx.image import Image
from typing import Optional, Tuple
import weakref as _weakref


class EditBox(object):
    """
    An on-screen edit box
    """
    # Weakrefs keyed by id so instances can be returned by EditBox.get_current without preventing deletion.
    _instances = _weakref.WeakValueDictionary()

    def __init__(self, x: float = 0.0, y: float = 0.0, width: float = 150.0, height: float = 18.0):
        """
        Creates an on-screen edit box.

        :param float x: The x-coordinate of the center of the joystick.
        :param float y: The y-coordinate of the center of the joystick.
        """
        _id = _create_edit_box()
        _set_edit_box_position(_id, x, y)
        self.__id = _id
        EditBox._instances[_id] = self
        self.__fixed_to_screen = False
        self.__background_image = None  # type: Optional[Image]
        self.__border_image = None  # type: Optional[Image]
        self.__extended_font_image = None  # type: Optional[Image]
        self.__font = None  # type: Optional[Font]
        self.__font_image = None  # type: Optional[Image]
        self.__max_chars = 0
        self.__max_lines = 0
        self.__multiline = False
        self.__password_mode = False
        self.__word_wrap = False
        _set_edit_box_size(_id, width, height)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_edit_box(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @classmethod
    def get_current(cls) -> Optional["EditBox"]:
        # noinspection PyProtectedMember
        return cls._instances.get(_get_current_edit_box())

    @property
    def is_current(self) -> bool:
        """Returns true if this edit box has focus and is currently active for user input."""
        return self.__id == _get_current_edit_box()

    @property
    def fixed_to_screen(self) -> bool:
        """Returns or sets whether the edit box is fixed to screen coordinates rather than world coordinates."""
        return self.__fixed_to_screen

    @fixed_to_screen.setter
    def fixed_to_screen(self, value: bool):
        self.__fixed_to_screen = value
        _fix_edit_box_to_screen(self.__id, value)

    @property
    def is_active(self) -> bool:
        """Returns or sets whether the edit box will capture mouse and touch events."""
        return _get_edit_box_active(self.__id)

    @is_active.setter
    def is_active(self, value: bool):
        _set_edit_box_active(self.__id, value)

    @property
    def lost_focus(self) -> bool:
        """Returns True when the edit box has lost focus this frame.  The text may have changed."""
        return _get_edit_box_changed(self.__id)

    @property
    def cursor_position(self) -> int:
        """Returns or sets the position of the cursor in the edit box."""
        return _get_edit_box_cursor_position(self.__id)

    @cursor_position.setter
    def cursor_position(self, value: bool):
        _set_edit_box_cursor_position(self.__id, value)

    @property
    def depth(self) -> int:
        """Returns or sets the depth of the edit box."""
        return _get_edit_box_depth(self.__id)

    @depth.setter
    def depth(self, value: int):
        _set_edit_box_depth(self.__id, value)

    @property
    def has_focus(self) -> bool:
        """Returns ot sets whether the edit box has focus."""
        return _get_edit_box_has_focus(self.__id)

    @has_focus.setter
    def has_focus(self, value: bool):
        _set_edit_box_focus(self.__id, value)

    @property
    def height(self) -> float:
        """Returns the height of the edit box."""
        return _get_edit_box_height(self.__id)

    # @height.setter
    # def height(self, value: float):
    #     """Returns the height of the edit box."""
    #     _id = self.__id
    #     _set_edit_box_size(_id, _get_edit_box_width(_id), value)

    @property
    def line_count(self) -> float:
        """Returns the number of lines the user has entered."""
        return _get_edit_box_lines(self.__id)

    @property
    def text(self) -> str:
        """Returns or sets the edit box text."""
        return _get_edit_box_text(self.__id)

    @text.setter
    def text(self, value: str):
        _set_edit_box_text(self.__id, value)

    @property
    def is_visible(self) -> bool:
        """Returns or sets the visibility of the edit box."""
        return _get_edit_box_visible(self.__id)

    @is_visible.setter
    def is_visible(self, value: bool):
        _set_edit_box_visible(self.__id, value)

    @property
    def width(self) -> float:
        """Returns or sets the width of the edit box."""
        return _get_edit_box_width(self.__id)

    # @width.setter
    # def width(self, value: float):
    #     _id = self.__id
    #     _set_edit_box_size(_id, value, _get_edit_box_height(_id))

    @property
    def x(self) -> float:
        """Returns the X value of the edit box."""
        return _get_edit_box_x(self.__id)

    @property
    def y(self) -> float:
        """Returns the X value of the edit box."""
        return _get_edit_box_y(self.__id)

    def set_background_color(self, red: int, green: int, blue: int, alpha: int = 255):
        """Sets the background color."""
        _set_edit_box_background_color(self.__id, red, green, blue, alpha)

    @property
    def background_image(self) -> Image:
        """Returns or sets the background image.  Clears the image when set to None."""
        return self.__background_image

    @background_image.setter
    def background_image(self, value: Image):
        self.__background_image = value
        _set_edit_box_background_image(self.__id, value.id if value else 0)

    def set_border_color(self, red: int, green: int, blue: int, alpha: int = 255):
        """Sets the border color."""
        _set_edit_box_border_color(self.__id, red, green, blue, alpha)

    @property
    def border_image(self) -> Image:
        """Returns or sets the border image.  Clears the image when set to None."""
        return self.__border_image

    @border_image.setter
    def border_image(self, value: Image):
        self.__border_image = value
        _set_edit_box_border_image(self.__id, value.id if value else 0)

    def set_border_size(self, size: float):
        """Sets the border size."""
        _set_edit_box_border_size(self.__id, size)

    def set_cursor_blink_time(self, seconds: float):
        _set_edit_box_cursor_blink_time(self.__id, seconds)

    def set_cursor_color(self, red: int, green: int, blue: int):
        _set_edit_box_cursor_color(self.__id, red, green, blue)

    def set_cursor_width(self, width: float):
        _set_edit_box_cursor_width(self.__id, width)

    @property
    def extended_font_image(self) -> Image:
        """Returns or sets the extended font image.  Clears the image when set to None."""
        return self.__extended_font_image

    @extended_font_image.setter
    def extended_font_image(self, value: Image):
        self.__extended_font_image = value
        _set_edit_box_extended_font_image(self.__id, value.id if value else 0)

    @property
    def font(self) -> Font:
        return self.__font

    @font.setter
    def font(self, value: Font):
        """Sets the font.  Clears the font if None is sent."""
        self.__font = value
        _set_edit_box_font(self.__id, value.id if value else 0)

    @property
    def font_image(self) -> Image:
        """Returns or sets the font image.  Clears the image when set to None."""
        return self.__font_image

    @font_image.setter
    def font_image(self, value: Image):
        self.__font_image = value
        _set_edit_box_font_image(self.__id, value.id if value else 0)

    @property
    def max_chars(self) -> int:
        return self.__max_chars

    @max_chars.setter
    def max_chars(self, value: int):
        """Sets the maximum characters.  0 for unlimited."""
        self.__max_chars = value
        _set_edit_box_max_chars(self.__id, value)

    @property
    def max_lines(self) -> int:
        return self.__max_lines

    @max_lines.setter
    def max_lines(self, value: int):
        """Sets the maximum lines.  0 for unlimited."""
        self.__max_lines = value
        _set_edit_box_max_lines(self.__id, value)

    @property
    def multiline(self) -> bool:
        return self.__multiline

    @multiline.setter
    def multiline(self, value: bool):
        """Sets whether text will wrap to a new line or be one continuous line."""
        self.__multiline = value
        _set_edit_box_multiline(self.__id, value)

    @property
    def password_mode(self) -> bool:
        """Returns or sets whether the edit box will show stars instead of the actual text."""
        return self.__password_mode

    @password_mode.setter
    def password_mode(self, value: bool):
        self.__password_mode = value
        _set_edit_box_password_mode(self.__id, value)

    @property
    def position(self) -> Tuple[float, float]:
        """Returns or sets the screen coordinates of the edit box."""
        return _get_edit_box_x(self.__id), _get_edit_box_y(self.__id)

    @position.setter
    def position(self, value: Tuple[float, float]):
        _set_edit_box_position(self.__id, *value)

    def set_scissor(self, x1: float, y1: float, x2: float, y2: float):
        """Clips the edit box to the specified world coordinates when drawn."""
        _set_edit_box_scissor(self.__id, x1, y1, x2, y2)

    @property
    def size(self) -> Tuple[float, float]:
        """Returns or sets the size of the edit box."""
        _id = self.__id
        return _get_edit_box_width(_id), _get_edit_box_height(_id)

    @size.setter
    def size(self, value: Tuple[float, float]):
        _set_edit_box_size(self.__id, *value)

    def set_text_color(self, red: int, green: int, blue: int):
        """Sets the color of the text being input."""
        _set_edit_box_text_color(self.__id, red, green, blue)

    def set_text_size(self, value: float):
        """Sets the size of the text being input."""
        _set_edit_box_text_size(self.__id, value)

    @property
    def word_wrap(self) -> bool:
        """
        Returns or sets the wrap mode of a single-line edit box.
        When multiline is set to False, this sets whether the single line of text will scroll to the right or wrap to a
        new line when it over flows the edit box width.
        """
        return self.__word_wrap

    @word_wrap.setter
    def word_wrap(self, value: bool):
        self.__word_wrap = value
        _set_edit_box_wrap_mode(self.__id, _EDIT_BOX_WRAP_NEW_LINE if value else _EDIT_BOX_WRAP_SCROLL)