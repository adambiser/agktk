"""
Zip file functionality
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # File > Zip
    add_zip_entry as _add_zip_entry,
    close_zip as _close_zip,
    create_zip as _create_zip,
    # extraction
    cancel_zip_extract as cancel_extract,
    extract_zip as extract,
    extract_zip_async as extract_async,
    get_zip_extract_complete as is_extract_complete,
    get_zip_extract_progress as get_extract_progress,
)


class ZipFile(object):
    """
    Wraps AppGameKit zip file methods.
    """

    def __init__(self, filename: str):
        """
        Creates a zip file for adding files.
        :param filename:
        """
        self.__id = _create_zip(filename)

    def __del__(self):
        """Deletes the object."""
        try:
            _close_zip(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def add_file(self, filename: str, zip_path: str):
        _add_zip_entry(self.__id, filename, zip_path)
