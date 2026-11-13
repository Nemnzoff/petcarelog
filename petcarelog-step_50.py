# === Stage 50: Add unit tests for import and export behavior ===
# Project: PetCareLog
import json
from datetime import datetime

class TestPetCareLog(unittest.TestCase):
    def setUp(self):
        self.pet = Pet(name="Buddy", species="Dog", breed="Labrador")
        self.log = PetCareLog()
        self.log.add_pet(self.pet)
        self.log.add_feeding(self.pet, food="Kibble", amount=200, note="Morning")
        self.log.add_weight(self.pet, weight=25.5, unit="kg", date="2024-01-15")

    def test_import_from_json_roundtrip(self):
        self.log.export_to_json("test_export.json")
        with open("test_export.json") as f:
            data = json.load(f)
        self.assertEqual(data["pets"][0]["name"], "Buddy")
        self.assertEqual(len(data["feedings"]), 1)
        self.assertEqual(data["weights"][0]["weight"], 25.5)

    def test_import_from_json_file(self):
        self.log.export_to_json("test_import.json")
        imported = PetCareLog()
        imported.import_from_json("test_import.json")
        self.assertEqual(len(imported.pets), 1)
        self.assertEqual(imported.pets[0].name, "Buddy")

    def test_export_to_csv(self):
        self.log.export_to_csv("test_export.csv")
        with open("test_export.csv") as f:
            content = f.read()
        self.assertIn("Buddy", content)
        self.assertIn("Kibble", content)

    def test_import_from_csv(self):
        self.log.export_to_csv("test_import.csv")
        imported = PetCareLog()
        imported.import_from_csv("test_import.csv")
        self.assertEqual(len(imported.pets), 1)

    def test_export_import_consistency(self):
        self.log.export_to_json("test_consistency.json")
        imported = PetCareLog()
        imported.import_from_json("test_consistency.json")
        self.assertEqual(len(self.log.pets), len(imported.pets))
        self.assertEqual(len(self.log.feedings), len(imported.feedings))
        self.assertEqual(len(self.log.weights), len(imported.weights))

    def tearDown(self):
        for f in ["test_export.json", "test_import.json", "test_export.csv", "test_import.csv", "test_consistency.json"]:
            if os.path.exists(f):
                os.remove(f)
