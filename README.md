![Coverage](coverage.svg)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Poetry](https://img.shields.io/badge/Poetry-1.1.0%2B-blue)

---

# Image Transformer

This Python application reads a .png image and generates a scalable .svg version. The .svg file can be used as a high-resolution wallpaper. The application samples the colors of each grid element (hexagon, square, etc) to reproduce the same picture.

## Install

```bash
pip install image-transformer
```

## How to use as a CLI tool ?

Example usage:

```
image-transformer [--help] [-g {hexagonal,square,triangle}] [-p {random,average,frequent}] [-s SIZE] image_path
```

**Note:** for more details about all the available params use the following command: `image-transformer --help`.

## How to use in a program ?

Example usage:

```py
from PIL import Image

from image_transformer import ImageTransformer
from image_transformer.output_builders import CairoSvgOutputBuilder
from image_transformer.image_processors import HexagonalGridImageProcessor
from image_transformer.pixels_processors import MostFrequentPixelsProcessor

def main():
    hexagon_size = 13
    output_image_path = "result.svg"
    # NOTE: assuming the image exists
    my_image_path = "./testing-image.jpg"

    image = Image.open(my_image_path)

    transformer = ImageTransformer.from_pil_image(image)

    output_builder = CairoSvgOutputBuilder(image.width, image.height, output_image_path)
    image_processor = HexagonalGridImageProcessor(hexagon_size)
    pixels_processor = MostFrequentPixelsProcessor()

    transformer.transform_and_save(
        image_processor=image_processor,
        pixels_processor=pixels_processor,
        output_builder=output_builder
    )

if __name__ == "__main__":
    main()
```

## Examples

<table>
    <tr>
        <td>Original Image</td>
        <td>Hexagonal SVG Version</td>
    </tr>
    <tr>
        <td>
            <img src="data/testing-image.jpg" alt="Original Image">
        </td>
        <td>
            <img src="data/testing-image.svg" alt="Generated SVG">
        </td>
    </tr>
    <tr>
        <td>
            <img src="data/simple-image.png" alt="Original Image">
        </td>
        <td>
            <img src="data/simple-image.svg" alt="Generated SVG">
        </td>
    </tr>
</table>

## Development

Below are notes for development only. You don't need to give it a look unless you want to contribute or build your own library.

### Materials & Notes:

This are for people who want to dig in hexagonal grids & know how to deal with it. Ignore if you only want to use the tool.

- https://www.redblobgames.com/
- https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/
- https://gamedev.stackexchange.com/a/61101

### Docs Building Notes

- `poetry add sphinx --dev`: to install sphinx.
- `poetry run sphinx-apidoc -o docs/ image_transformer/`: to generate the .rst files for each module. This command should be run each time you have a new module or there is some changes in one of your modules.
- `poetry run sphinx-build -b html docs docs/_build`: to build the documentation. Each time there is a change.

### Upload to Pypi

- `poetry config http-basic.pypi __token__ <api-toke>`: to specify your pipy credentials.
- `poetry build`: build the project.
- `poetry publish`: to publish the builded project into pypi.

### About Poetry

[Poetry Scripts Section](https://github.com/python-poetry/poetry/issues/241#issuecomment-470200353):

> It looks like there is a desire for developer/project specific helper scripts, but that's not what [tool.poetry.scripts] is for. As mentioned, scripts are entrypoints into a python packages. This section's purpose is for libraries to install useful command line tools. Libraries like pytest, poetry, and the aws cli would use this scripts section so you can call their tool from the command line.

[Reason why they don't add a `dev-scripts` section](https://github.com/python-poetry/poetry/issues/241#issuecomment-470212635).

[ ] Poetry support multi language ?
