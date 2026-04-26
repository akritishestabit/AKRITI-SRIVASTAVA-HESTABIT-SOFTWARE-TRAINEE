import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class RAGEvaluator:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    
    def embed(self, text):
        return self.model.encode([text])

    
    def context_score(self, context, answer):
        context_emb = self.embed(context)
        answer_emb = self.embed(answer)

        score = cosine_similarity(context_emb, answer_emb)[0][0]
        return float(score)

   
    def is_faithful(self, context, answer, threshold=0.5):
        score = self.context_score(context, answer)

        if score >= threshold:
            return True, score
        else:
            return False, score

   
    def evaluate(self, context, answer):
        faithful, score = self.is_faithful(context, answer)

        result = {
            "faithful": faithful,
            "context_score": round(score, 3),
            "confidence": round(score, 3)
        }

       
        if not faithful:
            result["warning"] = "Possible hallucination detected"

        return result



if __name__ == "__main__":
    evaluator = RAGEvaluator()

    print("\n RAG EVALUATION TEST\n")

    context = input("Enter context: ")
    answer = input("Enter answer: ")

    result = evaluator.evaluate(context, answer)

    print("\n Evaluation Result:\n")
    print(result)