import sqlite3
from src.generator.sql_generator import SQLGenerator


class SQLPipeline:
    def __init__(self, db_path="src/data/database.db"):
        self.db_path = db_path
        self.generator = SQLGenerator()

    
    def validate_query(self, sql):
        """
        Allow only safe SELECT queries
        """
        sql = sql.lower()

        if not sql.strip().startswith("select"):
            return False

        forbidden = ["drop", "delete", "update", "insert", "alter"]

        for word in forbidden:
            if word in sql:
                return False

        return True

    
    def execute_query(self, sql):
        """
        Execute SQL on database
        """
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute(sql)

            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            conn.close()

            return columns, rows

        except Exception as e:
            return None, str(e)

   
    def summarize_result(self, columns, rows):
        """
        Convert result table into readable answer
        """
        if not rows:
            return "No data found."

        result = ""

        for row in rows:
            line = ", ".join(f"{col}: {val}" for col, val in zip(columns, row))
            result += line + "\n"

        return result.strip()

    
    def run(self, question):
        print("\n User Question:", question)

        # Step 1: Generate SQL
        sql = self.generator.generate_sql(question)
        print("\n Generated SQL:\n", sql)

        # Step 2: Validate
        if not self.validate_query(sql):
            return " Unsafe or invalid SQL query."

        # Step 3: Execute
        columns, result = self.execute_query(sql)

        if columns is None:
            return f" SQL Error: {result}"

        # Step 4: Summarize
        answer = self.summarize_result(columns, result)

        return answer


# ---------------------------
# INTERACTIVE MODE 🔥
# ---------------------------
if __name__ == "__main__":
    pipeline = SQLPipeline()

    print("\n SQL QUESTION ANSWERING SYSTEM\n")

    while True:
        question = input("\nEnter your question (or 'exit'): ")

        if question.lower() == "exit":
            break

        answer = pipeline.run(question)

        print("\n Answer:\n")
        print(answer)