from abc import ABC, abstractmethod

class MasterWindowSave(ABC):

    """
    
    """

    def __init__(self,file) -> None:
        self.file = file
    
    @abstractmethod
    def __Save__(self) -> dict:
        pass