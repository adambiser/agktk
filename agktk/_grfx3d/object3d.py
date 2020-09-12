from appgamekit import (
    # 3D > Bones
    get_object_bone_angle_x as _get_object_bone_angle_x,
    get_object_bone_angle_y as _get_object_bone_angle_y,
    get_object_bone_angle_z as _get_object_bone_angle_z,
    get_object_bone_by_name as _get_object_bone_by_name,
    get_object_bone_name as _get_object_bone_name,
    get_object_bone_quat_w as _get_object_bone_quat_w,
    get_object_bone_quat_x as _get_object_bone_quat_x,
    get_object_bone_quat_y as _get_object_bone_quat_y,
    get_object_bone_quat_z as _get_object_bone_quat_z,
    get_object_bone_world_angle_x as _get_object_bone_world_angle_x,
    get_object_bone_world_angle_y as _get_object_bone_world_angle_y,
    get_object_bone_world_angle_z as _get_object_bone_world_angle_z,
    get_object_bone_world_quat_w as _get_object_bone_world_quat_w,
    get_object_bone_world_quat_x as _get_object_bone_world_quat_x,
    get_object_bone_world_quat_y as _get_object_bone_world_quat_y,
    get_object_bone_world_quat_z as _get_object_bone_world_quat_z,
    get_object_bone_world_x as _get_object_bone_world_x,
    get_object_bone_world_y as _get_object_bone_world_y,
    get_object_bone_world_z as _get_object_bone_world_z,
    get_object_bone_x as _get_object_bone_x,
    get_object_bone_y as _get_object_bone_y,
    get_object_bone_z as _get_object_bone_z,
    get_object_num_bones as _get_object_num_bones,
    rotate_object_bone_local_x as _rotate_object_bone_local_x,
    rotate_object_bone_local_y as _rotate_object_bone_local_y,
    rotate_object_bone_local_z as _rotate_object_bone_local_z,
    set_object_bone_can_animate as _set_object_bone_can_animate,
    set_object_bone_look_at as _set_object_bone_look_at,
    set_object_bone_position as _set_object_bone_position,
    set_object_bone_rotation as _set_object_bone_rotation,
    set_object_bone_rotation_quat as _set_object_bone_rotation_quat,
    # 3D > Objects
    clone_object as _clone_object,
    # clone_object_to,  & Not needed
    create_object_box as _create_object_box,
    # create_object_box_id,  # Not needed
    create_object_capsule as _create_object_capsule,
    # create_object_capsule_id,  # Not needed
    create_object_cone as _create_object_cone,
    # create_object_cone_id,  # Not needed
    create_object_cylinder as _create_object_cylinder,
    # create_object_cylinder_id,  # Not needed
    create_object_from_height_map as _create_object_from_height_map,
    # create_object_id_from_height_map,  # Not needed
    create_object_from_object_mesh as _create_object_from_object_mesh,
    # create_object_id_from_object_mesh,  # Not needed
    create_object_from_raw_height_map as _create_object_from_raw_height_map,
    # create_object_id_from_raw_height_map,  # Not needed
    create_object_plane as _create_object_plane,
    # create_object_plane_id,  # Not needed
    create_object_quad as _create_object_quad,
    # create_object_quad_id,  # Not needed
    create_object_sphere as _create_object_sphere,
    # create_object_sphere_id,  # Not needed
    # delete_all_objects,  # Not needed.
    delete_object as _delete_object,
    # delete_object_tree as _delete_object_tree,  # Not needed
    # delete_object_with_children as _delete_object_with_children,  # Not needed
    draw_object as _draw_object,
    fix_object_pivot as _fix_object_pivot,
    fix_object_to_bone as _fix_object_to_bone,
    fix_object_to_object as _fix_object_to_object,
    # get_3d_vector_x_from_screen,  # See display
    # get_3d_vector_y_from_screen,  # See display
    # get_3d_vector_z_from_screen,  # See display
    get_object_alpha as _get_object_alpha,
    get_object_angle_x as _get_object_angle_x,
    get_object_angle_y as _get_object_angle_y,
    get_object_angle_z as _get_object_angle_z,
    get_object_animation_duration as _get_object_animation_duration,
    get_object_animation_name as _get_object_animation_name,
    get_object_animation_time as _get_object_animation_time,
    get_object_child_id as _get_object_child_id,
    get_object_color_blue as _get_object_color_blue,
    get_object_color_green as _get_object_color_green,
    get_object_color_red as _get_object_color_red,
    get_object_cull_mode as _get_object_cull_mode,
    get_object_depth_bias as _get_object_depth_bias,
    get_object_depth_read_mode as _get_object_depth_read_mode,
    get_object_depth_write as _get_object_depth_write,
    # get_object_exists,  # Not needed
    get_object_height_map_height as _get_object_height_map_height,
    get_object_in_screen as _get_object_in_screen,
    get_object_is_animating as _get_object_is_animating,
    get_object_is_tweening as _get_object_is_tweening,
    get_object_mesh_size_max_x as _get_object_mesh_size_max_x,
    get_object_mesh_size_max_y as _get_object_mesh_size_max_y,
    get_object_mesh_size_max_z as _get_object_mesh_size_max_z,
    get_object_mesh_size_min_x as _get_object_mesh_size_min_x,
    get_object_mesh_size_min_y as _get_object_mesh_size_min_y,
    get_object_mesh_size_min_z as _get_object_mesh_size_min_z,
    get_object_name as _get_object_name,
    get_object_num_animations as _get_object_num_animations,
    get_object_num_children as _get_object_num_children,
    get_object_quat_w as _get_object_quat_w,
    get_object_quat_x as _get_object_quat_x,
    get_object_quat_y as _get_object_quat_y,
    get_object_quat_z as _get_object_quat_z,
    # get_object_ray_cast_bounce_x,  # see raycaster
    # get_object_ray_cast_bounce_y,  # see raycaster
    # get_object_ray_cast_bounce_z,  # see raycaster
    # get_object_ray_cast_distance,  # see raycaster
    # get_object_ray_cast_hit_id,  # see raycaster
    # get_object_ray_cast_normal_x,  # see raycaster
    # get_object_ray_cast_normal_y,  # see raycaster
    # get_object_ray_cast_normal_z,  # see raycaster
    # get_object_ray_cast_num_hits,  # see raycaster
    # get_object_ray_cast_slide_x,  # see raycaster
    # get_object_ray_cast_slide_y,  # see raycaster
    # get_object_ray_cast_slide_z,  # see raycaster
    # get_object_ray_cast_x,  # see raycaster
    # get_object_ray_cast_y,  # see raycaster
    # get_object_ray_cast_z,  # see raycaster
    get_object_size_max_x as _get_object_size_max_x,
    get_object_size_max_y as _get_object_size_max_y,
    get_object_size_max_z as _get_object_size_max_z,
    get_object_size_min_x as _get_object_size_min_x,
    get_object_size_min_y as _get_object_size_min_y,
    get_object_size_min_z as _get_object_size_min_z,
    get_object_transparency as _get_object_transparency,
    get_object_visible as _get_object_visible,
    get_object_world_angle_x as _get_object_world_angle_x,
    get_object_world_angle_y as _get_object_world_angle_y,
    get_object_world_angle_z as _get_object_world_angle_z,
    get_object_world_quat_w as _get_object_world_quat_w,
    get_object_world_quat_x as _get_object_world_quat_x,
    get_object_world_quat_y as _get_object_world_quat_y,
    get_object_world_quat_z as _get_object_world_quat_z,
    get_object_world_x as _get_object_world_x,
    get_object_world_y as _get_object_world_y,
    get_object_world_z as _get_object_world_z,
    get_object_x as _get_object_x,
    get_object_y as _get_object_y,
    get_object_z as _get_object_z,
    # get_screen_x_from_3d,  # See display
    # get_screen_y_from_3d,  # See display
    instance_object as _instance_object,
    # instance_object_id,  # Not needed
    load_object as _load_object,
    # load_object_id,  # Not needed
    load_object_with_children as _load_object_with_children,
    # load_object_id_with_children,  # Not needed
    move_object_local_x as _move_object_local_x,
    move_object_local_y as _move_object_local_y,
    move_object_local_z as _move_object_local_z,
    # object_ray_cast,  # see raycaster
    # object_sphere_cast,  # see raycaster
    # object_sphere_slide,  # see raycaster
    play_object_animation as _play_object_animation,
    reset_object_animation as _reset_object_animation,
    rotate_object_global_x as _rotate_object_global_x,
    rotate_object_global_y as _rotate_object_global_y,
    rotate_object_global_z as _rotate_object_global_z,
    rotate_object_local_x as _rotate_object_local_x,
    rotate_object_local_y as _rotate_object_local_y,
    rotate_object_local_z as _rotate_object_local_z,
    # SaveObject  # Not implemented
    set_object_alpha as _set_object_alpha,
    set_object_alpha_mask as _set_object_alpha_mask,
    set_object_animation_frame as _set_object_animation_frame,
    set_object_animation_speed as _set_object_animation_speed,
    set_object_blend_modes as _set_object_blend_modes,
    set_object_collision_mode as _set_object_collision_mode,
    set_object_color as _set_object_color,
    set_object_color_emissive as _set_object_color_emissive,
    set_object_cull_mode as _set_object_cull_mode,
    set_object_depth_bias as _set_object_depth_bias,
    set_object_depth_range as _set_object_depth_range,
    set_object_depth_read_mode as _set_object_depth_read_mode,
    set_object_depth_write as _set_object_depth_write,
    set_object_fog_mode as _set_object_fog_mode,
    set_object_image as _set_object_image,
    set_object_light_map as _set_object_light_map,
    set_object_light_mode as _set_object_light_mode,
    set_object_look_at as _set_object_look_at,
    set_object_mesh_normal_map_scale as _set_object_mesh_normal_map_scale,
    set_object_mesh_uv_offset as _set_object_mesh_uv_offset,
    set_object_mesh_uv_scale as _set_object_mesh_uv_scale,
    set_object_normal_map as _set_object_normal_map,
    set_object_normal_map_scale as _set_object_normal_map_scale,
    set_object_position as _set_object_position,
    set_object_rotation as _set_object_rotation,
    set_object_rotation_quat as _set_object_rotation_quat,
    set_object_scale as _set_object_scale,
    set_object_scale_permanent as _set_object_scale_permanent,
    set_object_screen_culling as _set_object_screen_culling,
    set_object_shader as _set_object_shader,
    set_object_shader_constant_array_by_name as _set_object_shader_constant_array_by_name,
    set_object_shader_constant_by_name as _set_object_shader_constant_by_name,
    set_object_shader_constant_default as _set_object_shader_constant_default,
    set_object_transparency as _set_object_transparency,
    set_object_uv_offset as _set_object_uv_offset,
    set_object_uv_scale as _set_object_uv_scale,
    set_object_visible as _set_object_visible,
    stop_object_animation as _stop_object_animation,
    # 3D > Shadows
    get_object_cast_shadow_mode as _get_object_cast_shadow_mode,
    get_object_receive_shadow_mode as _get_object_receive_shadow_mode,
    set_object_cast_shadow as _set_object_cast_shadow,
    set_object_receive_shadow as _set_object_receive_shadow,
    # 3D > Meshes
    get_object_mesh_name as _get_object_mesh_name,
    get_object_mesh_ps_source as _get_object_mesh_ps_source,
    get_object_mesh_vs_source as _get_object_mesh_vs_source,
    get_object_num_meshes as _get_object_num_meshes,
    get_object_num_textures as _get_object_num_textures,
    get_object_texture_name as _get_object_texture_name,
    set_object_mesh_collision_mode as _set_object_mesh_collision_mode,
    set_object_mesh_image as _set_object_mesh_image,
    set_object_mesh_light_map as _set_object_mesh_light_map,
    set_object_mesh_normal_map as _set_object_mesh_normal_map,
    set_object_mesh_shader as _set_object_mesh_shader,
    set_object_mesh_visible as _set_object_mesh_visible,
    # Memblock > Mesh
    add_object_mesh_from_memblock as _add_object_mesh_from_memblock,
    create_object_from_mesh_memblock as _create_object_from_mesh_memblock,
    set_object_mesh_from_memblock as _set_object_mesh_from_memblock,
    # 3DPhysics > CompoundCollisionShapes
    add_object_shape_box as _add_object_shape_box,
    add_object_shape_capsule as _add_object_shape_capsule,
    add_object_shape_cone as _add_object_shape_cone,
    add_object_shape_cylinder as _add_object_shape_cylinder,
    add_object_shape_sphere as _add_object_shape_sphere,
    # 3DPhysics > CollisionShapes
    set_object_shape_box as _set_object_shape_box,
    set_object_shape_box_xyz as _set_object_shape_box_xyz,
    set_object_shape_capsule as _set_object_shape_capsule,
    set_object_shape_capsule_xyz as _set_object_shape_capsule_xyz,
    set_object_shape_compound as _set_object_shape_compound,
    set_object_shape_cone as _set_object_shape_cone,
    set_object_shape_convex_hull as _set_object_shape_convex_hull,
    set_object_shape_cylinder as _set_object_shape_cylinder,
    set_object_shape_sphere as _set_object_shape_sphere,
    set_object_shape_static_polygon as _set_object_shape_static_polygon,
    # 3DPhysics > SavingAndLoading
    load_object_shape as _load_object_shape,
    save_object_shape as _save_object_shape,
    # 3DPhysics > CharacterController
    create_3d_physics_character_controller as _create_3d_physics_character_controller,
    crouch_3d_physics_character_controller as _crouch_3d_physics_character_controller,
    debug_3d_physics_character_controller as _debug_3d_physics_character_controller,
    delete_3d_physics_character_controller as _delete_3d_physics_character_controller,
    # get_3d_physics_character_controller_exists,  # Not needed
    get_3d_physics_character_controller_gravity as _get_3d_physics_character_controller_gravity,
    get_3d_physics_character_controller_max_slope as _get_3d_physics_character_controller_max_slope,
    jump_3d_physics_character_controller as _jump_3d_physics_character_controller,
    move_3d_physics_character_controller as _move_3d_physics_character_controller,
    move_3d_physics_character_controller_xz as _move_3d_physics_character_controller_xz,
    rotate_3d_physics_character_controller as _rotate_3d_physics_character_controller,
    set_3d_physics_character_controller_fall_speed as _set_3d_physics_character_controller_fall_speed,
    set_3d_physics_character_controller_gravity as _set_3d_physics_character_controller_gravity,
    set_3d_physics_character_controller_jump_speed as _set_3d_physics_character_controller_jump_speed,
    set_3d_physics_character_controller_max_slope as _set_3d_physics_character_controller_max_slope,
    set_3d_physics_character_controller_position as _set_3d_physics_character_controller_position,
    set_3d_physics_character_controller_step_height as _set_3d_physics_character_controller_step_height,
    stand_3d_physics_character_controller as _stand_3d_physics_character_controller,
    # 3DPhysics > Ragdoll
    add_3d_physics_ragdoll_bone as _add_3d_physics_ragdoll_bone,
    add_3d_physics_ragdoll_hinge_joint as _add_3d_physics_ragdoll_hinge_joint,
    add_3d_physics_ragdoll_twist_joint as _add_3d_physics_ragdoll_twist_joint,
    assign_to_3d_physics_ragdoll_bone_object_bone as _assign_to_3d_physics_ragdoll_bone_object_bone,
    create_3d_physics_ragdoll as _create_3d_physics_ragdoll,
    delete_3d_physics_ragdoll as _delete_3d_physics_ragdoll,
    finalize_3d_physics_ragdoll as _finalize_3d_physics_ragdoll,
    get_3d_physics_ragdoll_exist as _get_3d_physics_ragdoll_exist,
    # get_3d_physics_ragdoll_from_bone_object,  # Not needed.  Seems unnecessary.
    is_3d_physics_ragdoll_static as _is_3d_physics_ragdoll_static,
    set_3d_physics_ragdoll_bones_visible as _set_3d_physics_ragdoll_bones_visible,
    set_3d_physics_ragdoll_damping as _set_3d_physics_ragdoll_damping,
    set_3d_physics_ragdoll_deactivation as _set_3d_physics_ragdoll_deactivation,
    set_3d_physics_ragdoll_deactivation_time as _set_3d_physics_ragdoll_deactivation_time,
    set_3d_physics_ragdoll_sleeping_thresholds as _set_3d_physics_ragdoll_sleeping_thresholds,
    set_3d_physics_ragdoll_static as _set_3d_physics_ragdoll_static,
    # 3DPhysics > RigidBodies
    create_3d_physics_dynamic_body as _create_3d_physics_dynamic_body,
    create_3d_physics_kinematic_body as _create_3d_physics_kinematic_body,
    create_3d_physics_static_body as _create_3d_physics_static_body,
    delete_3d_physics_body as _delete_3d_physics_body,
    get_object_3d_physics_angular_damp as _get_object_3d_physics_angular_damp,
    get_object_3d_physics_angular_sleeping_threshold as _get_object_3d_physics_angular_sleeping_threshold,
    get_object_3d_physics_angular_velocity_x as _get_object_3d_physics_angular_velocity_x,
    get_object_3d_physics_angular_velocity_y as _get_object_3d_physics_angular_velocity_y,
    get_object_3d_physics_angular_velocity_z as _get_object_3d_physics_angular_velocity_z,
    get_object_3d_physics_friction as _get_object_3d_physics_friction,
    get_object_3d_physics_group as _get_object_3d_physics_group,
    get_object_3d_physics_linear_damp as _get_object_3d_physics_linear_damp,
    get_object_3d_physics_linear_sleeping_threshold as _get_object_3d_physics_linear_sleeping_threshold,
    get_object_3d_physics_linear_velocity_x as _get_object_3d_physics_linear_velocity_x,
    get_object_3d_physics_linear_velocity_y as _get_object_3d_physics_linear_velocity_y,
    get_object_3d_physics_linear_velocity_z as _get_object_3d_physics_linear_velocity_z,
    get_object_3d_physics_mask as _get_object_3d_physics_mask,
    get_object_3d_physics_mass as _get_object_3d_physics_mass,
    get_object_3d_physics_max_linear_velocity as _get_object_3d_physics_max_linear_velocity,
    get_object_3d_physics_restitution as _get_object_3d_physics_restitution,
    get_object_3d_physics_rolling_friction as _get_object_3d_physics_rolling_friction,
    set_object_3d_physics_angular_velocity as _set_object_3d_physics_angular_velocity,
    set_object_3d_physics_angular_velocity_xyz as _set_object_3d_physics_angular_velocity_xyz,
    set_object_3d_physics_anisotropic_friction as _set_object_3d_physics_anisotropic_friction,
    set_object_3d_physics_can_sleep as _set_object_3d_physics_can_sleep,
    set_object_3d_physics_damping as _set_object_3d_physics_damping,
    set_object_3d_physics_deactivation_time as _set_object_3d_physics_deactivation_time,
    set_object_3d_physics_friction as _set_object_3d_physics_friction,
    set_object_3d_physics_group_and_mask as _set_object_3d_physics_group_and_mask,
    set_object_3d_physics_linear_velocity as _set_object_3d_physics_linear_velocity,
    set_object_3d_physics_linear_velocity_xyz as _set_object_3d_physics_linear_velocity_xyz,
    set_object_3d_physics_mass as _set_object_3d_physics_mass,
    set_object_3d_physics_max_linear_velocity as _set_object_3d_physics_max_linear_velocity,
    set_object_3d_physics_restitution as _set_object_3d_physics_restitution,
    set_object_3d_physics_rolling_friction as _set_object_3d_physics_rolling_friction,
    set_object_3d_physics_sleeping_threshold as _set_object_3d_physics_sleeping_threshold,
    # 3DPhysics > ContactReports
    get_object_3d_physics_contact_object_b as _get_object_3d_physics_contact_object_b,
    get_object_3d_physics_contact_vector as _get_object_3d_physics_contact_vector,
    get_object_3d_physics_contact_x as _get_object_3d_physics_contact_x,
    get_object_3d_physics_contact_y as _get_object_3d_physics_contact_y,
    get_object_3d_physics_contact_z as _get_object_3d_physics_contact_z,
    get_object_3d_physics_first_contact as _get_object_3d_physics_first_contact,
    get_object_3d_physics_next_contact as _get_object_3d_physics_next_contact,
    get_objects_3d_physics_contact_position_vector as _get_objects_3d_physics_contact_position_vector,
)
from .shader import Shader
from .._grfx import Image
from .._vector3 import Vector3
from .._enums import (
    AlphaBlendMode,
    AnisotropicFrictionMode,
    Axis,
    ControllerMove,
    CullMode,
    DepthReadMode,
    TransparencyMode,
)
import weakref as _weakref
import warnings as _warnings
from typing import Dict, Tuple, Union, List, TYPE_CHECKING
if TYPE_CHECKING:
    from .._memblock import MeshMemblock

_LIGHT_MAP_IMAGE_STAGE = 1
_NORMAL_MAP_IMAGE_STAGE = 2


def _get_object_bone_index(object_id: int, index: Union[str, int]):
    return index if isinstance(index, int) else _get_object_bone_by_name(object_id, index)


class Bone3D(object):
    def __init__(self, object3d: "Object3D", bone_id: int):
        self.__object3d = object3d
        self.__object3d_id = object3d.id
        self.__id = bone_id

    def __repr__(self):
        return f"<{self.__class__.__name__}, object3d_id: {self.__object3d_id}, bone_id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def object3d(self) -> "Object3D":
        """This mesh's object."""
        return self.__object3d

    @property
    def name(self) -> str:
        return _get_object_bone_name(self.__object3d_id, self.__id)

    @property
    def angle_x(self) -> float:
        return _get_object_bone_angle_x(self.__object3d_id, self.__id)

    @property
    def angle_y(self) -> float:
        return _get_object_bone_angle_y(self.__object3d_id, self.__id)

    @property
    def angle_z(self) -> float:
        return _get_object_bone_angle_z(self.__object3d_id, self.__id)

    @property
    def quat_w(self) -> float:
        return _get_object_bone_quat_w(self.__object3d_id, self.__id)

    @property
    def quat_x(self) -> float:
        return _get_object_bone_quat_x(self.__object3d_id, self.__id)

    @property
    def quat_y(self) -> float:
        return _get_object_bone_quat_y(self.__object3d_id, self.__id)

    @property
    def quat_z(self) -> float:
        return _get_object_bone_quat_z(self.__object3d_id, self.__id)

    @property
    def x(self) -> float:
        return _get_object_bone_x(self.__object3d_id, self.__id)

    @property
    def y(self) -> float:
        return _get_object_bone_y(self.__object3d_id, self.__id)

    @property
    def z(self) -> float:
        return _get_object_bone_z(self.__object3d_id, self.__id)

    @property
    def world_angle_x(self) -> float:
        return _get_object_bone_world_angle_x(self.__object3d_id, self.__id)

    @property
    def world_angle_y(self) -> float:
        return _get_object_bone_world_angle_y(self.__object3d_id, self.__id)

    @property
    def world_angle_z(self) -> float:
        return _get_object_bone_world_angle_z(self.__object3d_id, self.__id)

    @property
    def world_quat_w(self) -> float:
        return _get_object_bone_world_quat_w(self.__object3d_id, self.__id)

    @property
    def world_quat_x(self) -> float:
        return _get_object_bone_world_quat_x(self.__object3d_id, self.__id)

    @property
    def world_quat_y(self) -> float:
        return _get_object_bone_world_quat_y(self.__object3d_id, self.__id)

    @property
    def world_quat_z(self) -> float:
        return _get_object_bone_world_quat_z(self.__object3d_id, self.__id)

    @property
    def world_x(self) -> float:
        return _get_object_bone_world_x(self.__object3d_id, self.__id)

    @property
    def world_y(self) -> float:
        return _get_object_bone_world_y(self.__object3d_id, self.__id)

    @property
    def world_z(self) -> float:
        return _get_object_bone_world_z(self.__object3d_id, self.__id)

    def rotate_local_x(self, angle: float):
        _rotate_object_bone_local_x(self.__object3d_id, self.__id, angle)

    def rotate_local_y(self, angle: float):
        _rotate_object_bone_local_y(self.__object3d_id, self.__id, angle)

    def rotate_local_z(self, angle: float):
        _rotate_object_bone_local_z(self.__object3d_id, self.__id, angle)

    def rotate_local(self, x: float = None, y: float = None, z: float = None):
        if x:
            _rotate_object_bone_local_x(self.__object3d_id, self.__id, x)
        if y:
            _rotate_object_bone_local_y(self.__object3d_id, self.__id, y)
        if z:
            _rotate_object_bone_local_z(self.__object3d_id, self.__id, z)

    def enable_animation(self, enabled: bool):
        _set_object_bone_can_animate(self.__object3d_id, self.__id, enabled)

    def look_at(self, x: float, y: float, z: float, roll: float):
        _set_object_bone_look_at(self.__object3d_id, self.__id, x, y, z, roll)

    def set_position(self, x: float, y: float, z: float):
        _set_object_bone_position(self.__object3d_id, self.__id, x, y, z)

    def set_rotation(self, x: float, y: float, z: float):
        _set_object_bone_rotation(self.__object3d_id, self.__id, x, y, z)

    def set_rotation_quat(self, w: float, x: float, y: float, z: float):
        _set_object_bone_rotation_quat(self.__object3d_id, self.__id, w, x, y, z)


class _Bone3DList(object):
    __slots__ = {'__object3d', '__object3d_id', '__bones', '__index'}

    def __init__(self, object3d: "Object3D"):
        # Store a weak ref so this instance won't prevent deletion, but
        # send a strong ref when creating the Bone3D objects so that they do.
        self.__object3d = _weakref.ref(object3d)
        self.__object3d_id = object3d.id
        self.__bones = _weakref.WeakValueDictionary()
        self.__index = 0

    def __iter__(self):
        """Allow iteration."""
        self.__index = 0
        return self

    def __next__(self) -> Bone3D:
        """Allow iteration."""
        if self.__index < len(self):
            index = self.__index
            self.__index += 1
            return self[index]
        raise StopIteration

    def __len__(self):
        """The number of meshes on the object."""
        return _get_object_num_bones(self.__object3d_id)

    def __getitem__(self, item: Union[str, int]) -> Union[Bone3D, None]:
        # Remember: bone_id for Object3D is 1-based!
        index = item if isinstance(item, int) else _get_object_bone_by_name(self.__object3d_id, item) - 1
        if index < 0:
            return None
        bone = self.__bones.get(index)
        if not bone:
            # Have to store the instance locally and pass it back so that it doesn't get deleted immediately.
            # Remember: bone_id for Object3D is 1-based!
            bone = Bone3D(self.__object3d(), index + 1)
            self.__bones[index] = bone
        return bone


class Mesh(object):
    def __init__(self, object3d: "Object3D", mesh_id: int):
        self.__object3d = object3d
        self.__object3d_id = object3d.id
        self.__id = mesh_id

    def __repr__(self):
        return f"<{self.__class__.__name__}, object3d_id: {self.__object3d_id}, mesh_id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def object3d(self) -> "Object3D":
        """This mesh's object."""
        return self.__object3d

    @property
    def name(self) -> str:
        return _get_object_mesh_name(self.__object3d_id, self.__id)

    @property
    def pixel_shader_source(self) -> str:
        return _get_object_mesh_ps_source(self.__object3d_id, self.__id)

    @property
    def vertex_shader_source(self) -> str:
        return _get_object_mesh_vs_source(self.__object3d_id, self.__id)

    @property
    def size_max_x(self) -> float:
        return _get_object_mesh_size_max_x(self.__object3d_id, self.__id)

    @property
    def size_max_y(self) -> float:
        return _get_object_mesh_size_max_y(self.__object3d_id, self.__id)

    @property
    def size_max_z(self) -> float:
        return _get_object_mesh_size_max_z(self.__object3d_id, self.__id)

    @property
    def size_min_x(self) -> float:
        return _get_object_mesh_size_min_x(self.__object3d_id, self.__id)

    @property
    def size_min_y(self) -> float:
        return _get_object_mesh_size_min_y(self.__object3d_id, self.__id)

    @property
    def size_min_z(self) -> float:
        return _get_object_mesh_size_min_z(self.__object3d_id, self.__id)

    def set_normal_map_scale(self, u: float, v: float):
        _set_object_mesh_normal_map_scale(self.__object3d_id, self.__id, u, v)

    def set_uv_offset(self, u: float = 0, v: float = 0, stage: int = 0):
        _set_object_mesh_uv_offset(self.__object3d_id, self.__id, stage, u, v)

    def set_uv_scale(self, u: float = 1.0, v: float = 1.0, stage: int = 0):
        _set_object_mesh_uv_scale(self.__object3d_id, self.__id, stage, u, v)

    def enable_collision_detection(self, enabled: bool = True):
        _set_object_mesh_collision_mode(self.__object3d_id, self.__id, enabled)

    def set_image(self, image: Image, stage: int = 0):
        # noinspection PyProtectedMember
        self.__object3d._store_image_ref(self.__id, image, stage)
        _set_object_mesh_image(self.__object3d_id, self.__id, image.id if image else 0, stage)

    def set_light_map(self, image: Image):
        # noinspection PyProtectedMember
        self.__object3d._store_image_ref(self.__id, image, _LIGHT_MAP_IMAGE_STAGE)
        _set_object_mesh_light_map(self.__object3d_id, self.__id, image.id if image else 0)

    def set_normal_map(self, image: Image):
        # noinspection PyProtectedMember
        self.__object3d._store_image_ref(self.__id, image, _NORMAL_MAP_IMAGE_STAGE)
        _set_object_mesh_normal_map(self.__object3d_id, self.__id, image.id if image else 0)

    def set_shader(self, shader: Shader):
        # noinspection PyProtectedMember
        self.__object3d._store_shader_ref(self.__id, shader)
        _set_object_mesh_shader(self.__object3d_id, self.__id, shader.id)

    def set_visible(self, visible: bool):
        _set_object_mesh_visible(self.__object3d_id, self.__id, visible)


class _MeshList(object):
    __slots__ = {'__object3d', '__object3d_id', '__meshes', '__index'}

    def __init__(self, object3d: "Object3D"):
        # Store a weak ref so this instance won't prevent deletion, but
        # send a strong ref when creating the Mesh objects so that they do.
        self.__object3d = _weakref.ref(object3d)
        self.__object3d_id = object3d.id
        self.__meshes = _weakref.WeakValueDictionary()
        self.__index = 0

    def __iter__(self):
        """Allow iteration."""
        self.__index = 0
        return self

    def __next__(self) -> Mesh:
        """Allow iteration."""
        if self.__index < len(self):
            index = self.__index
            self.__index += 1
            return self[index]
        raise StopIteration

    def __len__(self):
        """The number of meshes on the object."""
        return _get_object_num_meshes(self.__object3d_id)

    def __getitem__(self, index: int) -> Mesh:
        # Remember: mesh_id for Object3D is 1-based!
        mesh = self.__meshes.get(index)
        if not mesh:
            # Have to store the instance locally and pass it back so that it doesn't get deleted immediately.
            # Remember: mesh_id for Object3D is 1-based!
            mesh = Mesh(self.__object3d(), index + 1)
            self.__meshes[index] = mesh
        return mesh

    def append(self, memblock: "MeshMemblock"):
        _add_object_mesh_from_memblock(self.__object3d_id, memblock.id)

    def __setitem__(self, key: int, value: "MeshMemblock"):
        _set_object_mesh_from_memblock(self.__object3d_id, key, value.id)


class _ChildObject3DList(object):
    __slots__ = {'__object_id', '__index', '__children'}

    def __init__(self, object3d: "Object3D"):
        # Store a weak ref so this children won't prevent deletion of the parent.
        object_id = object3d.id
        self.__object_id = object_id
        self.__children = [Object3D("", _id=_get_object_child_id(object_id, index + 1), _parent=object3d)
                           for index in range(_get_object_num_children(object_id))]  # type:List[Union[Object3D, None]]
        self.__index = 0

    def __iter__(self):
        """Allow iteration."""
        self.__index = 0
        return self

    def __next__(self) -> "Object3D":
        """Allow iteration."""
        if self.__index < len(self):
            index = self.__index
            self.__index += 1
            return self[index]
        raise StopIteration

    def __len__(self):
        """The number of children for this object."""
        return _get_object_num_children(self.__object_id)

    def __getitem__(self, index: int) -> "Object3D":
        return self.__children[index]

    def __delitem__(self, index: int):
        # In AGK, the number of children doesn't change when deleting one.
        # To imitate, just replace the child with None.
        self.__children[index] = None


class _ObjectContact(object):
    def __init__(self):
        # Load everything now.
        # noinspection PyProtectedMember
        self.__other_object = Object3D._from_id(_get_object_3d_physics_contact_object_b())
        self.__contact_vector = Vector3()
        _get_object_3d_physics_contact_vector(self.__contact_vector.id)
        self.__contact_x = _get_object_3d_physics_contact_x()
        self.__contact_y = _get_object_3d_physics_contact_y()
        self.__contact_z = _get_object_3d_physics_contact_z()

    @property
    def other_object(self) -> "Object3D":
        return self.__other_object

    @property
    def contact_vector(self) -> Vector3:
        return self.__contact_vector

    @property
    def contact_x(self) -> float:
        return self.__contact_x

    @property
    def contact_y(self) -> float:
        return self.__contact_y

    @property
    def contact_z(self) -> float:
        return self.__contact_z


class _RigidBody(object):
    def __init__(self, object_id: int):
        self.__id = object_id

    def __del__(self):
        """Deletes the object."""
        try:
            # Ignore the RuntimeWarning that can occurs if the 3d physics world doesn't exists when this is called.
            with _warnings.catch_warnings():
                _warnings.simplefilter("ignore")
                _delete_3d_physics_body(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @property
    def angular_damp(self) -> float:
        return _get_object_3d_physics_angular_damp(self.__id)

    @property
    def linear_damp(self) -> float:
        return _get_object_3d_physics_linear_damp(self.__id)

    def set_damping(self, linear: float, angular: float):
        _set_object_3d_physics_damping(self.__id, linear, angular)

    @property
    def angular_sleeping_threshold(self) -> float:
        return _get_object_3d_physics_angular_sleeping_threshold(self.__id)

    @property
    def linear_sleeping_threshold(self) -> float:
        return _get_object_3d_physics_linear_sleeping_threshold(self.__id)

    def enable_sleep(self, enabled: bool = True):
        _set_object_3d_physics_can_sleep(self.__id, enabled)

    def set_sleeping_threshold(self, linear: float, angular: float):
        # Yes, the angular and linear parameters are in the opposite order here than they are for
        #   set_object_3d_physics_damping, set_3d_physics_ragdoll_sleeping_thresholds, and
        #   set_3d_physics_ragdoll_damping!
        _set_object_3d_physics_sleeping_threshold(self.__id, angular, linear)

    @property
    def angular_velocity_x(self) -> float:
        return _get_object_3d_physics_angular_velocity_x(self.__id)

    @property
    def angular_velocity_y(self) -> float:
        return _get_object_3d_physics_angular_velocity_y(self.__id)

    @property
    def angular_velocity_z(self) -> float:
        return _get_object_3d_physics_angular_velocity_z(self.__id)

    def set_angular_velocity_from_vector(self, vector: Vector3, initial_speed: float):
        _set_object_3d_physics_angular_velocity(self.__id, vector.id, initial_speed)

    def set_angular_velocity(self, x: float, y: float, z: float, initial_speed: float):
        _set_object_3d_physics_angular_velocity_xyz(self.__id, x, y, z, initial_speed)

    @property
    def friction(self) -> float:
        return _get_object_3d_physics_friction(self.__id)

    @friction.setter
    def friction(self, value: float):
        _set_object_3d_physics_friction(self.__id, value)

    def set_anisotropic_friction(self, mode: AnisotropicFrictionMode):
        _set_object_3d_physics_anisotropic_friction(self.__id, mode)

    @property
    def group(self) -> int:
        return _get_object_3d_physics_group(self.__id)

    @property
    def mask(self) -> int:
        return _get_object_3d_physics_mask(self.__id)

    def set_group_and_mask(self, group: int, mask: int):
        _set_object_3d_physics_group_and_mask(self.__id, group, mask)

    @property
    def linear_velocity_x(self) -> float:
        return _get_object_3d_physics_linear_velocity_x(self.__id)

    @property
    def linear_velocity_y(self) -> float:
        return _get_object_3d_physics_linear_velocity_y(self.__id)

    @property
    def linear_velocity_z(self) -> float:
        return _get_object_3d_physics_linear_velocity_z(self.__id)

    def set_linear_velocity_from_vector(self, vector: Vector3, initial_speed: float):
        _set_object_3d_physics_linear_velocity(self.__id, vector.id, initial_speed)

    def set_linear_velocity(self, x: float, y: float, z: float, initial_speed: float):
        _set_object_3d_physics_linear_velocity_xyz(self.__id, x, y, z, initial_speed)

    @property
    def mass(self) -> float:
        return _get_object_3d_physics_mass(self.__id)

    @mass.setter
    def mass(self, value: float):
        _set_object_3d_physics_mass(self.__id, value)

    @property
    def max_linear_velocity(self) -> float:
        return _get_object_3d_physics_max_linear_velocity(self.__id)

    @max_linear_velocity.setter
    def max_linear_velocity(self, value: float):
        _set_object_3d_physics_max_linear_velocity(self.__id, value)

    @property
    def restitution(self) -> float:
        return _get_object_3d_physics_restitution(self.__id)

    @restitution.setter
    def restitution(self, value: float):
        _set_object_3d_physics_restitution(self.__id, value)

    @property
    def rolling_friction(self) -> float:
        return _get_object_3d_physics_rolling_friction(self.__id)

    @rolling_friction.setter
    def rolling_friction(self, value: float):
        _set_object_3d_physics_rolling_friction(self.__id, value)

    def set_deactivation_time(self, time: float):
        _set_object_3d_physics_deactivation_time(self.__id, time)

    # 3DPhysics > CollisionShapes
    def set_shape_box(self):
        _set_object_shape_box(self.__id)

    def set_shape_box_xyz(self, x: float, y: float, z: float):
        _set_object_shape_box_xyz(self.__id, x, y, z)

    def set_shape_box_from_vector(self, vector: Vector3):
        _set_object_shape_box(self.__id, vector.id)

    def set_shape_capsule(self, axis: Axis):
        _set_object_shape_capsule(self.__id, axis)

    def set_shape_capsule_xyz(self, axis: Axis, x: float, y: float, z: float):
        _set_object_shape_capsule_xyz(self.__id, axis, x, y, z)

    def set_shape_capsule_from_vector(self, axis: Axis, vector: Vector3):
        _set_object_shape_capsule(self.__id, axis, vector.id)

    def set_shape_compound(self):
        _set_object_shape_compound(self.__id)

    def add_shape_box(self, position_vector: Vector3, rotation_vector: Vector3, size_vector: Vector3):
        _add_object_shape_box(self.__id, position_vector.id, rotation_vector.id, size_vector.id)

    def add_shape_capsule(self, position_vector: Vector3, rotation_vector: Vector3, size_vector: Vector3, axis: Axis):
        _add_object_shape_capsule(self.__id, position_vector.id, rotation_vector.id, size_vector.id, axis)

    def add_shape_cone(self, position_vector: Vector3, rotation_vector: Vector3, size_vector: Vector3, axis: Axis):
        _add_object_shape_cone(self.__id, position_vector.id, rotation_vector.id, size_vector.id, axis)

    def add_shape_cylinder(self, position_vector: Vector3, rotation_vector: Vector3, size_vector: Vector3, axis: Axis):
        _add_object_shape_cylinder(self.__id, position_vector.id, rotation_vector.id, size_vector.id, axis)

    def add_shape_sphere(self, position_vector: Vector3, diameter: float):
        _add_object_shape_sphere(self.__id, position_vector.id, diameter)

    def set_shape_cone(self, axis: Axis, height: float, diameter: float):
        _set_object_shape_cone(self.__id, axis, height, diameter)

    def set_shape_convex_hull(self):
        _set_object_shape_convex_hull(self.__id)

    def set_shape_cylinder(self, axis: Axis, height: float, diameter: float):
        _set_object_shape_cylinder(self.__id, axis, height, diameter)

    def set_shape_sphere(self, diameter: float):
        _set_object_shape_sphere(self.__id, diameter)

    def set_shape_static_poligon(self, diameter: float):
        _set_object_shape_static_polygon(self.__id)

    def load_shape(self, filename: str) -> bool:
        return _load_object_shape(self.__id, filename)

    def save_shape(self, filename: str) -> bool:
        return _save_object_shape(self.__id, filename)

    def get_contacts(self) -> List[_ObjectContact]:
        _id = self.__id

        def _get_contacts():
            if _get_object_3d_physics_first_contact(_id):
                yield _ObjectContact()
                while _get_object_3d_physics_next_contact():
                    yield _ObjectContact()

        return list(_get_contacts())

    def get_contact_position_vector(self, other_object: "Object3D", out_vector: Vector3) -> bool:
        return _get_objects_3d_physics_contact_position_vector(self.__id, other_object.id, out_vector.id)


class _CharacterController(object):
    def __init__(self, object_id):
        self.__id = object_id

    def __del__(self):
        """Deletes the object."""
        try:
            # Ignore the RuntimeWarning that can occurs if the 3d physics world doesn't exists when this is called.
            with _warnings.catch_warnings():
                _warnings.simplefilter("ignore")
                _delete_3d_physics_character_controller(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def enable_debug(self, enabled: bool = True):
        _debug_3d_physics_character_controller(self.__id, enabled)

    @property
    def gravity(self) -> float:
        return _get_3d_physics_character_controller_gravity(self.__id)

    @gravity.setter
    def gravity(self, value: float):
        _set_3d_physics_character_controller_gravity(self.__id, value)

    @property
    def max_slope(self) -> float:
        return _get_3d_physics_character_controller_max_slope(self.__id)

    @max_slope.setter
    def max_slope(self, value: float):
        _set_3d_physics_character_controller_max_slope(self.__id, value)

    def crouch(self):
        _crouch_3d_physics_character_controller(self.__id)

    def jump(self):
        _jump_3d_physics_character_controller(self.__id)

    def stand(self):
        _stand_3d_physics_character_controller(self.__id)

    def move(self, direction: ControllerMove, velocity: float):
        _move_3d_physics_character_controller(self.__id, direction, velocity)

    def move_xz(self, x: float, z: float, velocity: float):
        _move_3d_physics_character_controller_xz(self.__id, x, z, velocity)

    def rotate(self, angle: float):
        _rotate_3d_physics_character_controller(self.__id, angle)

    def set_fall_speed(self, value: float):
        _set_3d_physics_character_controller_fall_speed(self.__id, value)

    def set_jump_speed(self, value: float):
        _set_3d_physics_character_controller_jump_speed(self.__id, value)

    def set_position(self, x: float, y: float, z: float):
        _set_3d_physics_character_controller_position(self.__id, x, y, z)

    def set_step_height(self, value: float):
        _set_3d_physics_character_controller_step_height(self.__id, value)


class RagDollBone(object):
    def __init__(self, object_id, bone_id):
        self.__object_id = object_id
        self.__id = bone_id

    def __repr__(self):
        return f"<{self.__class__.__name__}, object_id: {self.__object_id}, ragdoll_bone_id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def add_hinge_joint(self, other_ragdoll_bone: "RagDollBone", object_bone: Union[str, int], rotation_vector: Vector3,
                        minimum: float, maximum: float):
        object_bone = _get_object_bone_index(self.__object_id, object_bone)
        _add_3d_physics_ragdoll_hinge_joint(self.__id, other_ragdoll_bone.__id, object_bone, rotation_vector.id,
                                            minimum, maximum)

    def add_twist_joint(self, other_ragdoll_bone: "RagDollBone", object_bone: Union[str, int], rotation_vector: Vector3,
                        limits_vector: Vector3):
        object_bone = _get_object_bone_index(self.__object_id, object_bone)
        _add_3d_physics_ragdoll_twist_joint(self.__id, other_ragdoll_bone.__id, object_bone, rotation_vector.id,
                                            limits_vector.id)

    def assign_to_object_bone(self, object_bone: Union[str, int]):
        object_bone = _get_object_bone_index(self.__object_id, object_bone)
        _assign_to_3d_physics_ragdoll_bone_object_bone(self.__id, object_bone)

    # def get_object(self):
    #     return _get_3d_physics_ragdoll_from_bone_object(self.__object_id)


class RagDollBuilder(object):
    def __init__(self, object3d: "Object3D", weight: float):
        self.__object_id = object3d.id
        self.__building = True
        _create_3d_physics_ragdoll(object3d.id, weight)

    def __del__(self):
        self.finish()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.finish()
        return exc_type is KeyboardInterrupt

    def finish(self):
        if self.__building:
            self.__building = False
            _finalize_3d_physics_ragdoll()

    def add_bone(self, start_bone: Union[str, int], end_bone: Union[str, int], diameter: float,
                 collision_group: int, collision_mask: int) -> RagDollBone:
        object_id = self.__object_id
        start_bone = _get_object_bone_index(object_id, start_bone)
        end_bone = _get_object_bone_index(object_id, end_bone)
        return RagDollBone(object_id, _add_3d_physics_ragdoll_bone(start_bone, end_bone, diameter,
                                                                   collision_group, collision_mask))

    # noinspection PyMethodMayBeStatic
    def set_damping(self, linear: float, angular: float):
        _set_3d_physics_ragdoll_damping(linear, angular)

    # noinspection PyMethodMayBeStatic
    def set_deactivation_time(self, time: float):
        _set_3d_physics_ragdoll_deactivation_time(time)

    # noinspection PyMethodMayBeStatic
    def set_sleeping_threshold(self, linear: float, angular: float):
        _set_3d_physics_ragdoll_sleeping_thresholds(linear, angular)


class Object3D(object):
    """Wraps 3d object functionality."""
    __instances = _weakref.WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        _id = kwargs.get("_id")
        # If an ID is given and it is 0, don't create an instance.
        if _id == 0:
            return None
        o = super().__new__(cls)
        # if _id:
        #     o.__id = _id
        return o

    def __init__(self, filename: str, height: float = None, load_children: bool = True, **kwargs):
        # 'Hidden' arguments for internal use only!
        _id = kwargs.get("_id")
        _parent = kwargs.get("_parent")
        if _id is None:
            _id = _load_object_with_children(filename) if load_children else _load_object(filename)
        self.__id = _id
        Object3D.__instances[_id] = self
        # When instanced, __instanced_object is set to the object that was instanced.
        # Maintain a ref so that the instanced object doesn't get deleted before its instances.
        self.__instanced_object = None
        # __parent_object is set for child objects.
        self.__parent_object = _weakref.ref(_parent) if _parent else None
        # Key: [mesh.id, stage] = image
        self.__images = {}  # type: Dict[Tuple[int, int], Image]
        # Key: [mesh.id] = image
        self.__shaders = {}  # type: Dict[int, Shader]
        self.__bones = _Bone3DList(self)
        self.__meshes = _MeshList(self)
        self.__rigidbody = None
        self.__rigidbody_proxy = None
        self.__controller = None
        self.__controller_proxy = None
        # self.__meshes = tuple(Mesh(self, mesh_id + 1) for mesh_id in range(_get_object_num_meshes(_id)))
        # self.__bones = tuple(Bone3D(self, bone_id + 1) for bone_id in range(_get_object_num_bones(_id)))
        self.__children = _ChildObject3DList(self)
        # Passing height into load_object appears to act like set_object_scale_permanent on the entire object.
        if height is not None:
            original_height = _get_object_size_max_y(_id) - _get_object_size_min_y(_id)
            # Make sure we actually have a height to scale.
            if original_height:
                scale = height / original_height

                # Scale this object and any child objects recursively.
                def scale_object(obj_id):
                    _set_object_scale_permanent(obj_id, scale, scale, scale)
                    for index in range(_get_object_num_children(obj_id)):
                        child_id = _get_object_child_id(obj_id, index + 1)
                        scale_object(child_id)

                scale_object(_id)

    def __del__(self):
        """Delete the object."""
        try:
            self.delete_ragdoll()
            self.delete_controller()
            self.delete_rigidbody()
            _delete_object(self.__id)
        except TypeError as e:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    @classmethod
    def _from_id(cls, object_id: int):
        # Check for <= 0 because get_3d_physics_ray_cast_object_hit and get_3d_physics_ray_cast_closest_object_hit
        # return -1 when the fraction_index is invalid.  Not a problem in this project, but good to know.
        if object_id <= 0:
            return None
        if object_id in cls.__instances:
            return cls.__instances.get(object_id)
        return Object3D("", _id=object_id)

    @property
    def bones(self):
        return self.__bones

    @property
    def meshes(self):
        return self.__meshes

    def _store_image_ref(self, mesh_id: Union[int, None], image: Image, stage: int):
        # Setting for the object sets for all meshes in the object.  (when mesh_id is None.)
        # Mesh ID is 1-based.
        mesh_ids = list(range(1, _get_object_num_meshes(self.__id) + 1)) if mesh_id is None else [mesh_id]
        # Setting for the object sets for all meshes in the object.
        for mesh_id in mesh_ids:
            self.__images[(mesh_id, stage)] = image

    def _store_shader_ref(self, mesh_id: Union[int, None], shader: Shader):
        # Setting for the object sets for all meshes in the object.  (when mesh_id is None.)
        # Mesh ID is 1-based.
        mesh_ids = list(range(1, _get_object_num_meshes(self.__id) + 1)) if mesh_id is None else [mesh_id]
        # Setting for the object sets for all meshes in the object.
        for mesh_id in mesh_ids:
            self.__shaders[mesh_id] = shader

    def create_instance(self) -> "Object3D":
        if self.__instanced_object:
            raise RuntimeError("An instance object cannot be instanced.")
        new_object = Object3D._from_id(_instance_object(self.__id))
        # Store a ref the original object so that it won't get deleted before the instance.
        new_object.__instanced_object = self
        # The new object also gets refs to the images and shaders from the original.
        new_object.__images = self.__images.copy()
        new_object.__shaders = self.__shaders.copy()
        return new_object

    def clone(self) -> "Object3D":
        new_object = Object3D._from_id(_clone_object(self.__id))
        # Cloning an instanced object creates another instanced object.
        new_object.__instanced_object = self.__instanced_object
        # The new object also gets refs to the images and shaders from the original.
        new_object.__images = self.__images.copy()
        new_object.__shaders = self.__shaders.copy()
        return new_object

    def draw(self):
        _draw_object(self.__id)

    @classmethod
    def create_box(cls, width: float, height: float, length: float) -> "Object3D":
        return cls._from_id(_create_object_box(width, height, length))

    @classmethod
    def create_capsule(cls, diameter: float, height: float, axis: Axis) -> "Object3D":
        return cls._from_id(_create_object_capsule(diameter, height, axis))

    @classmethod
    def create_cone(cls, height: float, diameter: float, segments: int) -> "Object3D":
        return cls._from_id(_create_object_cone(height, diameter, segments))

    @classmethod
    def create_cylinder(cls, height: float, diameter: float, segments: int) -> "Object3D":
        return cls._from_id(_create_object_cylinder(height, diameter, segments))

    @classmethod
    def create_plane(cls, width: float, height: float) -> "Object3D":
        return cls._from_id(_create_object_plane(width, height))

    @classmethod
    def create_quad(cls) -> "Object3D":
        return cls._from_id(_create_object_quad())

    @classmethod
    def create_sphere(cls, diameter: float, rows: int, columns: int) -> "Object3D":
        return cls._from_id(_create_object_sphere(diameter, rows, columns))

    @classmethod
    def from_height_map(cls, filename: str, width: float, height: float, length: float, smoothing: int,
                        split: int) -> "Object3D":
        return cls._from_id(_create_object_from_height_map(filename, width, height, length, smoothing, split))

    @classmethod
    def from_mesh(cls, mesh: Mesh) -> "Object3D":
        return cls._from_id(_create_object_from_object_mesh(mesh.object3d.id, mesh.id))

    @classmethod
    def from_raw_height_map(cls, filename: str, width: float, height: float, length: float, smoothing: int,
                            split: int, raw_width: int, raw_height: int) -> "Object3D":
        return cls._from_id(_create_object_from_raw_height_map(filename, width, height, length, smoothing, split,
                                                               raw_width, raw_height))

    @property
    def child_count(self) -> int:
        return _get_object_num_children(self.__id)

    @property
    def children(self):
        return self.__children

    def fix_pivot(self):
        if self.__instanced_object:
            raise RuntimeError("Cannot fix_pivot an object instance.")
        _fix_object_pivot(self.__id)

    def fix_to_bone(self, bone: Bone3D):
        _fix_object_to_bone(self.__id, bone.object3d.id, bone.id)

    def fix_to_object(self, object3d: "Object3D"):
        _fix_object_to_object(self.__id, object3d.id)

    @property
    def color_alpha(self) -> int:
        return _get_object_alpha(self.__id)

    @color_alpha.setter
    def color_alpha(self, value: int):
        _set_object_alpha(self.__id, value)

    @property
    def color_blue(self) -> int:
        return _get_object_color_blue(self.__id)

    @property
    def color_green(self) -> int:
        return _get_object_color_green(self.__id)

    @property
    def color_red(self) -> int:
        return _get_object_color_red(self.__id)

    def set_color(self, red: int, green: int, blue: int, alpha: int):
        _set_object_color(self.__id, red, green, blue, alpha)

    @property
    def angle_x(self) -> float:
        return _get_object_angle_x(self.__id)

    @property
    def angle_y(self) -> float:
        return _get_object_angle_y(self.__id)

    @property
    def angle_z(self) -> float:
        return _get_object_angle_z(self.__id)

    def set_rotation(self, x: float, y: float, z: float):
        _set_object_rotation(self.__id, x, y, z)

    @property
    def cull_mode(self) -> CullMode:
        return CullMode(_get_object_cull_mode(self.__id))

    @property
    def depth_bias(self) -> float:
        return _get_object_depth_bias(self.__id)

    @depth_bias.setter
    def depth_bias(self, value: float):
        _set_object_depth_bias(self.__id, value)

    @property
    def depth_read_mode(self) -> DepthReadMode:
        return DepthReadMode(_get_object_depth_read_mode(self.__id))

    @depth_read_mode.setter
    def depth_read_mode(self, value: DepthReadMode):
        _set_object_depth_read_mode(self.__id, value)

    @property
    def depth_write_enabled(self) -> bool:
        return _get_object_depth_write(self.__id)

    @depth_write_enabled.setter
    def depth_write_enabled(self, value: bool):
        _set_object_depth_write(self.__id, value)

    def get_height_at(self, x: float, z: float) -> float:
        return _get_object_height_map_height(self.__id, x, z)

    @property
    def is_in_screen(self) -> bool:
        return _get_object_in_screen(self.__id)

    @property
    def is_tweening(self) -> bool:
        return _get_object_is_tweening(self.__id)

    @property
    def name(self) -> str:
        return _get_object_name(self.__id)

    @property
    def quat_w(self) -> float:
        return _get_object_quat_w(self.__id)

    @property
    def quat_x(self) -> float:
        return _get_object_quat_x(self.__id)

    @property
    def quat_y(self) -> float:
        return _get_object_quat_y(self.__id)

    @property
    def quat_z(self) -> float:
        return _get_object_quat_z(self.__id)

    @property
    def size_max_x(self) -> float:
        return _get_object_size_max_x(self.__id)

    @property
    def size_max_y(self) -> float:
        return _get_object_size_max_y(self.__id)

    @property
    def size_max_z(self) -> float:
        return _get_object_size_max_z(self.__id)

    @property
    def size_min_x(self) -> float:
        return _get_object_size_min_x(self.__id)

    @property
    def size_min_y(self) -> float:
        return _get_object_size_min_y(self.__id)

    @property
    def size_min_z(self) -> float:
        return _get_object_size_min_z(self.__id)

    @property
    def transparency(self) -> TransparencyMode:
        return TransparencyMode(_get_object_transparency(self.__id))

    @property
    def visible(self) -> bool:
        return _get_object_visible(self.__id)

    @property
    def world_angle_x(self) -> float:
        return _get_object_world_angle_x(self.__id)

    @property
    def world_angle_y(self) -> float:
        return _get_object_world_angle_y(self.__id)

    @property
    def world_angle_z(self) -> float:
        return _get_object_world_angle_z(self.__id)

    @property
    def world_quat_w(self) -> float:
        return _get_object_world_quat_w(self.__id)

    @property
    def world_quat_x(self) -> float:
        return _get_object_world_quat_x(self.__id)

    @property
    def world_quat_y(self) -> float:
        return _get_object_world_quat_y(self.__id)

    @property
    def world_quat_z(self) -> float:
        return _get_object_world_quat_z(self.__id)

    @property
    def world_x(self) -> float:
        return _get_object_world_x(self.__id)

    @property
    def world_y(self) -> float:
        return _get_object_world_y(self.__id)

    @property
    def world_z(self) -> float:
        return _get_object_world_z(self.__id)

    @property
    def x(self) -> float:
        return _get_object_x(self.__id)

    @property
    def y(self) -> float:
        return _get_object_y(self.__id)

    @property
    def z(self) -> float:
        return _get_object_z(self.__id)

    def move_local_x(self, distance: float):
        _move_object_local_x(self.__id, distance)

    def move_local_y(self, distance: float):
        _move_object_local_y(self.__id, distance)

    def move_local_z(self, distance: float):
        _move_object_local_z(self.__id, distance)

    def move_local(self, x: float = None, y: float = None, z: float = None):
        if x:
            _move_object_local_x(self.__id, x)
        if y:
            _move_object_local_y(self.__id, y)
        if z:
            _move_object_local_z(self.__id, z)

    def rotate_global_x(self, angle: float):
        _rotate_object_global_x(self.__id, angle)

    def rotate_global_y(self, angle: float):
        _rotate_object_global_y(self.__id, angle)

    def rotate_global_z(self, angle: float):
        _rotate_object_global_z(self.__id, angle)

    def rotate_global(self, x: float = None, y: float = None, z: float = None):
        if x:
            _rotate_object_global_x(self.__id, x)
        if y:
            _rotate_object_global_y(self.__id, y)
        if z:
            _rotate_object_global_z(self.__id, z)

    def rotate_local_x(self, angle: float):
        _rotate_object_local_x(self.__id, angle)

    def rotate_local_y(self, angle: float):
        _rotate_object_local_y(self.__id, angle)

    def rotate_local_z(self, angle: float):
        _rotate_object_local_z(self.__id, angle)

    def rotate_local(self, x: float = None, y: float = None, z: float = None):
        if x:
            _rotate_object_local_x(self.__id, x)
        if y:
            _rotate_object_local_y(self.__id, y)
        if z:
            _rotate_object_local_z(self.__id, z)

    def enable_alpha_mask(self, enabled: bool = True):
        _set_object_alpha_mask(self.__id, enabled)

    def set_blend_modes(self, src: AlphaBlendMode, dst: AlphaBlendMode):
        _set_object_blend_modes(self.__id, src, dst)

    def enable_collision_detection(self, enabled: bool = True):
        _set_object_collision_mode(self.__id, enabled)

    def set_color_emissive(self, red: int, green: int, blue: int):
        _set_object_color_emissive(self.__id, red, green, blue)

    @cull_mode.setter
    def cull_mode(self, value: CullMode):
        _set_object_cull_mode(self.__id, value)

    def set_depth_range(self, near: float, far: float):
        _set_object_depth_range(self.__id, near, far)

    def enable_fog(self, enabled: bool = True):
        _set_object_fog_mode(self.__id, enabled)

    def set_image(self, image: Image, stage: int = 0):
        self._store_image_ref(None, image, stage)
        _set_object_image(self.__id, image.id if image else 0, stage)

    def set_light_map(self, image: Image):
        self._store_image_ref(None, image, _LIGHT_MAP_IMAGE_STAGE)
        _set_object_light_map(self.__id, image.id if image else 0)

    def enable_light_mode(self, enabled: bool = True):
        _set_object_light_mode(self.__id, enabled)

    def look_at(self, x: float, y: float, z: float, roll: float):
        _set_object_look_at(self.__id, x, y, z, roll)

    def set_normal_map(self, image: Image):
        self._store_image_ref(None, image, _NORMAL_MAP_IMAGE_STAGE)
        _set_object_normal_map(self.__id, image.id if image else 0)

    def set_normal_map_scale(self, u: float, v: float):
        _set_object_normal_map_scale(self.__id, u, v)

    def set_position(self, x: float, y: float, z: float):
        _set_object_position(self.__id, x, y, z)

    def set_rotation_quat(self, w: float, x: float, y: float, z: float):
        _set_object_rotation_quat(self.__id, w, x, y, z)

    def set_scale(self, x: float, y: float, z: float):
        _set_object_scale(self.__id, x, y, z)

    def set_scale_permanent(self, x: float, y: float, z: float):
        _set_object_scale_permanent(self.__id, x, y, z)

    def enable_screen_culling(self, enabled: bool = True):
        _set_object_screen_culling(self.__id, enabled)

    def set_shader(self, shader: Shader):
        self._store_shader_ref(None, shader)
        _set_object_shader(self.__id, shader.id if shader else 0)

    def set_shader_constant_array_by_name(self, name: str, index: int, value1: float, value2: float = 0,
                                          value3: float = 0, value4: float = 0):
        _set_object_shader_constant_array_by_name(self.__id, name, index, value1, value2, value3, value4)

    def set_shader_constant_by_name(self, name: str, value1: float, value2: float = 0, value3: float = 0,
                                    value4: float = 0):
        _set_object_shader_constant_by_name(self.__id, name, value1, value2, value3, value4)

    def set_shader_constant_to_default(self, name: str):
        _set_object_shader_constant_default(self.__id, name)

    @transparency.setter
    def transparency(self, value: TransparencyMode):
        _set_object_transparency(self.__id, value)

    def set_uv_offset(self, u: float = 0, v: float = 0, stage: int = 0):
        _set_object_uv_offset(self.__id, stage, u, v)

    def set_uv_scale(self, u: float = 1.0, v: float = 1.0, stage: int = 0):
        _set_object_uv_scale(self.__id, stage, u, v)

    @visible.setter
    def visible(self, value: bool):
        _set_object_visible(self.__id, value)

    # 3D > Shadows
    @property
    def casts_shadow(self) -> bool:
        return _get_object_cast_shadow_mode(self.__id)

    @casts_shadow.setter
    def casts_shadow(self, value: bool):
        _set_object_cast_shadow(self.__id, value)

    @property
    def receives_shadow(self) -> bool:
        return _get_object_receive_shadow_mode(self.__id)

    @receives_shadow.setter
    def receives_shadow(self, value: bool):
        _set_object_receive_shadow(self.__id, value)

    def get_animation_duration(self, name: str) -> float:
        return _get_object_animation_duration(self.__id, name)

    def get_animation_name(self, index: int):
        """index is 0-based here, not 1-based as in AppGameKit."""
        index += 1
        return _get_object_animation_name(self.__id, index)

    def get_animation_time(self):
        return _get_object_animation_time(self.__id)

    @property
    def is_animating(self) -> bool:
        return _get_object_is_animating(self.__id)

    @property
    def animation_count(self) -> int:
        return _get_object_num_animations(self.__id)

    def play_animation(self, name: str, start_time: float = 0.0, end_time: float = -1.0, loop: int = 0,
                       tween_time: float = 0.0):
        _play_object_animation(self.__id, name, start_time, end_time, loop, tween_time)

    def reset_animation(self):
        _reset_object_animation(self.__id)

    def set_animation_frame(self, name: str, time: float, tween_time: float = 0.0):
        _set_object_animation_frame(self.__id, name, time, tween_time)

    def set_animation_speed(self, speed: float):
        _set_object_animation_speed(self.__id, speed)

    def stop_animation(self):
        _stop_object_animation(self.__id)

    @property
    def mesh_count(self) -> int:
        return _get_object_num_meshes(self.__id)

    @property
    def texture_count(self) -> int:
        return _get_object_num_textures(self.__id)

    def get_texture_name(self, index: int) -> str:
        """index is 0-based here, not 1-based as in AppGameKit."""
        index += 1
        return _get_object_texture_name(self.__id, index)

    @classmethod
    def from_memblock(cls, memblock: "MeshMemblock") -> "Object3D":
        return cls._from_id(_create_object_from_mesh_memblock(memblock.id))

    def create_character_controller(self, axis: Axis, offset_vector: Vector3, orientation_vector: Vector3,
                                    crouch_scale: float):
        _create_3d_physics_character_controller(self.__id, axis, offset_vector.id, orientation_vector.id, crouch_scale)
        if not self.__controller:
            self.__controller = _CharacterController(self.__id)
            self.__controller_proxy = _weakref.proxy(self.__controller)

    @property
    def controller(self) -> _CharacterController:
        # Only make the rigidbody proxy available outside of this class.
        return self.__controller_proxy

    def delete_controller(self):
        self.__controller_proxy = None
        self.__controller = None

    def delete_ragdoll(self):
        with _warnings.catch_warnings():
            _warnings.simplefilter("ignore")
            if _get_3d_physics_ragdoll_exist(self.__id):
                _delete_3d_physics_ragdoll(self.__id)

    def set_ragdoll_visible(self, visible: bool = True):
        _set_3d_physics_ragdoll_bones_visible(self.__id, visible)

    def enable_ragdoll_deactivation(self, enabled: bool = True):
        _set_3d_physics_ragdoll_deactivation(self.__id, not enabled)

    @property
    def is_ragdoll_static(self) -> bool:
        return _is_3d_physics_ragdoll_static(self.__id)

    @is_ragdoll_static.setter
    def is_ragdoll_static(self, value: bool):
        _set_3d_physics_ragdoll_static(self.__id, value)

    def __create_rigid_body(self, create_func):
        create_func(self.__id)
        if not self.__rigidbody:
            self.__rigidbody = _RigidBody(self.__id)
            self.__rigidbody_proxy = _weakref.proxy(self.__rigidbody)

    def create_dynamic_body(self):
        self.__create_rigid_body(_create_3d_physics_dynamic_body)

    def create_kinematic_body(self):
        self.__create_rigid_body(_create_3d_physics_kinematic_body)

    def create_static_body(self):
        self.__create_rigid_body(_create_3d_physics_static_body)

    @property
    def rigidbody(self) -> _RigidBody:
        # Only make the rigidbody proxy available outside of this class.
        # RigidBodies are more internalized than other objects.
        # They piggyback onto an Object3D.
        return self.__rigidbody_proxy

    def delete_rigidbody(self):
        self.__rigidbody_proxy = None
        self.__rigidbody = None

    @classmethod
    def _delete_all_physics(cls):
        """Internal use."""
        for obj in cls.__instances.values():  # type: Object3D
            if obj:
                obj.delete_ragdoll()
                obj.delete_controller()
                obj.delete_rigidbody()

