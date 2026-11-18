# === Stage 57: Add structured result objects for command handlers ===
# Project: PetCareLog
class CareEntry:
    def __init__(self, pet_name, timestamp, category, details):
        self.pet_name = pet_name
        self.timestamp = timestamp
        self.category = category
        self.details = details

    def to_dict(self):
        return {
            "pet_name": self.pet_name,
            "timestamp": self.timestamp,
            "category": self.category,
            "details": self.details,
        }

    def __str__(self):
        return f"[{self.timestamp}] {self.category} - {self.pet_name}: {self.details}"


class CareLogResult:
    def __init__(self, success, message, entries=None):
        self.success = success
        self.message = message
        self.entries = entries or []

    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "entries": [entry.to_dict() for entry in self.entries],
        }

    def __str__(self):
        if not self.success:
            return f"Error: {self.message}"
        lines = [f"Success: {self.message}"]
        for entry in self.entries:
            lines.append(str(entry))
        return "\n".join(lines)


def format_result(result):
    return result.to_dict()
