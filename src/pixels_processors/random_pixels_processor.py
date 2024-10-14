import numpy as np

from typing import Tuple
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

class RandomPixelsProcessor(GenericPixelsProcessor):
    def getRGBColorFromPixels(self: 'RandomPixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        random_color = tuple(np.random.randint(0, 256, size=3))

        return random_color
