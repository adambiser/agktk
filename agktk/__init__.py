"""Wrapper classes for AppGameKit.

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
from appgamekit import Application

from .constants import *
# # from ._2dphysics import *
# from ._3d import Camera
# from ._3dparticles import Particles3D
# # from ._3dphysics import *
# # Adverts - Skipped
from . import device  # general
from . import display  # general
# # Extras - Skipped
# from ._file import Zip, File, Folder
from . import file  # io
from . import zipfile  # io
from .font import Font
from .http import *  # network?
from .image import *  # general
from .input import *  # general
from .memblock import *  # general?
# # from ._multiplayer import *
from . import mixer  # audio
from .music import Music  # audio
from . import qrcode
from .particles import *  # 2d
from .skeleton import Skeleton2D, Bone, Skeleton2DFileType  # 2d
from .sound import Sound, SoundInstance  # audio
from .sprite import Sprite, PhysicsMode, TransparencyMode  # 2d
from .text import Text, HorizontalAlign
from . import time
from .tweening import *
from .vector3 import *  # 3d
from . import video  # 2d

# # from ._shader import *

