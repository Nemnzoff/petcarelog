# === Stage 42: Add CSV export without external dependencies ===
# Project: PetCareLog
def export_to_csv(records, filename="petcare_export.csv"):
    if not records:
        return
    fields = ["pet", "date", "category", "description", "quantity", "notes"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in records:
            writer.writerow(r)
