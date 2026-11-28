# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: PetCareLog
def seed_demo_data(log):
    sample_owners = [
        {"id": "o1", "name": "Alice", "email": "alice@example.com"},
        {"id": "o2", "name": "Bob", "email": "bob@example.com"},
    ]
    sample_pets = [
        {"id": "p1", "name": "Bella", "species": "dog", "breed": "Labrador", "owner_id": "o1", "birth_date": "2020-01-15"},
        {"id": "p2", "name": "Whiskers", "species": "cat", "breed": "Siamese", "owner_id": "o1", "birth_date": "2019-06-20"},
        {"id": "p3", "name": "Rex", "species": "dog", "breed": "Beagle", "owner_id": "o2", "birth_date": "2021-03-10"},
    ]
    sample_visits = [
        {"id": "v1", "pet_id": "p1", "date": "2024-01-10", "reason": "Annual checkup", "notes": "Healthy overall"},
        {"id": "v2", "pet_id": "p2", "date": "2024-02-05", "reason": "Vaccination", "notes": "Rabies booster"},
    ]
    sample_medications = [
        {"id": "m1", "pet_id": "p1", "name": "HeartGuard", "dosage": "1 tablet", "frequency": "daily", "start_date": "2024-01-11", "end_date": None},
        {"id": "m2", "pet_id": "p3", "name": "Antibiotic", "dosage": "5 ml", "frequency": "twice daily", "start_date": "2024-03-01", "end_date": "2024-03-10"},
    ]
    sample_weights = [
        {"id": "w1", "pet_id": "p1", "date": "2024-01-01", "weight_kg": 28.5},
        {"id": "w2", "pet_id": "p1", "date": "2024-02-01", "weight_kg": 29.0},
        {"id": "w3", "pet_id": "p2", "date": "2024-02-01", "weight_kg": 4.2},
    ]
    log["owners"] = sample_owners
    log["pets"] = sample_pets
    log["visits"] = sample_visits
    log["medications"] = sample_medications
    log["weights"] = sample_weights
