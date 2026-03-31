# import pytesseract
# from PIL import Image
# import os


# class OCRExtractor:
#     def __init__(self):
#         pass

#     def extract_text(self, image_path):
#         """
#         Extract text from image using Tesseract OCR
#         """
#         try:
#             image = Image.open(image_path)
#             text = pytesseract.image_to_string(image)
#             return text.strip()

#         except Exception as e:
#             print("OCR Error:", e)
#             return ""



# if __name__ == "__main__":
#     ocr = OCRExtractor()

#     print("\n OCR TEST MODE\n")

   
#     print("Current working directory:", os.getcwd())

#     image_path = input("\nEnter image path (e.g., data/raw/test.png): ")

#     if not os.path.exists(image_path):
#         print(" File not found. Check path!")
#     else:
#         text = ocr.extract_text(image_path)

#         print("\n Extracted Text:\n")
#         print(text if text else "No text found in image")

import pytesseract
from PIL import Image
import cv2
import numpy as np
import os


class OCRExtractor:
    def __init__(self):
        # Optional: set path if needed
        # pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
        pass

    def preprocess_image(self, image_path):
        """
        Apply preprocessing for difficult images
        """
        img = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Adaptive threshold (better than simple threshold)
        thresh = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        return thresh

    def extract_text(self, image_path):
        """
        Extract text using:
        1. Normal OCR
        2. Fallback to preprocessing if needed
        """
        try:
            # ---------------------------
            # Step 1: Normal OCR
            # ---------------------------
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)

            if text.strip():
                print("Normal OCR worked")
                return text.strip()

            # ---------------------------
            # Step 2: Fallback OCR
            # ---------------------------
            print("Applying preprocessing...")

            processed_img = self.preprocess_image(image_path)
            text = pytesseract.image_to_string(processed_img)

            if text.strip():
                print("OCR worked after preprocessing")
            else:
                print("Still no text found")

            return text.strip()

        except Exception as e:
            print("OCR Error:", e)
            return ""


# ---------------------------
# INTERACTIVE MODE 🔥
# ---------------------------
if __name__ == "__main__":
    ocr = OCRExtractor()

    print("\n OCR TEST MODE\n")
    print("Current working directory:", os.getcwd())

    image_path = input("\nEnter image path (e.g., data/raw/test.png): ")

    if not os.path.exists(image_path):
        print(" File not found. Check path!")
    else:
        text = ocr.extract_text(image_path)

        print("\n Extracted Text:\n")
        print(text if text else " No text found in image")