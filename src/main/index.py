import os
import sys
import cairo

import numpy as np

from image_loader.loader import load_image

from utils.arguments_parser import arguments_parser_factory
from utils.configurations_loader import load_configurations
from utils.arguments_validator import validate_and_parse_arguments

from pixels_processors.random_pixels_processor import RandomPixelsProcessor
from pixels_processors.average_pixels_processor import AveragePixelsProcessor
from pixels_processors.most_frequent_pixels_processor import MostFrequentPixelsProcessor
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

from image_processors.triangle_grid_image_processor import TriangularGridImageProcessor
from image_processors.hexagonal_grid_image_processor import HexagonalGridImageProcessor
from image_processors.square_grid_image_processor import SquareGridImageProcessor
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

image_processors: dict[str, GenericGridImageProcessor] = {
    "triangle": TriangularGridImageProcessor,
    "hexagonal": HexagonalGridImageProcessor,
    "square": SquareGridImageProcessor,
}

pixels_processors: dict[str, GenericPixelsProcessor] = {
    "random": RandomPixelsProcessor,
    "average": AveragePixelsProcessor,
    "most-frequent": MostFrequentPixelsProcessor,
}

CONFIGURATION_FILE_PATH = "configurations.toml"

configurations = load_configurations(CONFIGURATION_FILE_PATH)

def main() -> None:
    
    arguments_parser = arguments_parser_factory(
        image_processors_keys=image_processors.keys(),
        pixels_processors_keys=pixels_processors.keys(),
        configurations=configurations    
    )
    
    raw_arguments = sys.argv[1:]
    
    arguments = validate_and_parse_arguments(
        raw_arguments=raw_arguments,
        arguments_parser=arguments_parser
    )
    
    image_path = arguments.image_path
    image_processor = arguments.grid
    pixels_processor = arguments.pixels
    size = arguments.size
    output_directory = arguments.output_directory
    verbose = arguments.verbose
    
    if verbose:
        print(f"[image-enhancer]: {arguments}")
        print("[image-enhancer]: welcome to the program!")
    
    image = load_image(image_path)
    
    image_file_name = os.path.basename(image_path)
    image_name = os.path.splitext(image_file_name)[0]
    
    image_array = np.array(image)
    
    image_height = image_array.shape[0]
    image_width = image_array.shape[1]
    
    grid_image_processor: GenericGridImageProcessor = image_processors[image_processor](size)
    image_pixels_processor: GenericPixelsProcessor = pixels_processors[pixels_processor]()
    
    grid_elements: dict[tuple[int, int], list[tuple[int, int]]] = {}
    
    # NOTE: image analysis
    for y in range(0, image_height):
        for x in range(0, image_width):
            grid_element_position = grid_image_processor.fromPixelCoordinatesToGridCoordinates(x, y)

            grid_elements.setdefault(grid_element_position, [])
            
            grid_elements[grid_element_position].append((x, y))
                
    if verbose:
        print(f"[image-enhancer](image-width): {image_width}")
        print(f"[image-enhancer](image-height): {image_height}")
        
        print(f"[image-enhancer](number-of-pixels): {image_height * image_width}")
        
        print(f"[image-enhancer](number-of-grid_elements): {len(grid_elements.keys())}")

    image_output_path = os.path.join(output_directory, image_name + ".svg")

    # NOTE: image reconstruction
    with cairo.SVGSurface(image_output_path, image_width, image_height) as surface: 
        context = cairo.Context(surface)
            
        context.set_source_rgb(255, 255, 255)
        context.paint()
        
        for grid_element in grid_elements:
            grid_element_position = grid_element
            
            pixels_coordinates = grid_elements[grid_element_position]
            
            pixels = np.array([image_array[y, x] for x, y in pixels_coordinates])
            
            grid_element_position_on_pixels_plane = grid_image_processor.fromGridCoordinatesToCenterInPixelCoordinates(grid_element_position)
                        
            color = image_pixels_processor.getRGBColorFromPixels(pixels)
            
            grid_image_processor.drawGridElementAt(context, grid_element_position_on_pixels_plane, color)
    
if __name__ == "__main__":
    main()