import tomllib

def load_configurations(configuration_file_path: str):
    configurations = None
    
    with open(configuration_file_path, "rb") as file:
        configurations = tomllib.load(file)
        
    return configurations