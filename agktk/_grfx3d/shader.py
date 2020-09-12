from appgamekit import (
    # 3D > Shaders
    delete_shader as _delete_shader,
    # get_shader_exists,
    # get_supported_shader_varyings as _get_supported_shader_varyings,  # see device
    load_full_screen_shader as _load_full_screen_shader,
    # load_full_screen_shader_id,  # Not needed.
    load_shader as _load_shader,
    # load_shader_id,  # Not needed.
    load_shader_from_string as _load_shader_from_string,
    # load_shader_id_from_string,  # Not needed.
    load_sprite_shader as _load_sprite_shader,
    # load_sprite_shader_id,  # Not needed.
    set_shader_constant_array_by_name as _set_shader_constant_array_by_name,
    set_shader_constant_by_name as _set_shader_constant_by_name,
    # Not listed on commands page.
    # set_shader_error_mode,  # Not needed.  AppGameKit Studio only.
    # set_shader_constant_array_float_by_name,  # Not needed.  Does the same as set_shader_constant_array_by_name.
    # set_shader_constant_array_vec2_by_name,  # Not needed.  Does the same as set_shader_constant_array_by_name.
    # set_shader_constant_array_vec3_by_name,  # Not needed.  Does the same as set_shader_constant_array_by_name.
    # set_shader_constant_array_vec4_by_name,  # Not needed.  Does the same as set_shader_constant_array_by_name.
)


class Shader(object):
    """Wraps shader functionality."""

    def __init__(self, *,
                 vertex_filename: str = None, pixel_filename: str = None,
                 vertex_source: str = None, pixel_source: str = None,
                 full_screen_filename: str = None,
                 sprite_filename: str = None):
        """
        Loads a shader from files or text strings.

        :param vertex_filename: Vertex shader file to be loaded.  `pixel_filename` must also be given.
        :param pixel_filename: Pixel shader file to be loaded.  `vertex_filename` must also be given.
        :param vertex_source: Vertex shader text to be loaded.  `pixel_source` must also be given.
        :param pixel_source: Pixel shader text to be loaded.  `vertex_source` must also be given.
        :param full_screen_filename: Full screen shader file to be loaded.
            The vertex shader will be automatically created.
        :param sprite_filename: Sprite shader file to be loaded. The vertex shader will be automatically created.
        """
        if vertex_filename and pixel_filename:
            self.__id = _load_shader(vertex_filename, pixel_filename)
        elif vertex_source and pixel_source:
            self.__id = _load_shader_from_string(vertex_source, pixel_source)
        elif full_screen_filename:
            self.__id = _load_full_screen_shader(full_screen_filename)
        elif sprite_filename:
            self.__id = _load_sprite_shader(sprite_filename)
        else:
            raise TypeError(f"{self.__class__.__name__}() requires"
                            f" both the 'vertex_filename' and 'pixel_filename' arguments,"
                            f" both the 'vertex_source' and 'pixel_source' arguments,"
                            f" the 'full_screen_filename' argument,"
                            f" or the 'sprite_filename' argument.")

    def __del__(self):
        """Delete the object."""
        try:
            _delete_shader(self.__id)
        except (TypeError, AttributeError):
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    # @staticmethod
    # def get_supported_varyings_count() -> int:
    #     return _get_supported_shader_varyings()

    def set_constant_array_by_name(self, name: str, index: int, value1: float, value2: float = 0, value3: float = 0,
                                   value4: float = 0):
        _set_shader_constant_array_by_name(self.__id, name, index, value1, value2, value3, value4)

    def set_constant_by_name(self, name: str, value1: float, value2: float = 0, value3: float = 0, value4: float = 0):
        _set_shader_constant_by_name(self.__id, name, value1, value2, value3, value4)
