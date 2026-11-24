# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: PetCareLog
import re


def merge_imports(source_lines):
    """Merge duplicate imports while preserving first-seen order and comments."""
    seen = {}
    order = []
    for raw in source_lines:
        stripped = raw.lstrip()
        if not stripped.startswith("import "):
            continue
        module = extract_module(stripped)
        if module is None:
            continue
        if module not in seen:
            seen[module] = raw
            order.append(module)
    return [seen[m] for m in order]


def extract_module(import_line):
    match = re.match(r"import\s+(\S+)\s*(?:as\s+(\w+))?", import_line)
    if not match:
        return None
    return match.group(1)


def dedupe_imports(text):
    lines = text.splitlines()
    merged = merge_imports(lines)
    return "\n".join(merged)


if __name__ == "__main__":
    sample = """
import os
import sys
import json
import os
import re
"""
    print(dedupe_imports(sample))
