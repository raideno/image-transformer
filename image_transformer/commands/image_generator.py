"""
This module provides a command-line interface (CLI) command for generating images with specified dimensions, colors, and processing options.
The command is created using the Click library and allows users to specify various parameters for image generation.
"""

import os
import click

import numpy as np

from alive_progress import alive_bar

from image_transformer.utils import ClickColor, hex_to_rgb_color_converter

from image_transformer import ImageTransformer, image_processors, outputs_builders

from image_transformer.commands.helpers import helpers

from image_transformer.image_processors import GenericGridImageProcessor
from image_transformer.pixels_processors import GenericPixelsProcessor, ColorPaletteBasedPixelProcessor
from image_transformer.output_builders import GenericOutputBuilder

GENERATED_IMAGE_NAME = "result"

def image_generator_command_factory(
    configurations: dict,
    image_processors_keys: list[str],
    _pixels_processors_keys: list[str],
    outputs_builders_keys: list[str]
):
    """
    Factory function to create the image generator command.

    Parameters:
        configurations (dict): Configuration dictionary containing default values for the command options.
        image_processors_keys (list[str]): List of available image processor keys.
        pixels_processors_keys (list[str]): List of available pixels processor keys.
        outputs_builders_keys (list[str]): List of available output builder keys.

    Returns:
        function: The image generator command function.
    """
    @click.command(
        name="generate",
        help="Generate an image with specified dimensions, colors, and processing options."
    )
    @click.option(
        '--width',
        type=click.INT,
        required=True,
        help=helpers["image_generator_command"]["--width"],
        default=configurations["defaults"]["width"]
    )
    @click.option('--height',
        type=click.INT,
        required=True,
        help=helpers["image_generator_command"]["--height"],
        default=configurations["defaults"]["height"]
    )
    @click.option('--hex-color',
        type=ClickColor(),
        multiple=True,
        required=True,
        help=helpers["image_generator_command"]["--hex-color"],
        default=configurations["defaults"]["hex-colors"]
    )
    @click.option(
        '--image-processor',
        type=click.Choice(image_processors_keys),
        default=configurations["defaults"]["image-processor"],
        required=True,
        help=helpers["image_generator_command"]["--image-processor"]
    )
    @click.option('--output-builder',
        type=click.Choice(outputs_builders_keys),
        default=configurations["defaults"]["output-builder"],
        required=True,
        help=helpers["image_generator_command"]["--output-builder"]
    )
    @click.option('--size',
        type=click.INT,
        default=configurations["defaults"]["size"],
        required=True,
        help=helpers["image_generator_command"]["--size"]
    )
    @click.option('--output-directory',
        type=click.Path(exists=True),
        default=configurations["defaults"]["output-directory"],
        required=True,
        help=helpers["image_generator_command"]["--output-directory"]
    )
    @click.option('--verbose/--no-verbose',
        type=click.BOOL,
        default=configurations["defaults"]["verbose"],
        required=True,
        help=helpers["image_generator_command"]["--verbose/--no-verbose"]
    )
    def image_generator_command(
        width,
        height,
        hex_color,
        image_processor,
        output_builder,
        size,
        output_directory,
        verbose,
    ):
        """
        Command to generate an image with specified dimensions, colors, and processing options.

        Parameters:
            width (int): Width of the generated image.
            height (int): Height of the generated image.
            hex_color (tuple): Tuple of hex color values for the image.
            image_processor (str): Key for the image processor to use.
            output_builder (str): Key for the output builder to use.
            size (int): Size parameter for the image processor.
            output_directory (str): Directory to save the generated image.
            verbose (bool): Flag to enable verbose output.
        """
        hex_colors = hex_color
        
        image_array = np.zeros((height, width, 3), dtype=np.uint8)
        
        image_transformer = ImageTransformer(image_array)
        
        image_output_path = os.path.join(output_directory, GENERATED_IMAGE_NAME + ".svg")
        
        rgb_colors = [hex_to_rgb_color_converter(hex_color, with_hashtag=False) for hex_color in hex_colors]
        
        output_builder: GenericOutputBuilder = outputs_builders[output_builder](width, height, image_output_path)
        grid_image_processor: GenericGridImageProcessor = image_processors[image_processor](size)
        image_pixels_processor: GenericPixelsProcessor = ColorPaletteBasedPixelProcessor(rgb_colors)
        
        callback_function = None
        
        number_of_grid_elements = grid_image_processor.approximate_number_of_grid_elements(width, height)

        if verbose:
            print("[image-transformer]: welcome to the program!")
            print(f"[image-transformer](width): {width}")
            print(f"[image-transformer](height): {height}")
            print(f"[image-transformer](#pixels): {width * height}")
        
        with alive_bar(width * height + number_of_grid_elements, title="[image-transformer](processing)", disable=not verbose) as progress_bar:
            callback_function = lambda step_name, step_size: progress_bar() # pylint: disable=not-callable

            image_transformer.transform_and_save(
                image_processor=grid_image_processor,
                output_builder=output_builder,
                pixels_processor=image_pixels_processor,
                callback=callback_function
            )
        
        output_builder.save()
        
    return image_generator_command