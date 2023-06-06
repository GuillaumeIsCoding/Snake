from pygame import Rect,draw, Color

class Object():

    def __init__(self, pos_x, pos_y, width, height) -> None:

        """
        
        """
        
        #
        self.x = pos_x                                      # default position == between 0 & 640 px
        #
        self.y = pos_y                                      # default position == 0 px
        # 
        self.width = width                                  # default size == 20 px
        #
        self.height = height                                # default size == 20 px
        
    
    def build_bloc(self,surface, color) -> None:

        """
        
        """
        
        #
        self.bloc = draw.rect(surface, Color(color), (self.x, self.y, self.width, self.height))
    
    def destroy_bloc(self) -> None:

        """
        
        """

        #
        del self.bloc
