from appgamekit import (
    # create_window as _create_window,
    destroy_window as _destroy_window,
    Application as _Application,
    # get_paused,
)
from typing import Optional, Any, Union


# TODO This is an idea.  Similar to Panda3D.
class TaskManager(object):
    def __init__(self):
        self.tasks = []  # (name, method, priority)
        self.tasks_to_add = []
        self.tasks_to_remove = []
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.tasks):
            # Reached the end of the task list.  Process task changes.
            if self.tasks_to_add or self.tasks_to_remove:
                # Add tasks.
                if self.tasks_to_add:
                    for name, method, priority in self.tasks_to_add:
                        self.tasks.append((name, method, priority or len(self.tasks) + 1))
                    self.tasks_to_add.clear()
                # Remove tasks.
                if self.tasks_to_remove:
                    for name in self.tasks_to_remove:
                        index = next((t for t in self.tasks if t[0] == name), None)
                        self.tasks.remove(index)
                    self.tasks_to_remove.clear()
                self.tasks.sort(key=lambda entry: entry[2])
            # Go back to the first task.
            self.index = 0
        if self.index >= len(self.tasks):
            raise StopIteration
        return self.tasks[self.index][1]

    def add(self, name: str, method: callable, priority: int = None):
        self.tasks_to_add.append((name, method, priority))

    def remove(self, name):
        self.tasks_to_remove.append(name)


class Scene(object):
    def __init__(self, previous: "Scene"):
        super().__init__()
        self.previous = previous

    def on_show(self):
        pass

    def on_hide(self):
        pass

    def loop(self) -> Union["Scene", None]:
        """
        The overwriting class must define this method.

        Return either the current scene or a new scene to change scenes.
        :return: None to exit the current scene.  If exiting the top-most scene, the game will exit.
        """
        raise NotImplementedError("Your scene needs to overwrite the loop method.")


class Game(_Application, Scene):
    def __init__(self, x: Optional[int] = None, y: Optional[int] = None, width: Optional[int] = 1024,
                 height: Optional[int] = 768, fullscreen: Optional[bool] = False, company_name: str = None,
                 app_name: str = None, show_appgamekit_logo: Optional[bool] = False) -> None:
        super().__init__(x, y, width, height, fullscreen, company_name, app_name, show_appgamekit_logo)
        self.__scene = self
        # self.tasks = TaskManager()

    # @property
    # def is_paused(self) -> bool:
    #     return get_paused()

    def change_scene(self, new_scene):
        self.__scene = new_scene

    def run(self):
        """
        Starts the game loop.
        """
        scene = self.__scene
        try:
            # while not self.loop():
            #     pass
            while scene:
                new_scene = scene.loop()
                if new_scene is not scene:
                    if scene:
                        scene.on_hide()
                    if new_scene:
                        new_scene.on_show()
                    scene = new_scene
            # for task_method in self.tasks:
            #     task_method()
        except KeyboardInterrupt:
            pass
        finally:
            _destroy_window()

    def loop(self):
        """
        The overwriting class must define this method.

        Return any value that can be interpreted as True to break the loop.
        :return: True to break the loop.
        """
        raise NotImplementedError("Your game needs to overwrite the loop method.")
