"""
Contains methods and classes for handling file I/O.
"""

# noinspection PyUnresolvedReferences
from appgamekit import (
    # File > Zip
    #   See _zipfile
    # File > Read
    #   See _file
    # File > Paths
    count_windows_drives as _count_windows_drives,
    get_windows_drive as _get_windows_drive,
    is_absolute_path,
    join_paths,
    simplify_path,
    # File > Write
    #   See _file
    # File > Directory Raw
    #   See _folder
    # File > Directory
    get_file_count as _get_file_count,
    get_first_file as _get_first_file,
    get_first_folder as _get_first_folder,
    get_folder_count as _get_folder_count,
    get_next_file as _get_next_file,
    get_next_folder as _get_next_folder,
    delete_folder,
    get_folder,
    make_folder,
    set_folder,
    # File > Access
    choose_raw_file,
    delete_file,
    get_documents_path,
    get_file_exists,
    get_read_path,
    get_write_path,
    #   See also _file
)
from .._enums import FolderMode
from ._file import *
from ._folder import *
from ._zipfile import *


def get_windows_drives():
    for index in range(_count_windows_drives()):
        yield _get_windows_drive(index)


def get_file_count(mode: FolderMode = FolderMode.BOTH):
    return _get_file_count(mode)


def get_files(mode: FolderMode = FolderMode.BOTH):
    f = _get_first_file(mode)
    while f:
        yield f
        f = _get_next_file()


def get_folder_count(mode: FolderMode = FolderMode.BOTH):
    return _get_folder_count(mode)


def get_folders(mode: FolderMode = FolderMode.BOTH):
    f = _get_first_folder(mode)
    while f:
        yield f
        f = _get_next_folder()
