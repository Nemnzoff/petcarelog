# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: PetCareLog
def validate_required(value, field_name=""):
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise ValueError(f"Field '{field_name}' is required")
    return True

def validate_positive(value, field_name=""):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"Field '{field_name}' must be a positive number")
    return True

def validate_short_text(value, max_length=50, field_name=""):
    if not isinstance(value, str) or len(value) > max_length:
        raise ValueError(f"Field '{field_name}' must be a short text string (max {max_length} chars)")
    return True

def validate_date_format(value, field_name=""):
    import datetime
    if not isinstance(value, str):
        raise ValueError(f"Field '{field_name}' must be a date string")
    try:
        datetime.datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError(f"Field '{field_name}' must be in YYYY-MM-DD format")
