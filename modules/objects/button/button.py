from abc import ABC, abstractmethod
from pygame_gui.elements import UIButton
from pygame import Rect

class Button(ABC):
    
    def __init__(self, surface, width, height, x_pos, y_pos, txt) -> None:
        
        """
        Initialisation des attributs de la classe Button
        """

        self.surface = surface
        self.width = width
        self.height = height
        self.txt = txt
        self.x = x_pos
        self.y = y_pos
    
    @abstractmethod
    def create_button(self) -> UIButton:
        
        """
        Retourne un bouton creer et initialisé
        """

        btn = UIButton(relative_rect= Rect((self.x,self.y),(self.height,self.width)),
                       manager = self.surface,
                       text = self.txt)

        return btn
    
    @abstractmethod
    def event_handler(self) -> bool:
        
        """
        Tout les événements se passent ici
        """
        pass

    def destroy_handler(self, btn) -> None:
        
        """
        Destruction du bouton
        """

        btn.kill()