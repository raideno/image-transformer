import numpy as np

from PIL import Image

from typing import Any, Callable, Optional

from main.constants import image_processors
from main.constants import pixels_processors
from main.constants import outputs_builders

from output_builders.generic_output_builder import GenericOutputBuilder
from pixels_processors.generic_pixels_processor import GenericPixelsProcessor
from image_processors.generic_grid_image_processor import GenericGridImageProcessor


class ImageTransformer:
    def __init__(self: 'ImageTransformer', image_array: np.ndarray) -> None:
        self.image_array = image_array

    @classmethod
    def from_pil_image(cls, pil_image: Image) -> 'ImageTransformer':
        image_array = np.array(pil_image)
        
        return cls(image_array)
        
    def transform_and_save(
        self: 'ImageTransformer',
        image_processor: GenericGridImageProcessor,
        pixels_processor: GenericPixelsProcessor,
        output_builder: GenericOutputBuilder,
        callback: Optional[Callable[[str, int], None]]
    ) -> Any:
        image_height = self.image_array.shape[0]
        image_width = self.image_array.shape[1]
    
        grid_elements: dict[tuple[int, int], list[tuple[int, int]]] = {}
        
        for y in range(0, image_height):
            for x in range(0, image_width):
                grid_element_position = image_processor.fromPixelCoordinatesToGridCoordinates(x, y)

                grid_elements.setdefault(grid_element_position, [])
                
                grid_elements[grid_element_position].append((x, y))
                
                if callback:
                    callback('step-1', image_height * image_width)
                
        for grid_element in grid_elements:
            grid_element_position = grid_element
            
            pixels_coordinates = grid_elements[grid_element_position]
            
            pixels = np.array([self.image_array[y, x] for x, y in pixels_coordinates])
            
            grid_element_position_on_pixels_plane = image_processor.fromGridCoordinatesToCenterInPixelCoordinates(grid_element_position)
                        
            color = pixels_processor.getRGBColorFromPixels(pixels)
            
            image_processor.drawGridElementAt(output_builder, grid_element_position_on_pixels_plane, color)

            if callback:
                callback('step-2', len(grid_elements))