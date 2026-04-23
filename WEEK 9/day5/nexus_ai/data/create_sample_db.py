import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "sample.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL,
    hire_date DATE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    budget REAL
)
''')

cursor.execute('DELETE FROM employees')
cursor.execute('DELETE FROM projects')

# Insert Employees
employees_data = [
    ("Alice Smith", "Engineering", 120000, "2021-03-15"),
    ("Bob Johnson", "Marketing", 85000, "2022-07-22"),
    ("Charlie Davis", "Engineering", 115000, "2023-01-10"),
    ("Diana Prince", "Sales", 95000, "2020-11-05"),
    ("Evan Wright", "HR", 70000, "2021-08-30")
]
cursor.executemany("INSERT INTO employees (name, department, salary, hire_date) VALUES (?, ?, ?, ?)", employees_data)

# Insert Projects
projects_data = [
    ("Project Alpha", "Active", 500000),
    ("Project Beta", "Completed", 150000),
    ("Project Gamma", "Planning", 250000)
]
cursor.executemany("INSERT INTO projects (name, status, budget) VALUES (?, ?, ?)", projects_data)


conn.commit()
conn.close()

print(f" Successfully created sample.db at: {db_path}")
print("Inserted 5 employees and 3 projects for testing.")
