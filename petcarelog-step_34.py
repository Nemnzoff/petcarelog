# === Stage 34: Add support for multiple local user profiles ===
# Project: PetCareLog
class UserProfile:
    def __init__(self, name, email, phone=""):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"UserProfile(name={self.name!r}, email={self.email!r}, phone={self.phone!r})"

    def __eq__(self, other):
        if not isinstance(other, UserProfile):
            return False
        return self.name == other.name and self.email == other.email

    def __hash__(self):
        return hash((self.name, self.email))


class UserStore:
    def __init__(self):
        self.profiles = {}

    def add(self, profile):
        if profile.email in self.profiles:
            raise ValueError(f"Email {profile.email!r} already registered")
        self.profiles[profile.email] = profile

    def get(self, email):
        return self.profiles.get(email)

    def list_profiles(self):
        return list(self.profiles.values())

    def remove(self, email):
        return self.profiles.pop(email, None)

    def __len__(self):
        return len(self.profiles)


store = UserStore()
