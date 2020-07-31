"""
Wrapper classes for AppGameKit.

Provides classes that encapsulate groups of AGK commands to allow for more rapid development.
"""
# Import agk functions like this to make calling them faster.

# from ._methods import *
# from ._application import Application

# __all__ = ["appgamekit", "qrcode", "VirtualButton"]

# separate imports:
# import agktk.debug as debug
# import agktk.network as network


# noinspection PyUnresolvedReferences
from appgamekit import Application  # , create_window, destroy_window

from ._constants import *
from ._game import Game

from . import device
from . import display
from . import io
from ._font import Font
from . import net  # network?
from ._image import *
from .input import *
from ._memblock import *  # general?
from . import mixer  # audio
from ._music import Music  # audio
from . import qrcode
from ._particles import *  # 2d
from ._skeleton import Skeleton2D, Bone, Skeleton2DFileType  # 2d
from ._sound import Sound, SoundInstance  # audio
from ._sprite import Sprite, PhysicsMode, TransparencyMode  # 2d
from ._text import Text, HorizontalAlign
from . import time  # general
from ._tweening import *
from ._vector3 import *  # 3d
from . import video  # 2d

# # from ._shader import *
