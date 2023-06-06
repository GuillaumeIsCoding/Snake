from abc import ABC, abstractmethod

class MasterWindowOpen(ABC):

    """
    
    """

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def __Open__(self) -> dict:
        pass
