# === Stage 22: Add favorite records and quick favorite listing ===
# Project: PetCareLog
import csv
import os
import datetime
from collections import defaultdict

class Favorites:
    """Manage favorite pet records and quick listing."""
    def __init__(self, db_path):
        self.db_path = db_path
        self._ensure_db(db_path)

    def _ensure_db(self, db_path):
        if not os.path.exists(db_path):
            with open(db_path, 'w', newline='') as f:
                f.write('name;species;breed;age;weight;notes\n')

    def add_favorite(self, name, species, breed, age, weight, notes=''):
        with open(self.db_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, species, breed, age, weight, notes])
        return True

    def get_favorites(self):
        favorites = []
        if not os.path.exists(self.db_path):
            return favorites
        with open(self.db_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                favorites.append({
                    'name': row.get('name', ''),
                    'species': row.get('species', ''),
                    'breed': row.get('breed', ''),
                    'age': row.get('age', ''),
                    'weight': row.get('weight', ''),
                    'notes': row.get('notes', '')
                })
        return favorites

    def get_favorite_names(self):
        favs = self.get_favorites()
        return [f['name'] for f in favs]
