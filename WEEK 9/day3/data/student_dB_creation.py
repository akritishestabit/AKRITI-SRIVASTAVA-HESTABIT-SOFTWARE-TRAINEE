import sqlite3

conn = sqlite3.connect("data/student.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT,
    marks INTEGER
)
""")

cur.executemany("""
INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)
""", [
    ("Aarav", 20, "CS", 88),
    ("Diya", 21, "IT", 92),
    ("Rohan", 19, "CS", 75),
    ("Meera", 22, "AI", 95),
    ("Kabir", 20, "IT", 67),
])

conn.commit()
conn.close()