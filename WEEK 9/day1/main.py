import autogen
from agents.research_agent import research_agent
from agents.summarizer_agent import summarizer_agent
from agents.answer_agent import answer_agent


MEMORY_WINDOW = 10
chat_history = []


def format_context(history):
    context = ""
    for msg in history[-MEMORY_WINDOW:]:
        context += f"{msg['role'].upper()}: {msg['content']}\n\n"
    return context


def print_section(title):
    print("\n" + "=" * 90)
    print(f"🔹 {title}")
    print("=" * 90 + "\n")


def main():
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        max_consecutive_auto_reply=0,
        code_execution_config=False,
    )

    query = "What are the core concepts of Multi-Agent Systems in AI, specifically the ReAct pattern?"

    print("\n MULTI-AGENT PIPELINE STARTED")
    print("=" * 90)
    print(f"\n USER QUERY:\n{query}")

    print_section("STEP 1: RESEARCH AGENT (RAW DATA)")

    chat_history.append({"role": "user", "content": query})

    research_chat = user_proxy.initiate_chat(
        recipient=research_agent,
        message=format_context(chat_history),
        max_turns=1,
    )

    research_output = research_chat.summary
    print(research_output)

    chat_history.append({"role": "research", "content": research_output})

    print_section("STEP 2: SUMMARIZER AGENT (COMPRESSED DATA)")

    summarizer_chat = user_proxy.initiate_chat(
        recipient=summarizer_agent,
        message=format_context(chat_history),
        max_turns=1,
    )

    summary_output = summarizer_chat.summary
    print(summary_output)

    chat_history.append({"role": "summary", "content": summary_output})

    print_section("STEP 3: ANSWER AGENT (FINAL OUTPUT)")

    answer_chat = user_proxy.initiate_chat(
        recipient=answer_agent,
        message=format_context(chat_history),
        max_turns=1,
    )

    final_answer = answer_chat.summary
    print(final_answer)

    chat_history.append({"role": "answer", "content": final_answer})

    print("\n" + "=" * 90)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 90)


if __name__ == "__main__":
    main()