import pytesseract
from PIL import Image
import cv2
import numpy as np
import os


class OCRExtractor:
    def __init__(self, lang="eng"):
        self.lang = lang

    def preprocess_image(self, image_path):
        """
        Apply preprocessing for better OCR accuracy
        """
        img = cv2.imread(image_path)

        if img is None:
            raise ValueError("Image not loaded properly")

        
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        
        gray = cv2.medianBlur(gray, 3)

        
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
       
        try:
          
            image = Image.open(image_path).convert("RGB")

            text = pytesseract.image_to_string(image, lang=self.lang)

            if text.strip():
                return {
                    "text": text.strip(),
                    "method": "normal"
                }

           
            processed_img = self.preprocess_image(image_path)

            text = pytesseract.image_to_string(processed_img, lang=self.lang)

            if text.strip():
                return {
                    "text": text.strip(),
                    "method": "preprocessed"
                }

            
            return {
                "text": "",
                "method": "failed"
            }

        except Exception as e:
            return {
                "text": "",
                "method": "error",
                "error": str(e)
            }



if __name__ == "__main__":
    ocr = OCRExtractor()

    print("\n OCR TEST MODE\n")

    image_path = input("Enter image path: ")

    if not os.path.exists(image_path):
        print("File not found!")
    else:
        result = ocr.extract_text(image_path)

        print("\nExtracted Text:\n")
        print(result["text"] if result["text"] else "No text found")
        print("\nMethod used:", result["method"])