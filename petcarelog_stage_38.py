# === Stage 38: Add data integrity checks for broken references ===
# Project: PetCareLog
def check_data_integrity(records):
    pet_ids = {entry["pet_id"] for entry in records if entry.get("pet_id") is not None}
    broken_references = []
    for entry in records:
        if entry.get("pet_id") not in pet_ids:
            broken_references.append((entry.get("id"), "pet_id", entry.get("pet_id")))
        if entry.get("medication_id") and entry["medication_id"] not in pet_ids:
            broken_references.append((entry.get("id"), "medication_id", entry["medication_id"]))
        if entry.get("vet_id") and entry["vet_id"] not in pet_ids:
            broken_references.append((entry.get("id"), "vet_id", entry["vet_id"]))
    if broken_references:
        raise ValueError(f"Broken references found: {broken_references}")
    return True
