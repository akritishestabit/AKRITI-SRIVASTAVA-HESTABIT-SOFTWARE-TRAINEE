import asyncio
import json
import autogen
from orchestrator.planner import planner_agent
from agents.worker_agent import create_worker
from agents.reflection_agent import reflection_agent
from agents.validator import validator_agent


def print_execution_tree(tasks):
    print("\n--- DAG EXECUTION TREE ---")
    print("Planner")
    for task in tasks:
        if isinstance(task, dict):
            deps = ", ".join(task.get("dependencies", []))
            dep_str = f" (Depends on: {deps})" if deps else " (No dependencies)"
            print(f"  ├── [{task.get('id', 'unknown')}] Worker_{task.get('id', 'unknown')}{dep_str}")
        else:
            print(f"  ├── Worker → {task}")
    print("  └── Reflection → Validator")
    print("--------------------------\n")


async def run_dag_workers(tasks, user_proxy):
    print_execution_tree(tasks)
    print(f"[Planner] Generated {len(tasks)} distinct tasks.\n")

    events = {}
    for task in tasks:
        if isinstance(task, dict) and "id" in task:
            events[task["id"]] = asyncio.Event()

    results = {}
    coroutines = []

    for i, task in enumerate(tasks):
        if isinstance(task, dict):
            task_id = task.get("id", str(i + 1))
            deps = task.get("dependencies", [])
            desc = task.get("description", str(task))
        else:
            task_id = str(i + 1)
            deps = []
            desc = str(task)

        worker = create_worker(task_id)
        print(f"[Dispatch] Worker_{task_id} initialized. Dependencies: {deps}")

        async def run_task(w, d, t_id, dependencies):
            # Wait for dependencies to finish
            for dep in dependencies:
                if dep in events:
                    await events[dep].wait()
            
            print(f"[Execute] Worker_{t_id} is running...")
            try:
                result = await user_proxy.a_initiate_chat(
                    recipient=w,
                    message=d,
                    max_turns=1,
                    summary_method="last_msg"
                )
                output = f"\n--- Worker {t_id} Output ---\n{result.summary}\n"
            except Exception as e:
                output = f"\n--- Worker {t_id} FAILED ---\n{str(e)}\n"
            
            results[t_id] = output
            if t_id in events:
                events[t_id].set()

        coroutines.append(run_task(worker, desc, task_id, deps))

    
    await asyncio.gather(*coroutines)

    final_output = ""
    for task in tasks:
        if isinstance(task, dict):
            final_output += results.get(task.get("id"), "")
    
    if not final_output:
        final_output = "".join(results.values())

    return final_output


async def main():
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config=False,
    )

    # query = "Analyze the impact of AI on three distinct sectors: 1) Education, 2) Logistics, and 3) Entertainment."
    # query = "Find out the current average price of a 1-bedroom apartment in San Francisco. Then, calculate how much a person needs to earn annually to afford it (assuming 30% of income goes to rent). Finally, suggest 3 jobs that pay that salary."
    # query = "Explain the core philosophy of React, Angular, and Vue frontend frameworks independently."
    query= "Explain Machine Learning and Deep Learning separately and then compare it"


    print("\n DAY 2 MULTI-AGENT SYSTEM")
    print("=" * 80)
    print(f"\n USER QUERY:\n{query}\n")

    print("[Planner] Analyzing the query...")

    planner_chat = await user_proxy.a_initiate_chat(
        recipient=planner_agent,
        message=query,
        max_turns=1
    )

    raw_tasks = planner_chat.summary

    try:
        tasks = json.loads(raw_tasks)
        if not isinstance(tasks, list):
            raise ValueError("Planner output is not a list")
    except Exception:
        print("[Warning] Planner did not return valid JSON. Using fallback parsing.\n")
        tasks = [t.strip() for t in raw_tasks.split("\n") if t.strip()]

    print("\n[Planner Output Tasks]")
    for i, t in enumerate(tasks):
        if isinstance(t, dict):
            print(f"{t.get('id', i+1)}. {t.get('description', t)}")
        else:
            print(f"{i+1}. {t}")

    
    print("\n[Workers] Executing tasks strictly following DAG...\n")
    aggregated_results = await run_dag_workers(tasks, user_proxy)

    print("\n[Reflection] Synthesizing outputs...")

    reflection_chat = await user_proxy.a_initiate_chat(
        recipient=reflection_agent,
        message=(
            "Please synthesize and logically merge the following outputs from parallel workers "
            "into a cohesive, concise, and structured draft:\n\n"
            f"{aggregated_results}"
        ),
        max_turns=1
    )

    print("\n[Validator] Performing final validation...")

    validator_chat = await user_proxy.a_initiate_chat(
        recipient=validator_agent,
        message=(
            "Please validate, refine, and finalize the following draft. "
            "Ensure correctness, clarity, and completeness:\n\n"
            f"{reflection_chat.summary}"
        ),
        max_turns=1
    )

    print("\n" + "=" * 80)
    print("FINAL VERIFIED ANSWER")
    print("=" * 80 + "\n")
    print(validator_chat.summary)


if __name__ == "__main__":
    asyncio.run(main())
