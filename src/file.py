import os
import json

MAIN_DIR = os.path.dirname(__file__)


def write_binary(relative_path, filename, content):
    filepath = os.path.join(MAIN_DIR, relative_path)

    with open(f"{filepath}{filename}", "wb") as f:
        f.write(content)

def write(relative_path, content):
    file = os.path.join(MAIN_DIR, relative_path)

    with open(file, "w+") as f:
        f.write(content)

def write_json(relative_path, content):
    json_content = json.dumps(content)
    write(relative_path, json_content)

def read(relative_path):
    file = os.path.join(MAIN_DIR, relative_path)

    with open(file, 'r') as f:
        content = f.read()

    return content

def read_json(relative_path):
    json_content = read(relative_path)
    return json.loads(json_content)
