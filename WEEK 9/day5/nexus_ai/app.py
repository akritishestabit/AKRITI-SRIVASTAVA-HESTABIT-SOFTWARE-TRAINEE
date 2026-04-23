import streamlit as st
import asyncio
import json
import re
import time
import os
import autogen
import logging

st.set_page_config(page_title="Nexus AI", page_icon="🚀", layout="centered")
st.title("🚀 Nexus AI (Simple UI)")
st.markdown("A minimalistic frontend. Just type your query below to get the final answer.")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

try:
    from memory.session_memory import MemoryManager
    from memory.vector_store import VectorMemory
    from agents.orchestrator import orchestrator_agent
    from agents.planner import planner_agent
    from agents.workers import researcher_agent, coder_agent, analyst_agent
    from agents.critics import critic_agent, optimizer_agent, validator_agent, reporter_agent
    from tools.file_agent import read_file, write_file, list_files
    from tools.db_agent import run_sql_query, get_schema
    from tools.code_executor import execute_python_code
    from main import extract_json, summarize_fact, run_worker
except ImportError as e:
    st.error(f"Dependencies could not be loaded. Please run this inside the day5/nexus_ai folder. Error: {e}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "system_initialized" not in st.session_state:
    st.session_state.memory_manager = MemoryManager("memory/long_term.db")
    st.session_state.vector_store = VectorMemory()
    
    st.session_state.user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )
    st.session_state.tool_proxy = autogen.UserProxyAgent(
        name="Tool_Proxy",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        code_execution_config=False,
        is_termination_msg=lambda x: not x.get("tool_calls") and not x.get("function_call"),
    )
    
    try:
        st.session_state.tool_proxy.register_for_execution(name="read_file")(read_file)
        st.session_state.tool_proxy.register_for_execution(name="write_file")(write_file)
        st.session_state.tool_proxy.register_for_execution(name="list_files")(list_files)
        st.session_state.tool_proxy.register_for_execution(name="run_sql_query")(run_sql_query)
        st.session_state.tool_proxy.register_for_execution(name="get_schema")(get_schema)
        st.session_state.tool_proxy.register_for_execution(name="execute_python_code")(execute_python_code)
    except Exception:
        pass
        
    st.session_state.system_initialized = True

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

query = st.chat_input("Enter your command here...")

async def generate_response(query):
    # 1. Memory
    past_memories = st.session_state.vector_store.search_similar(query, k=2)
    memory_context = "\n".join([f"• {m['fact']}" for m in past_memories])

    # 2. Orchestrator
    orch_prompt = f"User Request: {query}\nPast Context: {memory_context}\nPlease formulate a comprehensive objective for the planner."
    orch_chat = await st.session_state.user_proxy.a_initiate_chat(recipient=orchestrator_agent, message=orch_prompt, max_turns=1, silent=True)
    
    # 3. Planner
    plan_chat = await st.session_state.user_proxy.a_initiate_chat(recipient=planner_agent, message=orch_chat.summary, max_turns=1, silent=True)
    try:
        tasks = json.loads(extract_json(plan_chat.summary))
    except:
        tasks = {"researcher_task": "", "coder_task": "", "analyst_task": ""}

    # Keyword Override (Matches main.py EXACTLY)
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
        if not any(tasks.values()): tasks["researcher_task"] = query

    # 4. Workers
    coroutines = []
    if tasks.get("researcher_task"):
        coroutines.append(run_worker(st.session_state.tool_proxy, researcher_agent, tasks["researcher_task"], "Researcher"))
    if tasks.get("coder_task"):
        coroutines.append(run_worker(st.session_state.tool_proxy, coder_agent, tasks["coder_task"], "Coder"))
    if tasks.get("analyst_task"):
        coroutines.append(run_worker(st.session_state.tool_proxy, analyst_agent, tasks["analyst_task"], "Analyst"))
    
    worker_results = await asyncio.gather(*coroutines)
    aggregated_draft = "\n\n".join(worker_results)

    # 5-7. Reflection & Validation
    critic_chat = await st.session_state.user_proxy.a_initiate_chat(recipient=critic_agent, message=f"Review:\n\n{aggregated_draft}", max_turns=1, silent=True)
    opt_chat = await st.session_state.user_proxy.a_initiate_chat(recipient=optimizer_agent, message=f"Draft:\n{aggregated_draft}\n\nFeedback:\n{critic_chat.summary}\nApply feedback.", max_turns=1, silent=True)
    val_chat = await st.session_state.user_proxy.a_initiate_chat(recipient=validator_agent, message=f"Validate:\n{opt_chat.summary}", max_turns=1, silent=True)

    # 8. Reporter
    if tasks.get("coder_task"):
        reporter_prompt = (
            f"Format the final report beautifully in Markdown.\n"
            f"CRITICAL DOCUMENTATION REQUIREMENTS:\n"
            f"1. You MUST explicitly state what the original User Query was: '{query}'\n"
            f"2. You MUST provide a clear summary explaining how the code works and what it does.\n"
            f"3. You MUST provide concrete Input and Output examples showing how to use the code.\n"
            f"4. You MUST include the complete Python code written wrapped in ```python ... ``` blocks.\n"
            f"5. DO NOT include the Critic/Validator's lengthy grading rubric or metadata. Just add a simple 1 or 2 sentence summary of the Validation Result at the very end.\n\n"
            f"Validated Output to format:\n{val_chat.summary}"
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
            f"Validated Feedback to format:\n{val_chat.summary}"
        )
    else:
        reporter_prompt = (
            f"Format the final report beautifully in Markdown.\n"
            f"CRITICAL DOCUMENTATION REQUIREMENTS:\n"
            f"1. State the original User Query: '{query}'\n"
            f"2. You MUST write EXACTLY the facts and data points found in the RAW OUTPUT below. \n"
            f"3. DO NOT ADD ANY NEW INFORMATION.\n"
            f"4. DO NOT write or include any Python code snippet blocks or SQL blocks. Just format the exact final summary clearly.\n"
            f"5. DO NOT include the Critic/Validator's lengthy grading rubric. Add a simple 1 or 2 sentence summary of the Validation Result at the very end.\n\n"
            f"--- RAW FILE OUTPUT FROM RESEARCHER ---\n{aggregated_draft}\n----------------------------------------\n\n"
            f"Validated Feedback to format:\n{val_chat.summary}"
        )

    rep_chat = await st.session_state.user_proxy.a_initiate_chat(recipient=reporter_agent, message=reporter_prompt, max_turns=1, silent=True)
    final_output = rep_chat.summary

    # 9. Memory Store
    st.session_state.memory_manager.add_message("user", query)
    st.session_state.memory_manager.add_message("assistant", final_output)
    fact = summarize_fact(query, final_output)
    if fact:
        st.session_state.vector_store.insert_fact(fact)
        
    # 10. File Generation
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
        except:
            pass

    return final_output


if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
        
    with st.chat_message("assistant"):
        with st.spinner("🤖 Nexus AI is analyzing and computing your request..."):
            result = asyncio.run(generate_response(query))
        st.markdown(result)
        st.session_state.messages.append({"role": "assistant", "content": result})
