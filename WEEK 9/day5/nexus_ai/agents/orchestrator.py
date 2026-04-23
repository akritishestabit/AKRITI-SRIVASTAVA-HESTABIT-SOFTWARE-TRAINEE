import autogen
from config import llm_config

orchestrator_agent = autogen.ConversableAgent(
    name="Orchestrator",
    system_message=(
        "You are the Orchestrator Agent.\n"
        "Your role is to receive the user's high-level task and the retrieved memory context.\n"
        "You must reformulate and clarify the objective into a solid prompt for the Planner to consume."
    ),
    llm_config=llm_config,
    human_input_mode="NEVER"
)
