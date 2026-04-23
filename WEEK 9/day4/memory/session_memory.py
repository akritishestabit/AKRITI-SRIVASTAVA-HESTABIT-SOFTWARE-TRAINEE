import sqlite3
import os

class MemoryManager:
    
    def __init__(self, db_path="memory/long_term.db"):
        self.db_path = db_path
        self.short_term_history = []
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS conversation_log
                     (id INTEGER PRIMARY KEY, role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

    def add_message(self, role: str, content: str):
        """Saves message to RAM and persistent sequential database."""
        self.short_term_history.append({"role": role, "content": content})
        
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("INSERT INTO conversation_log (role, content) VALUES (?, ?)", (role, content))
        conn.commit()
        conn.close()

    def get_short_term_context(self, k=6):
        """Retrieves exactly the last `k` turns from active runtime RAM."""
        return self.short_term_history[-k:]

    def clear_short_term(self):
        """Simulates beginning a new session while keeping long term intact."""
        self.short_term_history = []
