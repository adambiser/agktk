"""
Contains methods and classes for various input devices, both physical and emulated.

To access emulated input, use ``import agktk.input.emulated``

To access sensors, use ``import agktk.input.sensors``

Sensors are not available on Windows or Linux, but are included for potential future mobile support.
"""

from . import joysticks
from . import keyboard
from . import mouse
from . import multitouch
from . import textinput
from ._editbox import EditBox
from ._virtualbutton import VirtualButton
from ._virtualjoystick import VirtualJoystick
