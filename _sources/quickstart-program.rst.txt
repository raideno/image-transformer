Quickstart Program
==================

This guide will help you install the necessary software and dependencies for the project.

Prerequisites
-------------

Before you begin, ensure you have met the following requirements:

- You have a Windows/Linux/Mac machine.
- You have Python 3.6 or higher installed.

Steps
-----

Example usage:

.. code-block:: python

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

Troubleshooting
---------------

If you encounter any issues during installation, please refer to the project's README file or open an issue on the project's `GitHub page <https://github.com/raideno/image-transformer>`_.