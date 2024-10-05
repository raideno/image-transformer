from typing import Tuple
from cairo import Context
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

class SquareGridImageProcessor(GenericGridImageProcessor):
    def __init__(self, square_size: int):
        self.square_size = square_size
    
    def convertToGridCoordinatesFromPixelCoordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        square_x_coordinate = (x // self.square_size)
        square_y_coordinate = (y // self.square_size)
        
        return (square_x_coordinate, square_y_coordinate)
    
    def getCoordinatesStartingPosition(self: 'GenericGridImageProcessor', grid_x: int, grid_y: int) -> Tuple[int, ...]:
        return (grid_x * self.square_size, grid_y * self.square_size)

    def drawGridElement(self: 'GenericGridImageProcessor', context: Context, pos_x: int, pos_y: int, color: Tuple[int, int, int]) -> None:
        context.rectangle(pos_x, pos_y, self.square_size, self.square_size)
        context.set_source_rgb(color[0], color[1], color[2])
        context.fill_preserve()