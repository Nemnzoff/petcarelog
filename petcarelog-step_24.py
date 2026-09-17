# === Stage 24: Add grouped summaries by category or status ===
# Project: PetCareLog
def summarize_records(records, group_by=None):
    """Group pet care records by category or status and return a summary dict.

    Args:
        records: List of record dicts with keys like 'category', 'status', 'date', etc.
        group_by: Optional key to group by. If None, returns overall counts.

    Returns:
        Dict with counts grouped by the specified key or overall.
    """
    if group_by:
        grouped = {}
        for r in records:
            key = r.get(group_by, 'unknown')
            grouped[key] = grouped.get(key, 0) + 1
        return grouped
    else:
        return {'total': len(records)}

# Example usage:
# records = [
#     {'category': 'feeding', 'status': 'completed', 'date': '2024-01-01'},
#     {'category': 'vet_visit', 'status': 'scheduled', 'date': '2024-01-15'},
#     {'category': 'medication', 'status': 'completed', 'date': '2024-01-10'},
# ]
# print(summarize_records(records, group_by='category'))
# print(summarize_records(records, group_by='status'))
# print(summarize_records(records))
