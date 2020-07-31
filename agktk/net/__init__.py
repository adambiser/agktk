"""
Contains classes and methods for networking.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # HTTP > Encoding
    http_decode,
    http_encode,
    # HTTP > General
    #   See _http
    # TODO Move these here now?
    #   get_internet_state,  # See device
    #   open_browser,  # See device
)
from ._http import *
from ._network import *
