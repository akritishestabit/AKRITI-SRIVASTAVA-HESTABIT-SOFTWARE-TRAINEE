import autogen
import sys
import io
import traceback
import time
from config import llm_config


# ─────────────────────────────────────────────
#  TOOL: Python Code Executor
# ─────────────────────────────────────────────

def execute_python_code(code: str) -> str:
    stdout_capture = io.StringIO()
    namespace = {}

    try:
        sys.stdout = stdout_capture
        exec(compile(code, "<code_agent>", "exec"), namespace)
    except Exception:
        return f"[Code Execution Error]\n{traceback.format_exc()}"
    finally:
        sys.stdout = sys.__stdout__

    output = stdout_capture.getvalue().strip()
    
    # Automatically save every executed script directly to the file system uniquely
    try:
        timestamp = int(time.time())
        code_file = f"executed_code_{timestamp}.py"
        md_file = f"executed_explanation_{timestamp}.md"
        
        with open(code_file, "w", encoding="utf-8") as f:
            f.write(code)
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(f"# Auto-Generated Code Explanation\n\nThis code was generated and executed by the Coder Agent.\n\n```python\n{code}\n```\n\n### Execution Output:\n```\n{output}\n```")
    except Exception as e:
        pass # Handle silently
        
    return output if output else "[Code executed successfully — no output produced]"


# ─────────────────────────────────────────────
#  AGENT DEFINITION
# ─────────────────────────────────────────────

code_agent = autogen.ConversableAgent(
    name="Code_Agent",
  
    system_message=(
    "You are a Code Execution Agent specializing in Python.\n\n"

    "Your Responsibilities:\n"
    "- Write and execute Python code ONLY for the given task\n"
    "- Perform computation exactly as requested\n\n"

    "Strict Rules (VERY IMPORTANT):\n"
    "- Execute ONLY what is asked — no extra analysis\n"
    "- DO NOT calculate anything not mentioned in the task\n"
    "- DO NOT create or assume any data\n"
    "- DO NOT change file names or paths\n"
    "- ALWAYS use the exact file path given in the task\n"
    "- If file path is missing → do NOT guess, return error\n"
    "- If execution fails → fix code and retry once\n\n"

    "Execution Rules:\n"
    "- ALWAYS call execute_python_code tool\n"
    "- DO NOT return raw code without execution\n"
    "- When injecting JSON or string data into your Python code, ALWAYS wrap the data string in triple quotes (''' or \"\"\") and use `json.loads(data)` to prevent escaping errors.\n\n"

    "Output Format:\n"
    "[Code]\n"
    "<code>\n\n"
    "[Result]\n"
    "<output>\n"
),
    llm_config=llm_config,
    human_input_mode="NEVER",
)


# ─────────────────────────────────────────────
#  TOOL REGISTRATION
# ─────────────────────────────────────────────

code_agent.register_for_llm(
    name="execute_python_code",
    description=(
        "Execute a Python code snippet and capture its standard output. "
        "Use this for any computation, data analysis, or transformation task. "
        "Returns the printed output or an error traceback."
    ),
)(execute_python_code)

code_agent.register_for_execution(name="execute_python_code")(execute_python_code)