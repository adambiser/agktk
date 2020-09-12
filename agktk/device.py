"""
Device capabilities and functionality.

See also the input.sensors package.
"""
# noinspection PyUnresolvedReferences
from appgamekit import (
    # Errors > General
    get_error_occurred as had_error,
    get_last_error,
    log,
    set_error_mode,

    # Python only
    enable_debug_log,
    import_plugin,

    # HTTP > General
    get_internet_state as has_internet,
    open_browser,

    # Image > Capture
    # GetCapturedImage,  # Not needed.  Deprecated
    get_device_camera_type as _get_device_camera_type,
    get_num_device_cameras as get_camera_count,
    # IsCapturingImage,  # Not needed.  Deprecated
    set_device_camera_to_image as _set_device_camera_to_image,
    # ShowImageCaptureScreen,  # Not needed.  Deprecated

    # Input-Raw > Existence
    # get_accelerometer_exists,  # See input.sensors.accelerometer
    get_camera_exists as has_camera,
    # get_gps_sensor_exists,  # See input.sensors.gps
    # get_gyro_sensor_exists,  # See input.sensors.gyro
    # get_joystick_exists,  # See input.joysticks
    # get_keyboard_exists,  # See input.keyboard
    # get_light_sensor_exists,  # See input.sensors.light
    # get_magnetic_sensor_exists,  # See input.sensors.magnetic
    # get_mouse_exists,  # See input.mouse
    # get_multi_touch_exists,  # See input.multitouch
    # get_proximity_sensor_exists,  # See input.proximity
    # get_rotation_vector_sensor_exists,  # See input.rotation

    # Multiplayer > Properties
    get_device_ip as get_ip_address,
    get_device_ipv6 as get_ipv6_address,

    # Core > Display
    # clear_depth_buffer,  # See display
    # clear_screen,  # See display
    # enable_clear_color,  # See display
    # enable_clear_depth,  # See display
    get_device_dpi,  # as get_dpi,
    get_device_height,  # as get_height,
    get_device_width,  # as get_width,
    # get_display_aspect,  # See display
    get_max_device_height,  # as get_max_height,
    get_max_device_width,  # as get_max_width,
    get_orientation,
    get_paused as is_paused,
    # get_polygons_drawn,  # See debug
    # get_renderer_name,  # See display
    get_resumed as is_resumed,
    # get_screen_bounds_bottom,  # See display
    # get_screen_bounds_left,  # See display
    # get_screen_bounds_right,  # See display
    # get_screen_bounds_top,  # See display
    # get_shadow_polygons_drawn,  # See debug
    # get_vertices_processed,  # See debug
    # get_view_offset_x,  # See display
    # get_view_offset_y,  # See display
    # get_view_zoom,  # See display
    # get_virtual_height,  # See display
    # get_virtual_width,  # See display
    get_window_height,
    get_window_width,
    is_supported_depth_texture as supports_depth_textures,
    maximize_window as maximize_app,
    minimize_app,
    # render,  # See display
    # render_2d_back,  # See display
    # render_2d_front,  # See display
    # render_3d,  # See display
    # render_shadow_map,  # See display
    restore_app,
    # screen_fps,  # See display
    # screen_to_world_x,  # See display
    # screen_to_world_y,  # See display
    # set_border_color,  # See display
    # set_clear_color,  # See display
    # set_display_aspect,  # See display
    # set_immersive_mode,  # Not needed.  Mobile only
    # SetIntendedDeviceSize,  # Not needed.  Deprecated
    set_orientation_allowed,
    # set_render_to_image,  # See display
    # set_render_to_screen,  # See display
    # set_resolution_mode,  # See display
    # set_scissor,  # See display
    # set_screen_resolution,  # See display
    # set_sync_rate,  # See display
    # SetTransitionMode,  # Not needed.  Deprecated
    # set_vsync,  # See display
    # set_view_offset,  # See display
    # set_view_zoom,  # See display
    # set_view_zoom_mode,  # See display
    # set_virtual_resolution,  # See display
    set_window_allow_resize,
    set_window_position,
    set_window_size,
    # swap,  # See display
    # sync,  # See display
    update_device_size,  # as update_size,
    # world_to_screen_x,  # See display
    # world_to_screen_y,  # See display

    # # Core > Strings
    # asc as _asc,
    # # bin
    # byte_len as _byte_len,
    # # Chr
    # compare_string as _compare_string,
    # count_string_tokens as _count_string_tokens,
    # count_string_tokens2 as _count_string_tokens2,
    # find_string as _find_string,
    # find_string_count as _find_string_count,
    # find_string_reverse as _find_string_reverse,
    # get_string_token as _get_string_token,
    # get_string_token2 as _get_string_token2,
    # # Hex
    # hex_to_base64 as _hex_to_base64,
    # # Left
    # # Len
    # # Lower
    # # Mid
    # replace_string as _replace_string,
    # # Right
    # # Spaces
    # # Str
    # string_to_base64 as _string_to_base64,
    # strip_string as _strip_string,
    # trim_string as _trim_string,
    # truncate_string as _truncate_string,
    # # Upper
    # # Val
    # # ValFloat

    # # Core > Maths
    # acos as _acos,
    # acos_rad as _acos_rad,
    # asin as _asin,
    # asin_rad as _asin_rad,
    # atan as _atan,
    # atan2 as _atan2,
    # atan2_rad as _atan2_rad,
    # atan_full as _atan_full,
    # atan_full_rad as _atan_full_rad,
    # atan_rad as _atan_rad,
    # abs as _abs,
    # ceil as _ceil,
    # cos as _cos,
    # cos_rad as _cos_rad,
    # fmod as _fmod,
    # floor as _floor,
    # log as _log,
    # # Mod
    # # Pow
    # random as _random,
    # random2 as _random2,
    # random_sign as _random_sign,
    # # Round
    # set_random_seed as _set_random_seed,
    # set_random_seed2 as _set_random_seed2,
    # sin as _sin,
    # sin_rad as _sin_rad,
    # sqrt as _sqrt,
    # tan as _tan,
    # tan_rad as _tan_rad,
    # trunc as _trunc,

    # Core > General
    # step_physics as _step_physics,  # TODO physics?  world?
    # update as _update,  # TODO display
    # update_2d as _update_2d,  # TODO display
    # update_3d as _update_3d,  # TODO display

    # Core > Misc
    # clear_url_scheme_text,  # Not needed.  Mobile only
    # download_expansion_file,  # Not needed.  Android only
    # get_app_installed,  # Not needed.  Android only
    get_app_name,
    # get_app_package_name,  # Not needed.  Mobile only
    get_device_base_name,  # as get_platform_name,
    get_device_id,  # as get_id,
    get_device_language,  # as get_language,
    # GetDeviceName  # Not needed.  Deprecated
    # get_device_network_type,  # Not needed.  Mobile only
    # get_device_platform,  # Not needed.  Android only
    get_device_type,  # as get_platform_type,
    # get_expansion_file_error,  # Not needed.  Android only
    # get_expansion_file_progress,  # Not needed.  Android only
    # get_expansion_file_state,  # Not needed.  Android only
    # get_frame_time,  # See display
    get_milliseconds,
    get_num_processors as get_processor_count,
    get_seconds,
    # get_storage_remaining,  # Not needed.  Mobile only
    # get_storage_total,  # Not needed.  Mobile only
    # get_url_scheme_text,  # Not needed.  Mobile only
    message,
    reset_timer,
    # set_antialias_mode,  # See display
    # set_default_mag_filter,  # See display
    # set_default_min_filter,  # See display
    # set_default_wrap_u,  # See display
    # set_default_wrap_v,  # See display
    # set_expansion_file_key,  # Not needed.  Android only
    # set_expansion_file_version,  # Not needed.  Android only
    # set_generate_mipmaps,  # See display
    set_sleep_mode,
    # set_sort_created,  # display
    # SetSortDepth  # Not needed.  Deprecated
    # SetSortTextures  # Not needed.  Deprecated
    # SetSortTransparentDepth  # Not needed.  Deprecated
    set_window_title,
    # sha1,  # TODO
    # sha256,  # TODO
    # sha512,  # TODO
    sleep,
    timer,

    # Core > External Apps
    get_app_running as _get_app_running,
    run_app as _run_app,
    terminate_app as _terminate_app,
    # share_file,  # Not needed.  Mobile only
    # share_image,  # Not needed.  Mobile only
    # share_image_and_text,  # Not needed.  Mobile only
    # share_text,  # Not needed.  Mobile only
    view_file,

    # Core > Drawing
    # draw_box,  # See display
    # draw_ellipse,  # See display
    # draw_line,  # See display
    # draw_line_rgb,  # See display

    # get_color_blue as _get_color_blue,  # color
    # get_color_green as _get_color_green,  # color
    # get_color_red as _get_color_red,  # color
    # make_color as _make_color,  # color

    # 3D > Shaders
    get_supported_shader_varyings as get_supported_shader_varyings_count,
    # 3D > Shadows
    get_shadow_mapping_supported as supports_shadow_mapping,
)
from ._enums import CameraType
from ._grfx.image import Image as _Image
from typing import Optional as _Optional


class App(object):
    def __init__(self, filename: str, parameters: str = None):
        self.__id = _run_app(filename, parameters)

    @property
    def is_running(self) -> bool:
        return _get_app_running(self.__id)

    def terminate(self):
        _terminate_app(self.__id)


def start_app(filename: str, parameters: str = None) -> App:
    return App(filename, parameters)


class DeviceCamera(object):
    """
    Wraps AppGameKit device camera methods.
    """
    __stream_image = None

    def __init__(self, camera_id: int = 0):
        self.__id = camera_id
        # if not 0 <= camera_id < _get_num_device_cameras():
        #     raise RuntimeWarning("Invalid camera ID for this device.")

    def __del__(self):
        """Deletes the object."""
        try:
            self.stop_streaming()
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    # @classmethod
    # def get_count(cls) -> int:
    #     return _get_num_device_cameras()

    @property
    def type(self) -> CameraType:
        return CameraType(_get_device_camera_type(self.__id))

    @property
    def is_streaming(self) -> bool:
        return DeviceCamera.__stream_image is not None

    def start_streaming(self) -> _Optional[_Image]:
        """
        Returns an image onto which the camera streams.

        If the device doesn't support streaming to an image, None is returned.
        """
        _id = self.__id
        image = _Image()
        if not _set_device_camera_to_image(_id, image.id):
            return None
        # Store the stream image so calling code doesn't have to.
        DeviceCamera.__stream_image = image
        return image

    def stop_streaming(self):
        _id = self.__id
        if DeviceCamera.__stream_image is not None:
            _set_device_camera_to_image(_id, 0)
            DeviceCamera.__stream_image = None
