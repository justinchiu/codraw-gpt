import openai
import tenacity
from pathlib import Path

SYSTEM_PATH = Path("codraw/prompts/system.txt")
INSTRUCTIONS_PATH = Path("codraw/prompts/instructions.txt")

def load_system():
    with SYSTEM_PATH.open("r") as f:
        return f.read()

def load_instructions():
    with INSTRUCTIONS_PATH.open("r") as f:
        return f.read()

def construct_messages(system, user):
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ],

#@tenacity.retry#(wait=tenacity.wait_fixed(0.5))
def complete(model, messages, temperature=1.0, n=1):
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
        stop="\n",
        temperature=temperature,
        n=n,
    )

def complete_code(model, prompt):
    system_string = load_system()
    instructions_string = load_instructions()
    messages = construct_messages(system_string, instructions_string + prompt)
    return complete(model, messages)

if __name__ == "__main__":
    instructions_prefix = load_instructions()
