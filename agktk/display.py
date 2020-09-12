# noinspection PyUnresolvedReferences, PyShadowingBuiltins
from appgamekit import (
    # 3D > Objects
    # Renamed to match the 2D functions.  screen_to_world_x, world_to_screen_x, etc
    get_3d_vector_x_from_screen as screen_to_3d_vector_x,
    get_3d_vector_y_from_screen as screen_to_3d_vector_y,
    get_3d_vector_z_from_screen as screen_to_3d_vector_z,
    get_screen_x_from_3d as world_3d_to_screen_x,
    get_screen_y_from_3d as world_3d_to_screen_y,

    # Core > Display
    clear_depth_buffer,
    clear_screen,
    enable_clear_color,
    enable_clear_depth,
    get_display_aspect,
    get_renderer_name,
    get_screen_bounds_bottom,
    get_screen_bounds_left,
    get_screen_bounds_right,
    get_screen_bounds_top,
    get_view_offset_x,
    get_view_offset_y,
    get_view_zoom,
    get_virtual_height,
    get_virtual_width,
    render,
    render_2d_back,
    render_2d_front,
    render_3d,
    render_shadow_map,
    screen_fps,
    screen_to_world_x,
    screen_to_world_y,
    set_border_color,
    set_clear_color,
    set_display_aspect,
    set_render_to_image,
    set_render_to_screen,
    set_resolution_mode,
    set_scissor,
    set_screen_resolution,
    set_sync_rate,
    set_vsync,
    set_view_offset,
    set_view_zoom,
    set_view_zoom_mode as _set_view_zoom_mode,
    set_virtual_resolution,
    swap,
    sync,
    world_to_screen_x,
    world_to_screen_y,

    # Core > General
    step_physics,  # TODO core?
    update,  # TODO core?
    update_2d,  # TODO core?
    update_3d,  # TODO core?

    # Core > Misc
    get_frame_time,
    set_antialias_mode,
    set_default_mag_filter,
    set_default_min_filter,
    set_default_wrap_u,
    set_default_wrap_v,
    set_generate_mipmaps,
    set_sort_created,

    # Core > Drawing
    draw_box,
    draw_ellipse,
    draw_line,
    draw_line_rgb,

    # get_color_blue as _get_color_blue,  # color
    # get_color_green as _get_color_green,  # color
    # get_color_red as _get_color_red,  # color
    # make_color as _make_color,  # color

    # Text > Print
    print_value,
    set_print_color,
    set_print_font as _set_print_font,
    set_print_size,
    set_print_spacing,
)
from ._enums import ZoomMode
from ._grfx.font import Font

__print_font = None


def set_print_font(font: Font):
    # Store the font so it doesn't get deleted.
    global __print_font
    __print_font = font
    _set_print_font(font.id)


def set_view_zoom_mode(mode: ZoomMode):
    _set_view_zoom_mode(mode)
