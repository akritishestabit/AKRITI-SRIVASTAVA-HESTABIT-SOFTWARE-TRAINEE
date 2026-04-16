import json
import os
from collections import deque
from datetime import datetime


class MemoryStore:
    def __init__(self, memory_path="memory/chat_memory.json", max_messages=5):
        self.memory_path = memory_path
        self.max_messages = max_messages

        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)

        if not os.path.exists(self.memory_path):
            with open(self.memory_path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)

    def load_memory(self):
        try:
            with open(self.memory_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return deque(data, maxlen=self.max_messages)
        except Exception:
            return deque(maxlen=self.max_messages)

    def save_memory(self, memory):
        with open(self.memory_path, "w", encoding="utf-8") as f:
            json.dump(list(memory), f, indent=4)

    def add_message(self, role, content):
        memory = self.load_memory()

        memory.append(
            {
                "role": role,
                "content": content,
                "timestamp": datetime.now().isoformat()
            }
        )

        self.save_memory(memory)

    def get_recent_context(self):
        memory = self.load_memory()

        if not memory:
            return ""

        context = []
        for msg in memory:
            context.append(f"{msg['role']}: {msg['content']}")

        return "\n".join(context)

    def clear_memory(self):
        self.save_memory(deque(maxlen=self.max_messages))


if __name__ == "__main__":
    memory = MemoryStore()

    print("\nMEMORY TEST MODE\n")

    while True:
        msg = input("Enter message (or 'exit'): ")

        if msg.lower() == "exit":
            break

        memory.add_message("user", msg)

        print("\nRecent Memory:\n")
        print(memory.get_recent_context())
