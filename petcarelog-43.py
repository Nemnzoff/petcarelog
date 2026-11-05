# === Stage 43: Add CSV import for the primary record type ===
# Project: PetCareLog
def import_csv(path):
    records = []
    with open(path, newline="") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(",")
            if len(parts) < 4:
                continue
            try:
                weight = float(parts[3])
            except ValueError:
                weight = None
            records.append({
                "date": parts[0],
                "time": parts[1] if len(parts) > 1 else "",
                "type": parts[2],
                "note": parts[3] if len(parts) > 3 else "",
                "weight": weight,
            })
    return records
