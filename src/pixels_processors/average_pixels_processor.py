import numpy as np

from typing import Tuple
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

class AveragePixelsProcessor(GenericPixelsProcessor):
    def getRGBColorFromPixels(self: 'AveragePixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        avg_color = np.mean(pixels, axis=0)
        avg_color = tuple(avg_color.astype(int))
        
        return avg_color