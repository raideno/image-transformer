import numpy as np

from typing import Tuple
from abc import ABC, abstractmethod

class GenericPixelsProcessor(ABC):
    @abstractmethod
    def getRGBColorFromPixels(self: 'GenericPixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        pass