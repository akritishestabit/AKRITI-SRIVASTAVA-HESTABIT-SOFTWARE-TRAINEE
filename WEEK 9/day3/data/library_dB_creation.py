import sqlite3

conn = sqlite3.connect("data/library.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    genre TEXT,
    issued INTEGER
)
""")

cur.executemany("""
INSERT INTO books (title, author, genre, issued) VALUES (?, ?, ?, ?)
""", [
    ("1984", "Orwell", "Dystopian", 12),
    ("Harry Potter", "Rowling", "Fantasy", 30),
    ("Alchemist", "Coelho", "Fiction", 20),
    ("Sapiens", "Harari", "History", 15),
])

conn.commit()
conn.close()