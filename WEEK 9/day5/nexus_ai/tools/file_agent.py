import autogen
import csv
import os
import json
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


# ─────────────────────────────────────────────
#  AGENT DEFINITION
# ─────────────────────────────────────────────

file_agent = autogen.ConversableAgent(
    name="File_Agent",
    system_message=(
        "You are a File Agent specializing in reading and writing .txt and .csv files.\n\n"

        "Your Responsibilities:\n"
        "- Use `list_files` to discover files\n"
        "- Use `read_file` to load file content\n"
        "- ALWAYS read the file before analysis\n\n"

        "Strict Rules:\n"
        "- NEVER fabricate data\n"
        "- ALWAYS call read_file when file is mentioned\n"
        "- DO NOT call tools multiple times unnecessarily\n"
        "- AFTER receiving tool output, you MUST produce a FINAL answer\n"
        "- DO NOT repeat tool calls after successful execution\n"
        "- DO NOT output '[Function Call Missing]'\n"
        "- DO NOT loop\n\n"
        "- If asked \"column names\" → return only column names\n"
        "- If asked \"summarize\" → return only summary\n"
        "- If asked \"show data\" → return file content\n"
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)


file_agent.register_for_llm(
    name="read_file",
    description="Read a .txt or .csv file and return its full content."
)(read_file)

file_agent.register_for_llm(
    name="write_file",
    description="Write or append text content to a file."
)(write_file)

file_agent.register_for_llm(
    name="list_files",
    description="List files in a directory."
)(list_files)


file_agent.register_for_execution(name="read_file")(read_file)
file_agent.register_for_execution(name="write_file")(write_file)
file_agent.register_for_execution(name="list_files")(list_files)