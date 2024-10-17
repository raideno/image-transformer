"""
This module defines the `GenericOutputBuilder` abstract base class, which provides an interface for rendering shapes 
and saving the final output. The class includes methods for adding rectangles and hexagons, as well as saving the 
rendered output to a file.
"""

from typing import Tuple

from abc import ABC, abstractmethod

class GenericOutputBuilder(ABC):
    """
    Abstract base class for shape rendering.

    Defines the interface for adding shapes and saving the final output.
    """

    @abstractmethod
    def add_rectangle(self: 'GenericOutputBuilder', x: int, y: int, size: int, color: Tuple[int, int, int]):
        """
        Add a square to the output.

        Parameters:
            x (int):
                The x-coordinate of the square's top-left corner.
            y (int):
                The y-coordinate of the square's top-left corner.
            size (int):
                The size of the square.
            color (str):
                The fill color of the square.
        """

    @abstractmethod
    def add_hexagon(self: 'GenericOutputBuilder', x: int, y: int, size: int, color: Tuple[int, int, int]):
        """
        Add a flat-topped hexagon to the output.

        Parameters:
            x (int):
                The x-coordinate of the top-left point of the hexagon's bounding box.
            y (int):
                The y-coordinate of the top-left point of the hexagon's bounding box.
            size (int):
                The distance between two opposite sides (the width) of the hexagon.
            color (str):
                The fill color of the hexagon.
        """

    @abstractmethod
    def save(self: 'GenericOutputBuilder'):
        """
        Save the rendered output to a file.
        """
