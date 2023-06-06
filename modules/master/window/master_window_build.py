from abc import ABC, abstractmethod
from pygame import Surface

class MasterWindowBuild(ABC):

    """
    
    """

    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def __build__(self) -> tuple[Surface, int, int]:
        pass