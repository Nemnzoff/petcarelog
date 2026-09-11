# === Stage 13: Add file save support using a configurable path ===
# Project: PetCareLog
import json
import os

class FileStorage:
    def __init__(self, file_path="petcare_log.json"):
        self.file_path = file_path

    def save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, "r") as f:
            return json.load(f)
