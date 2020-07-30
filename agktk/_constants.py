# noinspection PyUnresolvedReferences
from appgamekit import (
    # Anti-alias modes - set_antialias_mode
    AA_NONE,
    AA_4XMSAA,
    
    # Alignment - create_advert, create_advert_ex, set_advert_location, set_advert_location_ex, set_text_alignment
    ALIGN_LEFT,
    ALIGN_CENTER,
    ALIGN_RIGHT,
    ALIGN_TOP,
    ALIGN_BOTTOM,
    
    # Axis - add_object_shape_capsule, add_object_shape_cone, add_object_shape_cylinder,
    # create_3d_physics_character_controller, create_object_capsule, set_object_shape_capsule, set_object_shape_cone,
    # set_object_shape_cylinder
    AXIS_X,
    AXIS_Y,
    AXIS_Z,
    
    # Ad banner sizes - create_advert, create_advert_ex
    ADVERT_BANNER,
    ADVERT_LARGE_BANNER,
    ADVERT_MEDIUM_RECTANGLE,
    ADVERT_FULL_BANNER,
    ADVERT_LEADERBOARD,
    ADVERT_SMART_BANNER,
    ADVERT_FLUID_BANNER,
    
    # Alpha blend modes - set_object_blend_modes
    BLEND_ZERO,
    BLEND_ONE,
    BLEND_SRC_ALPHA,
    BLEND_ONE_MINUS_SRC_ALPHA,
    BLEND_DST_ALPHA,
    BLEND_ONE_MINUS_DST_ALPHA,
    BLEND_SRC_COLOR,
    BLEND_ONE_MINUS_SRC_COLOR,
    BLEND_DST_COLOR,
    BLEND_ONE_MINUS_DST_COLOR,
    BLEND_SRC_ALPHA_SATURATE,
    
    # Device camera types - returned by get_device_camera_type
    CAMERA_TYPE_BACK_FACING,
    CAMERA_TYPE_FRONT_FACING,
    CAMERA_TYPE_UNKNOWN,
    
    # Physics character controler move types - move_3d_physics_character_controller
    CONTROLLER_MOVE_STOP,
    CONTROLLER_MOVE_FORWARD,
    CONTROLLER_MOVE_BACKWARD,
    CONTROLLER_MOVE_STRAFE_LEFT,
    CONTROLLER_MOVE_STRAFE_RIGHT,
    
    # Color mask channels - set_image_mask
    COLOR_CHANNEL_RED,
    COLOR_CHANNEL_GREEN,
    COLOR_CHANNEL_BLUE,
    COLOR_CHANNEL_ALPHA,
    
    # Cull modes - set_object_cull_mode
    CULL_FRONT_AND_BACK,
    CULL_FRONT,
    CULL_BACK,
    
    # Depth read modes - set_object_depth_read_mode
    DEPTH_NEVER,
    DEPTH_LT,
    DEPTH_EQUAL,
    DEPTH_LT_OR_EQUAL,
    DEPTH_GT,
    DEPTH_NOT_EQUAL,
    DEPTH_GT_OR_EQUAL,
    DEPTH_ALWAYS,
    
    # Edit box wrap modes - set_edit_box_wrap_mode
    EDIT_BOX_WRAP_SCROLL,
    EDIT_BOX_WRAP_NEW_LINE,
    
    # Error modes - set_error_mode
    ERROR_MODE_IGNORE,
    ERROR_MODE_REPORT,
    ERROR_MODE_STOP,
    
    # Folder modes - get_file_count, get_folder_count, get_first_file, get_first_folder
    FOLDER_MODE_READ_ONLY,
    FOLDER_MODE_WRITE_ONLY,
    FOLDER_MODE_BOTH,
    
    # Texture filters - set_default_mag_filter, set_default_min_filter, set_image_mag_filter, set_image_min_filter,
    # set_text_default_mag_filter, set_text_default_min_filter
    FILTER_NEAREST,
    FILTER_LINEAR,
    
    # Text input state - returned by get_text_input_state
    INPUT_TEXT_ACTIVE,
    INPUT_TEXT_DONE,
    
    # Render image modes - create_render_image
    IMAGE_RGBA,
    IMAGE_DEPTH,
    
    # Color interpolation modes - set_3d_particles_color_interpolation, set_particles_color_interpolation
    INTERPOLATE_NONE,
    INTERPOLATE_SMOOTH,
    
    # Keyboard types - returned by get_keyboard_exists
    KEYBOARD_NONE,
    KEYBOARD_FULL_SIZE,
    KEYBOARD_VIRTUAL,
    
    # Network variable types - set_network_local_float, set_network_local_integer
    NETWORK_VAR_TYPE_NORMAL,
    NETWORK_VAR_TYPE_RESETTING,
    
    # Orientation mode - returned by get_orientation
    ORIENTATION_PORTRAIT,
    ORIENTATION_PORTRAIT_180,
    ORIENTATION_LANDSCAPE_CCW,
    ORIENTATION_LANDSCAPE_CW,
    
    # Physics modes - set_sprite_physics_on
    PHYSICS_MODE_STATIC,
    PHYSICS_MODE_DYNAMIC,
    PHYSICS_MODE_KINEMATIC,
    
    # Point light modes - set_point_light_mode
    POINT_LIGHT_VERTEX,
    POINT_LIGHT_PIXEL,
    
    # Ray cast contact - ray_cast_3d_physics, ray_cast_3d_physics_object
    RAY_CAST_CLOSEST,
    RAY_CAST_ALL,
    
    # Resolution Modes - set_resolution_mode
    RESOLUTION_MODE_LOW,
    RESOLUTION_MODE_HIGH,
    
    # Rotation modes - set_particles_face_direction
    ROTATE_NORMAL,
    ROTATE_MOVE_DIRECTION,
    
    # Music seek modes - seek_music_ogg
    SEEK_ABSOLUTE,
    SEEK_RELATIVE,
    
    # Shadow mapping modes - set_shadow_mapping_mode
    SHADOW_MAP_NONE,
    SHADOW_MAP_UNIFORM,
    SHADOW_MAP_LIPSM,
    SHADOW_MAP_CASCADE,
    
    # Shadow smoothing - set_shadow_smoothing
    SHADOW_SMOOTHING_NONE,
    SHADOW_SMOOTHING_MULTISAMPLE,
    SHADOW_SMOOTHING_RANDOM_MULTISAMPLE,
    
    # Sprite shapes - set_sprite_shape
    SHAPE_NONE,
    SHAPE_CIRCLE,
    SHAPE_BOX,
    SHAPE_POLYGON,
    
    # Key, button, and pointer states - returned by get_button_state, get_pointer_state, get_virtual_button_state,
    # get_raw_joystick_button_state, get_raw_key_state, get_raw_mouse_left_state, get_raw_mouse_middle_state,
    # get_raw_mouse_right_state
    STATE_UP,
    STATE_DOWN,
    
    # Touch types - returned by get_raw_touch_type
    TOUCH_UNKNOWN,
    TOUCH_SHORT,
    TOUCH_HOLD,
    TOUCH_DRAG,
    
    # Transparency modes - set_object_transparency, set_3d_particles_transparency, set_particles_transparency,
    # set_sprite_transparency, set_text_transparency, returned by get_sprite_transparency
    TRANSPARENCY_NONE,
    TRANSPARENCY_ALPHA,
    TRANSPARENCY_ADDITIVE,
    TRANSPARENCY_CUSTOM,
    
    # Tween interpolation types - the set_tween_* methods
    TWEEN_LINEAR,
    TWEEN_SMOOTH1,
    TWEEN_SMOOTH2,
    TWEEN_EASE_IN1,
    TWEEN_EASE_IN2,
    TWEEN_EASE_OUT1,
    TWEEN_EASE_OUT2,
    TWEEN_BOUNCE,
    TWEEN_OVERSHOOT,
    
    # UV Texture wrapping modes - set_default_wrap_u, set_default_wrap_v, set_image_wrap_u, set_image_wrap_v
    WRAP_CLAMP,
    WRAP_REPEAT,
    
    # View zoom modes
    ZOOM_TOP_LEFT,
    ZOOM_CENTER,
    
    # Key codes
    KEY_BACKSPACE,
    KEY_TAB,
    KEY_ENTER,
    KEY_SHIFT,
    KEY_CONTROL,
    KEY_ALT,
    KEY_PAUSE,
    KEY_CAPSLOCK,
    KEY_ESCAPE,
    KEY_SPACE,
    KEY_PAGE_UP,
    KEY_PAGE_DOWN,
    KEY_END,
    KEY_HOME,
    KEY_LEFT,
    KEY_UP,
    KEY_RIGHT,
    KEY_DOWN,
    KEY_INSERT,
    KEY_DELETE,
    KEY_NUM_0,
    KEY_NUM_1,
    KEY_NUM_2,
    KEY_NUM_3,
    KEY_NUM_4,
    KEY_NUM_5,
    KEY_NUM_6,
    KEY_NUM_7,
    KEY_NUM_8,
    KEY_NUM_9,
    KEY_A,
    KEY_B,
    KEY_C,
    KEY_D,
    KEY_E,
    KEY_F,
    KEY_G,
    KEY_H,
    KEY_I,
    KEY_J,
    KEY_K,
    KEY_L,
    KEY_M,
    KEY_N,
    KEY_O,
    KEY_P,
    KEY_Q,
    KEY_R,
    KEY_S,
    KEY_T,
    KEY_U,
    KEY_V,
    KEY_W,
    KEY_X,
    KEY_Y,
    KEY_Z,
    KEY_WIN_LEFT,
    KEY_WIN_RIGHT,
    KEY_MENU,
    KEY_NUMPAD_0,
    KEY_NUMPAD_1,
    KEY_NUMPAD_2,
    KEY_NUMPAD_3,
    KEY_NUMPAD_4,
    KEY_NUMPAD_5,
    KEY_NUMPAD_6,
    KEY_NUMPAD_7,
    KEY_NUMPAD_8,
    KEY_NUMPAD_9,
    KEY_ASTERISK,
    KEY_PLUS,
    KEY_SUBTRACT,
    KEY_DECIMAL,
    KEY_DIVIDE,
    KEY_F1,
    KEY_F2,
    KEY_F3,
    KEY_F4,
    KEY_F5,
    KEY_F6,
    KEY_F7,
    KEY_F8,
    KEY_F9,
    KEY_F10,
    KEY_F11,
    KEY_F12,
    KEY_NUMLOCK,
    KEY_SCROLLLOCK,
    KEY_VOLUME_MUTE,
    KEY_VOLUME_DOWN,
    KEY_VOLUME_UP,
    KEY_MEDIA_NEXT,
    KEY_MEDIA_PREV,
    KEY_MEDIA_STOP,
    KEY_MEDIA_PLAY,
    KEY_SEMICOLON,
    KEY_EQUALS,
    KEY_COMMA,
    KEY_MINUS,
    KEY_PERIOD,
    KEY_SLASH,
    KEY_GRAVE,
    KEY_TILDE,
    KEY_LEFT_BRACKET,
    KEY_BACKSLASH,
    KEY_RIGHT_BRACKET,
    KEY_APOSTROPHE,
    KEY_LEFT_SHIFT,
    KEY_RIGHT_SHIFT,
    KEY_LEFT_CTRL,
    KEY_RIGHT_CTRL,
    KEY_LEFT_ALT,
    KEY_RIGHT_ALT,
    KEY_TOP_0,
    KEY_TOP_1,
    KEY_TOP_2,
    KEY_TOP_3,
    KEY_TOP_4,
    KEY_TOP_5,
    KEY_TOP_6,
    KEY_TOP_7,
    KEY_TOP_8,
    KEY_TOP_9,
)
