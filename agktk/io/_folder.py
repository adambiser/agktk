from appgamekit import (
    # File > Directory Raw
    close_raw_folder as _close_raw_folder,
    get_raw_folder_file_name as _get_raw_folder_file_name,
    get_raw_folder_folder_name as _get_raw_folder_folder_name,
    get_raw_folder_num_files as _get_raw_folder_num_files,
    get_raw_folder_num_folders as _get_raw_folder_num_folders,
    open_raw_folder as _open_raw_folder,
)


class RawFolder(object):
    """
    Wraps AppGameKit raw folder methods.
    """

    def __init__(self, path: str):
        self.__id = _open_raw_folder(path)

    def __del__(self):
        """Deletes the object."""
        try:
            _close_raw_folder(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def file_count(self) -> int:
        return _get_raw_folder_num_files(self.__id)

    @property
    def files(self):
        for index in range(0, _get_raw_folder_num_files(self.__id)):
            yield _get_raw_folder_file_name(self.__id, index)

    @property
    def folder_count(self) -> int:
        return _get_raw_folder_num_folders(self.__id)

    @property
    def folders(self):
        for index in range(0, _get_raw_folder_num_folders(self.__id)):
            yield _get_raw_folder_folder_name(self.__id, index)
