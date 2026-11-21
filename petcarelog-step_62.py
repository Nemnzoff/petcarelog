# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: PetCareLog
def prioritize_care(entries):
    """Assign a priority score to each care entry and return sorted entries.

    Higher scores indicate more urgent care needs. Scoring is based on the
    type of activity, its recency, and whether it is overdue.
    """
    score_map = {
        "medication": 100,
        "vet_visit": 90,
        "weight_check": 50,
        "feeding": 20,
    }
    overdue_map = {"medication": 50, "vet_visit": 30, "weight_check": 10}
    now = time.time()
    for entry in entries:
        entry["priority"] = score_map.get(entry["type"], 0)
        age = now - entry["timestamp"]
        if entry["type"] in overdue_map and age > entry["interval"]:
            entry["priority"] += overdue_map[entry["type"]]
    return sorted(entries, key=lambda e: e["priority"], reverse=True)
