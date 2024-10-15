"""
A module for generating basic SVG (Scalable Vector Graphics) files. The `SVGBuilder`
class allows you to create an SVG canvas and draw simple shapes, including squares
and flat-topped hexagons. The generated SVG can then be saved to a file.
"""
import numpy as np

from typing import Tuple

from output_builders.generic_output_builder import GenericOutputBuilder

class HandmadeSvgOutputBuilder(GenericOutputBuilder):
    """
    An implementation of GenericSvgBuilder that builds SVG content.

    Allows users to add squares and hexagons to an SVG canvas and save the output as an SVG file.
    """

    def __init__(self: 'HandmadeSvgOutputBuilder', width: int, height: int, file_output_path: str):
        """
        Initialize the SVG canvas with the specified width and height.
        """
        self.width = width
        self.height = height
        self.file_output_path = file_output_path
        self.svg_content = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">']

    def add_rectangle(self: 'HandmadeSvgOutputBuilder', x: int, y: int, size: int, color: Tuple[int, int, int]):
        """
        Add a square to the SVG at the specified position, size, and color.
        """
        rgba_color = f"rgba({color[0]}, {color[1]}, {color[2]})"
        
        square_element = f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{rgba_color}" stroke="none" />'
        
        self.svg_content.append(square_element)

    def add_hexagon(self: 'HandmadeSvgOutputBuilder', x: int, y: int, size: int, color: Tuple[int, int, int]):
        """
        Add a flat-topped hexagon to the SVG at the specified position, size, and colors.
        """
        angles_deg = [0, 60, 120, 180, 240, 300]
        angles_rad = [np.radians(angle) for angle in angles_deg]
        
        points = [
            (
                x + size * np.cos(angle),
                y + size * np.sin(angle)
            )
            for angle in angles_rad
        ]
        
        points_str = ",".join([f"{px} {py}" for px, py in points])
        
        rgba_color = f"rgba({color[0]}, {color[1]}, {color[2]})"
        
        hexagon_element = f'<polygon points="{points_str}" fill="{rgba_color}" stroke="none" />'
        
        self.svg_content.append(hexagon_element)

    def save(self: 'HandmadeSvgOutputBuilder'):
        """
        Save the generated SVG content to a file with the specified filename.
        """
        self.svg_content.append('</svg>')
        with open(self.file_output_path, 'w') as f:
            f.write("\n".join(self.svg_content))
