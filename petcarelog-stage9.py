# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: PetCareLog
def sort_entries(entries, key="date", reverse=True):
    """Sort pet care entries by title, date, priority, or last update."""
    sort_keys = {
        "title": lambda e: e.get("title", "").lower(),
        "date": lambda e: e.get("date", ""),
        "priority": lambda e: e.get("priority", "normal"),
        "last_update": lambda e: e.get("last_update", ""),
    }
    key_func = sort_keys.get(key, sort_keys["date"])
    return sorted(entries, key=key_func, reverse=reverse)
