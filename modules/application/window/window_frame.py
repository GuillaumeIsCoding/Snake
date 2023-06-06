from modules.master.window.master_window_frame import MasterWindowFrame

class WindowFrame(MasterWindowFrame):

    """
    La classe retourne les dimensions de l'écran lorsque :      \n
    Le jeu est ouvert pour la première fois                     \n
    OU                                                          \n
    Manque les éléments suivants :                              \n
    - le folder "configuration"                                 \n
    - le fichier "dimensions.txt"                               \n

    """


    def __init__(self) -> None:
        super().__init__()

    def __avalaible_dimensions__(self) -> tuple[int, int]:
        
        super().__avalaible_dimensions__()

        # Screen -> QScreen
        screen = self.application.primaryScreen()
        # Available_dimensions -> QRect
        available_dimensions = screen.availableGeometry()
        # Retourne tuple[int, int]
        return (available_dimensions.width(), available_dimensions.height())
    
    def __maximum_dimensions__(self) -> tuple[int, int]:
    
        super().__maximum_dimensions__()

        # Screen -> QScreen
        screen = self.application.primaryScreen()
        # Maximum_dimensions -> QSize
        maximum_dimensions = screen.size()
        # Retourne tuple[int, int]
        return (maximum_dimensions.width(), maximum_dimensions.height())
    
    def __wrap_dimensions__(self, key="maximum") -> tuple[int, int]:

        super().__wrap_dimensions__(key)

        # Dictionnaire contenant les fonctions pour déterminer les dimensions de l'écran de l'utilisateur 
        dimensions_dict = {
            "available" : self.__avalaible_dimensions__(),
            "maximum"   : self.__maximum_dimensions__()
        }
        # Retourne un tuple[int, int] 
        return dimensions_dict[key]


        

