"""
This module defines the GenericGridImageProcessor abstract base class, which provides an interface
for processing grid-based images. Implementations of this class should provide methods to convert
between pixel and grid coordinates, and to draw grid elements on a given context.
"""

from typing import Tuple
from abc import ABC, abstractmethod

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder

class GenericGridImageProcessor(ABC):
    """
    Abstract base class for processing grid-based images. This class defines the interface
    for converting between pixel and grid coordinates, and for drawing grid elements.
    """

    @abstractmethod
    def from_pixel_coordinates_to_grid_coordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        """
        Convert pixel coordinates to grid coordinates.

        Parameters:
            x (int): The x-coordinate in pixels.
            y (int): The y-coordinate in pixels.

        Returns:
            Tuple[int, ...]: The corresponding grid coordinates.
        """
    
    @abstractmethod
    def from_grid_coordinates_to_center_in_pixel_coordinates(self: 'GenericGridImageProcessor', grid_element_position: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Convert grid coordinates to the center pixel coordinates of the grid element.

        Parameters:
            grid_element_position (Tuple[int, ...]): The position of the grid element in grid coordinates.

        Returns:
            Tuple[int, ...]: The center pixel coordinates of the grid element.
        """
    
    @abstractmethod
    def draw_grid_element_at(self: 'GenericGridImageProcessor', context: GenericOutputBuilder, grid_element_position: Tuple[int, ...], color: Tuple[int, int, int]) -> None:
        """
        Draw a grid element at the specified grid coordinates.

        Parameters:
            context (GenericOutputBuilder): The drawing context.
            grid_element_position (Tuple[int, ...]): The position of the grid element in grid coordinates.
            color (Tuple[int, int, int]): The color to use for drawing the grid element, as an RGB tuple.

        Returns:
            None
        """
    
    @abstractmethod
    def approximate_number_of_grid_elements(self: 'GenericGridImageProcessor', width: int, height: int) -> int:
        """
        Abstract method to approximate the number of grid elements in an image.

        Args:
            width (int): The width of the image.
            height (int): The height of the image.

        Returns:
            int: The approximated number of grid elements.
        """