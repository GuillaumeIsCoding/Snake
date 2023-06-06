from modules.master.window.master_window_build import MasterWindowBuild
from modules.application.window.window_init import WindowInit
from pygame import display, freetype,Surface

class WindowBuild(MasterWindowBuild):

    """
    
    """

    def __init__(self) -> None:

        """
        
        """
        
        super().__init__()

        WinInit = WindowInit()

        freetype.init()

        self.width, self.height, self.flags, self.isInit = WinInit.__Init__()
    
    def __build__(self) -> tuple[Surface, int, int]:

        """
        
        """

        super().__build__()
        #
        if self.isInit == False:
            #
            display.init()

        #
        window_surface = display.set_mode((self.width,self.height), self.flags)

        return window_surface,self.width,self.height


