from abc import ABC, abstractmethod
from pygame_gui.elements import UITextBox
from pygame import Rect

class Text(ABC):

    def __init__(self, surface, width, height, x_pos, y_pos, txt) -> None:
        
        """
        Initialisation des attributs de la classe Text
        """

        self.surface = surface
        self.width = width
        self.height = height
        self.txt = txt
        self.x = x_pos
        self.y = y_pos

    @abstractmethod
    def create_text(self) -> UITextBox:

        """
        Retourne un textbox creer et initialisé
        """

        self.text = UITextBox(relative_rect=Rect((self.x,self.y),(self.height,self.width)),
                              manager = self.surface,
                              html_text= self.text)
        return self.text
    