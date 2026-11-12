# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: PetCareLog
def test_update_missing_record_returns_false():
    pet = Pet(name="Rex", species="dog", weight=20.0)
    log = PetCareLog()
    log.add_pet(pet)
    result = log.update_pet_weight(999, 21.0)
    assert result is False
    assert pet.weight == 20.0


def test_update_nonnumeric_weight_is_rejected():
    pet = Pet(name="Rex", species="dog", weight=20.0)
    log = PetCareLog()
    log.add_pet(pet)
    result = log.update_pet_weight(0, "heavy")
    assert result is False
    assert pet.weight == 20.0


def test_delete_existing_record_returns_true():
    pet = Pet(name="Rex", species="dog", weight=20.0)
    log = PetCareLog()
    log.add_pet(pet)
    assert log.delete_pet(0) is True
    assert len(log.pets) == 0


def test_delete_missing_record_returns_false():
    log = PetCareLog()
    assert log.delete_pet(0) is False


def test_delete_out_of_range_index_returns_false():
    pet = Pet(name="Rex", species="dog", weight=20.0)
    log = PetCareLog()
    log.add_pet(pet)
    assert log.delete_pet(5) is False


def test_update_after_delete_uses_new_index():
    pet1 = Pet(name="Rex", species="dog", weight=20.0)
    pet2 = Pet(name="Bella", species="cat", weight=4.0)
    log = PetCareLog()
    log.add_pet(pet1)
    log.add_pet(pet2)
    log.delete_pet(0)
    assert log.update_pet_weight(0, 4.5) is True
    assert pet2.weight == 4.5
