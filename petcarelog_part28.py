# === Stage 28: Add overdue item detection based on due dates ===
# Project: PetCareLog
def detect_overdue_items(entries):
    overdue = []
    now = datetime.now()
    for entry in entries:
        due = entry.get("due_date")
        if due and due < now:
            overdue.append({
                "pet_name": entry.get("pet_name"),
                "item": entry.get("item_name"),
                "due_date": due.isoformat() if isinstance(due, datetime) else due,
                "overdue_days": (now - due).days if isinstance(due, datetime) else 0
            })
    return overdue
