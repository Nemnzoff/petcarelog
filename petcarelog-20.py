# === Stage 20: Add duplicate detection for newly created records ===
# Project: PetCareLog
def detect_duplicates(records, new_record):
    """Detect duplicate records based on type and key fields."""
    type_map = {
        'feeding': ['pet_name', 'pet_type', 'food_type', 'amount', 'time'],
        'vet_visit': ['pet_name', 'pet_type', 'date', 'symptoms'],
        'medication': ['pet_name', 'pet_type', 'medication_name', 'dose', 'frequency'],
        'weight': ['pet_name', 'pet_type', 'weight', 'date']
    }
    record_type = new_record.get('type', '')
    if record_type in type_map:
        key_fields = type_map[record_type]
        for record in records:
            if record.get('type', '') == record_type:
                if all(record.get(field) == new_record.get(field) for field in key_fields):
                    return True
    return False
