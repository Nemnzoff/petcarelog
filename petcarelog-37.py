# === Stage 37: Add recommendations for the next useful action ===
# Project: PetCareLog
def suggest_next_action(log):
    """Recommend the next useful action based on current log state."""
    actions = []

    if log.get("vet_visit_date") and log.get("vet_visit_date") < "2025-03-01":
        actions.append("Schedule a follow-up vet visit soon.")

    if log.get("medications"):
        for i, med in enumerate(log["medications"]):
            if med.get("days_remaining", 0) <= 0:
                actions.append(f"Refill medication: {med.get('name', 'Unknown')}.")

    if log.get("last_weight") and log.get("last_weight_date"):
        last_w = log["last_weight"]
        if last_w["weight"] < 2.0:
            actions.append("Consider increasing food intake or consult a vet about low weight.")
        elif last_w["weight"] > 4.0:
            actions.append("Consider reducing food intake or consult a vet about high weight.")

    if not log.get("feeding_schedule"):
        actions.append("Create a feeding schedule for the pet.")

    if not log.get("vet_visit_date"):
        actions.append("Record the next scheduled vet visit date.")

    if not log.get("medications"):
        actions.append("Add any current medications the pet is taking.")

    if not log.get("last_weight"):
        actions.append("Record the pet's current weight.")

    return actions
