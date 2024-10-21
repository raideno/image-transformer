"""
This module provides the main entry point for the image-transformer program. It parses command-line arguments,
loads an image, processes it using specified image and pixel processors, and outputs the result as an SVG file.
"""

import os
import sys

from importlib import resources

from alive_progress import alive_bar

from image_transformer.constants import image_processors, pixels_processors, outputs_builders

from image_transformer import ImageTransformer

from image_transformer.utils import load_image, arguments_parser_factory, load_configurations, validate_and_parse_arguments

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder

from image_transformer.pixels_processors.generic_pixels_processor import GenericPixelsProcessor

from image_transformer.image_processors.generic_grid_image_processor import GenericGridImageProcessor

CONFIGURATION_FILE_NAME = "configurations.toml"

def main() -> None:
    """
    Main function to run the image-transformer program.
    This function performs the following steps:
    
    1. Parses command-line arguments to get the image path, processors, size, output directory, and verbosity.
    2. Loads the image from the specified path.
    3. Analyzes the image to divide it into grid elements based on the specified grid processor.
    4. Processes the pixels within each grid element using the specified pixel processor.
    5. Outputs the processed image as an SVG file in the specified output directory.
    
    Command-line arguments:
    - image_path: Path to the input image file.
    - grid: Key for the grid image processor to use.
    - pixels: Key for the pixels processor to use.
    - size: Size parameter for the grid image processor.
    - output_directory: Directory to save the output SVG file.
    - verbose: Flag to enable verbose logging.
    
    The function prints various details about the image and processing steps if verbose mode is enabled.
    """
    configurations = None

    with resources.path("image_transformer", CONFIGURATION_FILE_NAME) as configuration_file_path:
        configurations = load_configurations(configuration_file_path)
    
    arguments_parser = arguments_parser_factory(
        image_processors_keys=image_processors.keys(),
        pixels_processors_keys=pixels_processors.keys(),
        outputs_builders_keys=outputs_builders.keys(),
        configurations=configurations    
    )
    
    raw_arguments = sys.argv[1:]
    
    arguments = validate_and_parse_arguments(
        raw_arguments=raw_arguments,
        arguments_parser=arguments_parser
    )
    
    image_path = arguments.image
    image_processor = arguments.grid
    output_builder = arguments.builder
    pixels_processor = arguments.pixels
    size = arguments.size
    output_directory = arguments.output_directory
    verbose = arguments.verbose
    
    image = load_image(image_path)
    
    image_transformer = ImageTransformer.from_pil_image(image)
    
    image_file_name = os.path.basename(image_path)
    image_name = os.path.splitext(image_file_name)[0]
    
    image_output_path = os.path.join(output_directory, image_name + ".svg")
    
    output_builder: GenericOutputBuilder = outputs_builders[output_builder](image.width, image.height, image_output_path)
    grid_image_processor: GenericGridImageProcessor = image_processors[image_processor](size)
    image_pixels_processor: GenericPixelsProcessor = pixels_processors[pixels_processor]()
    
    callback_function = None
    
    # FIX: need to contain the real value
    # NOTE: the number of iterations for the second loop
    number_of_grid_elements = grid_image_processor.approximate_number_of_grid_elements(image.width, image.height)

    if verbose:
        print("[image-transformer]: welcome to the program!")
        print(f"[image-transformer](width): {image.width}")
        print(f"[image-transformer](height): {image.height}")
        print(f"[image-transformer](#pixels): {image.width * image.height}")
    
    with alive_bar(image.width * image.height + number_of_grid_elements, title="[image-transformer](processing)", disable=not verbose) as progress_bar:
        callback_function = lambda step_name, step_size: progress_bar() # pylint: disable=not-callable

        image_transformer.transform_and_save(
            image_processor=grid_image_processor,
            output_builder=output_builder,
            pixels_processor=image_pixels_processor,
            callback=callback_function
        )
    
    output_builder.save()
    
if __name__ == "__main__":
    main()