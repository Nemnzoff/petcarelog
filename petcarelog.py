# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: PetCareLog
import random

pets = [
    {"name": "Buddy", "species": "Dog", "breed": "Labrador", "age": 3, "weight_kg": 28.5},
    {"name": "Whiskers", "species": "Cat", "breed": "Persian", "age": 5, "weight_kg": 4.2},
    {"name": "Tweety", "species": "Bird", "breed": "Parakeet", "age": 1, "weight_kg": 0.08},
]

feed_schedule = {
    "Buddy": {"meal": "Dry food", "amount_g": 200, "time": "08:00"},
    "Whiskers": {"meal": "Canned food", "amount_g": 80, "time": "09:00"},
    "Tweety": {"meal": "Seed mix", "amount_g": 15, "time": "10:00"},
}

vet_history = [
    {"pet": "Buddy", "date": "2024-03-15", "reason": "Annual checkup", "notes": "Healthy"},
    {"pet": "Whiskers", "date": "2024-02-20", "reason": "Eye infection", "notes": "Prescribed eye drops"},
]

medications = [
    {"pet": "Whiskers", "med": "Eye drops", "dosage": "2 drops twice daily", "start_date": "2024-02-20"},
]

weight_log = [
    {"pet": "Buddy", "date": "2024-01-01", "weight_kg": 27.0},
    {"pet": "Buddy", "date": "2024-04-01", "weight_kg": 28.5},
    {"pet": "Whiskers", "date": "2024-01-01", "weight_kg": 4.0},
    {"pet": "Whiskers", "date": "2024-04-01", "weight_kg": 4.2},
]
