from typing import Tuple

def hex_to_rgb_color_converter(hex_color: str, with_hashtag: bool=True) -> Tuple[int, int, int]:
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