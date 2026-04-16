import os
import pandas as pd
from pypdf import PdfReader
from docx import Document
from src.config.settings import RAW_DATA_PATH

def load_files():
    documents = []

    for file in os.listdir(RAW_DATA_PATH):
        file_path = os.path.join(RAW_DATA_PATH, file)

        
        if file.endswith(".pdf"):
            reader = PdfReader(file_path)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text and text.strip():
                    documents.append({
                        "text": text,
                        "source": file,
                        "page": i,
                        "type": "pdf"
                    })

        
        elif file.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append({
                    "text": text,
                    "source": file,
                    "page": 0,
                    "type": "txt"
                })

        
        elif file.endswith(".docx"):
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])

            documents.append({
                "text": text,
                "source": file,
                "page": 0,
                "type": "docx"
            })

       
        elif file.endswith(".csv"):
            df = pd.read_csv(file_path)

            for i, row in df.iterrows():
                text = ", ".join([f"{col} is {row[col]}" for col in df.columns])

                documents.append({
                    "text": text,
                    "source": file,
                    "page": i,
                    "type": "csv"
                 })

    return documents