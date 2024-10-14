import os
import sys
import cairo 

import numpy as np

from image_loader.loader import load_image

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
    "average": AveragePixelsProcessor,
    "frequent": MostFrequentPixelsProcessor
}

DEFAULT_PIXELS_PROCESSORS = "average"

SQUARE_WIDTH = 25
HEX_SIZE = 4

def main():
    print("[image-enhancer]: welcome to the program!")
    
    arguments = sys.argv[1:]
    
    if not arguments or len(arguments) < 2:
        print("[image-enhancer](error): wrong arguments provided.")
        print("[image-enhancer](error): expected a minimum of 2 arguments, <image-path> <image-processor> [<pixels-processor>]")
        sys.exit(1)
    
    image_path = arguments[0]
    image_processor = arguments[1] or DEFAULT_IMAGE_PROCESSOR
    pixels_processor = arguments[2] if len(arguments) > 2 else DEFAULT_PIXELS_PROCESSORS
    
    if not os.path.isfile(image_path):
        print(f"[image-enhancer](error): the provided path '{image_path}' is not a valid file.")
        sys.exit(1)
    
    if not (image_processor in image_processors.keys()):
        print(f"[image-enhancer](error): '{image_processor}' is not a supported image processor.")
        print(f"[image-enhancer](error): valid image processors are: {", ".join(image_processors.keys())}.")
        sys.exit(1)
        
    if not (pixels_processor in pixels_processors.keys()):
        print(f"[image-enhancer](error): '{pixels_processor}' is not a supported pixels processor.")
        print(f"[image-enhancer](error): valid pixels processors are: {", ".join(pixels_processors.keys())}.")
        sys.exit(1)
    
    image = load_image(image_path)
    
    image_file_name = os.path.basename(image_path)
    image_name = os.path.splitext(image_file_name)[0]
    
    image_array = np.array(image)
    
    image_height = image_array.shape[0]
    image_width = image_array.shape[1]
    
    grid_image_processor: GenericGridImageProcessor = image_processors[image_processor](SQUARE_WIDTH)
    image_pixels_processor: GenericPixelsProcessor = pixels_processors[pixels_processor]()
    
    grid_elements: dict[tuple[int, int], list[tuple[int, int]]] = {}
    
    # NOTE: image analysis
    for y in range(0, image_height):
        for x in range(0, image_width):
            grid_element_x, grid_element_y = grid_image_processor.convertToGridCoordinatesFromPixelCoordinates(x, y)
            
            key = (grid_element_x, grid_element_y)
            
            if grid_elements.get(key):
                grid_elements[key].append((x, y))
            else:
                grid_elements[key] = [(x, y)]
                
    print(f"[image-enhancer](image-width): {image_width}")
    print(f"[image-enhancer](image-height): {image_height}")
    
    print(f"[image-enhancer](number-of-pixels): {image_height * image_width}")
    
    print(f"[image-enhancer](number-of-grid_elements): {len(grid_elements.keys())}")
    
    grid_image_processor.enableStrokeColor()

    # NOTE: image reconstruction
    with cairo.SVGSurface(f"{image_name}.svg", image_width, image_height) as surface: 
        context = cairo.Context(surface)
            
        context.set_source_rgb(1, 1, 1)
        context.paint()
        
        context.set_source_rgb(0.2, 0.6, 0.9)
        context.set_line_width(2)
        
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