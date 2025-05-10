import os
import json

VISITS_FILE = "visits.json"

def load_visits():
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            json.dump({"count": 0}, f)
    with open(VISITS_FILE, "r") as f:
        return json.load(f)

def increment_visits():
    data = load_visits()
    data["count"] += 1
    with open(VISITS_FILE, "w") as f:
        json.dump(data, f)
    return data["count"]
