from image_loader.loader import load

TESTING_IMAGE_PATH = "data/testing-image.jpg"

def main():
    print("[image-enhancer]: welcome to the program!")
    
    image = load(TESTING_IMAGE_PATH)
    
    image.show()
    
if __name__ == "__main__":
    main()