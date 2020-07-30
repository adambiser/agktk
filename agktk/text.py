"""
Contains the Text class.

This module sets Text.use_new_default_fonts to True on import.
"""
from appgamekit import (
    # Text > Creation
    create_text as _create_text,
    delete_text as _delete_text,
    # Text > Properties
    draw_text as _draw_text,
    fix_text_to_screen as _fix_text_to_screen,
    get_text_alignment as _get_text_alignment,
    get_text_char_angle as _get_text_char_angle,
    get_text_char_angle_rad as _get_text_char_angle_rad,
    get_text_char_color_alpha as _get_text_char_color_alpha,
    get_text_char_color_blue as _get_text_char_color_blue,
    get_text_char_color_green as _get_text_char_color_green,
    get_text_char_color_red as _get_text_char_color_red,
    get_text_char_x as _get_text_char_x,
    get_text_char_y as _get_text_char_y,
    get_text_color_alpha as _get_text_color_alpha,
    get_text_color_blue as _get_text_color_blue,
    get_text_color_green as _get_text_color_green,
    get_text_color_red as _get_text_color_red,
    get_text_depth as _get_text_depth,
    # get_text_exists as _get_text_exists,  # Not needed
    get_text_hit_test as _get_text_hit_test,
    get_text_length as _get_text_length,
    get_text_line_spacing as _get_text_line_spacing,
    get_text_size as _get_text_size,
    get_text_spacing as _get_text_spacing,
    get_text_string as _get_text_string,
    get_text_total_height as _get_text_total_height,
    get_text_total_width as _get_text_total_width,
    get_text_visible as _get_text_visible,
    get_text_x as _get_text_x,
    get_text_y as _get_text_y,
    set_text_alignment as _set_text_alignment,
    set_text_angle as _set_text_angle,
    set_text_angle_rad as _set_text_angle_rad,
    set_text_bold as _set_text_bold,
    set_text_char_angle as _set_text_char_angle,
    set_text_char_angle_rad as _set_text_char_angle_rad,
    set_text_char_bold as _set_text_char_bold,
    set_text_char_color as _set_text_char_color,
    set_text_char_color_alpha as _set_text_char_color_alpha,
    set_text_char_color_blue as _set_text_char_color_blue,
    set_text_char_color_green as _set_text_char_color_green,
    set_text_char_color_red as _set_text_char_color_red,
    set_text_char_position as _set_text_char_position,
    set_text_char_x as _set_text_char_x,
    set_text_char_y as _set_text_char_y,
    set_text_color as _set_text_color,
    set_text_color_alpha as _set_text_color_alpha,
    set_text_color_blue as _set_text_color_blue,
    set_text_color_green as _set_text_color_green,
    set_text_color_red as _set_text_color_red,
    set_text_default_extended_font_image as _set_text_default_extended_font_image,
    set_text_default_font_image as _set_text_default_font_image,
    set_text_default_mag_filter as _set_text_default_mag_filter,
    set_text_default_min_filter as _set_text_default_min_filter,
    set_text_depth as _set_text_depth,
    set_text_extended_font_image as _set_text_extended_font_image,
    set_text_font as _set_text_font,
    set_text_font_image as _set_text_font_image,
    set_text_line_spacing as _set_text_line_spacing,
    set_text_max_width as _set_text_max_width,
    set_text_position as _set_text_position,
    set_text_scissor as _set_text_scissor,
    set_text_size as _set_text_size,
    set_text_spacing as _set_text_spacing,
    set_text_string as _set_text_string,
    set_text_transparency as _set_text_transparency,
    set_text_visible as _set_text_visible,
    set_text_x as _set_text_x,
    set_text_y as _set_text_y,
    use_new_default_fonts as _use_new_default_fonts,
    # Text > Print
    # print_value,  # Move to device module?
    # # PrintC
    # set_print_color,  # Move to device module?
    # set_print_font,  # Move to device module?
    # set_print_size,  # Move to device module?
    # set_print_spacing,  # Move to device module?
)
from .enums import (
    HorizontalAlign,
    Filter,
    TransparencyMode,
)
from .font import Font
from .image import Image
from typing import Optional, Sequence, Tuple, Union


# Idea for indexed char properties.
# class _CharProperties(object):
#     def __init__(self):
#         self.index = None
#
#     def __call__(self, index: int):
#         self.index = index
#         return self
#
#     @property
#     def y(self):
#         return 3
#
#
# class _Char(object):
#     def __init__(self, text_id: int):
#         self._text_id = text_id
#         self._ch = _CharProperties()
#
#     def __getitem__(self, index: int):
#         return self._ch(index)


class Text(object):
    """
    Wraps AppGameKit text object methods.
    """
    __extended_font_image = None  # type: Optional[Image]
    __font_image = None  # type: Optional[Image]

    def __init__(self, text: str, x: float = 0, y: float = 0, size: float = None, max_width: float = 0):
        _id = _create_text(text)
        self.__id = _id
        self.__fixed_to_screen = False
        # self.__char = _Char(self.__id)
        self.__extended_font_image = None  # type: Optional[Image]
        self.__font = None  # type: Optional[Font]
        self.__font_image = None  # type: Optional[Image]
        self.__max_width = max_width
        self.__transparency = TransparencyMode.ALPHA
        _set_text_position(_id, x, y)
        if size is not None:
            _set_text_size(_id, size)
        _set_text_max_width(_id, max_width)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_text(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def draw(self):
        _draw_text(self.__id)

    @property
    def fixed_to_screen(self) -> bool:
        """Returns or sets whether the text object is fixed to screen coordinates rather than world coordinates."""
        return self.__fixed_to_screen

    @fixed_to_screen.setter
    def fixed_to_screen(self, value: bool):
        self.__fixed_to_screen = value
        _fix_text_to_screen(self.__id, value)

    @property
    def alignment(self) -> HorizontalAlign:
        return HorizontalAlign(_get_text_alignment(self.__id))

    @alignment.setter
    def alignment(self, value: HorizontalAlign):
        _set_text_alignment(self.__id, value)

    def set_angle(self, value: float):
        _set_text_angle(self.__id, value)

    def set_angle_rad(self, value: float):
        _set_text_angle_rad(self.__id, value)

    def set_bold(self, enabled: bool):
        _set_text_bold(self.__id, enabled)

    @property
    def color_alpha(self) -> int:
        return _get_text_color_alpha(self.__id)

    @color_alpha.setter
    def color_alpha(self, value: int):
        _set_text_color_alpha(self.__id, value)

    @property
    def color_blue(self) -> int:
        return _get_text_color_blue(self.__id)

    @color_blue.setter
    def color_blue(self, value: int):
        _set_text_color_blue(self.__id, value)

    @property
    def color_green(self) -> int:
        return _get_text_color_green(self.__id)

    @color_green.setter
    def color_green(self, value: int):
        _set_text_color_green(self.__id, value)

    @property
    def color_red(self) -> int:
        return _get_text_color_red(self.__id)

    @color_red.setter
    def color_red(self, value: int):
        _set_text_color_red(self.__id, value)

    def set_color(self, red: int, green: int, blue: int, alpha: int = 255):
        _set_text_color(self.__id, red, green, blue, alpha)

    @property
    def depth(self) -> int:
        return _get_text_depth(self.__id)

    @depth.setter
    def depth(self, value: int):
        _set_text_depth(self.__id, value)

    def hit_test(self, x: float, y: float) -> bool:
        return _get_text_hit_test(self.__id, x, y)

    @property
    def length(self) -> int:
        return _get_text_length(self.__id)

    @property
    def line_spacing(self) -> float:
        return _get_text_line_spacing(self.__id)

    @line_spacing.setter
    def line_spacing(self, value: float):
        _set_text_line_spacing(self.__id, value)

    @property
    def size(self) -> float:
        return _get_text_size(self.__id)

    @size.setter
    def size(self, value: float):
        _set_text_size(self.__id, value)

    @property
    def spacing(self) -> float:
        return _get_text_spacing(self.__id)

    @spacing.setter
    def spacing(self, value: float):
        _set_text_spacing(self.__id, value)

    @property
    def string(self) -> str:
        return _get_text_string(self.__id)

    @string.setter
    def string(self, value: str):
        _set_text_string(self.__id, value)

    @property
    def total_height(self) -> float:
        return _get_text_total_height(self.__id)

    @property
    def total_width(self) -> float:
        return _get_text_total_width(self.__id)

    @property
    def visible(self) -> bool:
        return _get_text_visible(self.__id)

    @visible.setter
    def visible(self, value: bool):
        _set_text_visible(self.__id, value)

    @property
    def x(self) -> float:
        return _get_text_x(self.__id)

    @x.setter
    def x(self, value: float):
        _set_text_x(self.__id, value)

    @property
    def y(self) -> float:
        return _get_text_y(self.__id)

    @y.setter
    def y(self, value: float):
        _set_text_y(self.__id, value)

    def set_position(self, x: float, y: float):
        _set_text_position(self.__id, x, y)

    @property
    def extended_font_image(self) -> Image:
        return self.__extended_font_image

    @extended_font_image.setter
    def extended_font_image(self, value: Image):
        self.__extended_font_image = value
        _set_text_extended_font_image(self.__id, value.id if value else 0)

    @property
    def font(self) -> Font:
        return self.__font

    @font.setter
    def font(self, value: Font):
        self.__font = value
        self.__font_image = None
        _set_text_font(self.__id, value.id if value else 0)

    @property
    def font_image(self) -> Image:
        return self.__font_image

    @font_image.setter
    def font_image(self, value: Image):
        self.__font = None
        self.__font_image = value
        _set_text_font_image(self.__id, value.id if value else 0)

    @property
    def max_width(self) -> float:
        return self.__max_width

    @max_width.setter
    def max_width(self, value: float):
        self.__max_width = value
        _set_text_max_width(self.__id, value)

    def set_scissor(self, x1: float, y1: float, x2: float, y2: float):
        _set_text_scissor(self.__id, x1, y1, x2, y2)

    @property
    def transparency_mode(self) -> TransparencyMode:
        return self.__transparency

    @transparency_mode.setter
    def transparency_mode(self, value: TransparencyMode):
        self.__transparency = value
        _set_text_transparency(self.__id, value)

    # Character functions.

    def get_char_angle(self, char_index: int) -> float:
        return _get_text_char_angle(self.__id, char_index)

    def set_char_angle(self, char_index: int, value: float):
        _set_text_char_angle(self.__id, char_index, value)

    def get_char_angle_rad(self, char_index: int) -> float:
        return _get_text_char_angle_rad(self.__id, char_index)

    def set_char_angle_rad(self, char_index: int, value: float):
        _set_text_char_angle_rad(self.__id, char_index, value)

    def set_char_bold(self, char_index: int, enabled: bool):
        _set_text_char_bold(self.__id, char_index, enabled)

    def get_char_color_alpha(self, char_index: int) -> int:
        return _get_text_char_color_alpha(self.__id, char_index)

    def set_char_color_alpha(self, char_index: int, value: int):
        _set_text_char_color_alpha(self.__id, char_index, value)

    def get_char_color_blue(self, char_index: int) -> int:
        return _get_text_char_color_blue(self.__id, char_index)

    def set_char_color_blue(self, char_index: int, value: int):
        _set_text_char_color_blue(self.__id, char_index, value)

    def get_char_color_green(self, char_index: int) -> int:
        return _get_text_char_color_green(self.__id, char_index)

    def set_char_color_green(self, char_index: int, value: int):
        _set_text_char_color_green(self.__id, char_index, value)

    def get_char_color_red(self, char_index: int) -> int:
        return _get_text_char_color_red(self.__id, char_index)

    def set_char_color_red(self, char_index: int, value: int):
        _set_text_char_color_red(self.__id, char_index, value)

    def set_char_color(self, char_index: int, red: int, green: int, blue: int, alpha: int = 255):
        _set_text_char_color(self.__id, char_index, red, green, blue, alpha)

    def get_char_x(self, char_index: int) -> float:
        return _get_text_char_x(self.__id, char_index)

    def set_char_x(self, char_index: int, value: float):
        _set_text_char_x(self.__id, char_index, value)

    def get_char_y(self, char_index: int) -> float:
        return _get_text_char_y(self.__id, char_index)

    def set_char_y(self, char_index: int, value: float):
        _set_text_char_y(self.__id, char_index, value)

    def set_char_position(self, char_index: int, x: float, y: float):
        _set_text_char_position(self.__id, char_index, x, y)

    # Class methods.

    @classmethod
    def set_default_extended_font_image(cls, image: Image):
        cls.__extended_font_image = image
        _set_text_default_extended_font_image(image.id if image else 0)

    @classmethod
    def set_default_font_image(cls, image: Image):
        cls.__font_image = image
        _set_text_default_font_image(image.id if image else 0)

    @classmethod
    def set_default_mag_filter(cls, filter_mode: Filter):
        _set_text_default_mag_filter(filter_mode)

    @classmethod
    def set_default_min_filter(cls, filter_mode: Filter):
        _set_text_default_min_filter(filter_mode)

    @classmethod
    def use_new_default_fonts(cls, enabled: bool):
        _use_new_default_fonts(enabled)


# Use the new default fonts.
Text.use_new_default_fonts(True)
