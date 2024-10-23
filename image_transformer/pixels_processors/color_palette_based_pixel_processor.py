"""
This module contains the AveragePixelsProcessor class which is used to calculate
the average RGB color from a given set of pixels.
"""

from typing import Tuple

import numpy as np

from image_transformer.pixels_processors.generic_pixels_processor import GenericPixelsProcessor

# TO-READ: https://sighack.com/post/averaging-rgb-colors-the-right-way

class ColorPaletteBasedPixelProcessor(GenericPixelsProcessor):
    """
    A class used to process pixels and calculate the average RGB color.
    """
    
    def __init__(self: 'ColorPaletteBasedPixelProcessor', colors: list[Tuple[int, int, int]]):
        self.colors = colors

    def get_rgb_color_from_pixels(self: 'ColorPaletteBasedPixelProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        """
        Calculates the average RGB color from the given pixels.

        Parameters:
            pixels (np.ndarray): A numpy array of pixels from which the average color is to be calculated.

        Returns:
            Tuple[int, int, int]
                A tuple representing the average RGB color.
        """
        index = np.random.randint(0, len(self.colors))
        return self.colors[index]