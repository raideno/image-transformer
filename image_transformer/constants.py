"""
This module defines constants for various image processors, pixel processors, and output builders used in the project.
"""

from image_transformer.output_builders import GenericOutputBuilder, HandmadeSvgOutputBuilder, CairoSvgOutputBuilder

from image_transformer.pixels_processors import RandomPixelsProcessor, AveragePixelsProcessor, MostFrequentPixelsProcessor, GenericPixelsProcessor

from image_transformer.image_processors import TriangleGridImageProcessor, HexagonalGridImageProcessor, SquareGridImageProcessor, GenericGridImageProcessor

image_processors: dict[str, GenericGridImageProcessor] = {
    "hexagonal": HexagonalGridImageProcessor,
    "square": SquareGridImageProcessor,
    "triangle": TriangleGridImageProcessor
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