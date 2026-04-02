# import sqlite3
# from src.generator.sql_generator import SQLGenerator
# from src.evaluation.rag_eval import RAGEvaluator
# from src.evaluation.refiner import Refiner


# class SQLPipeline:
#     def __init__(self, db_path="src/data/database.db"):
#         self.db_path = db_path
#         self.generator = SQLGenerator()
#         self.evaluator = RAGEvaluator()
#         self.refiner = Refiner()

    
#     def validate_query(self, sql):
#         """
#         Allow only safe SELECT queries
#         """
#         sql = sql.lower()

#         if not sql.strip().startswith("select"):
#             return False

#         forbidden = ["drop", "delete", "update", "insert", "alter"]

#         for word in forbidden:
#             if word in sql:
#                 return False

#         return True

    
#     def execute_query(self, sql):
#         """
#         Execute SQL on database
#         """
#         try:
#             conn = sqlite3.connect(self.db_path)
#             cursor = conn.cursor()

#             cursor.execute(sql)

#             rows = cursor.fetchall()
#             columns = [desc[0] for desc in cursor.description]

#             conn.close()

#             return columns, rows

#         except Exception as e:
#             return None, str(e)

   
#     def summarize_result(self, columns, rows):
#         """
#         Convert result table into readable answer
#         """
#         if not rows:
#             return "No data found."

#         result = ""

#         for row in rows:
#             line = ", ".join(f"{col}: {val}" for col, val in zip(columns, row))
#             result += line + "\n"

#         return result.strip()

    
#     def run(self, question):
#         print("\n User Question:", question)

#         # Step 1: Generate SQL
#         sql = self.generator.generate_sql(question)
#         print("\n Generated SQL:\n", sql)

#         # Step 2: Validate
#         if not self.validate_query(sql):
#             return " Unsafe or invalid SQL query."

#         # Step 3: Execute
#         columns, result = self.execute_query(sql)

#         if columns is None:
#             return f" SQL Error: {result}"

#         # Step 4: Summarize
#         # Step 4: Summarize
#         answer = self.summarize_result(columns, result)

#         # Step 5: Evaluate
#         context = " ".join([str(r) for r in result])  # simple context
#         eval_result = self.evaluator.evaluate(context, answer)

#         print("\n📊 Evaluation:", eval_result)

#         # Step 6: Refinement (if needed)
#         if not eval_result["faithful"]:
#             print("\n🔁 Refining answer...")
#             answer = self.refiner.refine(question, context, answer)

#         # Step 7: Final output
#         return f"{answer}\n\nConfidence: {eval_result['confidence']}"

# # ---------------------------
# # INTERACTIVE MODE 🔥
# # ---------------------------
# if __name__ == "__main__":
#     pipeline = SQLPipeline()

#     print("\n SQL QUESTION ANSWERING SYSTEM\n")

#     while True:
#         question = input("\nEnter your question (or 'exit'): ")

#         if question.lower() == "exit":
#             break

#         answer = pipeline.run(question)

#         print("\n Answer:\n")
#         print(answer)

import sqlite3
from src.generator.sql_generator import SQLGenerator
from src.evaluation.rag_eval import RAGEvaluator
from src.evaluation.refiner import Refiner


class SQLPipeline:
    def __init__(self, db_path="src/data/database.db"):
        self.db_path = db_path
        self.generator = SQLGenerator()
        self.evaluator = RAGEvaluator()
        self.refiner = Refiner()

    
    def validate_query(self, sql):
        sql = sql.lower()

        if not sql.strip().startswith("select"):
            return False

        forbidden = ["drop", "delete", "update", "insert", "alter"]

        for word in forbidden:
            if word in sql:
                return False

        return True

    
    def execute_query(self, sql):
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
        if not rows:
            return "No data found."

        result = ""

        for row in rows:
            line = ", ".join(f"{col}: {val}" for col, val in zip(columns, row))
            result += line + "\n"

        return result.strip()

    
    def run(self, question):
        print("\n User Question:", question)

       
        sql = self.generator.generate_sql(question)
        print("\n Generated SQL:\n", sql)

        
        if not self.validate_query(sql):
            return " Unsafe or invalid SQL query."

       
        columns, result = self.execute_query(sql)

        if columns is None:
            return f" SQL Error: {result}"

        
        print("\n Raw Execution Result:\n")
        for row in result:
            print(row)

        
        answer = self.summarize_result(columns, result)

        
        context = " ".join([str(r) for r in result])
        eval_result = self.evaluator.evaluate(context, answer)

        print("\n Evaluation:", eval_result)

        
        if not eval_result["faithful"]:
            print("\n Refining answer...")
            answer = self.refiner.refine(question, context, answer)

        
        return f"{answer}\n\nConfidence: {eval_result['confidence']}"



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