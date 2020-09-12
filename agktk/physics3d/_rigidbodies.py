# from appgamekit import (
#     # 3DPhysics > RigidBodies
#     create_3d_physics_dynamic_body as _create_3d_physics_dynamic_body,
#     create_3d_physics_kinematic_body as _create_3d_physics_kinematic_body,
#     create_3d_physics_static_body as _create_3d_physics_static_body,
#     delete_3d_physics_body as _delete_3d_physics_body,
#     get_object_3d_physics_angular_damp as _get_object_3d_physics_angular_damp,
#     get_object_3d_physics_angular_sleeping_threshold as _get_object_3d_physics_angular_sleeping_threshold,
#     get_object_3d_physics_angular_velocity_x as _get_object_3d_physics_angular_velocity_x,
#     get_object_3d_physics_angular_velocity_y as _get_object_3d_physics_angular_velocity_y,
#     get_object_3d_physics_angular_velocity_z as _get_object_3d_physics_angular_velocity_z,
#     get_object_3d_physics_friction as _get_object_3d_physics_friction,
#     get_object_3d_physics_group as _get_object_3d_physics_group,
#     get_object_3d_physics_linear_damp as _get_object_3d_physics_linear_damp,
#     get_object_3d_physics_linear_sleeping_threshold as _get_object_3d_physics_linear_sleeping_threshold,
#     get_object_3d_physics_linear_velocity_x as _get_object_3d_physics_linear_velocity_x,
#     get_object_3d_physics_linear_velocity_y as _get_object_3d_physics_linear_velocity_y,
#     get_object_3d_physics_linear_velocity_z as _get_object_3d_physics_linear_velocity_z,
#     get_object_3d_physics_mask as _get_object_3d_physics_mask,
#     get_object_3d_physics_mass as _get_object_3d_physics_mass,
#     get_object_3d_physics_max_linear_velocity as _get_object_3d_physics_max_linear_velocity,
#     get_object_3d_physics_restitution as _get_object_3d_physics_restitution,
#     get_object_3d_physics_rolling_friction as _get_object_3d_physics_rolling_friction,
#     set_object_3d_physics_angular_velocity as _set_object_3d_physics_angular_velocity,
#     set_object_3d_physics_angular_velocity_xyz as _set_object_3d_physics_angular_velocity_xyz,
#     set_object_3d_physics_anisotropic_friction as _set_object_3d_physics_anisotropic_friction,
#     set_object_3d_physics_can_sleep as _set_object_3d_physics_can_sleep,
#     set_object_3d_physics_damping as _set_object_3d_physics_damping,
#     set_object_3d_physics_deactivation_time as _set_object_3d_physics_deactivation_time,
#     set_object_3d_physics_friction as _set_object_3d_physics_friction,
#     set_object_3d_physics_group_and_mask as _set_object_3d_physics_group_and_mask,
#     set_object_3d_physics_linear_velocity as _set_object_3d_physics_linear_velocity,
#     set_object_3d_physics_linear_velocity_xyz as _set_object_3d_physics_linear_velocity_xyz,
#     set_object_3d_physics_mass as _set_object_3d_physics_mass,
#     set_object_3d_physics_max_linear_velocity as _set_object_3d_physics_max_linear_velocity,
#     set_object_3d_physics_restitution as _set_object_3d_physics_restitution,
#     set_object_3d_physics_rolling_friction as _set_object_3d_physics_rolling_friction,
#     set_object_3d_physics_sleeping_threshold as _set_object_3d_physics_sleeping_threshold,
# )
# from .._vector3 import Vector3
# from .._enums import AnisotropicFrictionMode
# from .._grfx3d import object3d
#
#
# class _RigidBody(object):
#     def __init__(self, object_id: int):
#         self.__id = object_id
#
#     def __del__(self):
#         """Deletes the object."""
#         try:
#             _delete_3d_physics_body(self.__id)
#         except TypeError:
#             pass
#
#     def __repr__(self):
#         return f"<{self.__class__.__name__}, id: {self.__id}>"
#
#     @property
#     def id(self) -> int:
#         """The internal ID for this object."""
#         return self.__id
#
#     @property
#     def angular_damp(self) -> float:
#         return _get_object_3d_physics_angular_damp(self.__id)
#
#     @property
#     def linear_damp(self) -> float:
#         return _get_object_3d_physics_linear_damp(self.__id)
#
#     def set_damping(self, linear: float, angular: float):
#         _set_object_3d_physics_damping(self.__id, linear, angular)
#
#     @property
#     def angular_sleeping_threshold(self) -> float:
#         return _get_object_3d_physics_angular_sleeping_threshold(self.__id)
#
#     @property
#     def linear_sleeping_threshold(self) -> float:
#         return _get_object_3d_physics_linear_sleeping_threshold(self.__id)
#
#     def enable_sleep(self, enabled: bool = True):
#         _set_object_3d_physics_can_sleep(self.__id, enabled)
#
#     def set_sleeping_threshold(self, linear: float, angular: float):
#         # Yes, the angular and linear parameters are in the opposite order here than they are for
#         #   set_object_3d_physics_damping, set_3d_physics_ragdoll_sleeping_thresholds, and
#         #   set_3d_physics_ragdoll_damping!
#         _set_object_3d_physics_sleeping_threshold(self.__id, angular, linear)
#
#     @property
#     def angular_velocity_x(self) -> float:
#         return _get_object_3d_physics_angular_velocity_x(self.__id)
#
#     @property
#     def angular_velocity_y(self) -> float:
#         return _get_object_3d_physics_angular_velocity_y(self.__id)
#
#     @property
#     def angular_velocity_z(self) -> float:
#         return _get_object_3d_physics_angular_velocity_z(self.__id)
#
#     def set_angular_velocity_from_vector(self, vector: Vector3, initial_speed: float):
#         _set_object_3d_physics_angular_velocity(self.__id, vector.id, initial_speed)
#
#     def set_angular_velocity(self, x: float, y: float, z: float, initial_speed: float):
#         _set_object_3d_physics_angular_velocity_xyz(self.__id, x, y, z, initial_speed)
#
#     @property
#     def friction(self) -> float:
#         return _get_object_3d_physics_friction(self.__id)
#
#     @friction.setter
#     def friction(self, value: float):
#         _set_object_3d_physics_friction(self.__id, value)
#
#     def set_anisotropic_friction(self, mode: AnisotropicFrictionMode):
#         _set_object_3d_physics_anisotropic_friction(self.__id, mode)
#
#     @property
#     def group(self) -> int:
#         return _get_object_3d_physics_group(self.__id)
#
#     @property
#     def mask(self) -> int:
#         return _get_object_3d_physics_mask(self.__id)
#
#     def set_group_and_mask(self, group: int, mask: int):
#         _set_object_3d_physics_group_and_mask(self.__id, group, mask)
#
#     @property
#     def linear_velocity_x(self) -> float:
#         return _get_object_3d_physics_linear_velocity_x(self.__id)
#
#     @property
#     def linear_velocity_y(self) -> float:
#         return _get_object_3d_physics_linear_velocity_y(self.__id)
#
#     @property
#     def linear_velocity_z(self) -> float:
#         return _get_object_3d_physics_linear_velocity_z(self.__id)
#
#     def set_linear_velocity_from_vector(self, vector: Vector3, initial_speed: float):
#         _set_object_3d_physics_linear_velocity(self.__id, vector.id, initial_speed)
#
#     def set_linear_velocity(self, x: float, y: float, z: float, initial_speed: float):
#         _set_object_3d_physics_linear_velocity_xyz(self.__id, x, y, z, initial_speed)
#
#     @property
#     def mass(self) -> float:
#         return _get_object_3d_physics_mass(self.__id)
#
#     @mass.setter
#     def mass(self, value: float):
#         _set_object_3d_physics_mass(self.__id, value)
#
#     @property
#     def max_linear_velocity(self) -> float:
#         return _get_object_3d_physics_max_linear_velocity(self.__id)
#
#     @max_linear_velocity.setter
#     def max_linear_velocity(self, value: float):
#         _set_object_3d_physics_max_linear_velocity(self.__id, value)
#
#     @property
#     def restitution(self) -> float:
#         return _get_object_3d_physics_restitution(self.__id)
#
#     @restitution.setter
#     def restitution(self, value: float):
#         _set_object_3d_physics_restitution(self.__id, value)
#
#     @property
#     def rolling_friction(self) -> float:
#         return _get_object_3d_physics_rolling_friction(self.__id)
#
#     @rolling_friction.setter
#     def rolling_friction(self, value: float):
#         _set_object_3d_physics_rolling_friction(self.__id, value)
#
#     def set_deactivation_time(self, time: float):
#         _set_object_3d_physics_deactivation_time(self.__id, time)
#
#
# object3d._RigidBody = _RigidBody
