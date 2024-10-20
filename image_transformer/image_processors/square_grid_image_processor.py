"""
This module contains the SquareGridImageProcessor class, which is used to process images by dividing them into a grid of squares.
"""

from typing import Tuple

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder
from image_transformer.image_processors.generic_grid_image_processor import GenericGridImageProcessor

class SquareGridImageProcessor(GenericGridImageProcessor):
    """
    A class to process images by dividing them into a grid of squares.
    """
    
    def __init__(self, square_size: int):
        """
        Initializes the SquareGridImageProcessor with the given square size.
        
        Parameters:
            square_size (int): The size of each square in the grid.
        """
        self.square_size: int = square_size
    
    def from_pixel_coordinates_to_grid_coordinates(self: 'SquareGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        """
        Converts pixel coordinates to grid coordinates.
        
        Parameters:
            x (int): The x-coordinate in pixels.
            y (int): The y-coordinate in pixels.
        
        Returns:
            Tuple[int, ...]: The grid coordinates as a tuple (grid_x, grid_y).
        """
        square_x_coordinate = (x // self.square_size)
        square_y_coordinate = (y // self.square_size)
        
        return (square_x_coordinate, square_y_coordinate)
    
    def from_grid_coordinates_to_center_in_pixel_coordinates(self: 'SquareGridImageProcessor', grid_element_position: Tuple[int, int]) -> Tuple[int, ...]:
        """
        Converts grid coordinates to the center pixel coordinates of the grid element.
        
        Parameters:
            grid_element_position (Tuple[int, int]): The position of the grid element as a tuple (grid_x, grid_y).
        
        Returns:
            Tuple[int, ...]: The center pixel coordinates as a tuple (center_x, center_y).
        """
        grid_x, grid_y = grid_element_position
        
        return (grid_x * self.square_size, grid_y * self.square_size)

    def draw_grid_element_at(self: 'SquareGridImageProcessor', context: GenericOutputBuilder, grid_element_position: Tuple[int, int], color: Tuple[int, int, int]) -> None:
        """
        Draws a grid element at the specified position with the given color.
        
        Parameters:
            context (Context): The Cairo context to draw on.
            grid_element_position (Tuple[int, int]): The position of the grid element as a tuple (grid_x, grid_y).
            color (Tuple[int, int, int]): The color of the grid element as a tuple (r, g, b).
        """
        x, y = grid_element_position
        
        context.add_rectangle(x, y, self.square_size, color)
        
    def approximate_number_of_grid_elements(self: 'GenericGridImageProcessor', width: int, height: int) -> int:
        """
        Approximates the number of grid elements that can fit in the given width and height.
        
        Parameters:
            width (int): The width of the area in pixels.
            height (int): The height of the area in pixels.
        
        Returns:
            int: The approximate number of grid elements.
        """
        num_elements_x = width // self.square_size
        num_elements_y = height // self.square_size
        
        return num_elements_x * num_elements_y