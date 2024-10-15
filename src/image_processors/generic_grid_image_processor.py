"""
This module defines the GenericGridImageProcessor abstract base class, which provides an interface
for processing grid-based images. Implementations of this class should provide methods to convert
between pixel and grid coordinates, and to draw grid elements on a given context.
"""

from typing import Tuple
from cairo import Context
from abc import ABC, abstractmethod

class GenericGridImageProcessor(ABC):
    """
    Abstract base class for processing grid-based images. This class defines the interface
    for converting between pixel and grid coordinates, and for drawing grid elements.
    """

    @abstractmethod
    def fromPixelCoordinatesToGridCoordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        """
        Convert pixel coordinates to grid coordinates.

        Parameters:
            x (int): The x-coordinate in pixels.
            y (int): The y-coordinate in pixels.

        Returns:
            Tuple[int, ...]: The corresponding grid coordinates.
        """
        pass
    
    @abstractmethod
    def fromGridCoordinatesToCenterInPixelCoordinates(self: 'GenericGridImageProcessor', grid_element_position: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Convert grid coordinates to the center pixel coordinates of the grid element.

        Parameters:
            grid_element_position (Tuple[int, ...]): The position of the grid element in grid coordinates.

        Returns:
            Tuple[int, ...]: The center pixel coordinates of the grid element.
        """
        pass
    
    @abstractmethod
    def drawGridElementAt(self: 'GenericGridImageProcessor', context: Context, grid_element_position: Tuple[int, ...], color: Tuple[int, int, int]) -> None:
        """
        Draw a grid element at the specified grid coordinates.

        Parameters:
            context (Context): The drawing context.
            grid_element_position (Tuple[int, ...]): The position of the grid element in grid coordinates.
            color (Tuple[int, int, int]): The color to use for drawing the grid element, as an RGB tuple.

        Returns:
            None
        """
        pass