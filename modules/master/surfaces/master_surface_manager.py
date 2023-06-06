from abc import ABC, abstractmethod
from pygame import Surface
from pygame_gui import UIManager

class MasterSurfaceManager(ABC):

    """
    
    """

    def __init__(self,width,height,key) -> None:

        """
        
        """
        
        #
        self.width = width
        #
        self.height = height
        #
        self.key = key
    
    @abstractmethod
    def build_surface_manager(self) -> tuple[Surface, UIManager]:
        
        """
        
        """

        pass