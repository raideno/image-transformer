from PIL import Image

def load(image_path: str) -> Image.Image:
    image = Image.open(image_path)
    
    return image