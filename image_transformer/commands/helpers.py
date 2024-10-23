"""
This module contains helper dictionaries for image generation and transformation commands.
"""

helpers = {
    "image_generator_command": {
        "help": "Generate an image with specified dimensions, colors, and processing options.",
        "--width": "Specify the width of the generated image.",
        "--height": "Specify the height of the generated image.",
        "--hex-color": "Specify the hex color code for the image background.",
        "--image-processor": "Specify the image processor to use.",
        "--output-builder": "Specify the output builder to use.",
        "--size": "Specify the size of the image.",
        "--output-directory": "Specify the directory where the output image will be saved.",
        "--verbose/--no-verbose": "Enable or disable verbose output.",
    },
    "image_transformer_command": {
        "help": "Command to transform an image using specified processors and save the output. This command allows you to transform an image using various processors for the image, pixels, and output. The transformed image is then saved to the specified output directory.",
        "--image-path": "Specify the path to the image to be transformed.",
        "--image-processor": "Specify the image processor to use.",
        "--pixels-processor": "Specify the pixels processor to use.",
        "--output-builder": "Specify the output builder to use.",
        "--size": "Specify the size of the transformed image.",
        "--output-directory": "Specify the directory where the transformed image will be saved.",
        "--verbose/--no-verbose": "Enable or disable verbose output.",
    }
}