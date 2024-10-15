import cairo

import numpy as np

from typing import Tuple

from output_builders.generic_output_builder import GenericOutputBuilder

class CairoSvgOutputBuilder(GenericOutputBuilder):
    """
    An implementation of ShapeRenderer that uses the Cairo library to render shapes to an SVG file.
    """

    def __init__(self: 'CairoSvgOutputBuilder', width: int, height: int, file_output_path: str):
        """
        Initialize the Cairo canvas with the specified width and height.
        """
        self.width = width
        self.height = height
        # TODO: fix, it creates the file before and then fills it when calling .finish()
        self.surface = cairo.SVGSurface(file_output_path, width, height)
        self.context = cairo.Context(self.surface)

    def add_rectangle(self: 'CairoSvgOutputBuilder', x: int, y: int, size: int, color: Tuple[int, int, int]):
        """
        Add a square to the Cairo canvas at the specified position, size, and color.
        """
        self.context.set_source_rgb(color[0] / 255, color[1] / 255, color[2] / 255)
        self.context.rectangle(x, y, size, size)
        self.context.fill()

    def add_hexagon(self: 'CairoSvgOutputBuilder', x: int, y: int, size: int, color: Tuple[int, int, int]):
        """
        Add a flat-topped hexagon to the Cairo canvas.
        """
        hexagon_vertices = []
        for i in range(6):
            angle = np.pi / 3 * i
            x_vertex = x + size * np.cos(angle)
            y_vertex = y + size * np.sin(angle)
            hexagon_vertices.append((x_vertex, y_vertex))

        self.context.move_to(*hexagon_vertices[0])
        for vertex in hexagon_vertices[1:]:
            self.context.line_to(*vertex)
        self.context.close_path()

        self.context.set_source_rgb(color[0] / 255, color[1] / 255, color[2] / 255)
        self.context.fill_preserve()
        self.context.stroke()

    def save(self: 'CairoSvgOutputBuilder'):
        """
        Save the Cairo canvas to a file with the specified filename.
        """
        self.surface.finish()