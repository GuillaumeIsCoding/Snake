from abc import ABC, abstractmethod
from PyQt6 import QtWidgets
from sys import argv

class MasterWindowFrame(ABC):

    @abstractmethod
    def __init__(self) -> None:

        """
        Initialisation de la variable application
        """

        # application object
        self.application = QtWidgets.QApplication(argv)
        
    @abstractmethod
    def __avalaible_dimensions__(self) -> tuple[int,int]:
        
        """
        La fonction retourne un tuple composé des dimensions disponibles lorsque la window n'est pas en FULLSCREEN  \n
        - Largeur -> int                                                                                            \n
        - hauteur -> int                                                                                            \n
        """

    @abstractmethod
    def __maximum_dimensions__(self) -> tuple[int,int]:

        """
        La fonction retourne un tuple composé des dimensions maximal lorsque la window est en FULLSCREEN    \n
        - Largeur -> int                                                                                    \n
        - hauteur -> int                                                                                    \n
        """
        

    @abstractmethod
    def __wrap_dimensions__(self, key) -> tuple[int,int]:
        
        """
        La fonction retourne un tuple issu d'un dictionnaire qui conserve les fonctions     \n
        - __available_dimensions__                                                          \n
            - tuple[int,int]                                                                \n
        - __maximum_dimensions__                                                            \n
            - tuple[int,int]                                                                \n
        Pour accéder aux fonctions il faut une des keys suivantes :                         \n
        - available                                                                         \n
        - maximum                                                                           \n
        
        """
        