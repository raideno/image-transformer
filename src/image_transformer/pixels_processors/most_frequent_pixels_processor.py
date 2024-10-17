"""
This module contains the MostFrequentPixelsProcessor class, which is used to process an array of pixels
and determine the most frequently occurring RGB color.
"""


from typing import Tuple
from collections import Counter

import numpy as np

from image_transformer.pixels_processors.generic_pixels_processor import GenericPixelsProcessor


class MostFrequentPixelsProcessor(GenericPixelsProcessor):
    """
    A processor that identifies the most frequent RGB color from a given array of pixels.
    """
    
    def get_rgb_color_from_pixels(self: 'MostFrequentPixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        """
        Determines the most frequent RGB color from the provided array of pixels.

        Parameters:
            pixels (np.ndarray): A numpy array of pixels where each pixel is represented as an array of RGB values.

        Returns:
            Tuple[int, int, int]: The most frequently occurring RGB color as a tuple.
        """
        pixels_as_tuples = [tuple(pixel) for pixel in pixels]
        
        most_common_pixel = Counter(pixels_as_tuples).most_common(1)[0][0]
        
        return most_common_pixel
