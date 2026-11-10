# === Stage 46: Add a schema version field and migration helper ===
# Project: PetCareLog
SCHEMA_VERSION = 1


def migrate_logs(logs, target_version):
    migrated = []
    for log in logs:
        if log.get("schema_version", 0) < target_version:
            if "schema_version" not in log:
                log["schema_version"] = 0
            if target_version == 1:
                if "weight" not in log:
                    log["weight"] = None
                log["schema_version"] = 1
        migrated.append(log)
    return migrated


def bump_schema_version(logs, new_version):
    return [dict(log, schema_version=new_version) for log in logs]


def current_schema_version():
    return SCHEMA_VERSION
