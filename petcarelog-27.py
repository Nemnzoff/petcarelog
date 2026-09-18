# === Stage 27: Add monthly summary calculations ===
# Project: PetCareLog
def monthly_summary(records):
    """
    Compute a compact monthly summary from pet care records.
    Returns a list of dicts: month, total_cost, feeding_count, vet_count,
    avg_weight, notes.
    """
    from collections import defaultdict
    monthly = defaultdict(lambda: {
        'cost': 0.0, 'feedings': 0, 'vets': 0, 'weights': []
    })
    for r in records:
        key = (r.get('date', '')[:7])  # YYYY-MM
        m = monthly[key]
        m['cost'] += r.get('cost', 0)
        if r.get('type') == 'feeding': m['feedings'] += 1
        if r.get('type') == 'vet': m['vets'] += 1
        if 'weight' in r: m['weights'].append(r['weight'])
    result = []
    for month, data in sorted(monthly.items()):
        avg_w = (sum(data['weights']) / len(data['weights'])) if data['weights'] else 0
        result.append({
            'month': month,
            'total_cost': round(data['cost'], 2),
            'feeding_count': data['feedings'],
            'vet_count': data['vets'],
            'avg_weight': round(avg_w, 1),
        })
    return result
