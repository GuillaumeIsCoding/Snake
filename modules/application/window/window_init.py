from modules.master.window.master_window_init import MasterWindowInit
from modules.application.window.window_search import WindowSearch
from pygame.display import get_init, init
from pygame import FULLSCREEN

class WindowInit(MasterWindowInit):

    """
    
    """
    
    def __init__(self) -> None:

        """
        
        """
        
        super().__init__()

        #
        self.WinSearchDict = WindowSearch("window","configuration","dimensions.txt").__Search__()

    
    def __Init__(self) -> tuple[int, int, int, bool]:
        
        """
        
        """
        
        super().__Init__()

        #
        if get_init() == False:
            
            #
            init()

        #
        flags = FULLSCREEN

        #
        width,height = (int(self.WinSearchDict["maximum_width"]), int(self.WinSearchDict["maximum_height"]))

        #
        return width, height, flags, get_init()
