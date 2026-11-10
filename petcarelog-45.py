# === Stage 45: Add restore from backup with validation ===
# Project: PetCareLog
def restore_from_backup(backup_path, log_path):
    if not os.path.isfile(backup_path):
        raise FileNotFoundError("Backup file does not exist.")
    if os.path.isdir(backup_path):
        raise ValueError("Backup path must be a file, not a directory.")
    if not backup_path.endswith((".json", ".txt")):
        raise ValueError("Unsupported backup format.")
    with open(backup_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        raise ValueError("Backup file is empty.")
    if log_path and os.path.isdir(log_path):
        raise ValueError("Target log path is a directory.")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(content)
    return True
