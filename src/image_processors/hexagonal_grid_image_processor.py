"""
This module provides functionality to process images using a hexagonal grid layout.
It includes methods to convert between pixel and grid coordinates, draw grid elements,
and calculate hexagon vertices.
"""

import numpy as np

from typing import Tuple

from output_builders.generic_output_builder import GenericOutputBuilder
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

# NOTE: using offset coordinates - odd-q vertical layout (pointy-topped hexagons)
# NOTE: https://www.redblobgames.com/grids/hexagons/#coordinates-offset

class HexagonalGridImageProcessor(GenericGridImageProcessor):
    """
    A class to process images using a hexagonal grid layout.
    """
    
    def __init__(self, hexagon_size: int):
        """
        Initializes the HexagonalGridImageProcessor with the given hexagon size.
        
        Parameters:
            hexagon_size (int): The size of the hexagons in the grid.
        """
        self.hexagon_size = hexagon_size

    def fromPixelCoordinatesToGridCoordinates(self, x: int, y: int) -> Tuple[int, int]:
        # NOTE: https://www.redblobgames.com/grids/hexagons/#pixel-to-hex
        """
        Converts pixel coordinates to grid coordinates.
        
        Parameters:
            x (int): The x-coordinate in pixels.
            y (int): The y-coordinate in pixels.
        
        Returns:
            Tuple[int, int]: The corresponding grid coordinates (q, r).
        """
        pixel_matrix = np.matrix([
            [x],
            [y],
        ])
        
        conversion_matrix = np.matrix([
            [2 / 3, 0],
            [-1 / 3, np.sqrt(3) / 3],
        ])
        
        result = conversion_matrix @ pixel_matrix / self.hexagon_size
        
        q = int(round(result[0, 0]))
        r = int(round(result[1, 0]))

        return (q, r)

    def fromGridCoordinatesToCenterInPixelCoordinates(self, grid_element_position: Tuple[int, int]) -> Tuple[int, int]:
        # NOTE: https://www.redblobgames.com/grids/hexagons/#pixel-to-hex
        """
        Converts grid coordinates to the center pixel coordinates.
        
        Parameters:
            grid_element_position (Tuple[int, int]): The grid coordinates (q, r).
        
        Returns:
            Tuple[int, int]: The corresponding center pixel coordinates (x, y).
        """
        q, r = grid_element_position
        
        conversion_matrix = np.matrix([
            [3/2, 0],
            [np.sqrt(3) / 2, np.sqrt(3)],
        ])
        
        coordinates_matrix = np.matrix([
            [q],
            [r],
        ])
        
        result = np.round(self.hexagon_size * conversion_matrix @ coordinates_matrix).astype(int)

        return (result[0, 0], result[1, 0])
    
    def drawGridElementAt(self, context: GenericOutputBuilder, grid_element_position: Tuple[int, int], color: Tuple[int, int, int]) -> None:
        """
        Draws a hexagonal grid element at the specified grid coordinates.
        
        Parameters:
            context (GenericOutputBuilder): The Cairo context to draw on.
            grid_element_position (Tuple[int, int]): The grid coordinates (q, r).
            color (Tuple[int, int, int]): The color of the hexagon in RGB format.
        """
        q, r = grid_element_position
        
        context.add_hexagon(q, r, self.hexagon_size, color)
        
    def approximateNumberOfGridElements(self: 'GenericGridImageProcessor', width: int, height: int) -> int:
        """
        Approximates the number of hexagonal grid elements that can fit in the given width and height.
        
        Parameters:
            width (int): The width of the area in pixels.
            height (int): The height of the area in pixels.
        
        Returns:
            int: The approximate number of hexagonal grid elements.
        """
        hex_height = np.sqrt(3) * self.hexagon_size
        hex_width = 2 * self.hexagon_size
        
        num_hexagons_width = width / (3/2 * self.hexagon_size)
        num_hexagons_height = height / hex_height
        
        return int(num_hexagons_width * num_hexagons_height)