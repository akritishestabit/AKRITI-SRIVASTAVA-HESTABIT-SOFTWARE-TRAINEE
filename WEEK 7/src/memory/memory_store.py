import json
import os


class MemoryStore:
    def __init__(self, file_path="CHAT-LOGS.json", max_messages=5):
        self.file_path = file_path
        self.max_messages = max_messages
        self.memory = self.load_memory()

    
    def load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                return json.load(f)
        return []

   
    def save_memory(self):
        with open(self.file_path, "w") as f:
            json.dump(self.memory, f, indent=4)

    
    def add_message(self, role, content):
        self.memory.append({
            "role": role,
            "content": content
        })

        
        self.memory = self.memory[-self.max_messages:]

        self.save_memory()

    
    def get_memory(self):
        return self.memory

    
    def get_context(self):
        context = ""

        for msg in self.memory:
            context += f"{msg['role']}: {msg['content']}\n"

        return context.strip()

   
    def clear_memory(self):
        self.memory = []
        self.save_memory()



if __name__ == "__main__":
    memory = MemoryStore()

    print("\n MEMORY TEST MODE\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        
        memory.add_message("user", user_input)

        
        response = "This is a test response."

        memory.add_message("assistant", response)

        print("\n Current Memory:\n")
        print(memory.get_context())