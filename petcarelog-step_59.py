# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: PetCareLog
def _confirm_deletion(prompt):
    try:
        answer = input(prompt).strip().lower()
        return answer in ("y", "yes")
    except (EOFError, KeyboardInterrupt):
        return False


def delete_entries(record_id, confirm=True, message="Delete this record?", entries=None):
    if entries is None:
        entries = []
    for entry in entries:
        if entry.get("id") == record_id:
            entries.remove(entry)
            if confirm and not _confirm_deletion(message):
                entries.append(entry)
                return False
    return True
