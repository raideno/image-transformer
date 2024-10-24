"""
This module provides the main entry point for the image-transformer program. It parses command-line arguments,
loads an image, processes it using specified image and pixel processors, and outputs the result as an SVG file.
"""

from importlib import resources

from image_transformer.commands import initialize_commands

from image_transformer.constants import image_processors, pixels_processors, outputs_builders

from image_transformer.utils import load_configurations

CONFIGURATION_FILE_NAME = "configurations.toml"

def main():
    """
    Main function to execute the image transformation process.
    """
    
    configurations = None

    with resources.path("image_transformer", CONFIGURATION_FILE_NAME) as configuration_file_path:
        configurations = load_configurations(configuration_file_path)
        
    commands = initialize_commands(
        configurations,
        image_processors,
        pixels_processors,
        outputs_builders
    )

    commands()

if __name__ == "__main__":
    main()