## noinspection PyUnresolvedReferences
from appgamekit import (
    # 3DPhysics > CompoundCollisionShapes
    # See object3d
    # 3DPhysics > World
    create_3d_physics_world as create_world,
    # debug_3d_physics_world as debug_world,  # Not implemented in AGK yet.
    delete_3d_physics_world as _delete_3d_physics_world,
    get_3d_physics_active_objects as get_active_objects_count,
    get_3d_physics_total_joints as get_total_joints_count,
    get_3d_physics_total_objects as get_total_objects_object,
    reset_3d_physics_world as _reset_3d_physics_world,
    set_3d_physics_gravity as _set_3d_physics_gravity,
    set_3d_physics_gravity_xyz as set_gravity,
    step_3d_physics_world as step_world,
    # 3DPhysics > CollisionShapes
    # See object3d
    # 3DPhysics > SavingAndLoading
    # See object3d
    # 3DPhysics > CharacterController
    # See object3d
    # 3DPhysics > Ragdoll
    # See object3d
    # 3DPhysics > RayCast
    # See raycaster
    # 3DPhysics > Joints
    # See _joints
    # 3DPhysics > RigidBodies
    # See also object3d
    create_3d_physics_static_plane as _create_3d_physics_static_plane,
    delete_3d_physics_static_plane as _delete_3d_physics_static_plane,
    set_3d_physics_static_plane_position as _set_3d_physics_static_plane_position,
    set_3d_physics_static_plane_rotation as _set_3d_physics_static_plane_rotation,
    # 3DPhysics > ContactReports
    # See object3d
)
from . import raycaster
from .._grfx3d import Object3D
from .. import Vector3
from ._joints import (
    ConeTwistJoint,
    FixedJoint,
    HingeJoint,
    PickJoint,
    SixDOFJoint,
    SliderJoint,
)


def reset_world():
    # noinspection PyProtectedMember
    Object3D._delete_all_physics()
    _reset_3d_physics_world()


def delete_world():
    # noinspection PyProtectedMember
    Object3D._delete_all_physics()
    _delete_3d_physics_world()


def set_gravity_from_vector(gravity: Vector3):
    _set_3d_physics_gravity(gravity.id)


class StaticPlane(object):
    def __init__(self, x: float, y: float, z: float, offset: float):
        self.__id = _create_3d_physics_static_plane(x, y, z, offset)

    def __del__(self):
        """Deletes the object."""
        try:
            _delete_3d_physics_static_plane(self.__id)
        except TypeError:
            pass

    def __repr__(self):
        return f"<{self.__class__.__name__}, id: {self.__id}>"

    @property
    def id(self) -> int:
        """The internal ID for this object."""
        return self.__id

    def set_position(self, x: float, y: float, z: float):
        _set_3d_physics_static_plane_position(self.__id, x, y, z)

    def set_rotation(self, x: float, y: float, z: float):
        _set_3d_physics_static_plane_rotation(self.__id, x, y, z)
