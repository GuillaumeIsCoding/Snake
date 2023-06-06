from modules.master.window.master_window_search import MasterWindowSearch
from modules.application.window.window_save import WindowSave
from modules.application.window.window_open import WindowOpen
from os import path, mkdir

class WindowSearch(MasterWindowSearch):

    """
    
    """
    
    def __init__(self, start="", folder="", file="") -> None:

        super().__init__(start, folder, file)

        #
        self.realPath = path.realpath(__file__)         # Nous avons besoins d'enlever  "window_search.py from path"

    def rebuildPath(self) -> tuple[str, str]:

        super().rebuildPath()

        #
        path2list = self.realPath.split("\\")           # Nous avons besoins de split le chemin pour le reconstruire  
        #
        newpath = "{}".format(path2list[0])
        # counting variable
        indice = 0

        # rebuild loop
        while path2list[indice] < self.start:
            
            # Takes old "newpath" and add \\ + path2list[indice]
            newpath = "{}\{}".format(newpath, path2list[indice + 1])

            # add 1 to indice
            indice = indice + 1
        
        # Creates path to saving folder
        path2folder = "{}\\{}".format(newpath,self.folder)
        # Creates path to saving file
        path2file = "{}\\{}".format(path2folder,self.file)

        # 
        return (path2folder,path2file)
    
    def isFolderExist(self,path2folder) -> bool:

        """
        
        """

        super().isFolderExist()

        # returns True or False
        return path.exists(path2folder)

    def isFileExist(self, path2file) -> bool:

        """
        
        """
        
        super().isFileExist()

        # returns True or False
        return path.exists(path2file)
    
    def isConditionsRespected(self) -> bool:

        """
        
        """
        
        super().isConditionsRespected()

        # path
        path = self.rebuildPath()

        return [self.isFolderExist(self.rebuildPath()[0]),self.isFileExist(self.rebuildPath()[1])]
    
    def createFolder(self) -> None:
        
        super().createFolder()

        mkdir(self.rebuildPath()[0])

    def __Search__(self) -> dict:
        
        if not all(self.isConditionsRespected()):
            #
            try:
                self.createFolder()     
            #
            except:
                #
                pass
            #
            return WindowSave(self.rebuildPath()[1]).__Save__()
        else:
            #
            return WindowOpen(self.rebuildPath()[1]).__Open__()
            

            


        
            


