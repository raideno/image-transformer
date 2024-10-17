"""
This module provides functionality to load configurations from a TOML file.
"""

import tomllib
import os

def load_configurations(configuration_file_path: str) -> dict:
    """
    Loads configurations from a TOML file.

    Parameters:
        configuration_file_path (str): The path to the TOML configuration file.

    Returns:
        dict: The configurations loaded from the file.
    """
    configurations = None
    
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
  
    absolute_configuration_file_path = os.path.join(project_root, configuration_file_path)
    
    with open(absolute_configuration_file_path, "rb") as file:
        configurations = tomllib.load(file)
        
    return configurations