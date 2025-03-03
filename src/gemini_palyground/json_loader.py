import json

class PromptLoadError(Exception):
    pass

def load_prompt_from_json(filepath, key):
    try:
        with open(filepath, 'r', encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data.get(key)
    except (FileNotFoundError, json.JSONDecodeError):
        raise PromptLoadError("No Prompt Found!")
