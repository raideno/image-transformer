import os
import click

import numpy as np

from image_transformer.utils.click_color import ClickColor

from alive_progress import alive_bar

from image_transformer.constants import image_processors, pixels_processors, outputs_builders, distributions

from image_transformer import ImageTransformer

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder

from image_transformer.pixels_processors.generic_pixels_processor import GenericPixelsProcessor

from image_transformer.image_processors.generic_grid_image_processor import GenericGridImageProcessor

GENERATED_IMAGE_NAME = "result"

def image_generator_command_factory(
    configurations: dict,
    image_processors_keys: list[str],
    pixels_processors_keys: list[str],
    outputs_builders_keys: list[str],
    distributions_keys: list[str],
):
    @click.command("generate")
    
    @click.option('--width', type=click.INT, required=True)
    @click.option('--height', type=click.INT, required=True)
    
    @click.option('--colors', type=ClickColor(), multiple=True, required=True)
    @click.option('--distribution', type=click.Choice(distributions_keys), default=configurations["defaults"]["distribution"], required=True)
    
    @click.option('--pixels-processor', type=click.Choice(pixels_processors_keys), default=configurations["defaults"]["pixels-processor"], required=True)
    @click.option('--image-processor', type=click.Choice(image_processors_keys), default=configurations["defaults"]["image-processor"], required=True)
    
    @click.option('--output-builder', type=click.Choice(outputs_builders_keys), default=configurations["defaults"]["output-builder"], required=True)
    @click.option('--size', type=click.INT, default=configurations["defaults"]["size"], required=True)
    @click.option('--output-directory', type=click.Path(exists=True), default=configurations["defaults"]["output-directory"], required=True)
    
    @click.option('--verbose/--no-verbose', type=click.BOOL, default=True, required=True)
    def image_generator_command(
        width,
        height,
        colors,
        distribution,
        pixels_processor,
        image_processor,
        output_builder,
        size,
        output_directory,
        verbose,
    ):
        image_array =  np.zeros((height, width, 3), dtype=np.uint8)
        
        image_transformer = ImageTransformer(image_array)
        
        image_output_path = os.path.join(output_directory, GENERATED_IMAGE_NAME + ".svg")
        
        output_builder: GenericOutputBuilder = outputs_builders[output_builder](width, height, image_output_path)
        grid_image_processor: GenericGridImageProcessor = image_processors[image_processor](size)
        image_pixels_processor: GenericPixelsProcessor = pixels_processors[pixels_processor]()
        
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