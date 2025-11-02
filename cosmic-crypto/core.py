from PIL import Image
import secrets
from pathlib import Path

def generate_image(width: int = 256, height: int = 256) -> Image.Image:
    """
    Generate a random RGB image of specified width and height.
    """
    image = Image.new("RGB", (width, height))
    for x in range(width):
        for y in range(height):
            r = secrets.randbelow(256)
            g = secrets.randbelow(256)
            b = secrets.randbelow(256)
            image.putpixel((x, y), (r, g, b))
    return image


def save_image(image: Image.Image, path: str):
    """
    Save a PIL image to disk in PNG format.
    """
    image.save(path, format="PNG")


def load_image(path: str) -> Image.Image:
    """
    Load a PIL image from disk.
    """
    return Image.open(path)


def image_to_number(image: Image.Image) -> int:
    """
    Convert an image to a giant cryptographic number.
    """
    pixels = image.load()
    width, height = image.size
    number = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            number = (secrets.randbelow(1000) * 100**8) * (
                (secrets.randbelow(500) | r) +
                (secrets.randbelow(500) | g) +
                (secrets.randbelow(500) | b)
            )
    return number


def generate_number_from_size(width: int = 256, height: int = 256) -> int:
    """
    Convenience function: generate a new image and return its cryptographic number.
    """
    img = generate_image(width, height)
    return image_to_number(img)


def generate_number_from_image_path(path: str) -> int:
    """
    Load an image from disk and generate the cryptographic number.
    """
    img = load_image(path)
    return image_to_number(img)
