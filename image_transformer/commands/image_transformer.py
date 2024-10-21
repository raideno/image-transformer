import click

@click.command()
@click.option('--image', default=1, help='Number of greetings.')
@click.option('--grid', prompt='Your name', help='The person to greet.')
@click.option('--pixels', prompt='Your name', help='The person to greet.')
@click.option('--builder', prompt='Your name', help='The person to greet.')
@click.option('--size', prompt='Your name', help='The person to greet.')
@click.option('--output-directory', prompt='Your name', help='The person to greet.')
@click.option('--verbose/--no-verbose', default=True)
def image_transformer(
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