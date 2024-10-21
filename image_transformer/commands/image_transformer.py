import os
import click

from alive_progress import alive_bar

from image_transformer.constants import image_processors, pixels_processors, outputs_builders, distributions

from image_transformer import ImageTransformer

from image_transformer.utils import load_image

from image_transformer.output_builders.generic_output_builder import GenericOutputBuilder

from image_transformer.pixels_processors.generic_pixels_processor import GenericPixelsProcessor

from image_transformer.image_processors.generic_grid_image_processor import GenericGridImageProcessor

def image_transformer_command_factory(
    configurations: dict,
    image_processors_keys: list[str],
    pixels_processors_keys: list[str],
    outputs_builders_keys: list[str],
):
    @click.command("transform")
    
    @click.option('--image-path', type=click.Path(exists=True), required=True)
    @click.option('--image-processor', type=click.Choice(image_processors_keys), default=configurations["defaults"]["image-processor"], required=True)
    @click.option('--pixels-processor', type=click.Choice(pixels_processors_keys), default=configurations["defaults"]["pixels-processor"], required=True)
    @click.option('--output-builder', type=click.Choice(outputs_builders_keys), default=configurations["defaults"]["output-builder"], required=True)
    @click.option('--size', type=click.INT, default=configurations["defaults"]["size"], required=True)
    @click.option('--output-directory', type=click.Path(exists=True), default=configurations["defaults"]["output-directory"], required=True)
    
    @click.option('--verbose/--no-verbose', type=click.BOOL, default=True, required=True)
    def image_transformer_command(
        image_path,
        image_processor,
        pixels_processor,
        output_builder,
        size,
        output_directory,
        verbose,
    ):
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