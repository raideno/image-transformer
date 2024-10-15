import argparse

def arguments_parser_factory(image_processors_keys: list[str], pixels_processors_keys: list[str], configurations: dict) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="image-enhancer",
        description="Transform your images into svg",
    )

    parser.add_argument("image_path", type=str)
    parser.add_argument("-g", "--grid", type=str, choices=image_processors_keys, default=configurations["defaults"]["image-processor"])
    parser.add_argument("-p", "--pixels", type=str, choices=pixels_processors_keys, default=configurations["defaults"]["pixels-processor"])
    parser.add_argument("-s", "--size", type=int, default=configurations["defaults"]["size"])
    parser.add_argument("-o", "--output-directory", "--output_directory", type=str, default=configurations["defaults"]["output-directory"])
    parser.add_argument("-v", "--verbose", action="store_true")
    
    return parser