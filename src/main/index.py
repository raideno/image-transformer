import os
import sys
import cairo 

import argparse

import numpy as np

from image_loader.loader import load_image

from pixels_processors.random_pixels_processor import RandomPixelsProcessor
from pixels_processors.average_pixels_processor import AveragePixelsProcessor
from pixels_processors.frequent_pixels_processor import MostFrequentPixelsProcessor
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

from image_processors.hex_grid_image_processor import HexGridImageProcessor
from image_processors.square_grid_image_processor import SquareGridImageProcessor
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

image_processors: dict[str, GenericGridImageProcessor] = {
    "hexagonal": HexGridImageProcessor,
    "square": SquareGridImageProcessor,
}

DEFAULT_IMAGE_PROCESSOR = "hexagonal"

pixels_processors: dict[str, GenericPixelsProcessor] = {
    "random": RandomPixelsProcessor,
    "average": AveragePixelsProcessor,
    "frequent": MostFrequentPixelsProcessor,
}

DEFAULT_PIXELS_PROCESSORS = "average"

DEFAULT_SIZE = 10

def main():
    parser = argparse.ArgumentParser(
        prog="Image Enhancer",
        description="Transform your images into svg",
    )

    parser.add_argument("image_path", type=str)
    parser.add_argument("-g", "--grid", type=str, choices=image_processors.keys(), default=DEFAULT_IMAGE_PROCESSOR)
    parser.add_argument("-p", "--pixels", type=str, choices=pixels_processors.keys(), default=DEFAULT_PIXELS_PROCESSORS)
    parser.add_argument("-s", "--size", type=int, default=DEFAULT_SIZE)
    
    raw_arguments = sys.argv[1:]
    
    arguments = parser.parse_args(raw_arguments)
    
    image_path = arguments.image_path
    image_processor = arguments.grid
    pixels_processor = arguments.pixels
    size = arguments.size
    
    print(f"[image-enhancer]: {arguments}")
    
    if size < 1 or size > 100:
        print(f"[image-enhancer](error): the size '{size}' is not valid. It must be between 1 and 100.")
        sys.exit(1)
    
    if not os.path.isfile(image_path):
        print(f"[image-enhancer](error): the provided path '{image_path}' is not a valid file.")
        sys.exit(1)
        
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
            key = grid_image_processor.convertToGridCoordinatesFromPixelCoordinates(x, y)

            grid_elements.setdefault(key, []).append((x, y))
                
    print(f"[image-enhancer](image-width): {image_width}")
    print(f"[image-enhancer](image-height): {image_height}")
    
    print(f"[image-enhancer](number-of-pixels): {image_height * image_width}")
    
    print(f"[image-enhancer](number-of-grid_elements): {len(grid_elements.keys())}")
    
    grid_image_processor.enableStrokeColor()

    # NOTE: image reconstruction
    with cairo.SVGSurface(f"{image_name}.svg", image_width, image_height) as surface: 
        context = cairo.Context(surface)
            
        context.set_source_rgb(255, 255, 255)
        context.paint()
        
        for grid_element in grid_elements:
            grid_element_x, grid_element_y = grid_element
            
            pixels_coordinates = grid_elements[grid_element]
            
            pixels = np.array([image_array[y, x] for x, y in pixels_coordinates])
            
            pos_x, pos_y = grid_image_processor.getCoordinatesStartingPosition(grid_element_x, grid_element_y)
                        
            color = image_pixels_processor.getRGBColorFromPixels(pixels)
            
            grid_image_processor.drawGridElement(context, pos_x, pos_y, color)

        surface.write_to_png(f"{image_name}.svg")
    
if __name__ == "__main__":
    main()