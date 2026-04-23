import autogen
import sys
import io
import traceback
from config import llm_config


def execute_python_code(code: str) -> str:
    stdout_capture = io.StringIO()
    import json, csv, os, math, statistics, collections, datetime, re

    namespace = {
        "json":        json,
        "csv":         csv,
        "os":          os,
        "math":        math,
        "statistics":  statistics,
        "collections": collections,
        "datetime":    datetime,
        "re":          re,
        "io":          io,
    }

    try:
        import pandas as pd
        namespace["pd"] = pd
    except ImportError:
        pass 

    try:
        sys.stdout = stdout_capture
        exec(compile(code, "<code_agent>", "exec"), namespace)
    except Exception:
        sys.stdout = sys.__stdout__
        return f"[Code Execution Error]\n{traceback.format_exc()}"
    finally:
        sys.stdout = sys.__stdout__

    output = stdout_capture.getvalue().strip()
    return output if output else "[Code executed successfully — no output produced]"


code_agent = autogen.ConversableAgent(
    name="Code_Agent",
    system_message=(
        "You are a Code Execution Agent specializing in Python data analysis.\n\n"

        "Your Responsibilities:\n"
        "- Write and execute Python code for the given task\n"
        "- Perform computation, analysis, transformations, and formatting\n"
        "- Work with data passed as strings (JSON, CSV text, plain text)\n\n"

        "Strict Rules (VERY IMPORTANT):\n"
        "- ALWAYS call `execute_python_code` — never return raw code without executing it\n"
        "- When working with JSON data passed as a string, ALWAYS use triple quotes:\n"
        "    data = '''<json here>'''\n"
        "    import json; rows = json.loads(data)\n"
        "- DO NOT read files from disk unless a file path is explicitly provided\n"
        "- DO NOT assume or fabricate any data\n"
        "- If execution fails, read the error, fix the code, and retry ONCE\n"
        "- DO NOT calculate anything not requested in the task\n\n"

        "Standard Libraries Available (pre-imported in namespace):\n"
        "json, csv, os, math, statistics, collections, datetime, re, io\n"
        "pandas (as pd) — if installed\n\n"

        "Coding Patterns:\n"
        "- For JSON data: use json.loads() — wrap data in triple quotes\n"
        "- For numeric aggregation: use statistics.mean(), sum(), sorted()\n"
        "- For formatting output: use f-strings or print() clearly\n"
        "- For top-N: use sorted(data, key=lambda x: x['col'], reverse=True)[:N]\n\n"

        "Output Format:\n"
        "[Code]\n"
        "<the Python code>\n\n"
        "[Result]\n"
        "<the executed output>"
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)


code_agent.register_for_llm(
    name="execute_python_code",
    description=(
        "Execute a Python code snippet and capture its standard output. "
        "Use this for any computation, data analysis, sorting, filtering, or transformation. "
        "Pre-imported: json, csv, os, math, statistics, collections, datetime, re. "
        "Returns printed output or an error traceback if execution fails."
    )
)(execute_python_code)

code_agent.register_for_execution(name="execute_python_code")(execute_python_code)