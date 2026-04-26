from groq import Groq
import os


class Refiner:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def refine(self, question, context, answer):
        prompt = f"""
You are a system that improves answers.

Question:
{question}

Context:
{context}

Current Answer:
{answer}

If the answer is incorrect or incomplete, rewrite it using the context.
If correct, return the same answer.

Final Answer:
"""

        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You refine answers based on context."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )

            refined = response.choices[0].message.content.strip()

            return refined

        except Exception as e:
            print(" Refinement failed:", e)
            return answer