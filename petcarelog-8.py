# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: PetCareLog
def filter_entries(entries, status=None, category=None, owner=None, tag=None):
    result = entries
    if status is not None:
        result = [e for e in result if e.get("status") == status]
    if category is not None:
        result = [e for e in result if e.get("category") == category]
    if owner is not None:
        result = [e for e in result if e.get("owner") == owner]
    if tag is not None:
        result = [e for e in result if tag in e.get("tags", [])]
    return result
