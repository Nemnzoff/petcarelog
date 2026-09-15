# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: PetCareLog
def archive_records(log, days=365):
    cutoff = datetime.now() - timedelta(days=days)
    archived = []
    for entry in log:
        if entry.get('date') and entry['date'] < cutoff:
            archived.append(entry.copy())
    if archived:
        log['archive'] = archived
        log['archived_count'] = len(archived)
    return log

def restore_records(log, entries=None):
    if entries is None:
        entries = log.get('archive', [])
    log['archive'] = []
    log['archived_count'] = 0
    log.update(entries)
    return log
