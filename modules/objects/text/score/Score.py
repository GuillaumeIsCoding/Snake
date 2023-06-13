from pygame_gui.elements import UILabel
from modules.objects.text.text import Text

class Score(Text):

    def __init__(self, surface, width, height, x_pos, y_pos, txt) -> None:
        
        super().__init__(surface, width, height, x_pos, y_pos, txt)
    
    def create_text(self) -> UILabel:
        
        return super().create_text()
