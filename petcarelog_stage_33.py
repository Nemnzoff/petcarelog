# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: PetCareLog
# PetCareLog - Settings Module - Step 33: Add settings dictionary and update functions

_PET_CARE_SETTINGS = {
    "default_feeding_time": "07:00",
    "default_medication_duration_days": 10,
    "weight_unit": "kg",
    "temperature_unit": "celsius",
    "notification_enabled": True,
    "notification_sound": "default",
    "log_file_size_limit_mb": 50,
    "max_log_entries": 1000,
    "auto_backup_enabled": False,
    "backup_directory": "./backups",
    "theme": "light",
    "language": "en",
    "last_updated": None
}

def get_setting(key, default=None):
    """Retrieve a setting value, returning default if not found."""
    return _PET_CARE_SETTINGS.get(key, default)

def set_setting(key, value):
    """Update a setting value and return the updated settings dictionary."""
    if key not in _PET_CARE_SETTINGS:
        raise ValueError(f"Unknown setting: {key}")
    _PET_CARE_SETTINGS[key] = value
    _PET_CARE_SETTINGS["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return _PET_CARE_SETTINGS

def reset_settings():
    """Reset all settings to their default values."""
    _PET_CARE_SETTINGS["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return _PET_CARE_SETTINGS
