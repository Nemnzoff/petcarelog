# === Stage 11: Add JSON export for the current application state ===
# Project: PetCareLog
def export_json(path="petcare_log.json"):
    with open(path, "w") as f:
        json.dump(
            {
                "pets": pets,
                "feeding_schedule": feeding_schedule,
                "vet_visits": vet_visits,
                "medications": medications,
                "weights": weights,
                "notes": notes,
                "timestamp": datetime.now().isoformat(),
            },
            f,
            indent=2,
        )
