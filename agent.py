import uuid

from strands import Agent, tool
from strands.models import OpenAIModel

# Define a custom tool as a Python function using the @tool decorator
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.

    Args:
        word (str): The input word to search in
        letter (str): The specific letter to count

    Returns:
        int: The number of occurrences of the letter in the word
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())

local_qwen_model = OpenAIModel(
    model_id="qwen3.5:2b",
    client_args={
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama"  # Required string placeholder to pass internal safety checks
    }
)

# Tight instructions to keep the 2B model focused
system_prompt = (
    "You are a precise, silent background assistant. "
    "When you need to use a tool, execute it immediately. "
    "NEVER write out or print your internal thoughts, plans, or reasoning steps to the user. "
    "Only provide the final answer text after the tool execution completes."
)

# Create an agent with tools from the community-driven strands-tools package
# as well as our custom letter_counter tool
agent = Agent(
    model=local_qwen_model,
    system_prompt=system_prompt,
    tools=[letter_counter]
)

# Ask the agent a question that uses the available tools
def strawberry_prompt_test(agent):
    message = """
    Tell me how many letter R's are in the word "strawberry" 🍓
    """
    agent(message)

def run_agent_session():
    session_key = str(uuid.uuid4())
    invocation_state = {
        "conversation_id": session_key,
        "session_id": session_key
    }
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        # Pass the session_id so the agent remembers previous turns
        response = agent(user_input, invocation_state=invocation_state)
        print(f"\nAgent: {response}\n")

if __name__ == "__main__":
    run_agent_session()