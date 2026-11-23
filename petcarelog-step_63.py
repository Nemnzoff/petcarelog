# === Stage 63: Add relationships between records where useful ===
# Project: PetCareLog
class CareLog:
    def __init__(self):
        self.pets = {}
        self.feedings = []
        self.vet_visits = []
        self.medications = []
        self.weights = []

    def add_pet(self, name, species):
        pet_id = len(self.pets) + 1
        self.pets[pet_id] = {"name": name, "species": species}
        return pet_id

    def add_feeding(self, pet_id, food, amount, time):
        self.feedings.append({
            "pet_id": pet_id,
            "food": food,
            "amount": amount,
            "time": time,
        })

    def add_vet_visit(self, pet_id, date, notes, next_visit=None):
        self.vet_visits.append({
            "pet_id": pet_id,
            "date": date,
            "notes": notes,
            "next_visit": next_visit,
        })

    def add_medication(self, pet_id, name, dosage, start_date, end_date=None):
        self.medications.append({
            "pet_id": pet_id,
            "name": name,
            "dosage": dosage,
            "start_date": start_date,
            "end_date": end_date,
        })

    def add_weight(self, pet_id, date, weight):
        self.weights.append({
            "pet_id": pet_id,
            "date": date,
            "weight": weight,
        })

    def get_pet(self, pet_id):
        return self.pets.get(pet_id)

    def get_pet_feedings(self, pet_id):
        return [f for f in self.feedings if f["pet_id"] == pet_id]

    def get_pet_vet_visits(self, pet_id):
        return [v for v in self.vet_visits if v["pet_id"] == pet_id]

    def get_pet_medications(self, pet_id):
        return [m for m in self.medications if m["pet_id"] == pet_id]

    def get_pet_weights(self, pet_id):
        return [w for w in self.weights if w["pet_id"] == pet_id]
