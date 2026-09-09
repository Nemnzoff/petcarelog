# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: PetCareLog
def find_records(query, log):
    query_lower = query.lower()
    for entry in log:
        for k, v in entry.items():
            if isinstance(v, str) and query_lower in v.lower():
                return entry
    return None
