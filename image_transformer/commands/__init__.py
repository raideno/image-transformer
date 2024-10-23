import click

from image_transformer.commands.helpers import helpers
from image_transformer.commands.image_generator import image_generator_command_factory
from image_transformer.commands.image_transformer import image_transformer_command_factory

@click.group()
def commands():
    pass

def initialize_commands(
    configurations: dict,
    image_processors_keys: list[str],
    pixels_processors_keys: list[str],
    outputs_builders_keys: list[str]
):
    image_generator_command = image_generator_command_factory(
        configurations,
        image_processors_keys,
        pixels_processors_keys,
        outputs_builders_keys,
    )
    
    image_transformer_command = image_transformer_command_factory(
        configurations,
        image_processors_keys,
        pixels_processors_keys,
        outputs_builders_keys,
    )
    
    commands.add_command(image_generator_command)
    commands.add_command(image_transformer_command)
    
    return commands