# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: PetCareLog
def reset_demo_data():
    """Reset the demo dataset to its original seed state for manual testing."""
    from petcare_log.models import Pet, Feeding, VetVisit, Medication, WeightRecord
    from petcare_log.services import PetService
    import random

    random.seed(1234)

    pets = [
        Pet("Bella", "dog", "Labrador", "Female", "2021-03-15"),
        Pet("Whiskers", "cat", "Siamese", "Male", "2019-07-01"),
        Pet("Rex", "dog", "German Shepherd", "Male", "2020-11-20"),
    ]
    for pet in pets:
        PetService.create_pet(pet)

    for pet in pets:
        PetService.create_feeding_schedule(
            pet,
            [{"time": "08:00", "amount": 150, "type": "kibble", "notes": "Morning meal"},
             {"time": "18:00", "amount": 150, "type": "kibble", "notes": "Evening meal"}],
        )
        PetService.create_weight_records(pet, [
            (15.2, "2024-01-05"),
            (15.6, "2024-02-05"),
            (16.0, "2024-03-05"),
        ])

    PetService.create_vet_visits(pets[0], [
        VetVisit("Annual checkup", "Dr. Smith", "Healthy", "2024-01-10"),
        VetVisit("Vaccination", "Dr. Smith", "Done", "2023-06-15"),
    ])
    PetService.create_vet_visits(pets[1], [
        VetVisit("Dental cleaning", "Dr. Jones", "Clean", "2023-11-20"),
    ])

    PetService.create_medications(pets[0], [
        Medication("Antibiotics", "5 days", "Twice daily", "2024-02-01"),
        Medication("Heartworm prevention", "Monthly", "Once monthly", "2024-01-01"),
    ])
    PetService.create_medications(pets[2], [
        Medication("Pain relief", "3 days", "Once daily", "2024-03-10"),
    ])

    print("Demo data reset complete. 3 pets with schedules, visits, medications, and weights.")

if __name__ == "__main__":
    reset_demo_data()
