# === Stage 44: Add backup creation for the data file ===
# Project: PetCareLog
def backup_data(data_file, backup_dir="backups"):
    if not os.path.exists(data_file):
        print(f"No data file found at {data_file}")
        return
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(data_file)}.{timestamp}.bak")
    try:
        os.makedirs(backup_dir, exist_ok=True)
        shutil.copy2(data_file, backup_path)
        print(f"Backup created: {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")


def list_backups(backup_dir="backups"):
    if not os.path.exists(backup_dir):
        print(f"No backups found in {backup_dir}")
        return
    backup_files = [f for f in os.listdir(backup_dir) if f.endswith(".bak")]
    if not backup_files:
        print(f"No backups found in {backup_dir}")
        return
    for f in sorted(backup_files, reverse=True):
        print(f"{f}  ({datetime.fromtimestamp(os.path.getmtime(os.path.join(backup_dir, f))).strftime('%Y-%m-%d %H:%M:%S')})")
