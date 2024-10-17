"""
This module provides functionality to load configurations from a TOML file.
"""

import tomllib

def load_configurations(configuration_file_path: str) -> dict:
    """
    Loads configurations from a TOML file.

    Parameters:
        configuration_file_path (str): The path to the TOML configuration file.

    Returns:
        dict: The configurations loaded from the file.
    """
    configurations = None
    
    with open(configuration_file_path, "rb") as file:
        configurations = tomllib.load(file)
        
    return configurations