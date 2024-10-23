import numpy as np

from image_transformer.distributions import GenericDistribution

from typing import Tuple

class PoissonDistribution(GenericDistribution):
    """
    PoissonDistribution samples RGB color values from a predefined set of colors
    using Poisson distribution for selecting indices.
    """
    
    def __init__(self, width: int, height: int, colors: list[Tuple[int, int, int]]) -> None:
        """
        Initialize with a set of predefined colors.

        Parameters:
            colors (list[Tuple[int, int, int]]): A list of RGB color tuples to sample from.
        """
        self.colors = colors

    def sample_color(self: 'PoissonDistribution', x: int, y: int) -> Tuple[int, int, int]:
        """
        Samples a color from the predefined color set using Poisson distribution.

        Parameters:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            Tuple[int, int, int]: A tuple representing the RGB color values.
        """
        index = np.random.poisson(lam=(x + y) % len(self.colors)) % len(self.colors)

        return self.colors[index]
