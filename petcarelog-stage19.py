# === Stage 19: Add undo support for the last simple mutation ===
# Project: PetCareLog
import json

def undo_last_edit(log_file: str) -> bool:
    """Undo the last edit to the PetCareLog JSON file.
    
    Returns True if an undo was performed, False if the file is empty or
    already at its original state.
    """
    if not os.path.exists(log_file):
        return False
    
    try:
        with open(log_file, 'r') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        return False
    
    # Check if there's a history of edits to undo
    if 'edit_history' not in data or not data['edit_history']:
        return False
    
    # Get the last edit
    last_edit = data['edit_history'][-1]
    data['edit_history'].pop()
    
    # Revert the data based on the last edit
    edit_type = last_edit['type']
    edit_data = last_edit['data']
    
    if edit_type == 'add_entry':
        # Remove the entry that was added
        pet_name = edit_data.get('pet_name')
        if pet_name:
            del data['pets'][pet_name]
    elif edit_type == 'update_entry':
        # Restore the entry to its previous state
        pet_name = edit_data.get('pet_name')
        if pet_name and pet_name in data['pets']:
            data['pets'][pet_name] = edit_data['previous_state']
    elif edit_type == 'delete_entry':
        # Restore the deleted entry
        pet_name = edit_data.get('pet_name')
        if pet_name:
            data['pets'][pet_name] = edit_data['deleted_state']
    elif edit_type == 'add_medication':
        # Remove the medication record
        pet_name = edit_data.get('pet_name')
        med_name = edit_data.get('medication_name')
        if pet_name and med_name:
            if med_name in data['pets'][pet_name].get('medications', {}):
                del data['pets'][pet_name]['medications'][med_name]
    elif edit_type == 'update_medication':
        # Restore the medication to its previous state
        pet_name = edit_data.get('pet_name')
        med_name = edit_data.get('medication_name')
        if pet_name and med_name:
            if med_name in data['pets'][pet_name].get('medications', {}):
                data['pets'][pet_name]['medications'][med_name] = edit_data['previous_state']
    elif edit_type == 'add_feeding_schedule':
        # Remove the feeding schedule entry
        pet_name = edit_data.get('pet_name')
        feed_time = edit_data.get('feed_time')
        if pet_name and feed_time:
            if feed_time in data['pets'][pet_name].get('feeding_schedule', {}):
                del data['pets'][pet_name]['feeding_schedule'][feed_time]
    elif edit_type == 'add_weight_record':
        # Remove the weight record
        pet_name = edit_data.get('pet_name')
        weight_date = edit_data.get('weight_date')
        if pet_name and weight_date:
            if weight_date in data['pets'][pet_name].get('weight_records', {}):
                del data['pets'][pet_name]['weight_records'][weight_date]
    elif edit_type == 'add_vet_visit':
        # Remove the vet visit record
        pet_name = edit_data.get('pet_name')
        vet_date = edit_data.get('vet_date')
        if pet_name and vet_date:
            if vet_date in data['pets'][pet_name].get('vet_visits', {}):
                del data['pets'][pet_name]['vet_visits'][vet_date]
    
    # Save the reverted data
    try:
        with open(log_file, 'w') as f:
            json.dump(data, f, indent=2)
        print("Last edit undone successfully.")
        return True
    except IOError as e:
        print(f"Error saving reverted data: {e}")
        return False
