# === Stage 40: Add plain text report export ===
# Project: PetCareLog
def export_report(pets, records):
    lines = []
    for pet in pets:
        lines.append(f"Pet: {pet['name']} ({pet['species']})")
        lines.append(f"Weight: {pet['weight']}")
        lines.append("")
        for rec in records.get(pet['id'], []):
            if rec['type'] == 'feeding':
                lines.append(f"Feed {rec['amount']} at {rec['time']}")
            elif rec['type'] == 'medication':
                lines.append(f"Medication: {rec['medication']} {rec['dose']} at {rec['time']}")
            elif rec['type'] == 'vet_visit':
                lines.append(f"Vet visit: {rec['reason']} on {rec['date']}")
            elif rec['type'] == 'weight':
                lines.append(f"Weight: {rec['weight']} on {rec['date']}")
        lines.append("")
    return "\n".join(lines)
