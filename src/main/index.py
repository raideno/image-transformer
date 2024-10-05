import os
import sys
import cairo 

import numpy as np

from image_loader.loader import load_image

from pixels_processors.average_pixels_processor import AveragePixelsProcessor
from pixels_processors.frequent_pixels_processor import MostFrequentPixelsProcessor
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor

from image_processors.square_grid_image_processor import SquareGridImageProcessor
from image_processors.generic_grid_image_processor import GenericGridImageProcessor

SQUARE_WIDTH = 10

def main():
    print("[image-enhancer]: welcome to the program!")
    
    arguments = sys.argv[1:]
    
    if not arguments:
        print("[image-enhancer](error): no image path provided.")
        sys.exit(1)
    
    image_path = arguments[0]
    
    if not os.path.isfile(image_path):
        print(f"[image-enhancer](error): the provided path '{image_path}' is not a valid file.")
        sys.exit(1)
    
    image = load_image(image_path)
    
    image_file_name = os.path.basename(image_path)
    image_name = os.path.splitext(image_file_name)[0]
    
    image_array = np.array(image)
    
    image_height = image_array.shape[0]
    image_width = image_array.shape[1]
    
    square_grid_image_processor: GenericGridImageProcessor = SquareGridImageProcessor(SQUARE_WIDTH)
    
    squares: dict[tuple[int, int], list[tuple[int, int]]] = {}
    
    average_pixels_processor: GenericPixelsProcessor = AveragePixelsProcessor()
    frequent_pixels_processor: GenericPixelsProcessor = MostFrequentPixelsProcessor()
    
    # NOTE: image analysis
    for y in range(0, image_height):
        for x in range(0, image_width):
            square_grid_x, square_grid_y = square_grid_image_processor.convertToGridCoordinatesFromPixelCoordinates(x, y)
            
            key = (square_grid_x, square_grid_y)
            
            if squares.get(key):
                squares[key].append((x, y))
            else:
                squares[key] = [(x, y)]
                
    print(f"[image-enhancer](image-width): {image_width}")
    print(f"[image-enhancer](image-height): {image_height}")
    
    print(f"[image-enhancer](number-of-pixels): {image_height * image_width}")
    
    print(f"[image-enhancer](number-of-squares): {len(squares.keys())}")

    # NOTE: image reconstruction
    with cairo.SVGSurface(f"{image_name}.svg", image_width, image_height) as surface: 
        context = cairo.Context(surface)
            
        context.set_source_rgb(1, 1, 1)
        context.paint()
        
        context.set_source_rgb(0.2, 0.6, 0.9)
        context.set_line_width(2)
        
        for square in squares:
            square_grid_x, square_grid_y = square
            
            pixels_coordinates = squares[square]
            
            pixels = np.array([image_array[y, x] for x, y in pixels_coordinates])
            
            pos_x, pos_y = square_grid_image_processor.getCoordinatesStartingPosition(square_grid_x, square_grid_y)
            
            color = frequent_pixels_processor.getRGBColorFromPixels(pixels)
            
            square_grid_image_processor.drawGridElement(context, pos_x, pos_y, color)
            
            context.set_source_rgb(0, 0, 0)
            context.stroke()

        surface.write_to_png(f"{image_name}.svg")
    
if __name__ == "__main__":
    main()