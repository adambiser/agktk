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
    # GetCapturedImage,  # deprecated
    get_device_camera_type as _get_device_camera_type,
    get_num_device_cameras as get_camera_count,
    # IsCapturingImage,  # deprecated
    set_device_camera_to_image as _set_device_camera_to_image,
    # ShowImageCaptureScreen,  # deprecated

    # Input-Raw > Existence
    # get_accelerometer_exists as has_accelerometer,  # input.sensors.accelerometer
    get_camera_exists as has_camera,
    # get_gps_sensor_exists,  # input.sensors.gps
    # get_gyro_sensor_exists,  # input.sensors.gyro
    # get_joystick_exists,  # input.joysticks
    # get_keyboard_exists,  # input.keyboard
    # get_light_sensor_exists,  # input.sensors.light
    # get_magnetic_sensor_exists,  # input.sensors.magnetic
    # get_mouse_exists,  # input.mouse
    # get_multi_touch_exists,  # input.multitouch
    # get_proximity_sensor_exists,  # input.proximity
    # get_rotation_vector_sensor_exists,  # input.rotation

    # Multiplayer > Properties
    get_device_ip as get_ip_address,
    get_device_ipv6 as get_ipv6_address,

    # Core > Display
    # clear_depth_buffer,  # display
    # clear_screen,  # display
    # enable_clear_color,  # display
    # enable_clear_depth,  # display
    get_device_dpi,  # as get_dpi,
    get_device_height,  # as get_height,
    get_device_width,  # as get_width,
    # get_display_aspect,  # display
    get_max_device_height,  # as get_max_height,
    get_max_device_width,  # as get_max_width,
    get_orientation,
    get_paused as is_paused,
    # get_polygons_drawn,  # debug
    # get_renderer_name,  # display
    get_resumed as is_resumed,
    # get_screen_bounds_bottom,  # display
    # get_screen_bounds_left,  # display
    # get_screen_bounds_right,  # display
    # get_screen_bounds_top,  # display
    # get_shadow_polygons_drawn,  # debug
    # get_vertices_processed,  # debug
    # get_view_offset_x,  # display
    # get_view_offset_y,  # display
    # get_view_zoom,  # display
    # get_virtual_height,  # display
    # get_virtual_width,  # display
    get_window_height,
    get_window_width,
    is_supported_depth_texture as supports_depth_textures,
    maximize_window as maximize_app,
    minimize_app,
    # render,  # display
    # render_2d_back,  # display
    # render_2d_front,  # display
    # render_3d,  # display
    # render_shadow_map,  # display
    restore_app,
    # screen_fps,  # display
    # screen_to_world_x,  # display
    # screen_to_world_y,  # display
    # set_border_color,  # display
    # set_clear_color,  # display
    # set_display_aspect,  # display
    # set_immersive_mode,  # Mobile only
    # SetIntendedDeviceSize,  # Deprecated
    set_orientation_allowed,
    # set_render_to_image,  # display
    # set_render_to_screen,  # display
    # set_resolution_mode,  # display
    # set_scissor,  # display
    # set_screen_resolution,  # display
    # set_sync_rate,  # display
    # SetTransitionMode,  # Deprecated
    # set_vsync,  # display
    # set_view_offset,  # display
    # set_view_zoom,  # display
    # set_view_zoom_mode,  # display
    # set_virtual_resolution,  # display
    set_window_allow_resize,
    set_window_position,
    set_window_size,
    # swap,  # display
    # sync,  # display
    update_device_size,  # as update_size,
    # world_to_screen_x,  # display
    # world_to_screen_y,  # display

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
    # clear_url_scheme_text as _clear_url_scheme_text,  # Mobile only
    # download_expansion_file as _download_expansion_file,  # Android only
    # get_app_installed as is_app_installer,  # Android only
    get_app_name,
    # get_app_package_name,  # Mobile only
    get_device_base_name as get_platform_name,
    get_device_id,  # as get_id,
    get_device_language,  # as get_language,
    # GetDeviceName  # Deprecated
    # get_device_network_type,  # Mobile only
    # get_device_platform,  # Android only
    get_device_type as get_platform_type,
    # get_expansion_file_error,  # Android only
    # get_expansion_file_progress,  # Android only
    # get_expansion_file_state,  # Android only
    # get_frame_time,  # display
    get_milliseconds,
    get_num_processors as get_processor_count,
    get_seconds,
    # get_storage_remaining,  # Mobile only
    # get_storage_total,  # Mobile only
    # get_url_scheme_text,  # Mobile only
    message,
    reset_timer,
    # set_antialias_mode,  # display
    # set_default_mag_filter,  # display
    # set_default_min_filter,  # display
    # set_default_wrap_u,  # display
    # set_default_wrap_v,  # display
    # set_expansion_file_key,  # Android only
    # set_expansion_file_version,  # Android only
    # set_generate_mipmaps,  # display
    set_sleep_mode,
    # set_sort_created,  # display
    # SetSortDepth  # Deprecated
    # SetSortTextures  # Deprecated
    # SetSortTransparentDepth  # Deprecated
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
    # share_file,  # Mobile only
    # share_image,  # Mobile only
    # share_image_and_text,  # Mobile only
    # share_text,  # Mobile only
    view_file,

    # Core > Drawing
    # draw_box,  # display
    # draw_ellipse,  # display
    # draw_line,  # display
    # draw_line_rgb,  # display

    # get_color_blue as _get_color_blue,  # color
    # get_color_green as _get_color_green,  # color
    # get_color_red as _get_color_red,  # color
    # make_color as _make_color,  # color
)
from ._enums import CameraType
from ._image import Image
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

    def start_streaming(self) -> _Optional[Image]:
        """
        Returns an image onto which the camera streams.

        If the device doesn't support streaming to an image, None is returned.
        """
        _id = self.__id
        image = Image()
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
