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

# Create an agent with tools from the community-driven strands-tools package
# as well as our custom letter_counter tool
agent = Agent(
    model=local_qwen_model,
    tools=[letter_counter]
)

# Ask the agent a question that uses the available tools
message = """
Tell me how many letter R's are in the word "strawberry" 🍓
"""
agent(message)