# Aadhar_OCR

This repository provides a set of Python scripts that use Tesseract OCR to extract key information (Date of Birth, Aadhaar Number, Name, and Gender) from Aadhaar card images. These scripts are useful for automated processing of Aadhaar card data, often required in identity verification processes.

Table of Contents
Overview
Setup
Usage
Files
Contributing
License


## Overview
The Aadhar_OCR repository includes the following files:

Extract_DOB_and_AadharNumber.py - Extracts the date of birth (DOB) and Aadhaar number from an input image.
Extract_Name&Gender.py - Extracts the name and gender of the Aadhaar card holder from an input image.
These scripts utilize the Tesseract OCR library to identify and read text fields from scanned Aadhaar card images, outputting the recognized data in a structured format.

## Setup
Prerequisites
Ensure you have the following installed:
Python 3.12.2 
Tesseract OCR (Version 0.3.13 or higher is recommended)
Python libraries: pytesseract, opencv-python, and any other image processing libraries as needed.
Installation

### Clone the repository:
https://github.com/Sunilyadav03/Aadhar_OCR.git

### Install the required Python libraries:
pip install -r requirements.txt

#### Extracting DOB and Aadhaar Number

python Extract_DOB_and_AadharNumber.py --input <path_to_aadhar_image>

This will extract the Date of Birth (DOB) and Aadhaar number in the XXXX-XXXX-XXXX format.

#### Extracting Name and Gender

python Extract_Name&Gender.py --input <path_to_aadhar_image>

This will extract the name and gender of the Aadhaar card holder.

Command-line Arguments
--input - The path to the Aadhaar card image file.

## Files
Extract_DOB_and_AadharNumber.py: Uses Tesseract OCR to detect and extract the date of birth (DOB) and Aadhaar number (in the 4-4-4 digit format) from an input image.
Extract_Name&Gender.py: Uses Tesseract OCR to detect and extract the name and gender of the Aadhaar holder.


## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any feature requests or bugs.

## License
This project is licensed under the MIT License.

