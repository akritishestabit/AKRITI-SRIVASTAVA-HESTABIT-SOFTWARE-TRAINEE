import autogen
import sqlite3
import json
import os
from config import llm_config

def run_sql_query(db_path: str, query: str) -> str:
    if not os.path.exists(db_path):
        return f"[DB Error] Database file not found: '{db_path}'"

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
    if not os.path.exists(db_path):
        return f"[DB Error] Database file not found: '{db_path}'"

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
                pk_flag = " [PK]" if col[5] else ""
                nullable = "" if col[3] else " [NULLABLE]"
                schema_lines.append(
                    f"    - {col[1]:20s} {col[2]:15s}{pk_flag}{nullable}"
                )

            schema_lines.append("")

        conn.close()
        return "\n".join(schema_lines)

    except sqlite3.Error as e:
        return f"[DB Error] {str(e)}"


# ─────────────────────────────────────────────
#  AGENT DEFINITION
# ─────────────────────────────────────────────

db_agent = autogen.ConversableAgent(
    name="DB_Agent",
    system_message=(
        "You are a Database Agent specializing in SQLite querying and data extraction.\n\n"

        "Your Responsibilities:\n"
        "- Inspect database schemas using `get_schema`\n"
        "- Execute SQL queries using `run_sql_query`\n"
        "- Always inspect the schema FIRST before writing queries\n"
        "- Write correct, optimized SQL based on the task\n\n"

        "Strict Rules:\n"
        "- ALWAYS call `get_schema` before writing SELECT queries\n"
        "- NEVER assume column or table names — verify via schema tool first\n"
        "- Handle errors gracefully — if a query fails, fix and retry\n"
        "- Return clean JSON data + your interpretation\n\n"

        "Output Format:\n"
        "```\n"
        "[Schema Inspected]\n"
        "<schema output>\n\n"
        "[SQL Query]\n"
        "<your SQL query>\n\n"
        "[Query Result]\n"
        "<JSON data from tool>\n\n"
        "[Analysis]\n"
        "<interpretation of the data>\n"
        "```"
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)


# ─────────────────────────────────────────────
#  TOOL REGISTRATION
# ─────────────────────────────────────────────

db_agent.register_for_llm(
    name="run_sql_query",
    description="Execute SQL query on SQLite DB"
)(run_sql_query)

db_agent.register_for_llm(
    name="get_schema",
    description="Get database schema"
)(get_schema)


db_agent.register_for_execution(name="run_sql_query")(run_sql_query)
db_agent.register_for_execution(name="get_schema")(get_schema)