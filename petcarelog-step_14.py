# === Stage 14: Add file load support with fallback demo data ===
# Project: PetCareLog
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "pets": [
                {"name": "Buddy", "species": "dog", "weight": 25.0, "last_checkup": "2025-01-15", "medications": []},
                {"name": "Whiskers", "species": "cat", "weight": 4.2, "last_checkup": "2025-02-20", "medications": []},
            ],
            "feeding_schedule": [
                {"pet": "Buddy", "meal_time": "07:00", "food_type": "dry kibble", "amount": 1.5},
                {"pet": "Buddy", "meal_time": "19:00", "food_type": "dry kibble", "amount": 1.5},
                {"pet": "Whiskers", "meal_time": "08:00", "food_type": "wet food", "amount": 0.2},
                {"pet": "Whiskers", "meal_time": "18:00", "food_type": "wet food", "amount": 0.2},
            ],
            "vet_visits": [
                {"pet": "Buddy", "date": "2025-01-15", "reason": "Annual checkup", "notes": "Healthy, weight on track"},
                {"pet": "Whiskers", "date": "2025-02-20", "reason": "Vaccination", "notes": "Rabies vaccine given"},
            ],
            "medications": [
                {"pet": "Buddy", "name": "Heartgard", "dosage": "1 tablet", "frequency": "monthly", "next_due": "2025-04-15"},
            ],
        }
