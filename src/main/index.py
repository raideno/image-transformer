import numpy as np

from image_loader.loader import load_image
from image_processors.square_grid_image_processor import SquareGridImageProcessor

TESTING_IMAGE_PATH = "data/testing-image.jpg"
SQUARE_SIZE = 100

def main():
    print("[image-enhancer]: welcome to the program!")
    
    image = load_image(TESTING_IMAGE_PATH)
    
    image_array = np.array(image)
    
    image_height = image_array.shape[0]
    image_width = image_array.shape[1]
    
    square_grid_image_processor = SquareGridImageProcessor(SQUARE_SIZE)
    
    # TODO: add types
    squares = {}
    
    for y in range(0, image_height):
        for x in range(0, image_width):
            square_grid_x, square_grid_y = square_grid_image_processor.convertToGridCoordinatesFromPixelCoordinates(x, y)
            
            key = f"{square_grid_x}, {square_grid_y}"
            
            if squares.get(key):
                squares[key].append((x, y))
            else:
                squares[key] = [(x, y)]
                
    print(f"[image-enhancer](image-width): {image_width}")
    print(f"[image-enhancer](image-height): {image_height}")
    print(f"[image-enhancer](number-of-squares): {len(squares.keys())}")
    
if __name__ == "__main__":
    main()