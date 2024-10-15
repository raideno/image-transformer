"""
This module contains the RandomPixelsProcessor class, which is used to generate random RGB colors from pixel data.
"""

import numpy as np

from typing import Tuple
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

class RandomPixelsProcessor(GenericPixelsProcessor):
    """
    A processor that generates random RGB colors from pixel data.
    """

    def getRGBColorFromPixels(self: 'RandomPixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        """
        Generate a random RGB color.

        Parameters:
            pixels (np.ndarray): The pixel data from which to generate the color.

        Returns:
            Tuple[int, int, int]: A tuple representing the RGB color.
        """
        random_color = tuple(np.random.randint(0, 256, size=3))
        return random_color
