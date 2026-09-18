# === Stage 26: Add weekly summary calculations ===
# Project: PetCareLog
def weekly_summary(records):
    """Return a dict with weekly feeding, vet, med counts and avg weight change."""
    from datetime import datetime, timedelta, date
    today = date.today()
    week = {d.strftime("%Y-%m-%d") for d in [today - timedelta(days=i) for i in range(7)]}
    filtered = [r for r in records if r["date"].strftime("%Y-%m-%d") in week]
    return {
        "feeding_count": sum(1 for r in filtered if r["category"] == "Feeding"),
        "vet_count": sum(1 for r in filtered if r["category"] == "Vet Visit"),
        "med_count": sum(1 for r in filtered if r["category"] == "Medication"),
        "weight_changes": [r["value"] for r in filtered if r["category"] == "Weight"],
        "avg_weight_change": sum(r["value"] for r in filtered if r["category"] == "Weight") / max(len(r["value"] for r in filtered if r["category"] == "Weight"), 1),
    }
