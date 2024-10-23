"""
This module provides a utility function to convert hexadecimal color codes to RGB color tuples.
"""

from typing import Tuple

def hex_to_rgb_color_converter(hex_color: str, with_hashtag: bool=True) -> Tuple[int, int, int]:
    """
    Convert a hexadecimal color code to an RGB color tuple.

    Parameters:
        hex_color (str): The hexadecimal color code as a string. It can optionally start with a hashtag (#).
        with_hashtag (bool): A boolean indicating whether the provided hex_color includes a hashtag (#) at the beginning.
                                If False, a hashtag will be added to the hex_color.

    Returns:
        Tuple[int, int, int]: A tuple containing the RGB values (red, green, blue) as integers.
    """
    hex_color = "#" + hex_color if not with_hashtag else hex_color
    
    red_hex_color = hex_color[1: 3]
    green_hex_color = hex_color[3: 5]
    blue_hex_color = hex_color[5: 7]
    
    rgb_color = (
        int(red_hex_color, 16),
        int(green_hex_color, 16),
        int(blue_hex_color, 16)
    )
    
    return rgb_color