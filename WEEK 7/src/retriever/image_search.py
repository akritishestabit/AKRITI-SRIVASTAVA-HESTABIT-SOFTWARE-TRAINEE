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

        # Load stored data
        with open(self.data_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    # ---------------------------
    # Similarity Function
    # ---------------------------
    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # ---------------------------
    # TEXT → IMAGE
    # ---------------------------
    def text_to_image(self, query, top_k=3):
        query_embedding = self.embedder.embed_text(query)

        results = []
        for item in self.data:
            img_emb = np.array(item["embedding"])
            score = self.cosine_similarity(query_embedding, img_emb)
            results.append((score, item))

        results.sort(key=lambda x: x[0], reverse=True)

        return [item for score, item in results[:top_k]]

    # ---------------------------
    # IMAGE → IMAGE
    # ---------------------------
    def image_to_image(self, image_path, top_k=3):
        query_embedding = self.embedder.embed_image(image_path)

        results = []
        for item in self.data:
            img_emb = np.array(item["embedding"])
            score = self.cosine_similarity(query_embedding, img_emb)
            results.append((score, item))

        results.sort(key=lambda x: x[0], reverse=True)

        return [item for score, item in results[:top_k]]

    # ---------------------------
    # IMAGE → TEXT (UPGRADED )
    # ---------------------------
    def image_to_text(self, image_path, top_k=3):
        # Step 1: Get similar images
        similar_images = self.image_to_image(image_path, top_k)

        # Step 2: Combine knowledge
        combined_answer = ""

        for i, item in enumerate(similar_images):
            combined_answer += f"\n--- Result {i+1} ---\n"
            combined_answer += f"Image: {item['image']}\n"
            combined_answer += f"Caption: {item['caption']}\n"
            combined_answer += f"OCR Text: {item['ocr_text'][:200]}\n"

        return combined_answer.strip()


# ---------------------------
# INTERACTIVE MODE 
# ---------------------------
if __name__ == "__main__":
    searcher = ImageSearch()

    print("\n MULTIMODAL IMAGE SEARCH\n")
    print("Choose mode:")
    print("1. Text → Image")
    print("2. Image → Image")
    print("3. Image → Text Answer")

    choice = input("\nEnter choice (1/2/3): ")

    # ---------------------------
    # TEXT → IMAGE
    # ---------------------------
    if choice == "1":
        query = input("\nEnter text query: ")
        results = searcher.text_to_image(query)

        print("\n Top Results:\n")
        for i, r in enumerate(results):
            print(f"Result {i+1}:")
            print("Image:", r["image"])
            print("Caption:", r["caption"])
            print("-" * 50)

    # ---------------------------
    # IMAGE → IMAGE
    # ---------------------------
    elif choice == "2":
        image_path = input("\nEnter image path: ")

        if not os.path.exists(image_path):
            print(" File not found")
        else:
            results = searcher.image_to_image(image_path)

            print("\n Similar Images:\n")
            for i, r in enumerate(results):
                print(f"Result {i+1}:")
                print("Image:", r["image"])
                print("Caption:", r["caption"])
                print("-" * 50)

    # ---------------------------
    # IMAGE → TEXT
    # ---------------------------
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