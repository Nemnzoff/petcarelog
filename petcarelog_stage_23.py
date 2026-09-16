# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: PetCareLog
def add_tag(record, tag):
    if record.get("tags") is None:
        record["tags"] = []
    if tag not in record["tags"]:
        record["tags"].append(tag)

def remove_tag(record, tag):
    if record.get("tags") is not None:
        record["tags"] = [t for t in record["tags"] if t != tag]

def tag_summary(log, tag):
    if not tag:
        return {}
    counts = {}
    for entry in log:
        tags = entry.get("tags", [])
        if tag in tags:
            counts[entry.get("type", "unknown")] = counts.get(entry.get("type", "unknown"), 0) + 1
    return counts
