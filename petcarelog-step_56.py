# === Stage 56: Add compact error classes for domain failures ===
# Project: PetCareLog
class PetCareError(Exception):
    pass


class PetNotFoundError(PetCareError):
    pass


class UnknownPetError(PetCareError):
    pass


class InvalidPetTypeError(PetCareError):
    pass


class UnknownMedicationError(PetCareError):
    pass


class DuplicateEntryError(PetCareError):
    pass


class InvalidDateError(PetCareError):
    pass


class InvalidWeightError(PetCareError):
    pass


class InvalidFeedingError(PetCareError):
    pass
