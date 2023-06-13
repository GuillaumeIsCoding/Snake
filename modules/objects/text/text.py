from abc import ABC, abstractmethod
from pygame_gui.elements import UILabel
from pygame import Rect

class Text(ABC):

    def __init__(self, surface, width, height, x_pos, y_pos, txt) -> None:
        
        """
        Initialisation des attributs de la classe Text
        """

        self.surface = surface
        self.width = width
        self.height = height
        self.txt = str(txt)
        self.x = x_pos
        self.y = y_pos

    @abstractmethod
    def create_text(self) -> UILabel:

        """
        Retourne un textbox creer et initialisé
        """

        self.label = UILabel(relative_rect=Rect((self.x,self.y),(self.width,self.height)),
                             manager = self.surface,
                             text = self.txt)
        return self.label
    