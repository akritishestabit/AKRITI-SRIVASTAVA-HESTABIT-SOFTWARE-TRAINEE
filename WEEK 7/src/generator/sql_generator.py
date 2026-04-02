from groq import Groq
from src.utils.schema_loader import SchemaLoader
import os


class SQLGenerator:
    def __init__(self):
        self.schema_loader = SchemaLoader()
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def build_prompt(self, question, schema_text):
        prompt = f"""
You are an expert SQL generator.

Given the database schema below, generate a correct SQL query.

Schema:
{schema_text}

Rules:
- Only use available tables and columns
- Only generate SELECT queries
- Do NOT use DROP, DELETE, UPDATE, INSERT

User Question:
{question}

SQL Query:
"""
        return prompt.strip()

    def generate_sql(self, question):
        schema_text = self.schema_loader.get_schema_text()
        prompt = self.build_prompt(question, schema_text)

        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",  
                messages=[
                    {"role": "system", "content": "You generate SQL queries only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )

            sql = response.choices[0].message.content.strip()

            # clean formatting
            sql = sql.replace("```sql", "").replace("```", "").strip()

            return sql

        except Exception as e:
            print(" GROQ ERROR:", e)
            print(" Using fallback...")

            q = question.lower()

            if "salary" in q:
                return "SELECT * FROM employees WHERE salary > 70000;"
            elif "revenue" in q:
                return "SELECT SUM(revenue) FROM sales WHERE year = 2023;"
            elif "india" in q:
                return "SELECT * FROM customers WHERE country = 'India';"

            return "SELECT * FROM employees;"