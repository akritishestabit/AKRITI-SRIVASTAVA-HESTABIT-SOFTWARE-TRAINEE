import sqlite3


class SchemaLoader:
    def __init__(self, db_path):
        self.db_path = db_path

   
    def get_tables(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]

        conn.close()
        return tables

    
    def get_columns(self, table_name):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = [row[1] for row in cursor.fetchall()]

        conn.close()
        return columns

    
    def get_schema(self):
        tables = self.get_tables()

        schema_lines = []

        for table in tables:
            columns = self.get_columns(table)

            line = f"Table: {table}\nColumns: {', '.join(columns)}"
            schema_lines.append(line)

        return "\n\n".join(schema_lines)



if __name__ == "__main__":
    print("\n📊 SCHEMA LOADER TEST\n")

    db_path = input("Enter DB path (e.g., src/data/sample.db): ")

    loader = SchemaLoader(db_path)

    schema = loader.get_schema()

    print("\n📋 Extracted Schema:\n")
    print(schema)