import sqlite3
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("src/data/database.db")
cursor = conn.cursor()

# ---------------------------
# EMPLOYEES TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

employees_data = [
    (1, "Alice", "Engineering", 80000),
    (2, "Bob", "HR", 50000),
    (3, "Charlie", "Engineering", 90000),
    (4, "David", "Sales", 60000),
]

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", employees_data)

# ---------------------------
# SALES TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    year INTEGER,
    revenue INTEGER
)
""")

sales_data = [
    (1, "Laptop", 2023, 50000),
    (2, "Phone", 2023, 30000),
    (3, "Laptop", 2022, 20000),
    (4, "Tablet", 2023, 40000),
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?)", sales_data)

# ---------------------------
# CUSTOMERS TABLE
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    country TEXT,
    age INTEGER
)
""")

customers_data = [
    (1, "John", "India", 28),
    (2, "Emma", "USA", 32),
    (3, "Raj", "India", 25),
    (4, "Sophia", "UK", 30),
]

cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers_data)

conn.commit()
conn.close()

print("Database with multiple tables created successfully!")