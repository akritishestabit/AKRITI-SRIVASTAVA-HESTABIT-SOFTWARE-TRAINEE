import autogen
import csv
import os
import json
import io
from config import llm_config

def read_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        return f"[File Error] File not found: '{file_path}'"

    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".csv":
            with open(file_path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            if not rows:
                return "[File Result] CSV is empty — no data rows found."

            return (
                f"[File Read] CSV file: {file_path}\n"
                f"Rows: {len(rows)} | Columns: {list(rows[0].keys())}\n\n"
                f"{json.dumps(rows, indent=2, default=str)}"
            )

        elif ext == ".txt":
            with open(file_path, encoding="utf-8") as f:
                content = f.read()
            return (
                f"[File Read] TXT file: {file_path}\n"
                f"Characters: {len(content)} | Lines: {content.count(chr(10)) + 1}\n\n"
                f"{content}"
            )

        else:
            return f"[File Error] Unsupported file type '{ext}'. Only .txt and .csv are supported."

    except Exception as e:
        return f"[File Error] Could not read '{file_path}': {str(e)}"

def query_csv(file_path: str, operation: str, column: str = "", value: str = "", top_n: int = 5) -> str:
    if not os.path.exists(file_path):
        return f"[CSV Error] File not found: '{file_path}'"

    ext = os.path.splitext(file_path)[1].lower()
    if ext != ".csv":
        return f"[CSV Error] File must be .csv, got '{ext}'"

    try:
        with open(file_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            return "[CSV Result] File is empty."

        cols = list(rows[0].keys())
        op = operation.lower().strip()

        # ── columns ──────────────────────────────────────────────────────
        if op == "columns":
            return f"[CSV Columns] {cols}"

        # ── sample ───────────────────────────────────────────────────────
        if op == "sample":
            sample = rows[:top_n]
            return (
                f"[CSV Sample] First {len(sample)} rows of {len(rows)} total\n"
                f"Columns: {cols}\n\n"
                f"{json.dumps(sample, indent=2, default=str)}"
            )

        if op == "filter":
            if not column:
                return "[CSV Error] 'filter' requires a column name."
            filtered = [r for r in rows if r.get(column, "").strip().lower() == value.strip().lower()]
            if not filtered:
                return f"[CSV Result] No rows found where {column} = '{value}'"
            return (
                f"[CSV Filter] {len(filtered)} rows where {column} = '{value}'\n\n"
                f"{json.dumps(filtered, indent=2, default=str)}"
            )

        if op == "unique":
            if not column:
                return "[CSV Error] 'unique' requires a column name."
            if column not in cols:
                return f"[CSV Error] Column '{column}' not found. Available: {cols}"
            unique_vals = list(dict.fromkeys(r[column] for r in rows if column in r))
            return (
                f"[CSV Unique] {len(unique_vals)} unique values in '{column}':\n"
                f"{json.dumps(unique_vals, indent=2)}"
            )

        if op == "count":
            if column and value:
                c = sum(1 for r in rows if r.get(column, "").strip().lower() == value.strip().lower())
                return f"[CSV Count] {c} rows where {column} = '{value}' (total rows: {len(rows)})"
            return f"[CSV Count] Total rows: {len(rows)}"

        if op == "sum":
            if not column:
                return "[CSV Error] 'sum' requires a column name."
            if column not in cols:
                return f"[CSV Error] Column '{column}' not found. Available: {cols}"
            try:
                total = sum(float(r[column].replace(",", "")) for r in rows if r.get(column, "").strip())
                return f"[CSV Sum] Sum of '{column}': {total:,.2f}"
            except ValueError:
                return f"[CSV Error] Column '{column}' contains non-numeric data."
            
        if op == "average":
            if not column:
                return "[CSV Error] 'average' requires a column name."
            if column not in cols:
                return f"[CSV Error] Column '{column}' not found. Available: {cols}"
            try:
                nums = [float(r[column].replace(",", "")) for r in rows if r.get(column, "").strip()]
                avg = sum(nums) / len(nums) if nums else 0
                return f"[CSV Average] Average of '{column}': {avg:,.2f} (over {len(nums)} rows)"
            except ValueError:
                return f"[CSV Error] Column '{column}' contains non-numeric data."

        if op == "top_n":
            if not column:
                return "[CSV Error] 'top_n' requires a column name to sort by."
            if column not in cols:
                return f"[CSV Error] Column '{column}' not found. Available: {cols}"
            try:
                sorted_rows = sorted(
                    rows,
                    key=lambda r: float(r.get(column, "0").replace(",", "") or "0"),
                    reverse=True
                )
            except ValueError:
                sorted_rows = sorted(rows, key=lambda r: r.get(column, ""), reverse=True)

            top = sorted_rows[:top_n]
            return (
                f"[CSV Top {top_n}] Sorted by '{column}' (descending):\n\n"
                f"{json.dumps(top, indent=2, default=str)}"
            )

        return f"[CSV Error] Unknown operation '{operation}'. Valid ops: filter, top_n, unique, count, sum, average, columns, sample"

    except Exception as e:
        return f"[CSV Error] {str(e)}"

def write_file(file_path: str, content: str, mode: str = "w") -> str:
    if mode not in ("w", "a"):
        return "[File Error] Invalid mode. Use 'w' (overwrite) or 'a' (append)."

    ext = os.path.splitext(file_path)[1].lower()
    if ext not in (".txt", ".csv"):
        return f"[File Error] Unsupported file type '{ext}'. Only .txt and .csv are supported."

    try:
        os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
        with open(file_path, mode=mode, encoding="utf-8") as f:
            f.write(content)
        action = "Written" if mode == "w" else "Appended"
        return (
            f"[File {action}] Content successfully written to '{file_path}'\n"
            f"Size: {os.path.getsize(file_path)} bytes"
        )
    except Exception as e:
        return f"[File Error] Could not write to '{file_path}': {str(e)}"


def list_files(directory: str, extension_filter: str = "") -> str:
    if not os.path.exists(directory):
        return f"[File Error] Directory not found: '{directory}'"

    try:
        all_files = []
        for root, _, files in os.walk(directory):
            for f in files:
                full_path = os.path.join(root, f)
                if not extension_filter or f.endswith(extension_filter):
                    size = os.path.getsize(full_path)
                    all_files.append(f"  {full_path}  ({size} bytes)")

        if not all_files:
            return f"[File List] No files found in '{directory}'" + (
                f" with extension '{extension_filter}'" if extension_filter else ""
            )

        header = f"[File List] {len(all_files)} file(s) in '{directory}':\n"
        return header + "\n".join(all_files)

    except Exception as e:
        return f"[File Error] Could not list files in '{directory}': {str(e)}"


file_agent = autogen.ConversableAgent(
    name="File_Agent",
    system_message=(
        "You are a File Agent specializing in reading and querying .txt and .csv files.\n\n"

        "Available Tools:\n"
        "1. `list_files(directory, extension_filter)` — Discover files in a folder\n"
        "2. `read_file(file_path)` — Load FULL content of a .txt or .csv file\n"
        "3. `query_csv(file_path, operation, column, value, top_n)` — Query CSV data directly\n"
        "   Operations: filter | top_n | unique | count | sum | average | columns | sample\n"
        "4. `write_file(file_path, content, mode)` — Write/append to a file\n\n"

        "Decision Rules — Which tool to call:\n"
        "- 'summarize' / 'key takeaways' / 'insights' / 'what does the file say'  → call `read_file`, then answer directly from content\n"
        "- 'read file' / 'show all data' / 'what's in the file'                   → call `read_file`\n"
        "- 'top N by column'                                                       → call `query_csv` with op='top_n'\n"
        "- 'filter by X = Y' / 'who bought X' / 'find rows'                       → call `query_csv` with op='filter'\n"
        "- 'how many / count'                                                      → call `query_csv` with op='count'\n"
        "- 'total / sum of column'                                                 → call `query_csv` with op='sum'\n"
        "- 'average of column'                                                     → call `query_csv` with op='average'\n"
        "- 'unique values in column'                                               → call `query_csv` with op='unique'\n"
        "- 'show first few rows / preview'                                         → call `query_csv` with op='sample'\n"
        "- 'what are the columns'                                                  → call `query_csv` with op='columns'\n\n"

        "Answering Rules for .txt files:\n"
        "- After calling `read_file` on a .txt file, YOU must produce the answer yourself\n"
        "- For 'top 3 takeaways' → read the text, identify the 3 most important points, write them as numbered bullets\n"
        "- For 'summarize' → write a 3-5 sentence summary in your own words based on the content\n"
        "- For 'key insights' → list the main ideas as clean bullet points\n"
        "- NEVER say 'I cannot summarize' or delegate to another agent — you have the text, answer it\n\n"

        "Answering Rules for 'read file' tasks (data handoff to Code_Agent):\n"
        "- If the task is ONLY 'read file <path>' or 'read data/<file>.csv' with no specific question,\n"
        "  your job is ONLY to call read_file and return the raw output — do NOT summarize or paraphrase\n"
        "- Return the full JSON array exactly as the tool gave it — Code_Agent needs the actual data\n"
        "- Do NOT write 'The file contains X rows' — just return the raw tool output\n\n"

        "Strict Rules:\n"
        "- NEVER fabricate data — always call a tool first\n"
        "- ALWAYS call `query_csv` for analytical questions about CSV files\n"
        "- Use `read_file` for .txt files and when full raw data is needed\n"
        "- After receiving tool output, produce a clean, direct, conversational final answer\n"
        "- DO NOT dump raw JSON unless user asks for 'all data'\n"
        "- DO NOT call tools more than once per task\n\n"

        "Output Format:\n"
        "[Tool Called]\n"
        "<tool name and parameters>\n\n"
        "[Answer]\n"
        "<your direct, human-readable answer — no code, no JSON, just clear text>"
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)
file_agent.register_for_llm(
    name="read_file",
    description="Read a .txt or .csv file and return its full content as JSON rows + metadata."
)(read_file)

file_agent.register_for_llm(
    name="query_csv",
    description=(
        "Query a CSV file with structured operations. "
        "Operations: 'filter' (filter by column=value), 'top_n' (top N rows by column, descending), "
        "'unique' (unique values in column), 'count' (row count), 'sum' (sum a numeric column), "
        "'average' (average a numeric column), 'columns' (list column names), 'sample' (first N rows preview). "
        "Use this instead of read_file when you need analytical results."
    )
)(query_csv)

file_agent.register_for_llm(
    name="write_file",
    description="Write or append text content to a .txt or .csv file. mode='w' overwrites, mode='a' appends."
)(write_file)

file_agent.register_for_llm(
    name="list_files",
    description="List all files in a directory. Use extension_filter like '.csv' to filter by type."
)(list_files)


file_agent.register_for_execution(name="read_file")(read_file)
file_agent.register_for_execution(name="query_csv")(query_csv)
file_agent.register_for_execution(name="write_file")(write_file)
file_agent.register_for_execution(name="list_files")(list_files)