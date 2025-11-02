# Cosmic Crypto

A Python library for generating cryptographic numbers from random images.

## Overview

Cosmic Crypto transforms randomly generated images into large cryptographic numbers. Each pixel's RGB values are processed through a cryptographic random number generator to produce a unique numerical representation.

## Installation

This project requires Python 3.6+ and Pillow (PIL).

```bash
pip install Pillow
```

## Usage

### Generate a Random Image

```python
from cosmic_crypto.core import generate_image, save_image

# Generate a 256x256 random RGB image
img = generate_image(width=256, height=256)

# Save it to disk
save_image(img, "random_image.png")
```

### Convert Image to Cryptographic Number

```python
from cosmic_crypto.core import image_to_number, load_image

# Load an existing image
img = load_image("random_image.png")

# Convert to cryptographic number
number = image_to_number(img)
print(f"Cryptographic number: {number}")
```

### Convenience Functions

```python
from cosmic_crypto.core import generate_number_from_size, generate_number_from_image_path

# Generate image and return number in one step
number = generate_number_from_size(width=512, height=512)

# Load image from path and convert to number
number = generate_number_from_image_path("path/to/image.png")
```

## API Reference

### `generate_image(width: int = 256, height: int = 256) -> Image.Image`
Generates a random RGB image using cryptographically secure random numbers.

**Parameters:**
- `width`: Image width in pixels (default: 256)
- `height`: Image height in pixels (default: 256)

**Returns:** PIL Image object

### `save_image(image: Image.Image, path: str)`
Saves a PIL image to disk in PNG format.

**Parameters:**
- `image`: PIL Image object to save
- `path`: File path for the output PNG

### `load_image(path: str) -> Image.Image`
Loads a PIL image from disk.

**Parameters:**
- `path`: File path to the image

**Returns:** PIL Image object

### `image_to_number(image: Image.Image) -> int`
Converts an image to a large cryptographic number by processing pixel RGB values.

**Parameters:**
- `image`: PIL Image object

**Returns:** Integer representing the cryptographic number

### `generate_number_from_size(width: int = 256, height: int = 256) -> int`
Convenience function that generates a new random image and returns its cryptographic number.

**Parameters:**
- `width`: Image width in pixels (default: 256)
- `height`: Image height in pixels (default: 256)

**Returns:** Integer representing the cryptographic number

### `generate_number_from_image_path(path: str) -> int`
Loads an image from disk and converts it to a cryptographic number.

**Parameters:**
- `path`: File path to the image

**Returns:** Integer representing the cryptographic number

## Security Note

This library uses Python's `secrets` module for cryptographically secure random number generation, suitable for security-sensitive applications.

## License

No license... *yet*

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
