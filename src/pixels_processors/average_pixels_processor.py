import numpy as np

from typing import Tuple
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

class AveragePixelsProcessor(GenericPixelsProcessor):
    def getRGBColorFromPixels(self: 'AveragePixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        pass