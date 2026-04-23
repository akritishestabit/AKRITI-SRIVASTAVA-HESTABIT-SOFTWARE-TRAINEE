import asyncio
import json
import logging
import os
import re
import time
import autogen

# Subsystems
from memory.session_memory import MemoryManager
from memory.vector_store import VectorMemory

# Agents
from agents.orchestrator import orchestrator_agent
from agents.planner import planner_agent
from agents.workers import researcher_agent, coder_agent, analyst_agent
from agents.critics import critic_agent, optimizer_agent, validator_agent, reporter_agent

# Tools
from tools.file_agent import read_file, write_file, list_files
from tools.db_agent import run_sql_query, get_schema
from tools.code_executor import execute_python_code
from config import llm_config

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/nexus_system.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("NEXUS_AI")


def extract_json(text: str) -> str:
    clean = text.strip()
    if clean.startswith("```json"):
        clean = clean[7:]
    elif clean.startswith("```"):
        clean = clean[3:]
    if clean.endswith("```"):
        clean = clean[:-3]
    return clean.strip()


from openai import OpenAI
groq_client = OpenAI(
    api_key=llm_config["config_list"][0]["api_key"],
    base_url=llm_config["config_list"][0]["base_url"]
)

def summarize_fact(query: str, response: str) -> str:
    prompt = f"Extract a SINGLE factual conclusion from this interaction. If generic, return 'None'.\nUser: {query}\nSystem: {response}"
    try:
        resp = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        fact = resp.choices[0].message.content.strip()
        if fact.lower() != "none" and len(fact) > 5:
            return fact
    except:
        pass
    return None


async def run_worker(proxy: autogen.UserProxyAgent, agent: autogen.ConversableAgent, task: str, label: str) -> str:
    print(f"[{label}] Starting task...")
    logger.info(f"Dispatching to {label}: {task}")
    try:
        chat_result = await proxy.a_initiate_chat(
            recipient=agent,
            message=task,
            max_turns=3,
            summary_method="reflection_with_llm",
            silent=True
        )
        # Dig into chat history to find real factual output, stripping out tool artifacts and TERMINATE signals
        valid_messages = []
        for msg in chat_result.chat_history:
            content = msg.get("content", "")
            if content and not content.startswith("*****"):
                clean_content = content.replace("TERMINATE", "").strip()
                if clean_content:
                    valid_messages.append(clean_content)
        
        if valid_messages:
            logger.info(f"[{label}] Completed.")
            return f"--- {label} Output ---\n" + "\n\n".join(valid_messages) + "\n"
        
        return f"--- {label} No Valid Output ---"
    except Exception as e:
        logger.error(f"{label} failed: {e}")
        return f"--- {label} ERROR: {e} ---"


async def main():
    print("==================================================")
    print("   PROJECT: NEXUS AI")
    print("==================================================\n")

    # Proxies
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )

    tool_proxy = autogen.UserProxyAgent(
        name="Tool_Proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        code_execution_config=False,
        is_termination_msg=lambda x: not x.get("tool_calls") and not x.get("function_call"),
    )

    # Register execution logic to proxy
    tool_proxy.register_for_execution(name="read_file")(read_file)
    tool_proxy.register_for_execution(name="write_file")(write_file)
    tool_proxy.register_for_execution(name="list_files")(list_files)
    tool_proxy.register_for_execution(name="run_sql_query")(run_sql_query)
    tool_proxy.register_for_execution(name="get_schema")(get_schema)
    tool_proxy.register_for_execution(name="execute_python_code")(execute_python_code)

    # Init memory
    memory_manager = MemoryManager("memory/long_term.db")
    vector_store = VectorMemory()
    last_output = ""

    while True:
        query = input("\n Command Nexus AI (or 'exit'): ").strip()
        if query.lower() == 'exit':
            break
        if not query:
            continue

        print("\n[System] Commencing Operations...\n")
        logger.info(f"User Query: {query}")

        past_memories = vector_store.search_similar(query, k=2)
        memory_context = "\n".join([f"• {m['fact']}" for m in past_memories])

        if memory_context:
            print(f"Recovered Episodic Memory:\n{memory_context}\n")
        else:
            print(" No past relevant episodic memory found.")

        orch_prompt = f"""
                User Request: {query}

                Previous Output (Short-Term Memory):
                {last_output}

                Past Context (Long-Term Memory):
                {memory_context}

                If the user refers to "it", "this", or "previous output",
                use the Previous Output section to resolve context.

                Please formulate a comprehensive objective for the planner.
                """
        
        orch_chat = await user_proxy.a_initiate_chat(
            recipient=orchestrator_agent,
            message=orch_prompt,
            max_turns=1,
            silent=True
        )
        refined_objective = orch_chat.summary

        print("[Planner] Generating DAG Task execution plan...")
        plan_chat = await user_proxy.a_initiate_chat(
            recipient=planner_agent,
            message=refined_objective,
            max_turns=1,
            silent=True
        )

        try:
            raw_plan = extract_json(plan_chat.summary)
            tasks = json.loads(raw_plan)
        except Exception as e:
            print(f"[Warning] Planner JSON decode failed. Using fallback. Error: {e}")
            logger.error(f"Planner JSON error: {plan_chat.summary}")
            tasks = {"researcher_task": "", "coder_task": "", "analyst_task": ""}

        q = query.lower()
        if "sample.db" in q or "database" in q or "sql" in q:
            tasks["coder_task"] = ""
            tasks["researcher_task"] = ""
            if not tasks.get("analyst_task"): tasks["analyst_task"] = query
        elif "code" in q or "python" in q or "script" in q or "function" in q or "algorithm" in q:
            tasks["researcher_task"] = ""
            tasks["analyst_task"] = ""
            if not tasks.get("coder_task"): tasks["coder_task"] = query
        elif ".csv" in q or ".txt" in q or "file" in q or "summarize" in q or "read" in q or "append" in q or "write" in q:
            tasks["coder_task"] = ""
            tasks["analyst_task"] = ""
            tasks["researcher_task"] = query
        else:
            if not any(tasks.values()):
                tasks["researcher_task"] = query

        print("\n--- DAG Plan ---")
        for key, val in tasks.items():
            if val: print(f"  > {key.upper()}: {val}")
        print("----------------")

        print("\n[Workers] Dispatching parallel tasks...")
        coroutines = []
        if tasks.get("researcher_task"):
            coroutines.append(run_worker(tool_proxy, researcher_agent, tasks["researcher_task"], "Researcher"))
        if tasks.get("coder_task"):
            coroutines.append(run_worker(tool_proxy, coder_agent, tasks["coder_task"], "Coder"))
        if tasks.get("analyst_task"):
            coroutines.append(run_worker(tool_proxy, analyst_agent, tasks["analyst_task"], "Analyst"))

        worker_results = await asyncio.gather(*coroutines)
        aggregated_draft = "\n\n".join(worker_results)

        print("\n[Critic] Reviewing aggregated worker output...")
        critic_chat = await user_proxy.a_initiate_chat(
            recipient=critic_agent,
            message=f"Please review the following draft logic:\n\n{aggregated_draft}",
            max_turns=1,
            silent=True
        )

        print("[Optimizer] Refining based on Critic feedback...")
        opt_chat = await user_proxy.a_initiate_chat(
            recipient=optimizer_agent,
            message=f"Original Draft:\n{aggregated_draft}\n\nCritic Feedback:\n{critic_chat.summary}\n\nApply the feedback and rewrite the data natively.",
            max_turns=1,
            silent=True
        )

        print("[Validator] Validating edge cases and constraints...")
        val_chat = await user_proxy.a_initiate_chat(
            recipient=validator_agent,
            message=f"Guarantee instructions were met. Validated Output:\n{opt_chat.summary}",
            max_turns=1,
            silent=True
        )

        print("[Reporter] Generating Final MarkDown output...\n")
        
        if tasks.get("coder_task"):
            reporter_prompt = (
                f"Format the final report beautifully in Markdown.\n"
                f"CRITICAL DOCUMENTATION REQUIREMENTS:\n"
                f"1. You MUST explicitly state what the original User Query was: '{query}'\n"
                f"2. You MUST provide a clear summary explaining how the code works and what it does.\n"
                f"3. You MUST provide concrete Input and Output examples showing how to use the code.\n"
                f"4. You MUST include the complete Python code written wrapped in ```python ... ``` blocks.\n"
                f"5. DO NOT include the Critic/Validator's lengthy grading rubric or metadata. Just add a simple 1 or 2 sentence summary of the Validation Result at the very end.\n\n"
                # f"Validated Output to format:\n{val_chat.summary}"
            )
        elif tasks.get("analyst_task"):
            reporter_prompt = (
                f"Format the final report beautifully in Markdown.\n"
                f"CRITICAL DOCUMENTATION REQUIREMENTS:\n"
                f"1. State the original User Query: '{query}'\n"
                f"2. You MUST provide the generated SQL query wrapped cleanly in ```sql ... ``` blocks.\n"
                f"3. You MUST explicitly state the EXACT raw numerical or textual answer retrieved from the database. DO NOT write a vague summary, and DO NOT hallucinate features. Read the raw data provided below and print the final value.\n"
                f"4. DO NOT write or include any Python code snippet blocks.\n"
                f"5. DO NOT include the Critic/Validator's lengthy grading rubric. Add a simple 1 or 2 sentence summary of the Validation Result at the very end.\n\n"
                f"--- RAW DATABASE OUTPUT FROM ANALYST ---\n{aggregated_draft}\n----------------------------------------\n\n"
                # f"Validated Feedback to format:\n{val_chat.summary}"
            )
        else:
            reporter_prompt = (
                f"Format the final report beautifully in Markdown.\n"
                f"CRITICAL DOCUMENTATION REQUIREMENTS:\n"
                f"1. State the original User Query: '{query}'\n"
                f"2. You MUST write EXACTLY the facts and data points found in the RAW OUTPUT below. \n"
                f"3. DO NOT ADD ANY NEW INFORMATION. DO NOT Hallucinate 'Company Overview', 'Mission Statement', or file line counts if they are not explicitly written in the RAW OUTPUT below!\n"
                f"4. DO NOT write or include any Python code snippet blocks or SQL blocks. Just format the exact final summary clearly.\n"
                f"5. DO NOT include the Critic/Validator's lengthy grading rubric. Add a simple 1 or 2 sentence summary of the Validation Result at the very end.\n\n"
                f"--- RAW FILE OUTPUT FROM RESEARCHER ---\n{aggregated_draft}\n----------------------------------------\n\n"
                # f"Validated Feedback to format:\n{val_chat.summary}"
            )
        
        rep_chat = await user_proxy.a_initiate_chat(
            recipient=reporter_agent,
            message=reporter_prompt,
            max_turns=1,
            silent=True
        )

        final_output = rep_chat.summary
        print("\n==================================================")
        print(" FINAL REPORT")
        print("==================================================")
        print(final_output)
        print("==================================================\n")

        memory_manager.add_message("user", query)
        memory_manager.add_message("assistant", final_output)
        fact = summarize_fact(query, final_output)
        if fact:
            vector_store.insert_fact(fact)
            print(f" Fact embedded in FAISS Semantic Memory: '{fact}'")

        if tasks.get("coder_task"):
            try:
                
                search_target = final_output + "\n\n" + aggregated_draft
                python_matches = re.findall(r'```python\s*(.*?)\s*```', search_target, re.DOTALL)
                if python_matches:
                    timestamp = int(time.time())
                    code_content = "\n\n".join(python_matches)
                    
                    explanation_only = re.sub(r'```python\s*.*?\s*```', '[Code snippet relocated to the .py file]', final_output, flags=re.DOTALL)
                    
                    with open(f"nexus_code_{timestamp}.py", "w", encoding="utf-8") as f:
                        f.write(code_content)
                    with open(f"nexus_explanation_{timestamp}.md", "w", encoding="utf-8") as f:
                        f.write(explanation_only.strip())
                    print(f"Saved code to: 'nexus_code_{timestamp}.py'")
                    print(f"Saved report to: 'nexus_explanation_{timestamp}.md'\n")
            except Exception as e:
                pass

if __name__ == "__main__":
    asyncio.run(main())
