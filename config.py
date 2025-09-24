# config.py

import os
import json
import time

CONFIG_PATH = "config.json"

default_config = {
    "mode": "debug",
    "retries": 3,
    "last_run": None,
    "log_level": "INFO"
}


def load_config(path: str = CONFIG_PATH) -> dict:
    if not os.path.exists(path):
        print(f"[INFO] Config file {path} not found, using defaults")
        return default_config.copy()
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print(f"[WARN] Invalid config format in {path}, using defaults")
            return default_config.copy()

def save_config(config: dict, path: str = CONFIG_PATH):
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"[INFO] Config saved to {path}")


def update_last_run(path: str = CONFIG_PATH):
    config = load_config(path)
    config["last_run"] = time.strftime("%Y-%m-%d %H:%M:%S")
    save_config(config, path)
