import os
from openai import OpenAI
from memory.session_memory import MemoryManager
from memory.vector_store import VectorMemory

api_key = os.getenv("GROQ_API_KEY", "dummy_key_if_unauthorized")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

memory_manager = MemoryManager("memory/long_term.db")
vector_store = VectorMemory()


def summarize_fact(user_query, agent_response):
    prompt = f"""
Extract a SINGLE concise, objective fact about the user or their context.
- Prefer stable info (name, role, company, preferences)
- Ignore generic Q&A
- If nothing useful → return exactly: None

User: {user_query}
Agent: {agent_response}
"""
    try:
        resp = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        fact = resp.choices[0].message.content.strip()
        if fact.lower() != "none" and len(fact) > 5:
            return fact
    except Exception as e:
        print(f"[Warn] Summarization failed: {e}")
    return None


def process_query(query: str):
    print("\n" + "─" * 50)
    print(f"User: {query}")
    print("─" * 50)

    similar_facts = vector_store.search_similar(query, k=3)
    context_str = "\n".join([f"• {res['fact']}" for res in similar_facts])

    exact_match = any(query.lower() in res['fact'].lower() for res in similar_facts)

    if exact_match:
        print("You've asked something similar before.\n")

    if context_str:
        print("I remember this from earlier:\n")
        print(context_str)
        print()
    else:
        print("No relevant past memory found.\n")

    system_prompt = "You are a helpful AI assistant with memory."

    if context_str:
        system_prompt += f"\n\nUse this past context if relevant:\n{context_str}"

    messages = [{"role": "system", "content": system_prompt}]

   
    for msg in memory_manager.get_short_term_context():
        messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": query})

    memory_manager.add_message("user", query)

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.5
        )
        answer = response.choices[0].message.content.strip()
    except Exception as e:
        answer = f"[Error] Could not generate response: {e}"

    print(f"Assistant: {answer}\n")

    memory_manager.add_message("assistant", answer)


    fact = summarize_fact(query, answer)

    if fact:
        vector_store.insert_fact(fact)
        print(f" Stored memory: {fact}")


if __name__ == "__main__":
    print("=" * 60)
    print("DAY 4 — INTERACTIVE MEMORY SYSTEM")
    print("=" * 60)

    while True:
        query = input("\n Enter your query (type 'exit' to quit): ").strip()

        if query.lower() == "exit":
            print("Exiting...")
            break

        if query.lower() == "clear":
            memory_manager.clear_short_term()
            print("Session memory cleared.")
            continue

        process_query(query)