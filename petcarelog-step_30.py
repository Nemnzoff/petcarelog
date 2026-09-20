# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: PetCareLog
def parse_date(date_str, default_formats=None):
    """Parse a date string with clear error messages."""
    if default_formats is None:
        default_formats = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y", "%m-%d-%Y", "%m/%d/%Y"]

    if not date_str or not isinstance(date_str, str):
        raise ValueError(f"Invalid date string: '{date_str}' (must be a non-empty string)")

    date_str = date_str.strip()
    if not date_str:
        raise ValueError(f"Empty date string provided")

    for fmt in default_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Unable to parse date '{date_str}'. Supported formats: {', '.join(default_formats)}")
