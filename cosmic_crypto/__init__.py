"""
Cosmic Crypto
A fun, overkill cryptography module that generates huge cryptographic numbers from random images.
"""

from .core import (
    generate_image,
    save_image,
    load_image,
    image_to_number,
    generate_number_from_size,
    generate_number_from_image_path,
)

__all__ = [
    "generate_image",
    "save_image",
    "load_image",
    "image_to_number",
    "generate_number_from_size",
    "generate_number_from_image_path",
]

__version__ = "0.1.0"
__author__ = "ZaiperUnbound"
