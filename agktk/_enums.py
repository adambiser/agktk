import appgamekit
from enum import IntEnum as _IntEnum


# Anti-alias modes - set_antialias_mode
class AntiAlias(_IntEnum):
    NONE = appgamekit.AA_NONE
    FOURX_MSAA = appgamekit.AA_4XMSAA


# Alignment - create_advert, create_advert_ex, set_advert_location, set_advert_location_ex, set_text_alignment
class HorizontalAlign(_IntEnum):
    LEFT = appgamekit.ALIGN_LEFT
    CENTER = appgamekit.ALIGN_CENTER
    RIGHT = appgamekit.ALIGN_RIGHT


class VerticalAlign(_IntEnum):
    TOP = appgamekit.ALIGN_TOP
    CENTER = appgamekit.ALIGN_CENTER
    BOTTOM = appgamekit.ALIGN_BOTTOM


# Axis - add_object_shape_capsule, add_object_shape_cone, add_object_shape_cylinder,
# create_3d_physics_character_controller, create_object_capsule, set_object_shape_capsule, set_object_shape_cone,
# set_object_shape_cylinder
class Axis(_IntEnum):
    X = appgamekit.AXIS_X
    Y = appgamekit.AXIS_Y
    Z = appgamekit.AXIS_Z


# Ad banner sizes - create_advert, create_advert_ex
class AdvertSize(_IntEnum):
    BANNER = appgamekit.ADVERT_BANNER
    LARGE_BANNER = appgamekit.ADVERT_LARGE_BANNER
    MEDIUM_RECTANGLE = appgamekit.ADVERT_MEDIUM_RECTANGLE
    FULL_BANNER = appgamekit.ADVERT_FULL_BANNER
    LEADERBOARD = appgamekit.ADVERT_LEADERBOARD
    SMART_BANNER = appgamekit.ADVERT_SMART_BANNER
    FLUID_BANNER = appgamekit.ADVERT_FLUID_BANNER


# Alpha blend modes - set_object_blend_modes
class AlphaBlendMode(_IntEnum):
    ZERO = appgamekit.BLEND_ZERO
    ONE = appgamekit.BLEND_ONE
    SRC_ALPHA = appgamekit.BLEND_SRC_ALPHA
    ONE_MINUS_SRC_ALPHA = appgamekit.BLEND_ONE_MINUS_SRC_ALPHA
    DST_ALPHA = appgamekit.BLEND_DST_ALPHA
    ONE_MINUS_DST_ALPHA = appgamekit.BLEND_ONE_MINUS_DST_ALPHA
    SRC_COLOR = appgamekit.BLEND_SRC_COLOR
    ONE_MINUS_SRC_COLOR = appgamekit.BLEND_ONE_MINUS_SRC_COLOR
    DST_COLOR = appgamekit.BLEND_DST_COLOR
    ONE_MINUS_DST_COLOR = appgamekit.BLEND_ONE_MINUS_DST_COLOR
    SRC_ALPHA_SATURATE = appgamekit.BLEND_SRC_ALPHA_SATURATE


# Device camera types - returned by get_device_camera_type
class CameraType(_IntEnum):
    BACK_FACING = appgamekit.CAMERA_TYPE_BACK_FACING
    FRONT_FACING = appgamekit.CAMERA_TYPE_FRONT_FACING
    UNKNOWN = appgamekit.CAMERA_TYPE_UNKNOWN


# Physics character controler move types - move_3d_physics_character_controller
class ControllerMove(_IntEnum):
    STOP = appgamekit.CONTROLLER_MOVE_STOP
    FORWARD = appgamekit.CONTROLLER_MOVE_FORWARD
    BACKWARD = appgamekit.CONTROLLER_MOVE_BACKWARD
    STRAFE_LEFT = appgamekit.CONTROLLER_MOVE_STRAFE_LEFT
    STRAFE_RIGHT = appgamekit.CONTROLLER_MOVE_STRAFE_RIGHT


# Color mask channels - set_image_mask
class ColorChannel(_IntEnum):
    RED = appgamekit.COLOR_CHANNEL_RED
    GREEN = appgamekit.COLOR_CHANNEL_GREEN
    BLUE = appgamekit.COLOR_CHANNEL_BLUE
    ALPHA = appgamekit.COLOR_CHANNEL_ALPHA


# Cull modes - set_object_cull_mode
class CullMode(_IntEnum):
    FRONT_AND_BACK = appgamekit.CULL_FRONT_AND_BACK
    FRONT = appgamekit.CULL_FRONT
    BACK = appgamekit.CULL_BACK


# Depth read modes - set_object_depth_read_mode
class DepthReadMode(_IntEnum):
    NEVER = appgamekit.DEPTH_NEVER
    LESS_THAN = appgamekit.DEPTH_LT
    EQUAL = appgamekit.DEPTH_EQUAL
    LESS_THAN_OR_EQUAL = appgamekit.DEPTH_LT_OR_EQUAL
    GREATER_THAN = appgamekit.DEPTH_GT
    NOT_EQUAL = appgamekit.DEPTH_NOT_EQUAL
    GREATER_THAN_OR_EQUAL = appgamekit.DEPTH_GT_OR_EQUAL
    ALWAYS = appgamekit.DEPTH_ALWAYS


# Edit box wrap modes - set_edit_box_wrap_mode
class EditBoxWrapMode(_IntEnum):
    SCROLL = appgamekit.EDIT_BOX_WRAP_SCROLL
    NEW_LINE = appgamekit.EDIT_BOX_WRAP_NEW_LINE


# Error modes - set_error_mode
class ErrorMode(_IntEnum):
    IGNORE = appgamekit.ERROR_MODE_IGNORE
    REPORT = appgamekit.ERROR_MODE_REPORT
    STOP = appgamekit.ERROR_MODE_STOP


# Folder modes - get_file_count, get_folder_count, get_first_file, get_first_folder
class FolderMode(_IntEnum):
    READ_ONLY = appgamekit.FOLDER_MODE_READ_ONLY
    WRITE_ONLY = appgamekit.FOLDER_MODE_WRITE_ONLY
    BOTH = appgamekit.FOLDER_MODE_BOTH


# Texture filters - set_default_mag_filter, set_default_min_filter, set_image_mag_filter, set_image_min_filter,
# set_text_default_mag_filter, set_text_default_min_filter
class Filter(_IntEnum):
    NEAREST = appgamekit.FILTER_NEAREST
    LINEAR = appgamekit.FILTER_LINEAR


# HTTP response status - get_http_response_ready
class HttpResponseState(_IntEnum):
    FAILED = appgamekit.HTTP_RESPONSE_STATUS_FAILED
    IN_PROGRESS = appgamekit.HTTP_RESPONSE_STATUS_IN_PROGRESS
    COMPLETED = appgamekit.HTTP_RESPONSE_STATUS_COMPLETED


# Text input state - returned by get_text_input_state
class TextInputState(_IntEnum):
    ACTIVE = appgamekit.INPUT_TEXT_ACTIVE
    DONE = appgamekit.INPUT_TEXT_DONE


# Render image modes - create_render_image
class RenderImageType(_IntEnum):
    RGBA = appgamekit.IMAGE_RGBA
    DEPTH = appgamekit.IMAGE_DEPTH


# Color interpolation modes - set_3d_particles_color_interpolation, set_particles_color_interpolation
class InterpolationMode(_IntEnum):
    NONE = appgamekit.INTERPOLATE_NONE
    SMOOTH = appgamekit.INTERPOLATE_SMOOTH


# Keyboard types - returned by get_keyboard_exists
class KeyboardType(_IntEnum):
    NONE = appgamekit.KEYBOARD_NONE
    FULL_SIZE = appgamekit.KEYBOARD_FULL_SIZE
    VIRTUAL = appgamekit.KEYBOARD_VIRTUAL


# Network variable types - set_network_local_float, set_network_local_integer
class VariableType(_IntEnum):
    NORMAL = appgamekit.NETWORK_VAR_TYPE_NORMAL
    RESETTING = appgamekit.NETWORK_VAR_TYPE_RESETTING


# Orientation mode - returned by get_orientation
class Orientation(_IntEnum):
    PORTRAIT = appgamekit.ORIENTATION_PORTRAIT
    PORTRAIT_180 = appgamekit.ORIENTATION_PORTRAIT_180
    LANDSCAPE_CCW = appgamekit.ORIENTATION_LANDSCAPE_CCW
    LANDSCAPE_CW = appgamekit.ORIENTATION_LANDSCAPE_CW


# Physics modes - set_sprite_physics_on
class PhysicsMode(_IntEnum):
    # DISABLED = 0
    STATIC = appgamekit.PHYSICS_MODE_STATIC
    DYNAMIC = appgamekit.PHYSICS_MODE_DYNAMIC
    KINEMATIC = appgamekit.PHYSICS_MODE_KINEMATIC


# Point light modes - set_point_light_mode
class PointLightMode(_IntEnum):
    VERTEX = appgamekit.POINT_LIGHT_VERTEX
    PIXEL = appgamekit.POINT_LIGHT_PIXEL


# Anisotropic friction modes - set_object_3d_physics_anisotropic_friction
# TODO Use appgamekit constants once added to PYD.
class AnisotropicFrictionMode(_IntEnum):
    DISABLED = 0
    FRICTION = 1
    ROLLING_FRICTION = 2


# Ray cast contact - ray_cast_3d_physics, ray_cast_3d_physics_object
class RayCastMode(_IntEnum):
    CLOSEST = appgamekit.RAY_CAST_CLOSEST
    ALL = appgamekit.RAY_CAST_ALL


# Resolution Modes - set_resolution_mode
class ResolutionMode(_IntEnum):
    LOW = appgamekit.RESOLUTION_MODE_LOW
    HIGH = appgamekit.RESOLUTION_MODE_HIGH


# Rotation modes - set_particles_face_direction
class RotationMode(_IntEnum):
    NORMAL = appgamekit.ROTATE_NORMAL
    MOVE_DIRECTION = appgamekit.ROTATE_MOVE_DIRECTION


# Music seek modes - seek_music_ogg
class SeekMode(_IntEnum):
    ABSOLUTE = appgamekit.SEEK_ABSOLUTE
    RELATIVE = appgamekit.SEEK_RELATIVE


# Shadow mapping modes - set_shadow_mapping_mode
class ShadowMappingMode(_IntEnum):
    NONE = appgamekit.SHADOW_MAP_NONE
    UNIFORM = appgamekit.SHADOW_MAP_UNIFORM
    LISPSM = appgamekit.SHADOW_MAP_LISPSM
    CASCADE = appgamekit.SHADOW_MAP_CASCADE


# Shadow smoothing - set_shadow_smoothing
class ShadowSmoothingMode(_IntEnum):
    NONE = appgamekit.SHADOW_SMOOTHING_NONE
    MULTISAMPLE = appgamekit.SHADOW_SMOOTHING_MULTISAMPLE
    RANDOM_MULTISAMPLE = appgamekit.SHADOW_SMOOTHING_RANDOM_MULTISAMPLE


# Sprite shapes - set_sprite_shape
class SpriteShape(_IntEnum):
    NONE = appgamekit.SHAPE_NONE
    CIRCLE = appgamekit.SHAPE_CIRCLE
    BOX = appgamekit.SHAPE_BOX
    POLYGON = appgamekit.SHAPE_POLYGON


# Socket states - get_socket_connected
class SocketState(_IntEnum):
    DISCONNECTED = appgamekit.SOCKET_STATE_DISCONNECTED
    CONNECTING = appgamekit.SOCKET_STATE_CONNECTING
    CONNECTED = appgamekit.SOCKET_STATE_CONNECTED


# Key, button, and pointer states - returned by get_button_state, get_pointer_state, get_virtual_button_state,
# get_raw_joystick_button_state, get_raw_key_state, get_raw_mouse_left_state, get_raw_mouse_middle_state,
# get_raw_mouse_right_state
class ButtonState(_IntEnum):
    UP = appgamekit.STATE_UP
    DOWN = appgamekit.STATE_DOWN


class KeyState(_IntEnum):
    UP = appgamekit.STATE_UP
    DOWN = appgamekit.STATE_DOWN


# Touch types - returned by get_raw_touch_type
class TouchType(_IntEnum):
    UNKNOWN = appgamekit.TOUCH_UNKNOWN
    SHORT = appgamekit.TOUCH_SHORT
    HOLD = appgamekit.TOUCH_HOLD
    DRAG = appgamekit.TOUCH_DRAG


# Transparency modes - set_object_transparency, set_3d_particles_transparency, set_particles_transparency,
# set_sprite_transparency, set_text_transparency, returned by get_sprite_transparency
class TransparencyMode(_IntEnum):
    NONE = appgamekit.TRANSPARENCY_NONE
    ALPHA = appgamekit.TRANSPARENCY_ALPHA
    ADDITIVE = appgamekit.TRANSPARENCY_ADDITIVE
    CUSTOM = appgamekit.TRANSPARENCY_CUSTOM


# Tween interpolation types - the set_tween_* methods
class TweenInterpolation(_IntEnum):
    OFF = appgamekit.TWEEN_OFF
    LINEAR = appgamekit.TWEEN_LINEAR
    SMOOTH1 = appgamekit.TWEEN_SMOOTH1
    SMOOTH2 = appgamekit.TWEEN_SMOOTH2
    EASE_IN1 = appgamekit.TWEEN_EASE_IN1
    EASE_IN2 = appgamekit.TWEEN_EASE_IN2
    EASE_OUT1 = appgamekit.TWEEN_EASE_OUT1
    EASE_OUT2 = appgamekit.TWEEN_EASE_OUT2
    BOUNCE = appgamekit.TWEEN_BOUNCE
    OVERSHOOT = appgamekit.TWEEN_OVERSHOOT


# Video load responses - load_video
class VideoLoadResult(_IntEnum):
    UNSUPPORTED = appgamekit.VIDEO_LOAD_UNSUPPORTED
    ERROR = appgamekit.VIDEO_LOAD_ERROR
    SUCCESS = appgamekit.VIDEO_LOAD_SUCCESS


# UV Texture wrapping modes - set_default_wrap_u, set_default_wrap_v, set_image_wrap_u, set_image_wrap_v
class TextureWrap(_IntEnum):
    CLAMP = appgamekit.WRAP_CLAMP
    REPEAT = appgamekit.WRAP_REPEAT


# View zoom modes
class ZoomMode(_IntEnum):
    TOP_LEFT = appgamekit.ZOOM_TOP_LEFT
    CENTER = appgamekit.ZOOM_CENTER


# Key codes
# noinspection PyPep8
class Key(_IntEnum):
    BACKSPACE = appgamekit.KEY_BACKSPACE
    TAB = appgamekit.KEY_TAB
    ENTER = appgamekit.KEY_ENTER
    SHIFT = appgamekit.KEY_SHIFT
    CONTROL = appgamekit.KEY_CONTROL
    ALT = appgamekit.KEY_ALT
    PAUSE = appgamekit.KEY_PAUSE
    CAPSLOCK = appgamekit.KEY_CAPSLOCK
    ESCAPE = appgamekit.KEY_ESCAPE
    SPACE = appgamekit.KEY_SPACE
    PAGE_UP = appgamekit.KEY_PAGE_UP
    PAGE_DOWN = appgamekit.KEY_PAGE_DOWN
    END = appgamekit.KEY_END
    HOME = appgamekit.KEY_HOME
    LEFT = appgamekit.KEY_LEFT
    UP = appgamekit.KEY_UP
    RIGHT = appgamekit.KEY_RIGHT
    DOWN = appgamekit.KEY_DOWN
    INSERT = appgamekit.KEY_INSERT
    DELETE = appgamekit.KEY_DELETE
    NUM_0 = appgamekit.KEY_NUM_0
    NUM_1 = appgamekit.KEY_NUM_1
    NUM_2 = appgamekit.KEY_NUM_2
    NUM_3 = appgamekit.KEY_NUM_3
    NUM_4 = appgamekit.KEY_NUM_4
    NUM_5 = appgamekit.KEY_NUM_5
    NUM_6 = appgamekit.KEY_NUM_6
    NUM_7 = appgamekit.KEY_NUM_7
    NUM_8 = appgamekit.KEY_NUM_8
    NUM_9 = appgamekit.KEY_NUM_9
    A = appgamekit.KEY_A
    B = appgamekit.KEY_B
    C = appgamekit.KEY_C
    D = appgamekit.KEY_D
    E = appgamekit.KEY_E
    F = appgamekit.KEY_F
    G = appgamekit.KEY_G
    H = appgamekit.KEY_H
    I = appgamekit.KEY_I
    J = appgamekit.KEY_J
    K = appgamekit.KEY_K
    L = appgamekit.KEY_L
    M = appgamekit.KEY_M
    N = appgamekit.KEY_N
    O = appgamekit.KEY_O
    P = appgamekit.KEY_P
    Q = appgamekit.KEY_Q
    R = appgamekit.KEY_R
    S = appgamekit.KEY_S
    T = appgamekit.KEY_T
    U = appgamekit.KEY_U
    V = appgamekit.KEY_V
    W = appgamekit.KEY_W
    X = appgamekit.KEY_X
    Y = appgamekit.KEY_Y
    Z = appgamekit.KEY_Z
    WIN_LEFT = appgamekit.KEY_WIN_LEFT
    WIN_RIGHT = appgamekit.KEY_WIN_RIGHT
    MENU = appgamekit.KEY_MENU
    NUMPAD_0 = appgamekit.KEY_NUMPAD_0
    NUMPAD_1 = appgamekit.KEY_NUMPAD_1
    NUMPAD_2 = appgamekit.KEY_NUMPAD_2
    NUMPAD_3 = appgamekit.KEY_NUMPAD_3
    NUMPAD_4 = appgamekit.KEY_NUMPAD_4
    NUMPAD_5 = appgamekit.KEY_NUMPAD_5
    NUMPAD_6 = appgamekit.KEY_NUMPAD_6
    NUMPAD_7 = appgamekit.KEY_NUMPAD_7
    NUMPAD_8 = appgamekit.KEY_NUMPAD_8
    NUMPAD_9 = appgamekit.KEY_NUMPAD_9
    ASTERISK = appgamekit.KEY_ASTERISK
    PLUS = appgamekit.KEY_PLUS
    SUBTRACT = appgamekit.KEY_SUBTRACT
    DECIMAL = appgamekit.KEY_DECIMAL
    DIVIDE = appgamekit.KEY_DIVIDE
    F1 = appgamekit.KEY_F1
    F2 = appgamekit.KEY_F2
    F3 = appgamekit.KEY_F3
    F4 = appgamekit.KEY_F4
    F5 = appgamekit.KEY_F5
    F6 = appgamekit.KEY_F6
    F7 = appgamekit.KEY_F7
    F8 = appgamekit.KEY_F8
    F9 = appgamekit.KEY_F9
    F10 = appgamekit.KEY_F10
    F11 = appgamekit.KEY_F11
    F12 = appgamekit.KEY_F12
    NUMLOCK = appgamekit.KEY_NUMLOCK
    SCROLLLOCK = appgamekit.KEY_SCROLLLOCK
    VOLUME_MUTE = appgamekit.KEY_VOLUME_MUTE
    VOLUME_DOWN = appgamekit.KEY_VOLUME_DOWN
    VOLUME_UP = appgamekit.KEY_VOLUME_UP
    MEDIA_NEXT = appgamekit.KEY_MEDIA_NEXT
    MEDIA_PREV = appgamekit.KEY_MEDIA_PREV
    MEDIA_STOP = appgamekit.KEY_MEDIA_STOP
    MEDIA_PLAY = appgamekit.KEY_MEDIA_PLAY
    SEMICOLON = appgamekit.KEY_SEMICOLON
    EQUALS = appgamekit.KEY_EQUALS
    COMMA = appgamekit.KEY_COMMA
    MINUS = appgamekit.KEY_MINUS
    PERIOD = appgamekit.KEY_PERIOD
    SLASH = appgamekit.KEY_SLASH
    GRAVE = appgamekit.KEY_GRAVE
    TILDE = appgamekit.KEY_TILDE
    LEFT_BRACKET = appgamekit.KEY_LEFT_BRACKET
    BACKSLASH = appgamekit.KEY_BACKSLASH
    RIGHT_BRACKET = appgamekit.KEY_RIGHT_BRACKET
    APOSTROPHE = appgamekit.KEY_APOSTROPHE
    LEFT_SHIFT = appgamekit.KEY_LEFT_SHIFT
    RIGHT_SHIFT = appgamekit.KEY_RIGHT_SHIFT
    LEFT_CTRL = appgamekit.KEY_LEFT_CTRL
    RIGHT_CTRL = appgamekit.KEY_RIGHT_CTRL
    LEFT_ALT = appgamekit.KEY_LEFT_ALT
    RIGHT_ALT = appgamekit.KEY_RIGHT_ALT
    TOP_0 = appgamekit.KEY_TOP_0
    TOP_1 = appgamekit.KEY_TOP_1
    TOP_2 = appgamekit.KEY_TOP_2
    TOP_3 = appgamekit.KEY_TOP_3
    TOP_4 = appgamekit.KEY_TOP_4
    TOP_5 = appgamekit.KEY_TOP_5
    TOP_6 = appgamekit.KEY_TOP_6
    TOP_7 = appgamekit.KEY_TOP_7
    TOP_8 = appgamekit.KEY_TOP_8
    TOP_9 = appgamekit.KEY_TOP_9


del appgamekit
