# noinspection PyUnresolvedReferences
from appgamekit import (
    # Benchmarking
    # get_drawing_3d_setup_time  # AppGameKit Studio only.
    get_drawing_setup_time,
    get_drawing_time,
    get_image_memory_usage,
    get_loaded_images as get_loaded_image_count,
    get_managed_sprite_count,
    get_managed_sprite_draw_calls,
    get_managed_sprite_drawn_count,
    get_managed_sprite_sorted_count,
    # GetParticleDrawnPointCount - deprecated
    get_particle_drawn_quad_count,
    get_physics_time,
    get_pixels_drawn,
    get_unassigned_image_file_name as _get_unassigned_image_file_name,
    get_unassigned_images as _get_unassigned_images,
    get_update_time,

    # Core > Display
    get_polygons_drawn as get_polygons_drawn_count,  # debug
    get_shadow_polygons_drawn as get_shadow_polygons_drawn_count,  # debug
    get_vertices_processed as get_vertices_processed_count,  # debug
)
from typing import List


def unassigned_image_file_names():
    for index in range(1, _get_unassigned_images() + 1):
        yield _get_unassigned_image_file_name(index)
