# === Stage 36: Add templates for quickly creating common records ===
# Project: PetCareLog
# pet_care_log_templates.py
# Quick templates for common records.

def new_feeding_schedule(name: str, times: list[str]) -> dict:
    return {"schedule_name": name, "feeding_times": times}

def new_medication(name: str, drug: str, dosage: str, frequency: str) -> dict:
    return {"med_name": name, "drug": drug, "dosage": dosage, "frequency": frequency}

def new_vet_visit(name: str, reason: str, date: str, notes: str = "") -> dict:
    return {"visit_name": name, "reason": reason, "date": date, "notes": notes}

def new_weight_record(pet_name: str, weight: float, date: str) -> dict:
    return {"pet_name": pet_name, "weight": weight, "date": date}
