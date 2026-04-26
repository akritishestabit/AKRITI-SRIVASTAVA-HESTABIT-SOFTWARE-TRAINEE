from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import os


class ImageCaptioner:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        ).to(self.device)

    def generate_caption(self, image_path):
        try:
            image = Image.open(image_path).convert("RGB")

            inputs = self.processor(image, return_tensors="pt").to(self.device)

            out = self.model.generate(**inputs)

            caption = self.processor.decode(out[0], skip_special_tokens=True)

            return caption

        except Exception as e:
            print("Caption Error:", e)
            return ""



if __name__ == "__main__":
    captioner = ImageCaptioner()

    print("\n IMAGE CAPTION TEST MODE\n")
    print("Current working directory:", os.getcwd())

    image_path = input("\nEnter image path (e.g., data/raw/test.png): ")

    if not os.path.exists(image_path):
        print(" File not found!")
    else:
        caption = captioner.generate_caption(image_path)

        print("\n Generated Caption:\n")
        print(caption if caption else " No caption generated")