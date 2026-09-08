# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: PetCareLog
def format_pet_entry(entry):
    lines = [
        f"Name: {entry['name']}",
        f"Weight: {entry.get('weight', 'N/A')}",
        f"Last Vet Visit: {entry.get('last_vet_visit', 'N/A')}",
        f"Current Medication: {entry.get('current_meds', 'None')}",
    ]
    return "\n".join(lines)

def format_feeding_log(log):
    today = log.get('date', 'N/A')
    entries = log.get('entries', [])
    formatted = [f"Date: {today}"]
    for e in entries:
        formatted.append(f"  - {e['time']} | {e['food']} | {e['amount']}g")
    return "\n".join(formatted)

def format_vet_log(log):
    today = log.get('date', 'N/A')
    entries = log.get('entries', [])
    formatted = [f"Date: {today}"]
    for e in entries:
        formatted.append(
            f"  - {e['time']} | {e['reason']} | {e['vet']} | Cost: ${e.get('cost', 'N/A')}"
        )
    return "\n".join(formatted)
