-- Good for D.O.B and Aadhar_number extraction

import re
import pytesseract
from PIL import Image
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'write the original path of your pytesseract file.'

def preprocess_image(image_path):
     -- Load the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
     -- Apply thresholding to make text clearer
    _, img_thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    return Image.fromarray(img_thresh)

def extract_aadhar_details(image_path):
     -- Preprocess the image
    img = preprocess_image(image_path)
    
     -- Use OCR to extract text from the preprocessed image
    ocr_text = pytesseract.image_to_string(img, config='--psm 6')
    print("OCR Text:", ocr_text)
    
    -- Regular expression for Aadhaar number in 4-4-4 format
    aadhar_pattern = r'\b\d{4}\s\d{4}\s\d{4}\b'
    
     -- Regular expression for DOB
    dob_pattern = (
        r'\b\d{2}[/-]\d{2}[/-]\d{4}\b|'  # Matches dd/mm/yyyy or dd-mm-yyyy
        r'\b\d{2}\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b'  -- Matches dd month yyyy
    )
    
     -- Split OCR text into lines
    text_lines = [line.strip() for line in ocr_text.splitlines() if line.strip()]

     -- Search for Aadhaar number
    aadhar_number = None
    for line in text_lines:
        aadhar_match = re.search(aadhar_pattern, line)
        if aadhar_match:
            aadhar_number = aadhar_match.group()  -- Retain spaces for 4-4-4 format
            break
    
     -- Search for DOB
    dob = None
    dob_index = None
    for i, line in enumerate(text_lines):
        dob_match = re.search(dob_pattern, line, re.IGNORECASE)
        if dob_match:
            dob = dob_match.group()
            dob_index = i  -- Save the index for potential name extraction
            break
    
     -- Extract Name (assuming it's the line above the DOB/YoB if found)
    name = None
    if dob_index is not None and dob_index > 0:
        potential_name = text_lines[dob_index - 1]
         -- Remove any digits from the extracted name
        name = re.sub(r'\d', '', potential_name).strip()

    return {
        'aadhar_number': aadhar_number,
        'date_of_birth': dob
    }

 -- Example usage
image_path = "Screenshot 2024-11-02 at 21.51.50.png"

 -- Extract Aadhaar number, DOB, and name
extracted_data = extract_aadhar_details(image_path)

 -- Display the results
print("Extracted Aadhaar card details:", extracted_data)
