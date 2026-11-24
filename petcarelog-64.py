# === Stage 64: Add validation for relationship references ===
# Project: PetCareLog
class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def validate_relationships(entries, pets, medications, vet_visits):
    pet_ids = {p['id'] for p in pets}
    medication_ids = {m['id'] for m in medications}
    vet_visit_ids = {v['id'] for v in vet_visits}

    for entry in entries:
        if not entry.get('pet_id') or entry['pet_id'] not in pet_ids:
            raise ValidationError(
                "Entry %s: 'pet_id' %s does not match any known pet."
                % (entry.get('id'), entry.get('pet_id')))
        if 'medication_id' in entry and entry['medication_id'] not in medication_ids:
            raise ValidationError(
                "Entry %s: 'medication_id' %s does not match any known medication."
                % (entry.get('id'), entry.get('medication_id')))
        if 'vet_visit_id' in entry and entry['vet_visit_id'] not in vet_visit_ids:
            raise ValidationError(
                "Entry %s: 'vet_visit_id' %s does not match any known vet visit."
                % (entry.get('id'), entry.get('vet_visit_id')))
        if 'weight' in entry and entry['weight'] is not None:
            weight = float(entry['weight'])
            if weight <= 0:
                raise ValidationError(
                    "Entry %s: 'weight' must be positive, got %s."
                    % (entry.get('id'), entry.get('weight')))
        if 'temperature' in entry and entry['temperature'] is not None:
            temperature = float(entry['temperature'])
            if temperature < -100 or temperature > 100:
                raise ValidationError(
                    "Entry %s: 'temperature' %s is out of range."
                    % (entry.get('id'), entry.get('temperature')))
        if 'notes' in entry and len(entry['notes']) > 2000:
            raise ValidationError(
                "Entry %s: 'notes' exceed 2000 characters.")
        return True
