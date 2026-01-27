import json
import os
from types import SimpleNamespace

def read_json_file(file_path: str) -> str:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def wrap_namespace(data):
    """
    Recursively converts a dictionary into a SimpleNamespace object.
    """
    if isinstance(data, dict):
        for key, value in data.items():
            data[key] = wrap_namespace(value)
        return SimpleNamespace(**data)
    elif isinstance(data, list):
        return [wrap_namespace(item) for item in data]
    else:
        return data