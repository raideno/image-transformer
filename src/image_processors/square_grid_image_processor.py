from typing import Tuple
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

class SquareGridImageProcessor(GenericGridImageProcessor):
    def __init__(self, square_size: int):
        self.square_size = square_size
    
    def convertToGridCoordinatesFromPixelCoordinates(self: 'GenericGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        return (x, y)