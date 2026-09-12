# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: PetCareLog
def dispatch(text):
    text = text.strip().lower()
    if text == "help":
        return "Commands: help, feed <pet> <amount>, vet <pet>, med <pet> <drug> <dose>, weight <pet> <kg>, list, quit"
    elif text.startswith("feed"):
        parts = text.split(maxsplit=2)
        if len(parts) == 3:
            pet, amount = parts[1], parts[2]
            return f"Feeding {pet} with {amount}"
        return "Usage: feed <pet> <amount>"
    elif text.startswith("vet"):
        pet = text.split(maxsplit=1)[1] if ' ' in text else text[3:]
        return f"Scheduled vet visit for {pet}"
    elif text.startswith("med"):
        parts = text.split(maxsplit=2)
        if len(parts) == 3:
            pet, drug = parts[1], parts[2]
            return f"Medication {drug} given to {pet}"
        return "Usage: med <pet> <drug> <dose>"
    elif text.startswith("weight"):
        parts = text.split(maxsplit=1)
        if len(parts) == 2:
            return f"Recorded weight for {parts[1]}"
        return "Usage: weight <pet> <kg>"
    elif text == "list":
        return "Pet log contains no records yet"
    elif text == "quit":
        return "Goodbye!"
    else:
        return "Unknown command. Type 'help' for a list."
