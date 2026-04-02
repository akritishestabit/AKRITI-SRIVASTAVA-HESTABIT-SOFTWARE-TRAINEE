from src.pipelines.sql_pipeline import SQLPipeline
from src.memory.memory_store import MemoryStore




class GenAIApp:
    def __init__(self):
        self.sql_pipeline = SQLPipeline()
        self.memory = MemoryStore()

        
    def ask_text(self, question):
        
        return "Text RAG not integrated yet."

    
    def ask_sql(self, question):
        return self.sql_pipeline.run(question)

    
    def ask_image(self, query):
        # Placeholder (connect image_search later)
        return "Image RAG not integrated yet."

    
    def handle_query(self, mode, query):
        # Save user query
        self.memory.add_message("user", query)

        if mode == "text":
            answer = self.ask_text(query)

        elif mode == "sql":
            answer = self.ask_sql(query)

        elif mode == "image":
            answer = self.ask_image(query)

        else:
            answer = "Invalid mode selected."

        # Save response
        self.memory.add_message("assistant", answer)

        return answer



if __name__ == "__main__":
    app = GenAIApp()

    print("\n GENAI SYSTEM (DAY 5 CAPSTONE)\n")

    while True:
        print("\nChoose mode:")
        print("1. Text RAG")
        print("2. SQL QA")
        print("3. Image RAG")
        print("4. Exit")

        choice = input("\nEnter choice: ")

        if choice == "4":
            break

        query = input("\nEnter your query: ")

        if choice == "1":
            mode = "text"
        elif choice == "2":
            mode = "sql"
        elif choice == "3":
            mode = "image"
        else:
            print("Invalid choice")
            continue

        answer = app.handle_query(mode, query)

        print("\n Answer:\n")
        print(answer)