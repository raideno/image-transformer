"""
This module provides a custom Click parameter type for validating and converting hexadecimal color codes.
"""

import re
import click

class ClickColor(click.ParamType):
    """
    A custom Click parameter type for validating and converting hexadecimal color codes.
    """
    name = 'Color'
    hex_color_pattern = re.compile(r'^#?([0-9A-Fa-f]{6})$')
    
    def convert(self: 'ClickColor', value: str, param: click.Parameter, ctx: click.Context) -> str:
        """
        Validates and converts a hexadecimal color code to uppercase.
        
        Parameters:
            value (str): The hexadecimal color code to validate and convert.
            param (click.Parameter): The Click parameter object.
            ctx (click.Context): The Click context object.
        
        Returns:
            str: The validated and converted hexadecimal color code in uppercase.
        
        Raises:
            click.BadParameter: If the provided value is not a valid hexadecimal color code.
        """
        try:
            match = self.hex_color_pattern.match(value)
            if match:
                return match.group(1).upper()
            self.fail(f'{value} is not a valid color', param, ctx)
            return self.fail(f'{value} is not a valid color', param, ctx)
        except re.error as e:
            return self.fail(f'{value} is not a valid color: {str(e)}', param, ctx)