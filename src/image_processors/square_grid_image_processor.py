from typing import Tuple
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