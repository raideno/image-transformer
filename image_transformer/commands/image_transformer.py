"""
This module defines a command-line interface (CLI) for transforming images using various processors and builders.
It utilizes the Click library to handle command-line arguments and options.
"""

import os
import click

from alive_progress import alive_bar

from image_transformer.constants import image_processors, pixels_processors, outputs_builders

from image_transformer import ImageTransformer

from image_transformer.utils import load_image

from image_transformer.commands import helpers

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder
from image_transformer.pixels_processors.generic_pixels_processor import GenericPixelsProcessor
from image_transformer.image_processors.generic_grid_image_processor import GenericGridImageProcessor

def image_transformer_command_factory(
    configurations: dict,
    image_processors_keys: list[str],
    pixels_processors_keys: list[str],
    outputs_builders_keys: list[str],
):
    """
    Factory function to create the image transformer command.

    Parameters:
        configurations (dict): Configuration dictionary containing default values.
        image_processors_keys (list[str]): List of available image processor keys.
        pixels_processors_keys (list[str]): List of available pixels processor keys.
        outputs_builders_keys (list[str]): List of available output builder keys.

    Returns:
        function: The image transformer command function.
    """
    @click.command(
        name="transform",
        help=helpers["image_transformer_command"]["help"]
    )
    @click.option('--image-path',
        type=click.Path(exists=True),
        required=True,
        help=helpers["image_transformer_command"]["--image-path"]
    )
    @click.option('--image-processor',
        type=click.Choice(image_processors_keys),
        default=configurations["defaults"]["image-processor"],
        required=True,
        help=helpers["image_transformer_command"]["--image-processor"]
    )
    @click.option('--pixels-processor',
        type=click.Choice(pixels_processors_keys),
        default=configurations["defaults"]["pixels-processor"],
        required=True,
        help=helpers["image_transformer_command"]["--pixels-processor"]
    )
    @click.option('--output-builder',
        type=click.Choice(outputs_builders_keys),
        default=configurations["defaults"]["output-builder"],
        required=True,
        help=helpers["image_transformer_command"]["--output-builder"]
    )
    @click.option('--size',
        type=click.INT,
        default=configurations["defaults"]["size"],
        required=True,
        help=helpers["image_transformer_command"]["--size"]
    )
    @click.option('--output-directory',
        type=click.Path(exists=True),
        default=configurations["defaults"]["output-directory"],
        required=True,
        help=helpers["image_transformer_command"]["--output-directory"]
    )
    @click.option('--verbose/--no-verbose',
        type=click.BOOL,
        required=True,
        default=configurations["defaults"]["verbose"],
        help=helpers["image_transformer_command"]["--verbose/--no-verbose"]
    )
    def image_transformer_command(
        image_path,
        image_processor,
        pixels_processor,
        output_builder,
        size,
        output_directory,
        verbose,
    ):
        """
        Command to transform an image using specified processors and builders.

        Parameters:
            image_path (str): Path to the input image.
            image_processor (str): Key for the image processor to use.
            pixels_processor (str): Key for the pixels processor to use.
            output_builder (str): Key for the output builder to use.
            size (int): Size parameter for the image processor.
            output_directory (str): Directory to save the output image.
            verbose (bool): Flag to enable verbose output.
        """
        image = load_image(image_path)
        
        image_transformer = ImageTransformer.from_pil_image(image)
        
        image_file_name = os.path.basename(image_path)
        image_name = os.path.splitext(image_file_name)[0]
        
        image_output_path = os.path.join(output_directory, image_name + ".svg")
        
        output_builder: GenericOutputBuilder = outputs_builders[output_builder](image.width, image.height, image_output_path)
        grid_image_processor: GenericGridImageProcessor = image_processors[image_processor](size)
        image_pixels_processor: GenericPixelsProcessor = pixels_processors[pixels_processor]()
        
        callback_function = None
        
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
        
    return image_transformer_command