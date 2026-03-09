import json
import os

MEMORY_PATH = "math_memory.json"

def save_memory(input_text, output_text, feedback):
    history = load_history()
    history.append({"input": input_text, "output": output_text, "feedback": feedback})
    with open(MEMORY_PATH, "w") as f:
        json.dump(history, f)

def load_history():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    return []

def search_memory(query):
    history = load_history()
    # Simple semantic or keyword match logic here
    # For now, return recent correct cases
    return str([h for h in history if h.get("feedback") == "Correct"][-2:])
    