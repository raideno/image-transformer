"""
This module provides functionality to load images using the PIL library.
"""

from PIL import Image

def load_image(image_path: str) -> Image.Image:
    """
    Load an image from the specified file path.

    Parameters:
        image_path (str): The path to the image file.

    Returns:
        Image.Image: The loaded image object.
    """
    image = Image.open(image_path)
    
    return image