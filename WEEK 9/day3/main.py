import asyncio
import autogen
import re
import json
from tools.file_agent import file_agent, read_file, write_file, list_files, query_csv
from tools.db_agent import db_agent, run_sql_query, get_schema
from tools.code_executor import code_agent, execute_python_code
from config import llm_config



def extract_path(query: str) -> str | None:
    """Extract a data/... file path from the user's query string."""
    match = re.search(r"(data[/\\]\S+\.(csv|db|txt))", query)
    return match.group(1) if match else None



orchestrator_agent = autogen.ConversableAgent(
    name="Orchestrator",
    system_message=(
        "You are the Orchestrator Agent for a tool-calling multi-agent system.\n\n"

        "Available Agents and Their Capabilities:\n"
        "1. File_Agent   → Read/write .txt and .csv files, query CSV data (filter, top-N, sum, average, count, unique)\n"
        "2. DB_Agent     → Query SQLite databases (.db files), inspect schemas, run SQL queries\n"
        "3. Code_Agent   → Execute Python code for analysis, computation, sorting, formatting, transformations\n\n"

        "Your Job:\n"
        "- Analyze the user's task carefully\n"
        "- Decide which agent(s) are needed\n"
        "- Write specific, actionable task instructions for each activated agent\n"
        "- Return a JSON routing plan with EXACTLY this structure:\n\n"

        "{\n"
        "  \"requires_file_agent\": true/false,\n"
        "  \"requires_db_agent\": true/false,\n"
        "  \"requires_code_agent\": true/false,\n"
        "  \"file_task\": \"<specific instruction for File_Agent, or empty string>\",\n"
        "  \"db_task\": \"<specific instruction for DB_Agent, or empty string>\",\n"
        "  \"code_task\": \"<specific instruction for Code_Agent, or empty string>\",\n"
        "  \"reason\": \"<brief explanation of routing decision>\"\n"
        "}\n\n"

        "Routing Rules:\n"
        "- .csv or .txt files mentioned                                    → File_Agent (always)\n"
        "- .db or database/SQL/table/records mentioned                     → DB_Agent\n"
        "- Pure code task with no file/db (fibonacci, factorial, sort...)  → Code_Agent only\n\n"

        "CRITICAL — When NOT to use Code_Agent:\n"
        "- Reading a file and summarizing/listing takeaways from it → File_Agent ONLY\n"
        "- Describing what a file contains                          → File_Agent ONLY\n"
        "- Filtering a CSV (find rows where X = Y)                 → File_Agent ONLY\n"
        "- Sum / total of a CSV column                             → File_Agent ONLY (use query_csv sum)\n"
        "- Average of a CSV column                                 → File_Agent ONLY (use query_csv average)\n"
        "- Count rows in a CSV                                      → File_Agent ONLY (use query_csv count)\n"
        "- Top N rows by a CSV column                              → File_Agent ONLY (use query_csv top_n)\n"
        "- Unique values in a CSV column                           → File_Agent ONLY (use query_csv unique)\n"
        "- Any question whose answer is TEXT or a single number    → File_Agent ONLY\n\n"

        "When to ADD Code_Agent alongside File_Agent:\n"
        "- Multi-step computation across multiple columns: e.g. 'profit margin = revenue - cost, rank by margin'\n"
        "- Cross-file calculations combining data from both a CSV and a DB\n"
        "- Generating formatted reports, charts, or complex aggregations not possible with a single query_csv call\n\n"

        "Rule of thumb: File_Agent has query_csv which handles sum, average, count, filter, top_n, unique natively. "
        "Only add Code_Agent when the task requires logic BEYOND what query_csv can do in one call.\n\n"

        "Task Writing Rules:\n"
        "- file_task must include the exact file path and the specific question/operation\n"
        "- db_task must include the exact .db path and the specific SQL question\n"
        "- code_task must describe what to compute — data will be provided by other agents\n"
        "- Leave task strings EMPTY ('') if that agent is not required\n\n"

        "IMPORTANT: Return ONLY the raw JSON object. No markdown, no explanation, no extra text."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER",
)


def print_header(title: str) -> None:
    print("\n" + "=" * 90)
    print(f"  {title}")
    print("=" * 90 + "\n")


def print_section(label: str) -> None:
    print("\n" + "─" * 70)
    print(f"  {label}")
    print("─" * 70 + "\n")


def print_tool_chain(plan: dict) -> None:
    """Visualize which agents have been activated."""
    agents = []
    if plan.get("requires_file_agent"):
        agents.append("📄 File_Agent  [.txt / .csv]")
    if plan.get("requires_db_agent"):
        agents.append("🗄️  DB_Agent    [SQLite / SQL]")
    if plan.get("requires_code_agent"):
        agents.append("🐍 Code_Agent  [Python exec]")

    print("\n  ┌─ TOOL-CHAIN EXECUTION ─────────────────────────────────────────┐")
    print("  │                                                                  │")
    print("  │   🎯 Orchestrator                                                │")
    for agent in agents:
        print(f"  │       └── {agent:<54}│")
    print("  │                                                                  │")
    print("  └──────────────────────────────────────────────────────────────────┘\n")

async def run_agent(
    tool_proxy: autogen.UserProxyAgent,
    agent: autogen.ConversableAgent,
    task: str,
    agent_label: str,
    return_raw_tool_output: bool = False,
) -> str:
    """
    Initiate a chat between tool_proxy and the agent.
    tool_proxy is the executor authority that actually runs the tool calls.

    return_raw_tool_output=True  → return the raw tool execution result (for File_Agent
                                   when its data will be passed to Code_Agent).
    return_raw_tool_output=False → return the last LLM-generated reply (default).
    """
    print_section(f"RUNNING: {agent_label}")
    print(f"  Task: {task}\n")

    try:
        max_turns = 2 if agent_label == "Code_Agent" else 5

        result = await tool_proxy.a_initiate_chat(
            recipient=agent,
            message=task,
            max_turns=max_turns,
            summary_method="reflection_with_llm",
        )

        if return_raw_tool_output:
            for msg in result.chat_history:
                role = msg.get("role", "")
                content = msg.get("content", "")
                if role in ("tool", "function") and content and not content.startswith("*****"):
                    return content.strip()
                if "EXECUTED FUNCTION" in str(msg) or (
                    role == "user" and content and content.startswith("[File Read]")
                ):
                    return content.strip()
        for msg in reversed(result.chat_history):
            content = msg.get("content", "")
            if (
                content
                and not content.startswith("*****")
                and content.strip() != ""
            ):
                return content.strip()

        return "[No output received from agent]"

    except Exception as e:
        return f"[{agent_label} ERROR] {str(e)}"

async def main() -> None:

    tool_proxy = autogen.UserProxyAgent(
        name="Tool_Proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        code_execution_config=False,
        is_termination_msg=lambda x: (
            not x.get("tool_calls") and
            not x.get("function_call") and
            bool(x.get("content", "").strip())
        ),
    )

    tool_proxy.register_for_execution(name="read_file")(read_file)
    tool_proxy.register_for_execution(name="query_csv")(query_csv)
    tool_proxy.register_for_execution(name="write_file")(write_file)
    tool_proxy.register_for_execution(name="list_files")(list_files)
    tool_proxy.register_for_execution(name="run_sql_query")(run_sql_query)
    tool_proxy.register_for_execution(name="get_schema")(get_schema)
    tool_proxy.register_for_execution(name="execute_python_code")(execute_python_code)

    orch_proxy = autogen.UserProxyAgent(
        name="Orch_Proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0,
        code_execution_config=False,
    )

    # ── User Input ────────────────────────────────────────────────────────────
    print_header("DAY 3 — TOOL-CALLING AGENT SYSTEM")
    user_query = input("  Enter your query: ").strip()

    if not user_query:
        print("  [Error] No query entered. Exiting.")
        return

    # ── Fast path: pure code (no files or db) ────────────────────────────────
    code_keywords = {"execute", "python", "run", "calculate", "compute", "fibonacci",
                     "prime", "factorial", "sort", "reverse", "palindrome"}
    file_exts     = {".csv", ".txt", ".db"}

    is_pure_code = (
        any(kw in user_query.lower() for kw in code_keywords)
        and not any(ext in user_query for ext in file_exts)
    )

    if is_pure_code:
        print("\n  ⚙️  Detected: Pure Code Task — routing directly to Code_Agent\n")
        code_output = await run_agent(tool_proxy, code_agent, user_query, "Code_Agent")
        print("\n" + "=" * 90)
        print("   FINAL ANSWER")
        print("=" * 90 + "\n")
        print(code_output)
        print("\n    PIPELINE COMPLETED")
        print("=" * 90 + "\n")
        return

    # ── Step 1: Orchestrator decides routing ──────────────────────────────────
    print_section("STEP 1: ORCHESTRATOR — Routing Decision")

    orch_chat = await orch_proxy.a_initiate_chat(
        recipient=orchestrator_agent,
        message=user_query,
        max_turns=1,
    )

    raw_plan = orch_chat.summary or ""

    # Parse JSON plan safely (strip markdown fences if present)
    try:
        clean = raw_plan.strip()
        # Strip ```json ... ``` or ``` ... ``` fences
        clean = re.sub(r"^```(?:json)?\s*", "", clean)
        clean = re.sub(r"\s*```$", "", clean)
        plan = json.loads(clean.strip())
    except json.JSONDecodeError:
        print("    Orchestrator returned non-JSON. Activating all agents as fallback.\n")
        plan = {
            "requires_file_agent":  True,
            "requires_db_agent":    True,
            "requires_code_agent":  True,
            "file_task":  user_query,
            "db_task":    user_query,
            "code_task":  user_query,
            "reason":     "Fallback — JSON parse failed, all agents activated",
        }

    print(f"  Routing Reason : {plan.get('reason', 'N/A')}")
    if plan.get("file_task"):
        print(f"  File Task      : {plan['file_task']}")
    if plan.get("db_task"):
        print(f"  DB Task        : {plan['db_task']}")
    if plan.get("code_task"):
        print(f"  Code Task      : {plan['code_task']}")
    print_tool_chain(plan)

    print_section("STEP 2: TOOL-CALLING AGENTS — Execution")

    agent_results: dict[str, str] = {}

    async def _noop() -> str:
        return ""

    parallel_tasks = []

    
    file_needs_raw = plan.get("requires_code_agent", False)

    if plan.get("requires_file_agent") and plan.get("file_task", "").strip():
        parallel_tasks.append(
            run_agent(tool_proxy, file_agent, plan["file_task"], "File_Agent",
                      return_raw_tool_output=file_needs_raw)
        )
    else:
        parallel_tasks.append(_noop())  

    if plan.get("requires_db_agent") and plan.get("db_task", "").strip():
        parallel_tasks.append(
            run_agent(tool_proxy, db_agent, plan["db_task"], "DB_Agent")
        )
    else:
        parallel_tasks.append(_noop()) 

    file_result, db_result = await asyncio.gather(*parallel_tasks)

    if plan.get("requires_file_agent") and file_result:
        agent_results["File_Agent"] = file_result

    if plan.get("requires_db_agent") and db_result:
        agent_results["DB_Agent"] = db_result

    
    if plan.get("requires_code_agent") and plan.get("code_task", "").strip():

        context_parts = []
        if agent_results.get("File_Agent"):
            context_parts.append(f"=== File_Agent Output ===\n{agent_results['File_Agent']}")
        if agent_results.get("DB_Agent"):
            context_parts.append(f"=== DB_Agent Output ===\n{agent_results['DB_Agent']}")

        context = "\n\n".join(context_parts)

        code_task_full = (
            f"Use ONLY the following data (do NOT read any file from disk):\n\n"
            f"{context}\n\n"
            f"Task:\n{plan['code_task']}\n\n"
            "IMPORTANT:\n"
            "- Parse JSON data using: rows = json.loads(data) with triple-quoted strings\n"
            "- Print your results clearly with labels\n"
            "- Do NOT attempt to open any file paths"
        ) if context else plan["code_task"]

        code_result = await run_agent(tool_proxy, code_agent, code_task_full, "Code_Agent")
        agent_results["Code_Agent"] = code_result

    print("\n" + "=" * 90)
    print("  FINAL ANSWER")
    print("=" * 90 + "\n")

    if "Code_Agent" in agent_results:
        print(agent_results["Code_Agent"])

    elif "DB_Agent" in agent_results and "File_Agent" in agent_results:
        print("── File Analysis ────────────────────────────")
        print(agent_results["File_Agent"])
        print("\n── Database Analysis ────────────────────────")
        print(agent_results["DB_Agent"])

    elif "DB_Agent" in agent_results:
        print(agent_results["DB_Agent"])

    elif "File_Agent" in agent_results:
        print(agent_results["File_Agent"])

    else:
        print("  No result was generated. Check the routing plan above.")

    print("\n   DAY 3 TOOL-CHAIN PIPELINE COMPLETED")
    print("=" * 90 + "\n")


if __name__ == "__main__":
    asyncio.run(main())