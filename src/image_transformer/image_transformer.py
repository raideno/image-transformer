"""
This module provides the ImageTransformer class, which is used to transform images using various processors and save the output.
"""

from typing import Any, Callable, Optional

import numpy as np

from PIL import Image

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder
from image_transformer.pixels_processors.generic_pixels_processor import GenericPixelsProcessor
from image_transformer.image_processors.generic_grid_image_processor import GenericGridImageProcessor

class ImageTransformer:    
    """
    A class used to transform images using various processors and save the output.
    """
    
    steps: list[str] = ["step-1", "step-2"]
    
    
    def __init__(self: 'ImageTransformer', image_array: np.ndarray) -> None:
        """
        Constructs all the necessary attributes for the ImageTransformer object.
        
        Parameters:
            image_array (np.ndarray): A numpy array representing the image.
        """
        self.image_array = image_array

    @classmethod
    def from_pil_image(cls, pil_image: Image) -> 'ImageTransformer':
        """
        Class method to create an ImageTransformer instance from a PIL image.
        
        Parameters:
            pil_image (PIL.Image): A PIL image object.
        
        Returns:
            ImageTransformer: An instance of ImageTransformer.
        """
        image_array = np.array(pil_image)
        
        return cls(image_array)
        
    def transform_and_save(
        self: 'ImageTransformer',
        image_processor: GenericGridImageProcessor,
        pixels_processor: GenericPixelsProcessor,
        output_builder: GenericOutputBuilder,
        callback: Optional[Callable[[str, int], None]] = None
    ) -> Any:
        """
        Transforms the image using the provided processors and saves the output.
        
        Parameters:
            image_processor (GenericGridImageProcessor):
                An object responsible for processing the image grid.
            pixels_processor (GenericPixelsProcessor):
                An object responsible for processing the pixels.
            output_builder (GenericOutputBuilder):
                An object responsible for building the output.
            callback (Optional[Callable[[str, int], None]]):
                A callback function to report progress.

        Returns
            Any: The result of the output builder's save method.
        """
        image_height = self.image_array.shape[0]
        image_width = self.image_array.shape[1]
    
        grid_elements: dict[tuple[int, int], list[tuple[int, int]]] = {}
        
        for y in range(0, image_height):
            for x in range(0, image_width):
                grid_element_position = image_processor.from_pixel_coordinates_to_grid_coordinates(x, y)

                grid_elements.setdefault(grid_element_position, [])
                
                grid_elements[grid_element_position].append((x, y))
                
                if callback:
                    callback(ImageTransformer.steps[0], image_height * image_width)
                
        for grid_element in grid_elements:
            grid_element_position = grid_element
            
            pixels_coordinates = grid_elements[grid_element_position]
            
            pixels = np.array([self.image_array[y, x] for x, y in pixels_coordinates])
            
            grid_element_position_on_pixels_plane = image_processor.from_grid_coordinates_to_center_in_pixel_coordinates(grid_element_position)
                        
            color = pixels_processor.get_rgb_color_from_pixels(pixels)
            
            image_processor.draw_grid_element_at(output_builder, grid_element_position_on_pixels_plane, color)

            if callback:
                callback(ImageTransformer.steps[1], len(grid_elements))