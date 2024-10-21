import re
import click

class ClickColor(click.ParamType):
    name = 'Color'
    # hex_color_pattern = re.compile(r'^#[0-9A-Fa-f]{6}$')
    hex_color_pattern = re.compile(r'^[0-9A-Fa-f]{6}$')
    
    def __init__(self: 'ClickColor') -> None:
        super().__init__()

    def convert(self: 'ClickColor', value: str, param: click.Parameter, ctx: click.Context) -> str:
        try:
            if self.hex_color_pattern.match(value):
                return value.upper()
            self.fail('%s is not a valid color' % value, param, ctx)
        except Exception as e:
            self.fail('%s is not a valid color: %s' % (value, str(e)), param, ctx)