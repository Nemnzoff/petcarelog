# === Stage 51: Add unit tests for search and filter behavior ===
# Project: PetCareLog
def test_search_by_name(self):
    self.pet.add_feeding("kibble", "08:00", 40)
    self.pet.add_feeding("wet food", "19:00", 60)
    results = self.pet.search_entries("kibble")
    self.assertEqual(len(results), 1)
    self.assertEqual(results[0]["food"], "kibble")


def test_filter_by_date_range(self):
    self.pet.add_feeding("kibble", "2024-01-01", 40)
    self.pet.add_feeding("kibble", "2024-01-15", 45)
    self.pet.add_feeding("kibble", "2024-02-01", 50)
    results = self.pet.filter_entries("2024-01-01", "2024-01-10")
    self.assertEqual(len(results), 1)
    self.assertEqual(results[0]["date"], "2024-01-01")


def test_filter_by_food_type(self):
    self.pet.add_feeding("kibble", "08:00", 40)
    self.pet.add_feeding("wet food", "19:00", 60)
    results = self.pet.filter_entries(food_type="kibble")
    self.assertEqual(len(results), 1)
    self.assertEqual(results[0]["food"], "kibble")


def test_search_vet_visits_by_keyword(self):
    self.pet.add_vet_visit("Annual checkup", "2024-01-10", "Healthy", "Dr. Smith")
    self.pet.add_vet_visit("Vaccination", "2024-02-05", "Done", "Dr. Jones")
    results = self.pet.search_entries("vaccination")
    self.assertEqual(len(results), 1)
    self.assertEqual(results[0]["type"], "vet_visit")


def test_filter_medications_by_date(self):
    self.pet.add_medication("Amoxicillin", "2024-01-01", "500mg", 3)
    self.pet.add_medication("Ibuprofen", "2024-01-20", "200mg", 2)
    results = self.pet.filter_entries("2024-01-01", "2024-01-10")
    self.assertEqual(len(results), 1)
    self.assertEqual(results[0]["medication"], "Amoxicillin")
