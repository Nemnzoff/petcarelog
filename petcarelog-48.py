# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: PetCareLog
def test_create_entry():
    entry = Entry("2024-05-01", "feeding", "Kibble", 0.25)
    assert entry.date == "2024-05-01"
    assert entry.type == "feeding"
    assert entry.item == "Kibble"
    assert entry.amount == 0.25


def test_valid_date():
    assert is_valid_date("2024-05-01")
    assert is_valid_date("2024-12-31")


def test_invalid_date():
    assert not is_valid_date("2024-13-01")
    assert not is_valid_date("05-01-2024")
    assert not is_valid_date("not-a-date")


def test_valid_types():
    for t in ["feeding", "vet", "medication", "weight"]:
        assert is_valid_type(t)


def test_invalid_types():
    for t in ["", "play", "vaccination", "exercise"]:
        assert not is_valid_type(t)


def test_valid_weight():
    assert is_valid_weight(10.5)
    assert is_valid_weight(0.1)


def test_invalid_weight():
    assert not is_valid_weight(-1)
    assert not is_valid_weight("ten")
    assert not is_valid_weight(None)


def test_amount_non_negative():
    assert is_valid_amount(0.25)
    assert is_valid_amount(0)


def test_invalid_amount():
    assert not is_valid_amount(-0.5)
    assert not is_valid_amount("half")
