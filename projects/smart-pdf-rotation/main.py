import logging
import os
from uuid import uuid4

import cv2
import imutils
import numpy as np
from PIL import Image
import pytesseract
from pytesseract import Output

LOGGER = logging.getLogger(__name__)

def fix_rotation_of_image(image_path: str) -> np.ndarray:
    """
    Fix the rotation of an image

    Args:
        image_path (str): Path to the input image file

    Returns:
        np.ndarray: Rotated image array
    """
    # Read image directly using OpenCV
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"The image could not be found at {image_path}")

    # Convert to RGB for tesseract
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Detect orientation
    results = pytesseract.image_to_osd(
        rgb, config="--psm 0 -c min_characters_to_try=50", output_type=Output.DICT
    )
    
    LOGGER.info("Detected orientation: {}".format(results["orientation"]))
    LOGGER.info("Rotate by {} degrees to correct".format(results["rotate"]))
    LOGGER.info("Detected script: {}".format(results["script"]))
    
    # Rotate image
    rotated = imutils.rotate_bound(image, angle=results["rotate"])
    
    return rotated

def save_image(image: np.ndarray, output_dir: str) -> str:
    """
    Save the image to a file with a UUID filename

    Args:
        image (np.ndarray): Image array to save
        output_dir (str): Directory to save the image in

    Returns:
        str: Path to the saved image file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename
    filename = f"{uuid4()}.jpg"
    output_path = os.path.join(output_dir, filename)
    
    # Save image
    cv2.imwrite(output_path, image)
    LOGGER.info(f"Rotated image saved to {output_path}")
    
    return output_path

def process_images(input_dir: str, output_dir: str):
    """
    Process all images in the input directory and save rotated versions to output directory

    Args:
        input_dir (str): Directory containing input images
        output_dir (str): Directory to save rotated images
    """
    # Get all image files from input directory
    image_extensions = ('.jpg', '.jpeg', '.png')
    image_files = [
        f for f in os.listdir(input_dir) 
        if f.lower().endswith(image_extensions)
    ]
    
    for image_file in image_files:
        input_path = os.path.join(input_dir, image_file)
        try:
            # Fix rotation
            rotated_image = fix_rotation_of_image(input_path)
            # Save rotated image
            save_image(rotated_image, output_dir)
        except Exception as e:
            LOGGER.error(f"Error processing {image_file}: {str(e)}")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    
    # Set input and output directories
    input_dir = "samples"
    output_dir = "output"
    
    # Process all images
    process_images(input_dir, output_dir)