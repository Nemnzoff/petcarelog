# === Stage 31: Add compact table rendering for long lists ===
# Project: PetCareLog
def render_compact_table(records):
    """Render a long list of records into a compact table layout."""
    if not records:
        return "No records to display."
    lines = []
    col_widths = {}
    for record in records:
        for key, value in record.items():
            col_widths[key] = max(col_widths.get(key, 0), len(str(value)))
    col_widths = {k: max(v, 3) for k, v in col_widths.items()}
    header = " | ".join(f"{k:<{col_widths[k]}}" for k in col_widths)
    lines.append(header)
    lines.append("-" * len(header))
    for record in records:
        row = " | ".join(f"{record.get(k, ''):<{col_widths[k]}}" for k in col_widths)
        lines.append(row)
    return "\n".join(lines)
