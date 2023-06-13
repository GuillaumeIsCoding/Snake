from modules.master.surfaces.master_surface_manager import MasterSurfaceManager
from pygame_gui import UIManager
from pygame import Surface


class SurfaceManager(MasterSurfaceManager):

    def __init__(self, width, height, key) -> None:
        
        super().__init__(width, height, key)

        pass
    
    def build_surface_manager(self) -> tuple[Surface,UIManager]:

        theme_picker = {
            "game_surface"          : "modules/application/surfaces/surfaces_configuration/game.json",
            "menu_surface"          : "modules/application/surfaces/surfaces_configuration/menu.json",
            "score_surface"         : "modules/application/surfaces/surfaces_configuration/score.json",
            "game_upper_surface"    : "modules/application/surfaces/surfaces_configuration/upper_game.json",
            "game_lower_surface"    : "modules/application/surfaces/surfaces_configuration/lower_game.json"
        }

        return Surface((self.width,self.height)), UIManager((self.width,self.height), theme_picker[self.key])           
    
