# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: PetCareLog
print("=== PetCareLog Demo Scenario ===")

dog = {
    "name": "Buddy",
    "species": "Dog",
    "weight_kg": 22.5,
    "feedings": [
        {"time": "08:00", "amount_grams": 200, "food": "Dry kibble"},
        {"time": "18:00", "amount_grams": 200, "food": "Dry kibble"},
    ],
    "vet_visits": [
        {"date": "2025-01-10", "clinic": "City Vet", "notes": "Annual checkup", "cost": 65.0},
        {"date": "2025-07-20", "clinic": "City Vet", "notes": "Vaccination", "cost": 40.0},
    ],
    "medications": [
        {"name": "Heartworm prevent", "dosage": "1 tablet", "frequency": "Monthly", "next_date": "2025-08-10"},
    ],
    "weight_history": [
        {"date": "2025-01-10", "weight_kg": 22.0},
        {"date": "2025-04-01", "weight_kg": 22.3},
        {"date": "2025-07-20", "weight_kg": 22.5},
    ],
}

print(f"\nPet: {dog['name']} ({dog['species']})")
print(f"Weight: {dog['weight_kg']} kg")

print("\nFeeding schedule:")
for f in dog["feedings"]:
    print(f"  {f['time']} - {f['amount_grams']}g of {f['food']}")

print("\nVet visits:")
for v in dog["vet_visits"]:
    print(f"  {v['date']} at {v['clinic']}: {v['notes']} (${v['cost']:.2f})")

print("\nMedications:")
for m in dog["medications"]:
    print(f"  {m['name']}: {m['dosage']} every {m['frequency']}, next {m['next_date']}")

print("\nWeight history (kg):")
for w in dog["weight_history"]:
    print(f"  {w['date']}: {w['weight_kg']} kg")

total_spent = sum(v["cost"] for v in dog["vet_visits"])
print(f"\nTotal vet spending: ${total_spent:.2f}")
print(f"Weight change over period: {dog['weight_history'][-1]['weight_kg'] - dog['weight_history'][0]['weight_kg']:+.2f} kg")
print("=== Demo complete ===")
