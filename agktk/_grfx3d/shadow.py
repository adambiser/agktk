# noinspection PyUnresolvedReferences
from appgamekit import (
    # 3D > Shadows
    # get_object_cast_shadow_mode,  # See Object3D class
    # get_object_receive_shadow_mode,  # See Object3D class
    # set_object_cast_shadow,  # See Object3D class
    # set_object_receive_shadow,  # See Object3D class
    get_shadow_mapping_mode as _get_shadow_mapping_mode,
    # get_shadow_mapping_supported,  # See device.supports_shadow_mapping
    set_shadow_map_size,
    set_shadow_mapping_mode as _set_shadow_mapping_mode,
    set_shadow_bias as set_bias,
    set_shadow_cascade_values as set_cascade_values,
    set_shadow_light_step_size as set_light_step_size,
    set_shadow_range as set_range,
    set_shadow_smoothing as _set_shadow_smoothing,
)
from .._enums import (
    ShadowMappingMode,
    ShadowSmoothingMode,
)


def get_shadow_mapping_mode() -> ShadowMappingMode:
    return ShadowMappingMode(_get_shadow_mapping_mode())


def set_shadow_mapping_mode(mode: ShadowMappingMode):
    _set_shadow_mapping_mode(mode)


def set_smoothing_mode(mode: ShadowSmoothingMode):
    _set_shadow_smoothing(mode)
