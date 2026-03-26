import re
import os
from config.settings import CLEANED_DATA_PATH

def clean_text(text):
    
    text = re.sub(r'\s+', ' ', text)

   
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    return text.strip()


def save_cleaned_documents(documents):
    cleaned_docs = []

    for idx, doc in enumerate(documents):
        cleaned = clean_text(doc["text"])

      
        filename = f"cleaned_{idx}.txt"
        filepath = os.path.join(CLEANED_DATA_PATH, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(cleaned)

       
        doc["text"] = cleaned

        cleaned_docs.append(doc)

    return cleaned_docs