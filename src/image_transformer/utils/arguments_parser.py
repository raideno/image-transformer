"""
This module provides a factory function to create an argument parser for the image-enhancer program.
The parser handles command-line arguments for processing images and converting them into SVG format.
"""

import argparse

def arguments_parser_factory(
    image_processors_keys: list[str],
    pixels_processors_keys: list[str],
    outputs_builders_keys: list[str],
    configurations: dict
) -> argparse.ArgumentParser:
    """
    Creates and configures an ArgumentParser for the image-enhancer program.

    Parameters:
        image_processors_keys (list[str]): List of valid keys for image processors.
        pixels_processors_keys (list[str]): List of valid keys for pixel processors.
        configurations (dict): Dictionary containing default configuration values.

    Returns:
        argparse.ArgumentParser: Configured argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="image-enhancer",
        description="Transform your images into svg",
    )

    parser.add_argument("image_path", type=str)
    parser.add_argument("-g", "--grid", type=str, choices=image_processors_keys, default=configurations["defaults"]["image-processor"])
    parser.add_argument("-p", "--pixels", type=str, choices=pixels_processors_keys, default=configurations["defaults"]["pixels-processor"])
    parser.add_argument("-b", "--builder", type=str, choices=outputs_builders_keys, default=configurations["defaults"]["output-builder"])
    parser.add_argument("-s", "--size", type=int, default=configurations["defaults"]["size"])
    parser.add_argument("-o", "--output-directory", "--output_directory", type=str, default=configurations["defaults"]["output-directory"])
    parser.add_argument("-v", "--verbose", action="store_true")
    
    return parser