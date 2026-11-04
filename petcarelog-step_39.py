# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: PetCareLog
def repair_data_integrity(log):
    pets = log.get("pets", {})
    for name, pet in pets.items():
        entries = pet.get("entries", [])
        for entry in entries:
            if entry.get("type") == "feeding":
                if not entry.get("amount"):
                    entry["amount"] = 0.0
                if "timestamp" in entry and entry["timestamp"] is None:
                    entry["timestamp"] = datetime.now().isoformat()
                if not entry.get("status"):
                    entry["status"] = "scheduled"
            elif entry.get("type") == "weight":
                value = entry.get("value")
                if value is not None and value <= 0:
                    entry["value"] = None
            elif entry.get("type") == "medication":
                if not entry.get("dose"):
                    entry["dose"] = 0.0
            elif entry.get("type") == "vet_visit":
                if not entry.get("cost"):
                    entry["cost"] = 0.0
                if not entry.get("status"):
                    entry["status"] = "completed"
    return log
