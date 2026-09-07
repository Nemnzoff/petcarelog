# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: PetCareLog
import json, os

LOG_FILE = "pet_care_log.json"

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def save_log(entries):
    with open(LOG_FILE, "w") as f:
        json.dump(entries, f, indent=2)

def delete_entry(entry_id, confirm=True):
    entries = load_log()
    filtered = [e for e in entries if e["id"] != entry_id]
    if len(entries) != len(filtered):
        if confirm:
            print(f"Deleted entry #{entry_id}.")
        save_log(filtered)
    return filtered
