# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: PetCareLog
def update_record(self, record_type, record_id, updates):
    """Update an existing record, returning the modified record or None if not found."""
    if record_type not in self._db:
        return None
    records = self._db[record_type]
    for i, rec in enumerate(records):
        if rec.get("id") == record_id:
            for key, value in updates.items():
                rec[key] = value
            return rec
    return None

def update_feeding(self, pet_id, meal_time, amount_grams, notes=""):
    """Add a new feeding log entry for a pet."""
    record = {"id": f"feed_{pet_id}_{meal_time}", "pet_id": pet_id, "meal_time": meal_time, "amount_grams": amount_grams, "notes": notes, "logged_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
    self._db["feedings"].append(record)
    return record

def update_medication(self, pet_id, medication_name, dosage, frequency, duration_days, notes=""):
    """Add a new medication record for a pet."""
    record = {"id": f"med_{pet_id}_{datetime.datetime.now().strftime('%Y%m%d')}", "pet_id": pet_id, "medication_name": medication_name, "dosage": dosage, "frequency": frequency, "duration_days": duration_days, "start_date": datetime.datetime.now().strftime("%Y-%m-%d"), "end_date": (datetime.datetime.now() + datetime.timedelta(days=int(duration_days))).strftime("%Y-%m-%d"), "notes": notes}
    self._db["medications"].append(record)
    return record

def update_vet_visit(self, pet_id, diagnosis, treatment, cost, vet_name, notes=""):
    """Add a new vet visit record for a pet."""
    record = {"id": f"vet_{pet_id}_{datetime.datetime.now().strftime('%Y%m%d')}", "pet_id": pet_id, "diagnosis": diagnosis, "treatment": treatment, "cost": float(cost), "vet_name": vet_name, "visit_date": datetime.datetime.now().strftime("%Y-%m-%d"), "notes": notes}
    self._db["vet_visits"].append(record)
    return record

def update_weight(self, pet_id, weight_grams, measurement_date=None):
    """Add a new weight tracking record for a pet."""
    if measurement_date is None:
        measurement_date = datetime.datetime.now().strftime("%Y-%m-%d")
    record = {"id": f"weight_{pet_id}_{measurement_date}", "pet_id": pet_id, "weight_grams": float(weight_grams), "measurement_date": measurement_date}
    self._db["weights"].append(record)
    return record
