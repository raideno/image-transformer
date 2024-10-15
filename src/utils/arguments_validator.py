import os
import sys
import argparse

def validate_and_parse_arguments(raw_arguments: list[str], arguments_parser: argparse.ArgumentParser) -> argparse.Namespace:    
    arguments = arguments_parser.parse_args(raw_arguments)
    
    image_path = arguments.image_path
    image_processor = arguments.grid
    pixels_processor = arguments.pixels
    size = arguments.size
    output_directory = arguments.output_directory
    verbose = arguments.verbose
    
    if size < 1 or size > 100:
        print(f"[image-enhancer](error): the size '{size}' is not valid. It must be between 1 and 100.")
        sys.exit(1)
    
    if not os.path.isfile(image_path):
        print(f"[image-enhancer](error): the provided path '{image_path}' is not a valid file.")
        sys.exit(1)
    
    if not os.path.isdir(output_directory):
        print(f"[image-enhancer](error): the provided output path '{output_directory}' is not a valid directory.")
        sys.exit(1)
        
    return arguments
        