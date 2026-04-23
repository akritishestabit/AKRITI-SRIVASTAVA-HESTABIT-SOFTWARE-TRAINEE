import autogen
from config import llm_config
from tools.file_agent import read_file, write_file, list_files
from tools.db_agent import run_sql_query, get_schema
from tools.code_executor import execute_python_code

researcher_agent = autogen.ConversableAgent(
    name="Researcher",
    system_message=(
        "You are the Researcher/File Agent.\n"
        "Your job is to read files, analyze text, and write or append data to text files when requested.\n"
        "CRITICAL RULES:\n"
        "1. If asked to read, use `read_file`. Once you successfully use it, DO NOT call it again for the same file.\n"
        "2. If asked to write or append, use the `write_file` tool with the correct mode ('w' or 'a').\n"
        "3. LITERALLY copy the exact text from the tool output or provide exact confirmation of what was written.\n"
        "4. After your final factual answer/confirmation, append the word 'TERMINATE' on a new line to end the sequence."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)

researcher_agent.register_for_llm(name="read_file", description="Read a .txt or .csv file")(read_file)
researcher_agent.register_for_llm(name="write_file", description="Write or append text content to a file.")(write_file)
researcher_agent.register_for_llm(name="list_files", description="List files in a directory.")(list_files)


coder_agent = autogen.ConversableAgent(
    name="Coder",
    system_message=(
        "You are the Coder Agent specializing in Python.\n"
        "Your task is to write and carefully test python code.\n"
        "Always use the `execute_python_code` tool to run your snippets and capture the output.\n"
        "CRITICAL INSTRUCTION: Once your code executes successfully, format the final Python code and explanation into your message, and append 'TERMINATE' on a new line."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)

coder_agent.register_for_llm(name="execute_python_code", description="Execute Python code")(execute_python_code)


analyst_agent = autogen.ConversableAgent(
    name="Analyst",
    system_message=(
        "You are the Analyst Agent specializing in SQLite and Data extraction.\n"
        "You MUST always call `get_schema` first to inspect the schema before running a `run_sql_query`.\n"
        "Perform SQL queries, then interpret the resulting JSON data."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)

analyst_agent.register_for_llm(name="run_sql_query", description="Execute SQL query")(run_sql_query)
analyst_agent.register_for_llm(name="get_schema", description="Get database schema")(get_schema)
