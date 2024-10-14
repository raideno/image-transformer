# Image Scaler

This Python application reads a low-resolution .png image and generates a scalable .svg version. The .svg file can be used as a high-resolution wallpaper. The application samples the colors of each hexagon to reproduce the same picture.

## How to use ?

1. Clone the repository.
2. Install the tool and necessary libraries using: `poetry install`.
3. Use it: `poetry run main [--help] [-g {hexagonal,square}] [-p {random,average,frequent}] [-s SIZE] image_path`.

**Note:** for more details about all the available params use the following command: `poetry run main --help`.

## Materials & Notes:

This are for people who want to dig in hexagonal grids & know how to deal with it. Ignore if you only want to use the tool.

- https://www.redblobgames.com/
- https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/
- https://gamedev.stackexchange.com/a/61101
