# utils.py
# Utility functions for Project Alpha


import os
import random
import string
import time
import json

# ------------------------------
# File Utilities
# ------------------------------
def write_file(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"[INFO] Wrote to {path}")

def read_file(path: str) -> str:
    if not os.path.exists(path):
        print(f"[WARN] File {path} does not exist")
        return ""
    with open(path, "r") as f:
        return f.read()

def list_files(directory: str):
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# ------------------------------
# String & Random Utilities
# ------------------------------
def random_string(length: int = 8) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def safe_print(obj):
    try:
        print(str(obj))
    except Exception:
        print("[ERROR] Cannot print object")

# ------------------------------
# Timing Utilities
# ------------------------------
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} executed in {end-start:.4f}s")
        return result
    return wrapper


def load_json(path: str) -> dict:
    if not os.path.exists(path):
        print(f"[WARN] JSON file {path} not found")
        return {}
    with open(path, "r") as f:
        return json.load(f)

def save_json(path: str, data: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
