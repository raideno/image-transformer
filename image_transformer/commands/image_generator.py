import click

@click.command()
@click.option('--width', default=1, help='Number of greetings.')
@click.option('--height', default=1, help='Number of greetings.')

@click.option('--colors', default=1, help='Number of greetings.')
@click.option('--distribution', default=1, help='Number of greetings.')

@click.option('--grid', prompt='Your name', help='The person to greet.')
@click.option('--builder', prompt='Your name', help='The person to greet.')
@click.option('--size', prompt='Your name', help='The person to greet.')
@click.option('--output-directory', prompt='Your name', help='The person to greet.')
@click.option('--verbose/--no-verbose', default=True)
def image_generator(
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