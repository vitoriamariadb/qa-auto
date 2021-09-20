import json
from pathlib import Path

def load_json_data(filename):
    data_dir = Path(__file__).parent.parent / "data"
    filepath = data_dir / filename

    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_users():
    return load_json_data("users.json")

def load_api_endpoints():
    return load_json_data("api_endpoints.json")
