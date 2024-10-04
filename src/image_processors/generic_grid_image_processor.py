from typing import Tuple
from abc import ABC, abstractmethod

class GenericGridImageProcessor(ABC):
    @abstractmethod
    def convertToGridCoordinatesFromPixelCoordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        pass
    
    @abstractmethod
    def getCoordinatesStartingPosition(self: 'GenericGridImageProcessor', grid_x: int, grid_y: int) -> Tuple[int, ...]:
        pass