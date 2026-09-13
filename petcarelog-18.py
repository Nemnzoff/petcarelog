# === Stage 18: Add an activity log with timestamps and action names ===
# Project: PetCareLog
class ActivityLog:
    """Records daily activities with timestamps and action names."""

    def __init__(self, pet_name):
        self.pet_name = pet_name
        self.entries = []

    def add_activity(self, action, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now()
        entry = {
            "pet": self.pet_name,
            "action": action,
            "timestamp": timestamp,
        }
        self.entries.append(entry)
        return entry

    def get_activities(self, start=None, end=None):
        activities = sorted(self.entries, key=lambda x: x["timestamp"])
        if start:
            activities = [e for e in activities if e["timestamp"] >= start]
        if end:
            activities = [e for e in activities if e["timestamp"] <= end]
        return activities

    def __repr__(self):
        return f"<ActivityLog pet={self.pet_name} entries={len(self.entries)}>"
