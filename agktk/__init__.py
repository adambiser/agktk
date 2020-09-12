"""
Wrapper classes for AppGameKit.

Provides classes that encapsulate groups of AGK commands to allow for more rapid development.
"""
__version__ = "0.2"

# Import agk functions like this to make calling them faster.

# from ._methods import *
# from ._application import Application

# __all__ = ["appgamekit", "qrcode", "VirtualButton"]

# separate imports:
# import agktk.debug
# import agktk.network
# import agktk.physics2d
# import agktk.physics3d

# noinspection PyUnresolvedReferences
# from appgamekit import Application  # , create_window, destroy_window

# from ._constants import *
from ._enums import *
from ._game import Game

from . import device
from . import display
from . import io
from . import net
from . import time

from ._audio import *
from ._grfx import *
from ._grfx3d import *
from .input import *

from ._memblock import Memblock, MeshMemblock
from ._tweening import *
from ._vector3 import Vector3
