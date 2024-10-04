from typing import Tuple
from abc import ABC, abstractmethod

class GenericGridImageProcessor(ABC):
    @abstractmethod
    def convertToGridCoordinatesFromPixelCoordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        pass