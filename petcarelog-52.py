# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: PetCareLog
def get_feeding_times(pet_id, date=None):
    """Return the list of scheduled feeding times for a pet.

    Fetches feeding entries for the given pet and optionally filters
    by a single calendar date (YYYY-MM-DD). When date is None, all
    feeding times are returned in chronological order.
    """
    entries = select_feeding_entries(pet_id, date)
    return sorted([e["time"] for e in entries], key=lambda t: t)


def get_next_vet_visit(pet_id):
    """Return the earliest upcoming vet visit for a pet.

    Inspects scheduled vet visits and returns the next one whose visit
    date is at or after today. Returns None when no future visits exist.
    """
    today = date.today().isoformat()
    visits = [v for v in get_vet_visits(pet_id) if v["visit_date"] >= today]
    return min(visits, key=lambda v: v["visit_date"], default=None)


def get_current_medications(pet_id, date=None):
    """Return medications that are active for a pet on the given date.

    A medication is considered active when its start date is on or
    before the reference date and its end date is after the reference
    date. Passing None uses today as the reference date.
    """
    ref = date.today().isoformat() if date is None else date
    medications = get_medications(pet_id)
    return [
        m for m in medications
        if m["start_date"] <= ref and m["end_date"] > ref
    ]


def get_weight_history(pet_id):
    """Return weight records for a pet ordered from oldest to newest.

    Retrieves every recorded weight entry for the pet and sorts them
    by record date so the earliest measurement appears first.
    """
    records = get_weight_records(pet_id)
    return sorted(records, key=lambda r: r["record_date"])


def get_weight_summary(pet_id):
    """Return a summary of weight measurements for a pet.

    Computes the count of recorded weights, the minimum, maximum, and
    average weight in grams. Returns None when no records exist.
    """
    records = get_weight_history(pet_id)
    if not records:
        return None
    weights = [r["weight_grams"] for r in records]
    return {
        "count": len(weights),
        "min": min(weights),
        "max": max(weights),
        "average": sum(weights) / len(weights),
    }
