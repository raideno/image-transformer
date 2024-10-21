import click

def image_generator_command_factory(
    configurations: dict,
    image_processors_keys: list[str],
    pixels_processors_keys: list[str],
    outputs_builders_keys: list[str],
    distributions_keys: list[str],
):
    @click.command("generate")
    
    @click.option('--width', type=click.Path(exists=True), required=True)
    @click.option('--height', type=click.Choice(image_processors_keys), required=True)
    
    @click.option('--colors', type=click.STRING, multiple=True, required=True)
    @click.option('--distribution', type=click.Choice(distributions_keys), default=configurations["defaults"]["distribution"], required=True)
    
    @click.option('--builder', type=click.Choice(outputs_builders_keys), default=configurations["defaults"]["output-builder"], required=True)
    @click.option('--size', type=click.INT, default=configurations["defaults"]["size"], required=True)
    @click.option('--output-directory', type=click.Path(exists=True), default=configurations["defaults"]["output-directory"], required=True)
    @click.option('--verbose/--no-verbose', type=click.BOOL, default=True, required=True)
    def image_generator_command(
        image,
        grid,
        pixels,
        builder,
        size,
        output_directory,
        verbose,
    ):
        """Simple program that greets NAME for a total of COUNT times."""
        print("Hello guys !!!")
        
    return image_generator_command