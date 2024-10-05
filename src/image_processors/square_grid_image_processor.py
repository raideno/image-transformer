from typing import Tuple
from cairo import Context
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

class SquareGridImageProcessor(GenericGridImageProcessor):
    def __init__(self, square_size: int):
        self.square_size: int = square_size
        self.color_stroke: bool = False
    
    def convertToGridCoordinatesFromPixelCoordinates(self: 'SquareGridImageProcessor', x: int, y: int) -> Tuple[int, ...]:
        square_x_coordinate = (x // self.square_size)
        square_y_coordinate = (y // self.square_size)
        
        return (square_x_coordinate, square_y_coordinate)
    
    def getCoordinatesStartingPosition(self: 'SquareGridImageProcessor', grid_x: int, grid_y: int) -> Tuple[int, ...]:
        return (grid_x * self.square_size, grid_y * self.square_size)

    def drawGridElement(self: 'SquareGridImageProcessor', context: Context, pos_x: int, pos_y: int, color: Tuple[int, int, int]) -> None:
        context.rectangle(pos_x, pos_y, self.square_size, self.square_size)
        context.set_source_rgb(color[0], color[1], color[2])
        context.fill_preserve()
        
        if (self.color_stroke):
            context.set_source_rgb(0, 0, 0)
        
        context.stroke()
        
    def enableStrokeColor(self: 'SquareGridImageProcessor') -> None:
        self.color_stroke = True
        
    def disableStrokeColor(self: 'SquareGridImageProcessor') -> None:
        self.color_stroke = False
        
    def toggleStrokeColor(self: 'SquareGridImageProcessor') -> None:
        self.color_stroke = not self.color_stroke