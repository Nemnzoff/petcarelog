# === Stage 66: Add export of a short status dashboard ===
# Project: PetCareLog
def export_status_dashboard(pets, entries):
    dashboard = []
    for pet in pets:
        pet_entries = [e for e in entries if e['pet_id'] == pet['id']]
        total_feeds = sum(1 for e in pet_entries if e['type'] == 'feed')
        total_vet_visits = sum(1 for e in pet_entries if e['type'] == 'vet')
        total_medications = sum(1 for e in pet_entries if e['type'] == 'medication')
        recent_weights = [e['weight'] for e in pet_entries if e['type'] == 'weight']
        latest_weight = max(recent_weights) if recent_weights else None
        average_weight = sum(recent_weights) / len(recent_weights) if recent_weights else None
        dashboard.append({
            'name': pet['name'],
            'species': pet['species'],
            'total_feeds': total_feeds,
            'total_vet_visits': total_vet_visits,
            'total_medications': total_medications,
            'latest_weight': latest_weight,
            'average_weight': average_weight,
        })
    return dashboard
