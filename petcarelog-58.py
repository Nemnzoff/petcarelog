# === Stage 58: Add bulk update behavior for selected records ===
# Project: PetCareLog
def bulk_update_records(records, updates):
    """Apply a single uniform update to every record in the list.

    Each record is a dict. The updates mapping contains keys whose values
    are either a plain value (applied to every record) or a callable
    receiving the record and returning the new value for that field.
    Returns the number of records updated.
    """
    count = 0
    for record in records:
        for key, value in updates.items():
            if callable(value):
                record[key] = value(record)
            else:
                record[key] = value
        count += 1
    return count


def bulk_update_field(records, field, new_value):
    """Set a single field to a constant value across all records.

    Returns the number of records updated.
    """
    return bulk_update_records(records, {field: new_value})


def bulk_set_weight(records, weight_by_id):
    """Set the weight of each record using a mapping of id to weight.

    Only records whose id appears in weight_by_id are updated. Returns the
    number of records updated.
    """
    updated = 0
    for record in records:
        record_id = record.get("id")
        if record_id in weight_by_id:
            record["weight_kg"] = weight_by_id[record_id]
            updated += 1
    return updated


def bulk_add_to_schedule(records, schedule_info):
    """Append a new scheduled entry to every record in the list.

    schedule_info is a dict with keys: day, time, meal_type, amount_g.
    Returns the number of records updated.
    """
    count = 0
    for record in records:
        record["schedule"].append({
            "day": schedule_info["day"],
            "time": schedule_info["time"],
            "meal_type": schedule_info["meal_type"],
            "amount_g": schedule_info["amount_g"],
        })
        count += 1
    return count
