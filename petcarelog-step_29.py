# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: PetCareLog
def upcoming_reminders(data):
    """Return upcoming feeding reminders and vet visits."""
    reminders = []
    for pet in data.get("pets", []):
        for feeding in pet.get("feedings", []):
            if feeding["next_due"] and feeding["next_due"] < datetime.now().date():
                reminders.append({
                    "pet": pet["name"],
                    "type": "Feeding",
                    "due": feeding["next_due"],
                    "amount": feeding["amount"],
                    "notes": feeding["notes"],
                })
        for vet in pet.get("vet_visits", []):
            if vet["next_due"] and vet["next_due"] < datetime.now().date():
                reminders.append({
                    "pet": pet["name"],
                    "type": "Vet Visit",
                    "due": vet["next_due"],
                    "vet": vet["vet"],
                    "notes": vet["notes"],
                })
    reminders.sort(key=lambda r: r["due"])
    return reminders[:10]
