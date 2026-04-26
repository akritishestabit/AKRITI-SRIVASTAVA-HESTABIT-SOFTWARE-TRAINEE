import sqlite3


class SchemaLoader:
    def __init__(self, db_path="src/data/database.db"):
        self.db_path = db_path

    def get_schema(self):
        """
        Returns database schema as dictionary
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        schema = {}

        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table';"
        )
        tables = cursor.fetchall()

        for table in tables:
            table_name = table[0]

            
            if table_name.startswith("sqlite_"):
                continue

        
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns_info = cursor.fetchall()

            columns = [col[1] for col in columns_info]

            schema[table_name] = columns

        conn.close()

        return schema

    def get_schema_text(self):
        """
        Returns schema in text format (for LLM prompt)
        """
        schema = self.get_schema()

        schema_text = ""

        for table, columns in schema.items():
            schema_text += f"Table: {table}\n"
            schema_text += f"Columns: {', '.join(columns)}\n\n"

        return schema_text.strip()



if __name__ == "__main__":
    loader = SchemaLoader()

    print("\n DATABASE SCHEMA\n")

    schema = loader.get_schema()

    for table, cols in schema.items():
        print(f"\nTable: {table}")
        print("Columns:", ", ".join(cols))