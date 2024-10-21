"""
This module provides an implementation of the GenericOutputBuilder interface using the Cairo library to render shapes to an SVG file.
"""

from typing import Tuple

import cairo

import numpy as np

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder

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
        self.surface = cairo.SVGSurface(file_output_path, width, height) # pylint: disable=no-member
        self.context = cairo.Context(self.surface) # pylint: disable=no-member

    def add_polygon(self: 'CairoSvgOutputBuilder', vertices: list[Tuple[float, float]], color: Tuple[int, int, int]):
        """
        Adds a polygon to the Cairo canvas based on the provided vertices and fills it with the specified color.
        
        Parameters:
            vertices (list[Tuple[float, float]]): A list of (x, y) coordinates for the polygon's vertices.
            color (Tuple[int, int, int]): The color of the polygon in RGB format (0-255 for each component).
        """
        if not vertices:
            return

        self.context.move_to(*vertices[0])
        
        for vertex in vertices[1:]:
            self.context.line_to(*vertex)
        
        self.context.close_path()
        
        self.context.set_source_rgb(color[0] / 255, color[1] / 255, color[2] / 255)
        
        self.context.fill_preserve()
        
        self.context.stroke()

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
            x_vertex = x + (size - 1) * np.cos(angle)
            y_vertex = y + (size - 0.5) * np.sin(angle)
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