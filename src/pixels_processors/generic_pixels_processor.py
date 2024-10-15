"""
This module contains the definition of the GenericPixelsProcessor abstract base class, 
which provides an interface for processing pixel data to extract RGB color information.
"""

import numpy as np

from typing import Tuple
from abc import ABC, abstractmethod

class GenericPixelsProcessor(ABC):
    """
    An abstract base class for processing pixel data to extract RGB color information.
    """

    @abstractmethod
    def getRGBColorFromPixels(self: 'GenericPixelsProcessor', pixels: np.ndarray) -> Tuple[int, int, int]:
        """
        Extracts the RGB color from the given pixel data.

        Parameters:
            pixels (np.ndarray): A numpy array representing the pixel data.

        Returns:
            Tuple[int, int, int]: A tuple containing the RGB color values.
        """
        pass