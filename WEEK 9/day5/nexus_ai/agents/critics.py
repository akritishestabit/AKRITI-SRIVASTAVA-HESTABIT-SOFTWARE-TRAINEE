import autogen
from config import llm_config

critic_agent = autogen.ConversableAgent(
    name="Critic",
    system_message=(
        "You are the Critic Agent.\n"
        "Your task is to take the raw aggregated output from the workers and critique it.\n"
        "Look for logical flaws, incomplete tasks, or missing tool implementations.\n"
        "Provide a concise list of fixes."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)


optimizer_agent = autogen.ConversableAgent(
    name="Optimizer",
    system_message=(
        "You are the Optimizer Agent.\n"
        "Your task is to take the original draft and the Critic's feedback, and produce an improved, optimized version."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)

validator_agent = autogen.ConversableAgent(
    name="Validator",
    system_message=(
        "You are the Validator Agent.\n"
        "Your task is to apply final constraints formatting. "
        "Ensure no prohibited language is used, check for system safety, and verify it perfectly answers the user query."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)

reporter_agent = autogen.ConversableAgent(
    name="Reporter",
    system_message=(
        "You are the Reporter Agent.\n"
        "Your job is strictly formatting. Take the final validated output and format it into a gorgeous Markdown structure.\n"
        "Use headers, bullet points, and code blocks where applicable."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)
