"""
Contains the Image class.
"""
from appgamekit import (
    sync as _sync,
    # Image > General
    # copy_image,  # Use copy_image_to
    copy_image_to,
    # create_image_color,  # Use create_image_color_id
    create_image_color_id,
    # create_render_image,  # Use create_render_image_id
    create_render_image_id,
    # delete_all_images,  # not needed
    delete_image,
    # get_image,  # TODO Move to Device class... this is the backbuffer image.
    # get_image_exists,  # not needed
    get_image_size_from_file,
    # load_image,  # Use load_image_id
    load_image_id,
    # load_image_resized,  # Use load_image_id and resize_image instead.
    # load_image_id_resized,  # Use load_image_id and resize_image instead.
    load_subimage_id,
    print_image,
    save_image,
    # Image > Choose
    get_chosen_image,
    is_choosing_image,
    show_choose_image_screen,
    # Image > Properties
    get_image_filename,
    get_image_height,
    get_image_width,
    set_image_mag_filter,
    set_image_min_filter,
    set_image_wrap_u,
    set_image_wrap_v,
    # Image > Capture
    #   See device.DeviceCamera
    # Image > QR
    # See qrcode
    # Image > Modify
    resize_image,
    set_image_mask,
    set_image_transparent_color,
    # Memblock > Image
    create_image_id_from_memblock as _create_image_id_from_memblock,
)
from ._enums import (
    Filter,
    TextureWrap,
    ColorChannel,
    RenderImageType,
)
from ._utils import iter_id
from typing import (
    Tuple,
    Optional,
    Union,
    TYPE_CHECKING
)
if TYPE_CHECKING:
    from ._memblock import Memblock


class Image:
    """
    Wraps AGK image methods.
    """
    __iter_id = iter_id()

    def __init__(self, filename: str = None, black_to_alpha: bool = False, scale_x: float = 1.0, scale_y: float = 1.0):
        """
        This class wraps the variety of different image types that AGK provides.

        When `filename` is given, the image is loaded from that file.  If `scale` is also given, the image is resized.

        Otherwise, an empty Image is created.

        :param str filename: The filename of the image to load.
        :param bool black_to_alpha: When True, black pixels are made transparent and all others are opaque.
        :param float scale_x: The amount to scale the image in the x-direction, 1.0 is the original size.
        :param float scale_y: The amount to scale the image in the y-direction, 1.0 is the original size.
        """
        # Because it is sometimes necessary to create empty Images that have only an ID, mainly for
        # set_device_camera_to_image, this class generates its own ID in order to hide the whole ID stuff from users.
        # noinspection PyShadowingBuiltins
        self.__id = next(Image.__iter_id)
        # Begin with an empty image.
        self.__parent_image = None  # type: Optional["Image"]  # Used by subimages.
        if filename:
            self.load(filename, black_to_alpha, scale_x, scale_y)

    def __del__(self):
        """Delete the image."""
        try:
            delete_image(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def load(self, filename: str = None, black_to_alpha: bool = False, scale_x: float = 1.0, scale_y: float = 1.0):
        # noinspection PyShadowingBuiltins
        id = self.__id
        load_image_id(id, filename, black_to_alpha)
        if scale_x != 1.0 or scale_y != 1.0:
            resize_image(id, int(get_image_width(id) * scale_x), int(get_image_height(id) * scale_y))

    def copy(self, x: int, y: int, width: int, height: int) -> 'Image':
        """Copies a portion of this image into a new image."""
        image = Image()
        copy_image_to(image.__id, self.__id, x, y, width, height)
        return image

    @classmethod
    def create_color_image(cls, red: int, green: int, blue: int, alpha: int = 255) -> "Image":
        """
        Creates a 1x1 pixel of the specified color.

        :param int red: The red component of the image (0 to 255).
        :param int green: The green component of the image (0 to 255).
        :param int blue: The blue component of the image (0 to 255).
        :param int alpha: The alpha component of the image (0 to 255), 0 is completely transparent.
        """
        image = Image()
        create_image_color_id(image.__id, red, green, blue, alpha)
        return image

    @classmethod
    def create_render_image(cls, width: int, height: int, is_depth_map: bool = False,
                            generate_mipmaps: bool = False) -> "Image":
        """
        Creates a blank image suitable for rendering.

        :param int width: The width of the render image.
        :param int height: The height of the render image.
        :param bool is_depth_map: For render images, True to create a depthmap; False to create an RGBA image.
        :param bool generate_mipmaps: For render images, True to use mipmapping on this image, False to turn it off.
        """
        image = Image()
        create_render_image_id(image.__id, width, height,
                               RenderImageType.DEPTH if is_depth_map else RenderImageType.RGBA, generate_mipmaps)
        return image

    @classmethod
    def get_size_from_file(cls, filename: str) -> Tuple[int, int]:
        size = get_image_size_from_file(filename)
        return size >> 16, size & 0xffff

    def get_subimage(self, subimage_name: str) -> 'Image':
        """Loads a sub image from an atlas texture into a standalone image."""
        image = Image()
        load_subimage_id(image.__id, self.__id, subimage_name)
        # Store a reference to the parent image to prevent it from being deleted until all subimages are deleted.
        image.__parent_image = self
        return image

    def print(self, percentage: float):
        """Prints an image to a connected printer. Not guaranteed to work on all platforms."""
        print_image(self.__id, percentage)

    def save(self, filename: str):
        """Saves the image to the file name specified within AGK's write path."""
        save_image(self.__id, filename)

    @staticmethod
    def _from_id(image_id: int) -> Optional['Image']:
        """
        Takes an image ID returned by AppGameKit creates and Image instance from it that is guaranteed to have an ID
        that hasn't already been assigned by the class.  This ID might be different from the given ID.
        """
        if image_id == 0:
            return None
        image = Image()
        # If the ID generated by this class matches the one given, everything is good.
        if image_id == image.__id:
            return image
        # Otherwise, copy the given image into the generated one so it doesn't conflict with an ID this class has
        # already assigned.
        return image.copy(0, 0, image.width, image.height)

    @classmethod
    def get_chosen_image(cls) -> Optional['Image']:
        """
        Returns the newly chosen image picked using show_choose_image_screen() or None if canceled or the chosen Image
        was already returned by a previous call to this function.
        """
        return cls._from_id(get_chosen_image())

    @staticmethod
    def is_choosing_image() -> bool:
        """
        Returns True if AGK is currently displaying a choose image screen and waiting for the user to pick an image.

        When False, the user has either cancelled or chosen an image, check get_chosen_image to see what
        the result was.
        """
        return is_choosing_image()

    @staticmethod
    def show_choose_image_screen() -> bool:
        """
        Presents the user with an option to choose an image stored on their current platform.

        Assume the app is running but no longer visible and use is_choosing_image to check when the user returns from
        the image choosing process, and get_chosen_image to discover the result of the process.

        This function returns True if it was successful in displaying the choose screen, otherwise False.
        """
        return show_choose_image_screen()

    @classmethod
    def choose(cls, sync_function: callable = _sync) -> Optional['Image']:
        """
        A function that performs all image choosing functionality and returns the result.

        :param sync_function: The function to call each frame (should call `sync`).  If not given, `sync` is called.
        :returns: The chosen Image or None if cancelled.
        """
        if show_choose_image_screen():
            while is_choosing_image():
                sync_function()
            # Sync again to clear frame state values.
            sync_function()
        return cls._from_id(get_chosen_image())

    @property
    def filename(self) -> str:
        """Returns the file name used to load this image."""
        return get_image_filename(self.__id)

    @property
    def height(self) -> int:
        """Returns the height of the image in pixels."""
        return int(get_image_height(self.__id))

    @property
    def width(self) -> int:
        """Returns the width of the image in pixels."""
        return int(get_image_width(self.__id))

    def set_mag_filter(self, filter_mode: Union[Filter, int]):
        """
        Sets the filter to use when magnifying textures.

        Valid filter values are FILTER_NEAREST and FILTER_LINEAR.
        """
        set_image_mag_filter(self.__id, filter_mode)

    def set_min_filter(self, filter_mode: Union[Filter, int]):
        """
        Sets the filter to use when minifying textures.

        Valid filter values are FILTER_NEAREST and FILTER_LINEAR.
        """
        set_image_min_filter(self.__id, filter_mode)

    def set_wrap_u(self, wrap_mode: Union[TextureWrap, int]):
        """
        Sets the texture wrap mode of the image when the U coordinate goes outside the range 0-1.

        Valid wrap_mode values are WRAP_REPEAT and WRAP_CLAMP.
        """
        set_image_wrap_u(self.__id, wrap_mode)

    def set_wrap_v(self, wrap_mode: Union[TextureWrap, int]):
        """
        Sets the texture wrap mode of the image when the V coordinate goes outside the range 0-1.

        Valid wrap_mode values are WRAP_REPEAT and WRAP_CLAMP.
        """
        set_image_wrap_v(self.__id, wrap_mode)

    def resize(self, width: int, height: int):
        """Resizes an image to new width and height."""
        resize_image(self.__id, width, height)

    def scale(self, scale_x: float, scale_y: float):
        """Scales the size of the image."""
        # noinspection PyShadowingBuiltins
        id = self.__id
        resize_image(id, int(get_image_width(id) * scale_x), int(get_image_height(id) * scale_y))

    def set_mask(self, src_image: 'Image',
                 dst_color_channel: Union[ColorChannel, int],
                 src_color_channel: Union[ColorChannel, int], x: int, y: int):
        """Copies a color channel from one image to another."""
        set_image_mask(self.__id, src_image.__id, dst_color_channel, src_color_channel, x, y)

    def set_transparent_color(self, red: int, green: int, blue: int):
        """Turns a particular color completely transparent in the chosen image."""
        set_image_transparent_color(self.__id, red, green, blue)

    @classmethod
    def from_memblock(cls, memblock: "Memblock") -> "Image":
        image = Image()
        _create_image_id_from_memblock(image.__id, memblock.id)
        return image
