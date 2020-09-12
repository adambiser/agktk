# TODO Make method, classmethod of Image?
# Image > QR
from appgamekit import (
    decode_qr_code as _decode_qr_code,
    encode_qr_code as _encode_qr_code
)
from .image import Image as _Image


def decode(image: _Image) -> str:
    """
    Attempts to decode a QR code and return the string encoded within it.

    :param Image image: The image to decode.
    :return: The string encoded in the image when successful or an empty string if it fails.
    :rtype: str
    """
    return _decode_qr_code(image.id)


def encode(text: str, error_mode: int) -> _Image:
    """
    Encodes the given text into a QR code and returns a new Image containing that code.

    :param str text: The text to encode.
    :param int error_mode: The level of error correction to include in the code from 0 (lowest) to 3 (highest).
    :return: An Image of the encoded text.
    :rtype: Image
    """
    # noinspection PyProtectedMember
    return _Image._from_id(_encode_qr_code(text, error_mode))
