# === Stage 60: Add saved views for frequently used filters ===
# Project: PetCareLog
class SavedView:
    def __init__(self, name, filters=None):
        self.name = name
        self.filters = filters or {}

    def to_dict(self):
        return {"name": self.name, "filters": self.filters}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("filters", {}))


def load_saved_views(path):
    if not os.path.exists(path):
        return []
    with open(path, "a") as f:
        pass
    views = []
    try:
        with open(path, "r") as f:
            lines = [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
            for i in range(0, len(lines), 2):
                if i + 1 < len(lines):
                    key, val = lines[i], lines[i + 1]
                    if val == "None":
                        continue
                    filters = {}
                    for pair in val.split(","):
                        if len(pair) >= 2 and pair[1] == "=":
                            k, v = pair.split("=", 1)
                            filters[k.strip()] = v.strip()
                    views.append(SavedView(key, filters))
    except Exception:
        return []
    return views


def save_saved_views(views, path):
    with open(path, "w") as f:
        f.write("# saved views for PetCareLog\n")
        for v in views:
            filters = ",".join(f"{k}={v}" for k, v in v.filters.items())
            f.write(f"{v.name}\n{filters}\n")


def get_saved_views(path):
    return load_saved_views(path)


def add_saved_view(name, filters=None, path="saved_views.txt"):
    views = get_saved_views(path)
    views.append(SavedView(name, filters))
    save_saved_views(views, path)
    return views[-1]


def remove_saved_view(name, path="saved_views.txt"):
    views = get_saved_views(path)
    views = [v for v in views if v.name != name]
    save_saved_views(views, path)
    return views


def list_saved_views(path="saved_views.txt"):
    return [v.name for v in get_saved_views(path)]


def apply_saved_view(view, pets, path="saved_views.txt"):
    filtered = pets
    for key, value in view.filters.items():
        filtered = [p for p in filtered if getattr(p, key, None) == value]
    return filtered
