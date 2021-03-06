from appgamekit import (
    # File > Read
    file_eof as _file_eof,
    open_to_read as _open_to_read,
    # open_to_read_id,  # Not needed.
    read_byte as _read_byte,
    read_float as _read_float,
    read_integer as _read_integer,
    read_line as _read_line,
    read_string as _read_string,
    read_string2 as _read_string2,
    # File > Write
    open_to_write as _open_to_write,
    # open_to_write_id,  # Not needed.
    write_byte as _write_byte,
    write_float as _write_float,
    write_integer as _write_integer,
    write_line as _write_line,
    write_string as _write_string,
    write_string2 as _write_string2,
    # File > Access
    close_file as _close_file,
    file_is_open as _file_is_open,
    get_file_pos as _get_file_pos,
    get_file_size as _get_file_size,
    set_file_pos as _set_file_pos,
)


class FileReader(object):
    """
    Wraps AppGameKit file read methods.
    """

    def __init__(self, filename: str):
        """
        Opens a file for reading.
        Calling code should call close() explicitly when finished or use in a with block.
        :param filename: The filename.
        """
        self.__id = _open_to_read(filename)

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

    def close(self):
        _id = self.__id
        if _id:
            self.__id = 0
            _close_file(_id)

    @property
    def is_open(self) -> bool:
        return _file_is_open(self.__id)

    @property
    def position(self) -> int:
        return _get_file_pos(self.__id)

    @position.setter
    def position(self, value: int):
        _set_file_pos(self.__id, value)

    @property
    def size(self) -> int:
        return _get_file_size(self.__id)

    @property
    def eof(self) -> bool:
        return _file_eof(self.__id)

    def read_byte(self) -> int:
        return _read_byte(self.__id)

    def read_float(self) -> float:
        return _read_float(self.__id)

    def read_integer(self) -> int:
        return _read_integer(self.__id)

    def read_line(self) -> str:
        return _read_line(self.__id)

    def read_string(self) -> str:
        return _read_string(self.__id)

    def read_string2(self) -> str:
        return _read_string2(self.__id)

    def _read_generator(self, read_func):
        _id = self.__id
        while True:
            b = read_func(_id)
            if _file_eof(_id):
                # This is so read_line works when the last line doesn't end with a newline.
                if b:
                    yield b
                break
            yield b

    @property
    def bytes(self):
        return self._read_generator(_read_byte)

    @property
    def floats(self):
        return self._read_generator(_read_float)

    @property
    def integers(self):
        return self._read_generator(_read_integer)

    @property
    def lines(self):
        return self._read_generator(_read_line)

    @property
    def strings(self):
        return self._read_generator(_read_string)

    @property
    def string2s(self):
        return self._read_generator(_read_string2)


class FileWriter(object):
    """
    Wraps AppGameKit file write methods.
    """

    def __init__(self, filename: str):
        """
        Opens a file for writing.
        Calling code should call close() explicitly when finished or use in a with block.
        :param filename:
        """
        self.__id = _open_to_write(filename)

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

    def close(self):
        _id = self.__id
        if _id:
            self.__id = 0
            _close_file(_id)

    @property
    def is_open(self) -> bool:
        return _file_is_open(self.__id)

    @property
    def position(self) -> int:
        return _get_file_pos(self.__id)

    @position.setter
    def position(self, value: int):
        _set_file_pos(self.__id, value)

    @property
    def size(self) -> int:
        return _get_file_size(self.__id)

    def write_byte(self, value: int):
        _write_byte(self.__id, value)

    def write_float(self, value: float):
        _write_float(self.__id, value)

    def write_integer(self, value: int):
        _write_integer(self.__id, value)

    def write_line(self, value: str):
        _write_line(self.__id, value)

    def write_string(self, value: str):
        _write_string(self.__id, value)

    def write_string2(self, value: str):
        _write_string2(self.__id, value)
