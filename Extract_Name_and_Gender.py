import cv2
import pytesseract
import re

class AadharOCR:
    def __init__(self, img_path):
        self.user_aadhar_no = None
        self.user_gender = None
        self.user_dob = None
        self.user_name = None
        self.img_name = img_path

    def preprocess_image(self):
        # Read and preprocess the image
        img = cv2.imread(self.img_name)
        if img is None:
            print("Error: Could not open or find the image.")
            return None
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return thresh

    def extract_data(self):
        # Preprocess the image and extract text
        img = self.preprocess_image()
        if img is None:
            return None
        
        # Extracting text from image using Tesseract OCR
        text = pytesseract.image_to_string(img, lang='eng')
        text_list = [line.strip() for line in re.split(r'[\n]', text) if line.strip()]
        print(text)

        # Regular expression pattern for Aadhaar number in 4-4-4 format
        aadhar_pattern = r'\b\d{4}\s\d{4}\s\d{4}\b'
        
        # Extract Aadhar Card Number using the specified pattern
        for line in text_list:
            aadhar_match = re.search(aadhar_pattern, line)
            if aadhar_match:
                self.user_aadhar_no = aadhar_match.group()  # Retain spaces for 4-4-4 format
                break

        # Extract Gender
        for line in text_list:
            if re.search(r'\b(Male|male|MALE)\b', line):
                self.user_gender = 'MALE'
                break
            elif re.search(r'\b(Female|female|FEMALE)\b', line):
                self.user_gender = 'FEMALE'
                break

        # Extract Date of Birth or Year of Birth
        for line in text_list:
            if re.search(r'(Year|Birth|YoB|YOB|DOB|Date of Birth)', line):
                dob_match = re.search(r'(\d{2}/\d{2}/\d{4})|(\d{2}-\d{2}-\d{4})|(\d{8})', line)
                if dob_match:
                    self.user_dob = dob_match.group()
                break

        # Extract Name (assuming it’s the line above DOB/YoB)
        dob_index = next((idx for idx, line in enumerate(text_list) if 'DOB' in line or 'YoB' in line), None)
        if dob_index and dob_index > 0:
            self.user_name = text_list[dob_index - 1]

        return [self.user_aadhar_no, self.user_gender, self.user_dob, self.user_name]

# Main function to run the code in VS Code
def main():
    # Input the image path manually
    img_path = input("Please enter the path to the Aadhar card image: ")
    ocr = AadharOCR(img_path)
    
    # Extract data
    data = ocr.extract_data()
    if data:
        print("\nExtracted Aadhar Card Details:")
        print(f"Gender: {ocr.user_gender}")
        print(f"Name: {ocr.user_name}")
    else:
        print("Failed to extract data from the image.")

if __name__ == "__main__":
    main()
