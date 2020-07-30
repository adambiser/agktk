"""
Contains the Font class.
"""
from appgamekit import (
    delete_font as _delete_font,
    # get_font_exists,  # not needed
    get_system_font_exists,
    load_font as _load_font,
)


class Font(object):
    def __init__(self, name: str):
        """Loads a font"""
        self.__id = _load_font(name)

    def __del__(self):
        """Delete the font."""
        try:
            _delete_font(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

