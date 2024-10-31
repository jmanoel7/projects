# Image Rotation Tool

This tool automatically detects and corrects the rotation of images using OCR (Optical Character Recognition) technology. It processes all images in an input directory and saves the rotated versions to an output directory.

## Features

- Automatic rotation detection using Tesseract OCR
- Supports multiple image formats (JPG, JPEG, PNG)
- Batch processing of multiple images
- UUID-based unique filenames for output
- Detailed logging of the rotation process

## Prerequisites

- Python 3.6 or higher
- Tesseract OCR engine

### Installing Tesseract OCR

#### On Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

#### On macOS:

```bash
brew install tesseract
```

## Installation

1. Clone the repository:

```bash
git clone [repository-url]
cd projects/smart-pdf-rotation
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Directory Structure

Create the following directory structure:

```
image-rotation-tool/
├── input/           # Place input images here
├── output/          # Rotated images will be saved here
├── main.py
└── requirements.txt
```

## Usage

1. Place your images in the `input` directory

2. Run the script:

```bash
python main.py
```

3. Check the `output` directory for the rotated images
   - Each output image will have a UUID filename
   - Original image format will be converted to JPG

## Logging

The tool provides detailed logging information including:

- Detected orientation of each image
- Required rotation angle
- Detected script type
- Success/failure status of each operation

## Supported Image Formats

- JPG/JPEG
- PNG

## Error Handling

The tool includes error handling for common issues:

- Missing input files
- Invalid image formats
- OCR processing errors
- File system errors

Each error is logged with detailed information for troubleshooting.

## Contributing

Feel free to submit issues and enhancement requests!
