# NOTE: most helpful "thread": https://gamedev.stackexchange.com/a/61101

import numpy as np

from typing import Tuple
from cairo import Context
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

# NOTE: using offset coordinates - odd-q vertical layout (pointy-topped hexagons)
# NOTE: https://www.redblobgames.com/grids/hexagons/#coordinates-offset

class HexagonalGridImageProcessor(GenericGridImageProcessor):
    def __init__(self, hexagon_size: int):
        self.hexagon_size = hexagon_size

    def fromPixelCoordinatesToGridCoordinates(self: 'HexagonalGridImageProcessor', x: int, y: int) -> Tuple[int, int]:
        # NOTE: https://www.redblobgames.com/grids/hexagons/#pixel-to-hex

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

    def fromGridCoordinatesToCenterInPixelCoordinates(self: 'HexagonalGridImageProcessor', grid_element_position: Tuple[int, int]) -> Tuple[int, int]:
        # NOTE: https://www.redblobgames.com/grids/hexagons/#pixel-to-hex
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
    
    def drawGridElementAt(self: 'HexagonalGridImageProcessor', context: Context, grid_element_position: Tuple[int, int], color: Tuple[int, int, int]) -> None:
        q, r = grid_element_position
        
        hexagon_vertices = self.__calculate_hexagon_vertices(q, r, self.hexagon_size)

        self.__draw_hexagon(context, hexagon_vertices)

        context.set_source_rgb(color[0] / 255, color[1] / 255, color[2] / 255)
        context.fill_preserve()
        
        context.stroke()
    
    @staticmethod
    def __draw_hexagon(context: Context, hexagon_vertices: list[Tuple[float, float]]):
        context.move_to(*hexagon_vertices[0])
        
        for vertex in hexagon_vertices[1:]:
            context.line_to(*vertex)
        context.close_path()
    
    @staticmethod
    def __calculate_hexagon_vertices(q: int, r: int, hexagon_size: int) -> list[Tuple[float, float]]:
        hexagon_vertices = []
        for i in range(6):
            angle = np.pi / 3 * i
            x_vertex = q + hexagon_size * np.cos(angle)
            y_vertex = r + hexagon_size * np.sin(angle)
            hexagon_vertices.append((x_vertex, y_vertex))
        return hexagon_vertices