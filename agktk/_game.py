from appgamekit import (
    # create_window as _create_window,
    destroy_window as _destroy_window,
    Application as _Application,
    # get_paused,
)
from typing import Optional, Any


class Game(_Application):
    def __init__(self, x: Optional[int] = None, y: Optional[int] = None, width: Optional[int] = 1024,
                 height: Optional[int] = 768, fullscreen: Optional[bool] = False, company_name: str = None,
                 app_name: str = None, show_appgamekit_logo: Optional[bool] = False) -> None:
        super().__init__(x, y, width, height, fullscreen, company_name, app_name, show_appgamekit_logo)

    # @property
    # def is_paused(self) -> bool:
    #     return get_paused()

    def run(self):
        """
        Starts the game loop.
        """
        try:
            while True:
                if self.loop():
                    break
        except KeyboardInterrupt:
            pass
        finally:
            _destroy_window()

    def loop(self) -> Any:
        """
        The overwriting class must define this method.

        Return any value that can be interpreted as True to break the loop.
        :return: True to break the loop.
        """
        raise NotImplementedError("Your game needs to overwrite the loop method.")
