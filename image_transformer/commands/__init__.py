"""
Module for initializing image transformation commands.
This module provides functionality to initialize and register commands
for image generation and transformation based on provided configurations
and processor keys.
"""
    
import click

from image_transformer.commands.helpers import helpers
from image_transformer.commands.image_generator import image_generator_command_factory
from image_transformer.commands.image_transformer import image_transformer_command_factory

@click.group()
def commands():
    """
    Function that groups commands.
    """

def initialize_commands(
    configurations: dict,
    image_processors_keys: list[str],
    pixels_processors_keys: list[str],
    outputs_builders_keys: list[str]
):
    """
    Initialize and register image transformation commands.
    This function creates and registers commands for image generation and
    transformation using the provided configurations and processor keys.
    
    Parameters:
        configurations (dict): Configuration settings for the commands.
        image_processors_keys (list[str]): List of keys for image processors.
        pixels_processors_keys (list[str]): List of keys for pixel processors.
        outputs_builders_keys (list[str]): List of keys for output builders.
    
    Returns:
        commands: The registered commands.
    """
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