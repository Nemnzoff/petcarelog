# === Stage 67: Add a function that returns key project metrics ===
# Project: PetCareLog
def get_project_metrics(entries, pets):
    """Return key project metrics from the log."""
    total_records = len(entries)
    total_pets = len(pets)
    feeding_count = sum(1 for e in entries if e.get("type") == "feeding")
    vet_count = sum(1 for e in entries if e.get("type") == "vet_visit")
    medication_count = sum(1 for e in entries if e.get("type") == "medication")
    weight_count = sum(1 for e in entries if e.get("type") == "weight")

    weights = [e["weight_grams"] for e in entries if e.get("type") == "weight"]
    if weights:
        latest_weight = max(weights)
        earliest_weight = min(weights)
        weight_change = latest_weight - earliest_weight
    else:
        latest_weight = earliest_weight = weight_change = None

    return {
        "total_records": total_records,
        "total_pets": total_pets,
        "feedings": feeding_count,
        "vet_visits": vet_count,
        "medications": medication_count,
        "weight_entries": weight_count,
        "latest_weight_grams": latest_weight,
        "earliest_weight_grams": earliest_weight,
        "weight_change_grams": weight_change,
    }
