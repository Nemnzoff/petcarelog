# === Stage 25: Add daily summary calculations ===
# Project: PetCareLog
def daily_summary(records):
    """Return a dict with daily summary stats from a list of records."""
    from datetime import date
    today = date.today()
    summary = {
        "today": {
            "feedings": 0,
            "vet_visits": 0,
            "medications": 0,
            "weight_records": 0,
        },
        "week": {
            "feedings": 0,
            "vet_visits": 0,
            "medications": 0,
            "weight_records": 0,
        },
        "month": {
            "feedings": 0,
            "vet_visits": 0,
            "medications": 0,
            "weight_records": 0,
        },
    }
    for r in records:
        if isinstance(r, dict):
            rec = r.get("record", r)
        else:
            rec = r
        rec_date = rec.get("date") or rec.get("record_date")
        if not rec_date:
            continue
        try:
            rd = date.fromisoformat(str(rec_date))
        except (ValueError, TypeError):
            continue
        if rd == today:
            for cat in summary["today"]:
                summary["today"][cat] += rec.get(cat, 0)
        week_start = today - timedelta(days=6)
        month_start = today - timedelta(days=30)
        if week_start <= rd <= today:
            for cat in summary["week"]:
                summary["week"][cat] += rec.get(cat, 0)
        if month_start <= rd <= today:
            for cat in summary["month"]:
                summary["month"][cat] += rec.get(cat, 0)
    return summary
