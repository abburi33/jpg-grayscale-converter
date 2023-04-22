from PIL import Image


def img_converter(image):
    """Gets an image file and returns its grayscale version"""

    # Create a pillow image instance
    img = Image.open(image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    return gray_img
