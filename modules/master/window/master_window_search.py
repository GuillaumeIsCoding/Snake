from abc import ABC, abstractmethod

class MasterWindowSearch(ABC):

    """
    
    """

    def __init__(self,start, folder, file) -> None:

        """
        Initialisation des arguments suivants :                                             \n
        - start -> directory qui contient la variable folder                                \n
        - folder -> directory qui contient la variable file                                 \n
        - file -> fichier qui devrait contenir les dimensions de l'écran de l'utilisateur   \n
        - realPath -> chemin vers le fichier window_search.py                               \n
        """

        self.start = start
        self.folder = folder
        self.file = file
        
    
    
    @abstractmethod
    def __Search__(self) -> dict:
        pass

    @abstractmethod
    def rebuildPath(self) -> tuple[str,str]:

        """
        La fonction reconstruit les chemins vers :                                                  \n
        - Le folder "configuration"                                                                 \n
        ET                                                                                          \n
        - Le fichier "dimensions.txt"                                                               \n
        La fonction retourne par la suite ses chemins reconstruit dans un tuple contenant 2 string  \n
        - path2folder -> str                                                                        \n
        - path2file -> str                                                                          \n
        """
        
    @abstractmethod
    def isFolderExist(self) -> bool:
        pass

    @abstractmethod
    def isFileExist(self) -> bool:
        pass

    @abstractmethod
    def isConditionsRespected(self) -> bool:
        pass

    @abstractmethod
    def createFolder(self) -> None:
        pass


    

