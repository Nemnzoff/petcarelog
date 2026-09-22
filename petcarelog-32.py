# === Stage 32: Add pagination helpers for long console output ===
# Project: PetCareLog
def paginate(text, chunk_size=80):
    """Yield text in chunks of approximately chunk_size characters."""
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]
