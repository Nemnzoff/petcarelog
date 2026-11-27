# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: PetCareLog
CLEAR_CONFIRM = False


def _prompt_yes_no(prompt):
    answer = input(prompt).strip().lower()
    return answer in ("y", "yes")


def clear_state():
    global CLEAR_CONFIRM
    CLEAR_CONFIRM = False
    while not CLEAR_CONFIRM:
        answer = input("This will erase ALL data. Type 'yes' to confirm: ")
        CLEAR_CONFIRM = _prompt_yes_no(answer)
    if CLEAR_CONFIRM:
        pets.clear()
        feedings.clear()
        vet_visits.clear()
        medications.clear()
        weights.clear()
        logs.clear()
        print("PetCareLog has been cleared.")
    else:
        print("Clear cancelled.")
