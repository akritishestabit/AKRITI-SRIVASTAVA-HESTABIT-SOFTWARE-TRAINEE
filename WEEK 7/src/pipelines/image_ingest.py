import os
import json
from src.embeddings.clip_embedder import CLIPEmbedder
from src.utils.ocr import OCRExtractor
from src.utils.captioner import ImageCaptioner


class ImageIngestPipeline:
    def __init__(self, image_folder="src/data/raw", output_path="src/data/chunks/image_chunks.json"):
        self.image_folder = image_folder
        self.output_path = output_path

        self.embedder = CLIPEmbedder()
        self.ocr = OCRExtractor()
        self.captioner = ImageCaptioner()

        self.data = []

    
    def process_images(self):
        if os.path.isfile(self.image_folder):
            images = [os.path.basename(self.image_folder)]
            base_path = os.path.dirname(self.image_folder)
        else:
            base_path = self.image_folder
            images = [f for f in os.listdir(base_path)
                    if f.lower().endswith((".png", ".jpg", ".jpeg"))]

        for idx, img_name in enumerate(images):
            image_path = os.path.join(base_path, img_name)

            print(f"\n Processing: {img_name}")

            ocr_text = self.ocr.extract_text(image_path)
            caption = self.captioner.generate_caption(image_path)
            embedding = self.embedder.embed_image(image_path)

            item = {
                "id": idx,
                "image": img_name,
                "type": "image",
                "source": image_path,
                "ocr_text": ocr_text,
                "caption": caption,
                "embedding": embedding.tolist()
            }

            self.data.append(item)

        
        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)

        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

        print(f"\n Saved {len(self.data)} image entries")



if __name__ == "__main__":
    print("\n IMAGE INGEST PIPELINE\n")

    folder = input("Enter image folder path (e.g., data/raw): ")

    pipeline = ImageIngestPipeline(image_folder=folder)
    pipeline.process_images()