from pygame_gui.elements import UIButton
from modules.objects.button.button import Button

class QuitButton(Button):
    
    def create_button(self) -> UIButton:
        
        return super().create_button()
    
    def event_handler(self) -> bool:
        
        return True