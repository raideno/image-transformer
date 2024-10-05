from typing import Tuple
from cairo import Context
from abc import ABC, abstractmethod

class GenericGridImageProcessor(ABC):
    @abstractmethod
    def convertToGridCoordinatesFromPixelCoordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        pass
    
    @abstractmethod
    def getCoordinatesStartingPosition(self: 'GenericGridImageProcessor', grid_x: int, grid_y: int) -> Tuple[int, ...]:
        pass
    
    @abstractmethod
    def drawGridElement(self: 'GenericGridImageProcessor', context: Context, pos_x: int, pos_y: int, color: Tuple[int, int, int]) -> None:
        pass