# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: PetCareLog
def generate_changelog(records, limit=20):
    """Generate a compact changelog from activity log records."""
    entries = []
    for r in records[-limit:]:
        date = r.get("date", "unknown")
        action = r.get("action", "activity")
        pet = r.get("pet", "pet")
        detail = r.get("detail", "")
        if detail:
            entries.append(f"{date} — {pet}: {action} ({detail})")
        else:
            entries.append(f"{date} — {pet}: {action}")
    if entries:
        return "Changelog:\n" + "\n".join(entries)
    return "Changelog:\nNo activity recorded."
