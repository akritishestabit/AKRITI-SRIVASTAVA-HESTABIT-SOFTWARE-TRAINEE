from sentence_transformers import SentenceTransformer
from PIL import Image
import numpy as np


class CLIPEmbedder:
    def __init__(self, model_name="clip-ViT-B-32"):
        
        self.model = SentenceTransformer(model_name)

    def embed_image(self, image_path):
        """
        Convert image → embedding vector
        """
        image = Image.open(image_path).convert("RGB")

        embedding = self.model.encode(image)

        return np.array(embedding)

    def embed_text(self, text):
        """
        Convert text → embedding vector
        """
        embedding = self.model.encode(text)

        return np.array(embedding)
    
if __name__ == "__main__":
    embedder = CLIPEmbedder()

    print("Choose input type:")
    print("1. Image")
    print("2. Text")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        image_path = input("Enter image path: ")

        try:
            vec = embedder.embed_image(image_path)
            print("\n Image embedding generated!")
            print("Shape:", vec.shape)
        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        text = input("Enter text: ")

        vec = embedder.embed_text(text)
        print("\n Text embedding generated!")
        print("Shape:", vec.shape)

    else:
        print("Invalid choice")