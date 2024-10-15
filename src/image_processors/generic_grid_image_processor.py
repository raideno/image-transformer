from typing import Tuple
from cairo import Context
from abc import ABC, abstractmethod

class GenericGridImageProcessor(ABC):
    @abstractmethod
    def fromPixelCoordinatesToGridCoordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        pass
    
    @abstractmethod
    def fromGridCoordinatesToCenterInPixelCoordinates(self: 'GenericGridImageProcessor', grid_element_position: Tuple[int, ...]) -> Tuple[int, ...]:
        pass
    
    @abstractmethod
    def drawGridElementAt(self: 'GenericGridImageProcessor', context: Context, grid_element_position: Tuple[int, ...], color: Tuple[int, int, int]) -> None:
        pass