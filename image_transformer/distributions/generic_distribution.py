"""
This module defines the GenericDistribution abstract base class, which provides an interface for sampling colors in a 2D space.
"""

from typing import Tuple
from abc import ABC, abstractmethod

class GenericDistribution(ABC):
    """
    GenericDistribution is an abstract base class that defines the interface for sampling colors in a 2D space.
    """
    
    @abstractmethod
    def __init__(self: 'GenericDistribution', width: int, height: int, colors: list[Tuple[int, int, int]]) -> None:
        """
        Initialize the distribution with a set of predefined colors.

        Parameters:
            colors (List[Tuple[int, int, int]]): A list of RGB color tuples.
        """
    
    @abstractmethod
    def sample_color(self: 'GenericDistribution', x: int, y: int) -> Tuple[int, int, int]:
        """
        Abstract method to sample a color at a given (x, y) coordinate.

        Parameters:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            Tuple[int, int, int]: A tuple representing the RGB color values.
        """
            