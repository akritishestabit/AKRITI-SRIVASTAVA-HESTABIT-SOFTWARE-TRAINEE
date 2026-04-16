import json
import numpy as np
import os
from src.embeddings.clip_embedder import CLIPEmbedder
from src.utils.ocr import OCRExtractor
from src.utils.captioner import ImageCaptioner


class ImageSearch:
    def __init__(self, data_path="src/data/chunks/image_chunks.json"):
        self.data_path = data_path

        self.embedder = CLIPEmbedder()
        self.ocr = OCRExtractor()
        self.captioner = ImageCaptioner()

        with open(self.data_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # TEXT → IMAGE
    def text_to_image(self, query, top_k=3):
        query_embedding = self.embedder.embed_text(query)

        results = []
        for item in self.data:
            img_emb = np.array(item["embedding"])
            score = self.cosine_similarity(query_embedding, img_emb)
            results.append((score, item))

        threshold = 0.5
        results.sort(key=lambda x: x[0], reverse=True)

        filtered = [(score, item) for score, item in results if score >= threshold]

        if filtered:
            return {
                "message": "Relevant results found",
                "results": [item for score, item in filtered[:top_k]]
            }
        else:
            return {
                "message": "No exact match found, showing closest results",
                "results": [item for score, item in results[:top_k]]
            }

    # IMAGE → IMAGE
    def image_to_image(self, image_path, top_k=3):
        query_embedding = self.embedder.embed_image(image_path)

        results = []
        for item in self.data:
            img_emb = np.array(item["embedding"])
            score = self.cosine_similarity(query_embedding, img_emb)
            results.append((score, item))

        threshold = 0.7
        results.sort(key=lambda x: x[0], reverse=True)

        filtered = [(score, item) for score, item in results if score >= threshold]

        if filtered:
            return {
                "message": "Relevant results found",
                "results": [item for score, item in filtered[:top_k]]
            }
        else:
            return {
                "message": "No exact match found, showing closest results",
                "results": [item for score, item in results[:top_k]]
            }

    # IMAGE → TEXT
    def image_to_text(self, image_path, top_k=3):

        ocr_result = self.ocr.extract_text(image_path)

        if isinstance(ocr_result, dict):
            ocr_text = ocr_result.get("text", "")
        else:
            ocr_text = ocr_result

        caption = self.captioner.generate_caption(image_path)

        similar_images = self.image_to_image(image_path, top_k)

        answer = f"Caption: {caption}\n\n"
        answer += f"OCR Text:\n{ocr_text}\n\n"

        answer += similar_images["message"] + "\n"
        answer += "Similar Images:\n"

        for i, item in enumerate(similar_images["results"]):
            answer += f"\n---------- Result {i+1} ----------\n"
            answer += f"\nImage: {item['image']}\n"
            answer += f"Caption: {item['caption']}\n"

            ocr_text_item = item.get("ocr_text", "")

            if isinstance(ocr_text_item, dict):
                ocr_text_item = ocr_text_item.get("text", "")

            answer += f"OCR Text: {ocr_text_item}\n"

        return answer.strip()


if __name__ == "__main__":
    searcher = ImageSearch()

    print("\n MULTIMODAL IMAGE SEARCH\n")
    print("Choose mode:")
    print("1. Text → Image")
    print("2. Image → Image")
    print("3. Image → Text Answer")

    choice = input("\nEnter choice (1/2/3): ")

    if choice == "1":
        query = input("\nEnter text query: ")
        results = searcher.text_to_image(query)

        print("\n Top Results:\n")
        print(results["message"])

        for i, r in enumerate(results["results"]):
            print(f"Result {i+1}:")
            print("Image:", r["image"])
            print("Caption:", r["caption"])
            print("-" * 50)

    elif choice == "2":
        image_path = input("\nEnter image path: ")

        if not os.path.exists(image_path):
            print(" File not found")
        else:
            results = searcher.image_to_image(image_path)

            print("\n Similar Images:\n")
            print(results["message"])

            for i, r in enumerate(results["results"]):
                print(f"Result {i+1}:")
                print("Image:", r["image"])
                print("Caption:", r["caption"])
                print("-" * 50)

    elif choice == "3":
        image_path = input("\nEnter image path: ")

        if not os.path.exists(image_path):
            print(" File not found")
        else:
            answer = searcher.image_to_text(image_path)

            print("\n Generated Answer:\n")
            print(answer)

    else:
        print(" Invalid choice")