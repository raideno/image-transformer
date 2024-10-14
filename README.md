# Image Scaler

This Python application reads a low-resolution .png image and generates a scalable .svg version. The .svg file can be used as a high-resolution wallpaper. The application samples the colors of each hexagon to reproduce the same picture.

# Instructions & Notes:

- Start with a square grid to begin with
- We'll have a loop that simply traverse the image pixel by pixel
- - Inside this loop we'll call a function that'll handle that pixel coordinates and return it's associated grid coordinates
- Define different pixel merger procedures, like for each grid point is associated multiple pixels from the original grid
- - So multiple strategies can be used to combine those pixels into a single color for that cell
- - - Average color
- - - Most occurrent color
- - - Least occurrent color
- - - Left most pixel
- - - etc etc
- Take a look: https://www.geeksforgeeks.org/creating-svg-image-using-pycairo/

# TODO:

- [ ] Have a multiple parameters of hexagonal grid / traversals.
- [ ] Setup linting etc
- [ ] Generate SVG File at the end
- [ ] Have the "grid" be generalized in a class or something, like it should be easy to implement a new grid
- [ ] Learn about numpy meshgrid
- [ ] Do the resolution have an importance in this case ? Recall what is the resolution
