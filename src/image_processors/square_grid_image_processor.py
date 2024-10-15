from typing import Tuple
from cairo import Context
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

class SquareGridImageProcessor(GenericGridImageProcessor):
    def __init__(self, square_size: int):
        self.square_size: int = square_size
    
    def fromPixelCoordinatesToGridCoordinates(self: 'SquareGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        square_x_coordinate = (x // self.square_size)
        square_y_coordinate = (y // self.square_size)
        
        return (square_x_coordinate, square_y_coordinate)
    
    def fromGridCoordinatesToCenterInPixelCoordinates(self: 'SquareGridImageProcessor', grid_element_position: Tuple[int, int]) -> Tuple[int, ...]:
        grid_x, grid_y = grid_element_position
        
        return (grid_x * self.square_size, grid_y * self.square_size)

    def drawGridElementAt(self: 'SquareGridImageProcessor', context: Context, grid_element_position: Tuple[int, int], color: Tuple[int, int, int]) -> None:
        x, y = grid_element_position
        
        context.rectangle(x, y, self.square_size, self.square_size)
        
        context.set_source_rgb(color[0] / 255, color[1] / 255, color[2] / 255)
        
        context.fill_preserve()
        
        context.stroke()