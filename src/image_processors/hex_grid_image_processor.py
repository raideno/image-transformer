# NOTE: most helpful "thread": https://gamedev.stackexchange.com/a/61101

import numpy as np

from typing import Tuple
from cairo import Context
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

# NOTE: using offset coordinates - odd-q vertical layout (pointy-topped hexagons)
# NOTE: https://www.redblobgames.com/grids/hexagons/#coordinates-offset

class HexGridImageProcessor(GenericGridImageProcessor):
    def __init__(self, hex_size: int):
        self.hex_size = hex_size
        self.color_stroke: bool = False

    def convertToGridCoordinatesFromPixelCoordinates(self: 'HexGridImageProcessor', x: int, y: int) -> Tuple[int, int]:
        # NOTE: https://www.redblobgames.com/grids/hexagons/#hex-to-pixel-offset
        q = int(round((2 / 3 * x) / self.hex_size))
        r = int(round((-1 / 3 * x + np.sqrt(3) / 3 * y) / self.hex_size))
        # r = int(round((y - (q % 2) * (self.hex_size * np.sqrt(3) / 2)) / (self.hex_size * np.sqrt(3))))

        return (q, r)

    def getCoordinatesStartingPosition(self: 'HexGridImageProcessor', grid_x: int, grid_y: int) -> Tuple[int, int]:
        # NOTE: https://www.redblobgames.com/grids/hexagons/#pixel-to-hex
        conversion_matrix = np.matrix([
            [3/2, 0],
            [np.sqrt(3) / 2, np.sqrt(3)],
        ])
        
        coordinates_matrix = np.matrix([
            [grid_x],
            [grid_y],
        ])
        
        result = self.hex_size * conversion_matrix @ coordinates_matrix

        return int(result[0, 0]), int(result[1, 0])
    
    def drawGridElement(self: 'HexGridImageProcessor', context: Context, pos_x: int, pos_y: int, color: Tuple[int, int, int]) -> None:
        hexagon_vertices = []
        for i in range(6):
            angle = np.pi / 3 * i  # 60-degree increments (for pointy-topped hexagons)
            x_vertex = pos_x + self.hex_size * np.cos(angle)
            y_vertex = pos_y + self.hex_size * np.sin(angle)
            hexagon_vertices.append((x_vertex, y_vertex))

        # Draw the hexagon using the calculated vertices
        context.move_to(*hexagon_vertices[0])
        for vertex in hexagon_vertices[1:]:
            context.line_to(*vertex)
        context.close_path()  # Close the hexagon shape

        # Set the fill color and stroke the outline
        context.set_source_rgb(color[0] / 255, color[1] / 255, color[2] / 255)  # Normalize to [0, 1] for Cairo
        context.fill_preserve()
        context.stroke()
        
    def enableStrokeColor(self: 'HexGridImageProcessor') -> None:
        self.color_stroke = True
        
    def disableStrokeColor(self: 'HexGridImageProcessor') -> None:
        self.color_stroke = False
        
    def toggleStrokeColor(self: 'HexGridImageProcessor') -> None:
        self.color_stroke = not self.color_stroke