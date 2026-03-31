from transformers import pipeline


class SQLGenerator:
    def __init__(self):
        # Lightweight model (replace with better if needed)
        self.generator = pipeline(
            "text-generation",
            model="gpt2"
        )

    # ---------------------------
    # Prompt Builder (IMPROVED 🔥)
    # ---------------------------
    def build_prompt(self, schema, question):
        prompt = f"""
You are an expert SQL generator.

Strict Rules:
- Only use given tables and columns
- Do NOT hallucinate tables or columns
- Only return SQL query
- Do NOT explain anything
- Use correct SQL syntax

Schema:
{schema}

Question:
{question}

SQL:
"""
        return prompt.strip()

    # ---------------------------
    # Clean SQL Output 🔥
    # ---------------------------
    def clean_sql(self, text):
        lines = text.split("\n")

        sql_lines = []
        for line in lines:
            line = line.strip()

            # Keep only SQL lines
            if line.upper().startswith("SELECT") or \
               line.upper().startswith("FROM") or \
               line.upper().startswith("WHERE") or \
               line.upper().startswith("GROUP BY") or \
               line.upper().startswith("ORDER BY"):
                sql_lines.append(line)

        return " ".join(sql_lines)

    # ---------------------------
    # Generate SQL
    # ---------------------------
    def generate_sql(self, schema, question):
        prompt = self.build_prompt(schema, question)

        output = self.generator(
            prompt,
            max_length=150,
            num_return_sequences=1,
            truncation=True
        )

        generated_text = output[0]["generated_text"]

        # Remove prompt part
        sql_part = generated_text.replace(prompt, "").strip()

        # Clean SQL
        sql = self.clean_sql(sql_part)

        return sql if sql else "SELECT * FROM sales;"



# ---------------------------
# INTERACTIVE TEST 🔥
# ---------------------------
if __name__ == "__main__":
    generator = SQLGenerator()

    print("\n🧾 SQL GENERATOR TEST\n")

    # Example schema (later dynamic होगा)
    schema = """
Table: sales
Columns: id, artist, year, amount

Table: employees
Columns: id, name, department, salary
"""

    question = input("Enter your question: ")

    sql = generator.generate_sql(schema, question)

    print("\n✅ Generated SQL:\n")
    print(sql)