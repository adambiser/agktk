"""
Memblocks
MeshMemblocks
"""
from appgamekit import (
    # Memblock > Sound
    create_memblock_from_sound as _create_memblock_from_sound,
    # create_memblock_id_from_sound,  # Not needed.
    # create_sound_from_memblock as _create_sound_from_memblock,  # See Sound class.
    # create_sound_id_from_memblock,  # Not needed.
    # Memblock > General
    copy_memblock as _copy_memblock,
    create_memblock as _create_memblock,
    # create_memblock_id,  # Not needed.
    delete_memblock as _delete_memblock,
    get_memblock_byte as _get_memblock_byte,
    get_memblock_byte_signed as _get_memblock_byte_signed,
    # get_memblock_exists as _get_memblock_exists,  # Not needed
    get_memblock_float as _get_memblock_float,
    get_memblock_int as _get_memblock_int,
    get_memblock_short as _get_memblock_short,
    get_memblock_size as _get_memblock_size,
    get_memblock_string as _get_memblock_string,
    set_memblock_byte as _set_memblock_byte,
    set_memblock_byte_signed as _set_memblock_byte_signed,
    set_memblock_float as _set_memblock_float,
    set_memblock_int as _set_memblock_int,
    set_memblock_short as _set_memblock_short,
    set_memblock_string as _set_memblock_string,
    # Memblock > File
    create_file_from_memblock as _create_file_from_memblock,
    create_memblock_from_file as _create_memblock_from_file,
    # create_memblock_id_from_file,  # Not needed.
    # Memblock > Image
    # create_image_from_memblock as _create_image_from_memblock,  # See Image class.
    # create_image_id_from_memblock,  # Not needed.
    create_memblock_from_image as _create_memblock_from_image,
    # create_memblock_id_from_image,  # Not needed.
    # Memblock > Mesh
    # add_object_mesh_from_memblock,  # See Object3D class
    create_memblock_from_object_mesh as _create_memblock_from_object_mesh,
    # create_memblock_id_from_object_mesh,  # Not needed.
    # create_object_from_mesh_memblock,  # See Object3D class
    # create_object_id_from_mesh_memblock,  # Not needed.
    # set_object_mesh_from_memblock,  # See Object3D class
    get_mesh_memblock_vertex_alpha as _get_mesh_memblock_vertex_alpha,
    get_mesh_memblock_vertex_blue as _get_mesh_memblock_vertex_blue,
    get_mesh_memblock_vertex_green as _get_mesh_memblock_vertex_green,
    get_mesh_memblock_vertex_normal_x as _get_mesh_memblock_vertex_normal_x,
    get_mesh_memblock_vertex_normal_y as _get_mesh_memblock_vertex_normal_y,
    get_mesh_memblock_vertex_normal_z as _get_mesh_memblock_vertex_normal_z,
    get_mesh_memblock_vertex_red as _get_mesh_memblock_vertex_red,
    get_mesh_memblock_vertex_u as _get_mesh_memblock_vertex_u,
    get_mesh_memblock_vertex_v as _get_mesh_memblock_vertex_v,
    get_mesh_memblock_vertex_x as _get_mesh_memblock_vertex_x,
    get_mesh_memblock_vertex_y as _get_mesh_memblock_vertex_y,
    get_mesh_memblock_vertex_z as _get_mesh_memblock_vertex_z,
    set_mesh_memblock_vertex_color as _set_mesh_memblock_vertex_color,
    set_mesh_memblock_vertex_normal as _set_mesh_memblock_vertex_normal,
    set_mesh_memblock_vertex_position as _set_mesh_memblock_vertex_position,
    set_mesh_memblock_vertex_uv as _set_mesh_memblock_vertex_uv,
)
from ._grfx import Image
from ._audio.sound import Sound
from ._grfx3d.object3d import Mesh


class Memblock(object):
    """
    Wraps AppGameKit memblock methods.
    """
    def __init__(self, *,
                 size: int = None,
                 filename: str = None,
                 image: Image = None,
                 sound: Sound = None,
                 **kwargs
                 ):
        if "_id" in kwargs:
            # Internal use only!
            self.__id = kwargs["_id"]
        elif filename:
            self.__id = _create_memblock_from_file(filename)
        elif image:
            self.__id = _create_memblock_from_image(image.id)
        elif sound:
            self.__id = _create_memblock_from_sound(sound.id)
        elif size is not None:
            self.__id = _create_memblock(size)
        else:
            raise TypeError(f"{self.__class__.__name__}() requires"
                            f" a 'size' argument"
                            f" a 'filename' argument,"
                            f" an 'image' argument,"
                            f" or a 'sound' argument.")

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_memblock(self.__id)
        except (TypeError, AttributeError):
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def copy(self, dst: "Memblock", src_offset: int, dst_offset: int, size: int):
        _copy_memblock(self.__id, dst.__id, src_offset, dst_offset, size)

    def get_byte(self, offset: int) -> int:
        return _get_memblock_byte(self.__id, offset)

    def set_byte(self, offset: int, value: int):
        _set_memblock_byte(self.__id, offset, value)

    def get_byte_signed(self, offset: int) -> int:
        return _get_memblock_byte_signed(self.__id, offset)

    def set_byte_signed(self, offset: int, value: int):
        _set_memblock_byte_signed(self.__id, offset, value)

    def get_float(self, offset: int) -> float:
        return _get_memblock_float(self.__id, offset)

    def set_float(self, offset: int, value: float):
        _set_memblock_float(self.__id, offset, value)

    def get_int(self, offset: int) -> int:
        return _get_memblock_int(self.__id, offset)

    def set_int(self, offset: int, value: int):
        _set_memblock_int(self.__id, offset, value)

    def get_short(self, offset: int) -> int:
        return _get_memblock_short(self.__id, offset)

    def set_short(self, offset: int, value: int):
        _set_memblock_short(self.__id, offset, value)

    @property
    def size(self) -> int:
        return _get_memblock_size(self.__id)

    def get_string(self, offset: int, length: int) -> str:
        return _get_memblock_string(self.__id, offset, length)

    def set_string(self, offset: int, value: str):
        _set_memblock_string(self.__id, offset, value)

    def save_to_file(self, filename):
        _create_file_from_memblock(filename, self.__id)


class MeshMemblock(Memblock):
    """
    Wraps AppGameKit mesh memblock methods.
    """
    def __init__(self, *, mesh: Mesh):
        if mesh:
            super().__init__(_id=_create_memblock_from_object_mesh(mesh.object3d.id, mesh.id))
        else:
            raise TypeError(f"{self.__class__.__name__}() requires"
                            f" a 'mesh' argument.")
        # Store the id privately so this subclass has a copy.
        self.__id = self.id

    def get_vertex_alpha(self, vertex: int) -> int:
        return _get_mesh_memblock_vertex_alpha(self.__id, vertex)

    def get_vertex_blue(self, vertex: int) -> int:
        return _get_mesh_memblock_vertex_blue(self.__id, vertex)

    def get_vertex_green(self, vertex: int) -> int:
        return _get_mesh_memblock_vertex_green(self.__id, vertex)

    def get_vertex_red(self, vertex: int) -> int:
        return _get_mesh_memblock_vertex_red(self.__id, vertex)

    def set_vertex_color(self, vertex: int, red: int, green: int, blue: int, alpha: int):
        _set_mesh_memblock_vertex_color(self.__id, vertex, red, green, blue, alpha)

    def get_vertex_normal_x(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_normal_x(self.__id, vertex)

    def get_vertex_normal_y(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_normal_y(self.__id, vertex)

    def get_vertex_normal_z(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_normal_z(self.__id, vertex)

    def set_vertex_normal(self, vertex: int, x: float, y: float, z: float):
        _set_mesh_memblock_vertex_normal(self.__id, vertex, x, y, z)

    def get_vertex_u(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_u(self.__id, vertex)

    def get_vertex_v(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_v(self.__id, vertex)

    def set_vertex_uv(self, vertex: int, u: float, v: float):
        _set_mesh_memblock_vertex_uv(self.__id, vertex, u, v)

    def get_vertex_x(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_x(self.__id, vertex)

    def get_vertex_y(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_y(self.__id, vertex)

    def get_vertex_z(self, vertex: int) -> float:
        return _get_mesh_memblock_vertex_z(self.__id, vertex)

    def set_vertex_position(self, vertex: int, x: float, y: float, z: float):
        _set_mesh_memblock_vertex_position(self.__id, vertex, x, y, z)
