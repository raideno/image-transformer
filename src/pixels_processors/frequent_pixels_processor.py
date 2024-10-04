import numpy as np
from collections import Counter
from typing import Tuple
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

class MostFrequentPixelsProcessor(GenericPixelsProcessor):
    def getRGBColorFromPixels(self: 'MostFrequentPixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        pixels_as_tuples = [tuple(pixel) for pixel in pixels]
        
        most_common_pixel = Counter(pixels_as_tuples).most_common(1)[0][0]
        
        return most_common_pixel
