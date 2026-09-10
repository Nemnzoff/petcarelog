# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: PetCareLog
import json
from pathlib import Path

def load_json_safe(path: Path) -> dict:
    """Load a JSON file with friendly error handling for malformed data."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Malformed JSON in {path}: {e}")
        return {}
    except PermissionError:
        print(f"Permission denied reading: {path}")
        return {}
    except Exception as e:
        print(f"Unexpected error reading {path}: {e}")
        return {}
