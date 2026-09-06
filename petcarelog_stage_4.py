# === Stage 4: Implement create operations for the primary records ===
# Project: PetCareLog
def create_pet(self, name, species, breed, date_of_birth):
    """Create a new pet record."""
    pet = {
        'id': self._next_id('pets'),
        'name': name,
        'species': species,
        'breed': breed,
        'date_of_birth': date_of_birth,
        'created_at': datetime.now().isoformat(),
    }
    self._data['pets'].append(pet)
    return pet

def create_feeding_schedule(self, pet_id, meal_time, amount, notes, frequency):
    """Create a new feeding schedule entry."""
    entry = {
        'id': self._next_id('feeding'),
        'pet_id': pet_id,
        'meal_time': meal_time,
        'amount': amount,
        'notes': notes,
        'frequency': frequency,
        'created_at': datetime.now().isoformat(),
    }
    self._data['feeding'].append(entry)
    return entry

def create_vet_visit(self, pet_id, date, description, cost, vet_name):
    """Create a new vet visit record."""
    visit = {
        'id': self._next_id('vet'),
        'pet_id': pet_id,
        'date': date,
        'description': description,
        'cost': cost,
        'vet_name': vet_name,
        'created_at': datetime.now().isoformat(),
    }
    self._data['vet'].append(visit)
    return visit

def create_medication(self, pet_id, medication_name, dosage, frequency, start_date, end_date):
    """Create a new medication record."""
    med = {
        'id': self._next_id('med'),
        'pet_id': pet_id,
        'medication_name': medication_name,
        'dosage': dosage,
        'frequency': frequency,
        'start_date': start_date,
        'end_date': end_date,
        'created_at': datetime.now().isoformat(),
    }
    self._data['med'].append(med)
    return med

def create_weight_record(self, pet_id, date, weight):
    """Create a new weight record."""
    record = {
        'id': self._next_id('weight'),
        'pet_id': pet_id,
        'date': date,
        'weight': weight,
        'created_at': datetime.now().isoformat(),
    }
    self._data['weight'].append(record)
    return record
