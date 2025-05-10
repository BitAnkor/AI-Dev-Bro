import json
from datetime import datetime

COMMENTS_FILE = "comments.json"

def load_comments():
    try:
        with open(COMMENTS_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_comment(name: str, comment: str, rating: int):
    comments = load_comments()
    comments.append({
        "name": name,
        "comment": comment,
        "rating": rating,
        "date": datetime.now().isoformat()
    })
    with open(COMMENTS_FILE, "w") as f:
        json.dump(comments, f)
    