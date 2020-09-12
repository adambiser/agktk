#!/usr/bin/python3
import appgamekit as agk
from agktk import *
import agktk.debug as debug
import agktk.physics3d as physics
# import agktk.net as net

from typing import Any

# ^(\s*)([a-z_0-9]+),
# \1\2 as _\2,

# TODO
#   Core > Strings, Math, sha1/256/512
#   Sound > TextToSpeech?, Device?, Vibration?

# TODO Maybe?
#   Advert
#   Extras

# Use as metaclass
# import weakref as _weakref
# class CameraCache(type):
#     _instances = _weakref.WeakValueDictionary()
#
#     def __call__(cls, camera_id: int = 1, *args, **kwargs):
#         camera = cls._instances.get(camera_id)
#         if camera is None:
#             # Store ref so this doesn't get deleted immediately.
#             camera = super().__call__(camera_id, *args, **kwargs)
#             cls._instances[camera_id] = camera
#         return camera

# Consider for MeshMemblocks, etc.
# class Vertex(object):
#     def __init__(self):
#         self.index = None
#         self._x = 1
#
#     @property
#     def x(self):
#         print(f"get {self.index}.x")
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         print(f"set {self.index}.x")
#         self._x = value
#
#
# class VertexList(object):
#     def __init__(self):
#         self._vertices = Vertex()
#
#     def __getitem__(self, index):
#         self._vertices.index = index
#         return self._vertices
#
#
# class Test(object):
#     def __init__(self):
#         self._vertices = VertexList()
#
#     @property
#     def vertices(self):
#         return self._vertices
#
#
# x = Test()
# x.vertices[2].x += 2
# print(x.vertices[2].x)

# >> > x = Test(3)
# >> > x.get[2]

# class _BoneList(object):
#     def __init__(self, skeleton: "Skeleton2D"):
#         self.__skeleton = weakref.proxy(skeleton)
#         self.__skeleton_id = skeleton.id
#
#     def __getitem__(self, item):
#         try:
#             index = _get_skeleton_2d_bone(self.__skeleton_id, item)
#         except TypeError:
#             index = item
#         if index < 0:
#             return None
#         return Bone(self.__skeleton, index)


# Also consider:
# class AppGameKitObject(type):
#     # Needed to ignore the `delete_function` kwarg.
#     def __new__(mcs, name, bases, namespace, **kargs):
#         return super().__new__(mcs, name, bases, namespace)
#
#     def __init__(cls, name, bases, attr_dict, delete_function):
#         # print(cls, name, bases, attr_dict)
#         # print(delete_function)
#         super().__init__(name, bases, attr_dict)
#
#         def __del__(self):
#             """Deletes the object."""
#             try:
#                 delete_function(self.__id)
#             except TypeError:
#                 pass
#
#         def __repr__(self):
#             return f"<{self.__class__.__name__}, id: {self.__id}>"
#
#         @property
#         def id(self) -> int:
#             """The internal ID for this object."""
#             return self.__id
#
#         cls.__id = None
#         cls.__repr__ = __repr__
#         cls.id = id
#         if delete_function:
#             cls.__del__ = __del__
#
#
# class UdpListener(object, metaclass=AppGameKitObject, delete_function=_delete_udp_listener):
#     pass

# Idea
# class EvaluatingAttribute(object):
#     def __init__(self, func):
#         self._callable = func
#
#     def __call__(self):
#         # print("Calling")
#         return self._callable()
#
#     def __repr__(self):
#         return repr(self())
#
#
# device_base_name = EvaluatingAttribute(get_device_base_name)

#  at {id(self):#018x}

# Write-only property
# class Test():
# 	def __init__(self):
# 		self.x = 2
# 	def write(self, value):
# 		self.x = value
# 	write = property(None, write)

# Attach method to class:
# class X:
#     def __init__(self):
#         self.__x = 2
#
# def make_test():
#     # Needed to access private attributes
#     class X:
#         def test(self):
#             print(self.__x)
#     return X.test
#
# X.test = make_test()
#
# x = X()
# x.test()

# def add_methods(cls):
#     # noinspection PyShadowingNames
#     class VirtualButton(object):
#         def __init__(self):
#             self.__id = None
#
#         def test(self):
#             print(f"testing: {self.__id}")
#     cls.test = VirtualButton.test


# import agktk
#
#
# class NewVirtualButton(agktk.VirtualButton):
#     def test(self):
#         print(f"testing new method: {self.id}")
#
# agktk.VirtualButton = NewVirtualButton

# VirtualButton.test = test


# add_methods(VirtualButton)


class MyGame(Game):
    def __init__(self):
        super().__init__(width=1024, height=768)
        device.set_error_mode(ErrorMode.REPORT)
        device.enable_debug_log()
        display.set_sync_rate(0, 0)
        display.set_virtual_resolution(1024, 768)
        self.play_song_button = VirtualButton(50, 718, 100, text="Play\nSong")
        self.play_sound_button = VirtualButton(150, 718, 100, text="Play\nSound")
        # self.play_song_button.test()
        self.joystick = VirtualJoystick(50, 500, 100)
        arial = Font("Arial")
        display.set_print_font(arial)
        self.editbox = EditBox(5, 200)
        self.image = Image("flyFly1-power2.png")
        self.image2 = Image("flyFly2.png")
        # load JSON exported Spriter file.
        # self.spriter = Skeleton2D(spriter_filename="Spriter/GreyGuy.scon")
        # self.spriter.set_position(512, 768)
        # self.spriter.play_animation("walk", 0, 1, 0.3)
        # bone = self.spriter.bones["head"]
        # print(bone)
        # print(bone.parent_bone)
        # self.actor = Object3D("lara3/YCYKIV23WPVIAC6SMZ6V0EBZE_booty_hip_hop_dance.fbx")
        # self.actor = Object3D("lara/lara.obj")
        physics.create_world()
        physics.set_gravity(0, -0.2, 0)
        soldier_image = Image("soldier/Soldier_body_1_D.png")
        print(soldier_image)
        self.actor = Object3D("soldier/Original_Soldier.X", 6)
        self.actor.set_image(soldier_image)
        for bone in self.actor.bones:
            print(f"{bone.id} = {bone.name}")
        # self.bone = self.actor.bones['$dummy_root']
        # print("---end")
        # del self.actor.child[0]  # .visible = False
        self.actor.children[1].set_image(Image("soldier/gun_D.png"))
        # del self.actor.child[1]  # .visible = False
        self.actor.set_position(0, 0, 4)
        self.actor.create_static_body()
        self.actor.rigidbody.set_shape_box()
        with RagDollBuilder(self.actor, 175) as ragdoll:
            pelvis = ragdoll.add_bone("Bip01_Pelvis", "Bip01_Spine", 10, 0, 0)
            pelvis.assign_to_object_bone("Bip01_R_Thigh")
            pelvis.assign_to_object_bone("Bip01_L_Thigh")

        # self.actor.create_character_controller(Axis.Y, Vector3(0, 0, 0), Vector3(0, 0, 0), 0.5)
        # self.actor.controller.gravity = 0
        # self.actor.rotate_local_y(45)
        self.actor.play_animation("", 1000, 1282, 1, 0)
        self.actor.set_animation_speed(20)
        self.actor2 = self.actor.clone()
        self.actor2.set_position(0, 0, 7)
        self.actor2.create_static_body()
        self.actor2.rigidbody.set_shape_box()
        self.actor2.play_animation("", 1000, 1282, 1, 0.5)
        # gun = MeshMemblock(mesh=self.actor.children[1].meshes[0])
        # print(len(self.actor2.meshes))
        # self.actor2.meshes.append(gun)
        # print(len(self.actor2.meshes))
        # print(self.actor2.meshes[1].name)
        print(self.actor)
        print(self.actor2)
        # del self.actor
        # del self.bone
        # print("after del")
        # self.boxes = [Object3D.create_box(1, 1, 1) for x in range(3)]
        # for index, box in enumerate(self.boxes):
        #     print(f"Box {index} = {box}")
        #     box.set_position(index * 1, 0, index * 1)
        # start = (1, 0, -1)
        # end = (-2, 0, 4)
        # start = (-1, 0, -1)
        # end = (4, 0, 4)
        # self.start = Object3D.create_sphere(0.5, 10, 10)
        # self.start.set_position(*start)
        # self.end = Object3D.create_sphere(0.5, 10, 10)
        # self.end.set_position(*end)
        # print(raycaster.intersects(self.boxes[1], *start, *end))
        # # print(agk.object_sphere_cast(0, *start, *end, 0.25))
        # # print(agk.object_sphere_slide(0, *start, *end, 0.25))  # add 1 to get_object_ray_cast_num_hits
        # # self.camera = Camera3D()
        # # self.camera.set_position(0, 3, -3)
        # # self.camera.look_at(1, 0, 1, 0)
        # num_hits = raycaster.get_hit_count()
        # print(f"hits: {num_hits}")
        # self.hits = [Object3D.create_sphere(0.5, 10, 10) for _ in range(num_hits)]
        # colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        # for index in range(num_hits):
        #     print(f"index: {index}")
        #     print(f"\thit: {raycaster.get_hit_object(index)}")
        #     print(f"\tdistance: {raycaster.get_distance(index)}")
        #     self.hits[index].set_position(*raycaster.get_slide_position(index))
        #     self.hits[index].set_color(*colors[index], 255)
        #     print(f"\tpos: {raycaster.get_hit_position(index)}")
        #     print(f"\tnormal: {raycaster.get_normal(index)}")
        #     print(f"\tbounce: {raycaster.get_bounce_position(index)}")
        #     # object_sphere_slide
        #     print(f"\tslide: {raycaster.get_slide_position(index)}")
        #     # print(mesh.name)
        # x = network.UdpListener(device.get_ip(), 1024)
        # camera = device.Camera()
        # image2 = camera.start_streaming()
        self.image.set_mag_filter(Filter.NEAREST)
        self.image.set_min_filter(Filter.NEAREST)
        self.image.set_wrap_u(TextureWrap.REPEAT)
        self.image.set_wrap_v(TextureWrap.REPEAT)
        # self.fly = Sprite(self.image, x=100, width=512, height=512)
        # self.text = Text("Hello!", x=200, size=30)
        # self.fly2 = Sprite(self.image2)
        # # fly2 = fly.clone()
        # # fly2.set_flip(True, False)
        # self.fly.set_animation(64, 64, 4)
        # self.fly.play(4)
        # self.fly2.x += self.fly.width
        # device.log(self.fly)
        # device.log(self.fly2)
        # self.emitter = ParticleEmitter(400, 400)
        # self.emitter.image = self.image
        # # for f in debug.unassigned_image_file_names():
        # #     device.log(f)
        # self.emitter.add_force(0, .2, 200, 0)
        # self.emitter.size = 16
        # self.emitter2 = ParticleEmitter3D(1, 1, 1)
        # self.emitter2.set_direction_range(90, 90)
        # # self.emitter2.set_direction(-1, 1, 0, 0)
        # # self.emitter2.add_force(0, .2, 20, 0, 0)
        # self.emitter2.image = self.image
        # self.emitter2.size = 4
        # fly.set_uv(0, 0, 0, 2, 2, 0, 2, 2)
        mixer.set_music_volume(10)
        mixer.set_sound_volume(10)
        self.song = Music("Juhani Junkala [Retro Game Music Pack] Title Screen.ogg")
        self.song2 = Music("Juhani Junkala [Retro Game Music Pack] Title Screen.ogg")
        self.sound = Sound("sfx_sounds_button2.wav")
        # with io.FileReader("readtest.txt") as f:
        #     for b in f.strings:
        #         print(f'"{b}"')
        self.vector = Vector3()

    def loop(self):
        display.print_value(f"{display.screen_fps():.2f}")
        display.print_value(self.image)
        # display.print(SoundSystem.min_rate)
        # display.print(SoundSystem.max_rate)
        display.print_value(mouse.get_position())
        display.print_value(EditBox.get_current())
        # if keyboard.is_key_pressed(Key.UP):
        #     self.actor.controller.move(ControllerMove.FORWARD, 5)
        # elif keyboard.is_key_released(Key.UP):
        #     self.actor.controller.move(ControllerMove.STOP, 0)
        if keyboard.is_key_pressed(Key.SPACE):
            ray = physics.raycaster.cast((0, 0.5, -10), (0, 0.5, 10), RayCastMode.ALL)
            for contact in ray.contacts():
                print(contact)
        if self.play_song_button.is_pressed:
            if self.song.is_playing:
                self.song.stop()
            else:
                self.song.play()
            self.play_song_button.text = f'{"Stop" if self.song.is_playing else "Play"}\nSong'
        if self.play_sound_button.is_pressed:
            self.sound.play()
        physics.step_world()
        # if self.actor.rigidbody.get_contact_position_vector(self.actor2, self.vector):
        #     print(self.vector.x)
        #     # self.actor.controller.move(ControllerMove.STOP, 0)
        #     pass
        display.sync()
        if not EditBox.get_current():
            if keyboard.is_key_pressed(Key.ESCAPE):
                return None
        return self


class SpriteTest(Game):
    def __init__(self):
        super().__init__()
        display.set_sync_rate(0, 0)
        self.sprite = Sprite(Image("flyFly2.png"))
        self.loop_function = self.loop

    def loop(self) -> Any:
        display.print_value(f"{display.screen_fps():.2f}")
        self.sprite.x += 4
        display.sync()
        if keyboard.is_key_pressed(Key.ESCAPE):
            return True


class SimpleDemo(Game):
    def __init__(self):
        super().__init__(width=1024, height=768)
        device.set_window_title("Simple 3D Physics")
        # set display properties
        display.set_virtual_resolution(1024, 768)
        device.set_orientation_allowed(True, True, True, True)
        display.set_scissor(0, 0, 0, 0)
        physics.create_world()
        physics.set_gravity(0, -1, 0)
        self.box1 = Object3D.create_box(10, 10, 10)
        self.box1.set_color(255, 0, 0, 255)
        self.box1.create_static_body()
        self.box1.rigidbody.set_shape_box()
        self.box2 = Object3D.create_box(5, 5, 5)
        self.box2.set_position(5.1, 30, 0)
        self.box2.create_dynamic_body()
        self.box2.rigidbody.set_shape_box()
        self.box2.rigidbody.set_angular_velocity(1, 1, 1, 1)
        self.camera = Camera3D()
        self.camera.set_position(0, 30, -80)
        self.camera.look_at(0, 10, 0, 0)
        self.vector = Vector3()

    def loop(self):
        display.print_value(display.screen_fps())
        physics.step_world()
        display.sync()
        return self


def verify_imports():
    import appgamekit as agk
    import inspect
    import os
    import re

    def isfunction(f):
        return inspect.isbuiltin(f) or inspect.isfunction(f)

    def get_methods_in_file(filename):
        used_functions = []
        with open(filename) as fp:
            found_agk_import = False
            for line in fp:
                line = line.strip()
                if line.startswith("from appgamekit import ("):
                    found_agk_import = True
                elif line.startswith(")") and found_agk_import:
                    break
                elif found_agk_import:
                    # match = re.match(r"\s*(?:#\s*)?([a-z0-9_]+)", line)
                    match = re.match(r"\s*([a-z0-9_]+)", line)
                    if match:
                        used_functions.append(match.group(1))
                    else:
                        # Add methods marked as "not needed"
                        match = re.match(r"\s*#\s*([a-z0-9_]+).+#.+not needed", line, re.IGNORECASE)
                        if match:
                            used_functions.append(match.group(1))
        return used_functions

    methods = [k for k, v in agk.__dict__.items() if isfunction(v) and not k.startswith("_")]
    print(f"Start: {len(methods)}")
    for root, dirs, files in os.walk("agktk"):
        for name in [f for f in files if f.endswith(".py")]:
            # print(os.path.join(root, name))
            used_methods = get_methods_in_file(os.path.join(root, name))
            methods = list(filter(lambda m: m not in used_methods, methods))
    # Remove mobile-only commands.
    # methods = list(filter(lambda m: not m.startswith("ar_"), methods))
    methods = list(filter(lambda m: "_admob" not in m, methods))
    methods = list(filter(lambda m: "_chartboost" not in m, methods))
    methods = list(filter(lambda m: "_amazon" not in m, methods))
    methods = list(filter(lambda m: "_advert" not in m, methods))
    # methods = list(filter(lambda m: "rate_app" not in m, methods))
    # methods = list(filter(lambda m: "request_app_review" not in m, methods))
    # methods = list(filter(lambda m: "_inneractive_" not in m, methods))
    # methods = list(filter(lambda m: "game_center" not in m, methods))
    # methods = list(filter(lambda m: "push_notification" not in m, methods))
    # methods = list(filter(lambda m: "n_app_purchase" not in m, methods))
    # methods = list(filter(lambda m: "_permission" not in m, methods))
    # methods = list(filter(lambda m: "_snap_chat" not in m, methods))
    # methods = list(filter(lambda m: "_smart_watch" not in m, methods))
    print(f"Finish: {len(methods)}")
    for name in methods:
        print(name)


# MyGame().run()
# SimpleDemo().run()
verify_imports()

# with MyGame() as game:
#     game.run()
