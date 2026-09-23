# === Stage 35: Add active user switching and user-specific records ===
# Project: PetCareLog
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User({self.name}, {self.email})"
