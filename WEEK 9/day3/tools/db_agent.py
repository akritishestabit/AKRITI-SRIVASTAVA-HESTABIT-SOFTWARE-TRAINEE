import autogen
import sqlite3
import json
import os
from config import llm_config

def run_sql_query(db_path: str, query: str) -> str:
    def resolve_db_path(path: str) -> str:
        for prefix in ["", "data/", "nexus_ai/data/", "../data/"]:
            test_path = os.path.join(prefix, path.split('/')[-1])
            if os.path.exists(test_path):
                return test_path
        return path

    db_path = resolve_db_path(db_path)
    if not os.path.exists(db_path):
        return f"[DB Error] Database file not found: '{db_path}'. Make sure to provide the full relative path from the script execution directory."


    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(query)

        if query.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            if not rows:
                return "[DB Result] Query returned no rows."
            data = [dict(row) for row in rows]
            conn.close()
            return json.dumps(data, indent=2, default=str)

        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return f"[DB Result] Query executed successfully. Rows affected: {affected}"

    except sqlite3.Error as e:
        return f"[DB Error] {str(e)}"

def get_schema(db_path: str) -> str:
    """
    Retrieve the full schema of a SQLite database:
    all table names, column names, types, PK flags, and nullability.
    """
    def resolve_db_path(path: str) -> str:
        for prefix in ["", "data/", "nexus_ai/data/", "../data/"]:
            test_path = os.path.join(prefix, path.split('/')[-1])
            if os.path.exists(test_path):
                return test_path
        return path

    db_path = resolve_db_path(db_path)
    if not os.path.exists(db_path):
        return f"[DB Error] Database file not found: '{db_path}'. Make sure to provide the full relative path from the script execution directory."

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tables = [row[0] for row in cursor.fetchall()]

        if not tables:
            conn.close()
            return "[DB Schema] Database is empty — no tables found."

        schema_lines = [f"Database: {db_path}", f"Tables ({len(tables)}):\n"]

        for table in tables:
            cursor.execute(f"PRAGMA table_info('{table}');")
            columns = cursor.fetchall()
            schema_lines.append(f"  TABLE: {table}")

            for col in columns:
                pk_flag   = " [PK]"       if col[5] else ""
                nullable  = ""            if col[3] else " [NULLABLE]"
                default   = f" DEFAULT={col[4]}" if col[4] is not None else ""
                schema_lines.append(
                    f"    - {col[1]:25s} {col[2]:15s}{pk_flag}{nullable}{default}"
                )
            cursor.execute(f"PRAGMA foreign_key_list('{table}');")
            fks = cursor.fetchall()
            if fks:
                for fk in fks:
                    schema_lines.append(
                        f"    FK: {fk[3]} → {fk[2]}.{fk[4]}"
                    )

            schema_lines.append("") 

        conn.close()
        return "\n".join(schema_lines)

    except sqlite3.Error as e:
        return f"[DB Error] {str(e)}"

db_agent = autogen.ConversableAgent(
    name="DB_Agent",
    system_message=(
        "You are a Database Agent specializing in SQLite querying and data extraction.\n\n"

        "Available Tools:\n"
        "1. `get_schema(db_path)` — Inspect all tables, columns, types, PKs, and FKs\n"
        "2. `run_sql_query(db_path, query)` — Execute any SQL query\n\n"

        "Mandatory Workflow (ALWAYS follow this order):\n"
        "Step 1 → Call `get_schema` FIRST — NEVER skip this\n"
        "Step 2 → Write SQL using ONLY the column/table names from the schema\n"
        "Step 3 → Call `run_sql_query` with your query\n"
        "Step 4 → Interpret and summarize the results\n\n"

        "SQL Writing Rules:\n"
        "- NEVER assume column or table names — verify via get_schema first\n"
        "- Use proper SQLite syntax (no LIMIT outside SELECT)\n"
        "- For aggregations use GROUP BY correctly\n"
        "- Use LOWER() for case-insensitive string comparisons\n"
        "- Handle NULLs with COALESCE or IS NOT NULL filters\n"
        "- If a query fails, read the error carefully, fix the SQL, and retry once\n\n"

        "Strict Rules:\n"
        "- NEVER fabricate query results\n"
        "- DO NOT call get_schema more than once per task\n"
        "- DO NOT run destructive queries (DROP, DELETE, TRUNCATE) unless explicitly asked\n\n"

        "Output Format:\n"
        "```\n"
        "[Schema Inspected]\n"
        "<schema output>\n\n"
        "[SQL Query]\n"
        "<your SQL query>\n\n"
        "[Query Result]\n"
        "<JSON data from tool>\n\n"
        "[Analysis]\n"
        "<clear interpretation of the data>\n"
        "```"
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)

db_agent.register_for_llm(
    name="run_sql_query",
    description=(
        "Execute a SQL query on a SQLite database at db_path. "
        "Returns JSON rows for SELECT queries, or a rows-affected message for write queries."
    )
)(run_sql_query)

db_agent.register_for_llm(
    name="get_schema",
    description=(
        "Retrieve the complete schema of a SQLite database: "
        "all table names, column names, data types, primary keys, and foreign keys."
    )
)(get_schema)


db_agent.register_for_execution(name="run_sql_query")(run_sql_query)
db_agent.register_for_execution(name="get_schema")(get_schema)