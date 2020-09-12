"""
Zip file functionality
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # File > Zip
    add_zip_entry as _add_zip_entry,
    close_zip as _close_zip,
    create_zip as _create_zip,
    # create_zip_id,  # Not needed.
    # extraction
    cancel_zip_extract,
    extract_zip,
    extract_zip_async,
    get_zip_extract_complete,
    get_zip_extract_progress,
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

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    def __enter__(self):
        """Allows the class to be used in a with block."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return exc_type is KeyboardInterrupt

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def add_file(self, filename: str, zip_path: str):
        _add_zip_entry(self.__id, filename, zip_path)

    def close(self):
        _id = self.__id
        if _id:
            self.__id = 0
            _close_zip(_id)
