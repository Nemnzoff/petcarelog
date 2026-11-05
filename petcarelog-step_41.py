# === Stage 41: Add plain text import for a simple line-based format ===
# Project: PetCareLog
def parse_line_log(text):
    records = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t')
        if len(parts) < 2:
            continue
        key = parts[0].strip()
        value = '\t'.join(parts[1:]).strip()
        records.append((key, value))
    return records


def load_line_log(path):
    with open(path, 'r', encoding='utf-8') as f:
        return parse_line_log(f.read())


def save_line_log(records, path):
    with open(path, 'w', encoding='utf-8') as f:
        for key, value in records:
            f.write('{}\t{}\n'.format(key, value))
