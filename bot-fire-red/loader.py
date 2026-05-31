import json

def load_types(path="data/types.json"):
    with open(path, "r") as f:
        return json.load(f)

def load_moves(path="data/moves.json"):
    with open(path, "r") as f:
        return json.load(f)

# -----------------------------

from models import Move

def build_move(name, moves_db):
    data = moves_db[name]
    return Move(name, data["type"], data["power"])