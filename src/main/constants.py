"""
This module defines constants for various image processors, pixel processors, and output builders used in the project.
"""

from output_builders.generic_output_builder import GenericOutputBuilder
from output_builders.cairo_svg_output_builder import CairoSvgOutputBuilder
from output_builders.handmade_svg_output_builder import HandmadeSvgOutputBuilder

from pixels_processors.random_pixels_processor import RandomPixelsProcessor
from pixels_processors.average_pixels_processor import AveragePixelsProcessor
from pixels_processors.most_frequent_pixels_processor import MostFrequentPixelsProcessor
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

from image_processors.hexagonal_grid_image_processor import HexagonalGridImageProcessor
from image_processors.square_grid_image_processor import SquareGridImageProcessor
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

image_processors: dict[str, GenericGridImageProcessor] = {
    "hexagonal": HexagonalGridImageProcessor,
    "square": SquareGridImageProcessor,
}

pixels_processors: dict[str, GenericPixelsProcessor] = {
    "random": RandomPixelsProcessor,
    "average": AveragePixelsProcessor,
    "most-frequent": MostFrequentPixelsProcessor,
}

outputs_builders: dict[str, GenericOutputBuilder] = {
    "handmade-svg": HandmadeSvgOutputBuilder,
    "cairo-svg": CairoSvgOutputBuilder
}