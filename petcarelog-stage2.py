# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: PetCareLog
from dataclasses import dataclass
from datetime import date

@dataclass
class Pet:
    name: str
    species: str
    breed: str
    dob: date
    owner: str

@dataclass
class FeedingRecord:
    pet: Pet
    date: date
    food_type: str
    amount_grams: float
    notes: str = ""

@dataclass
class VetVisit:
    pet: Pet
    date: date
    symptoms: str
    diagnosis: str
    cost: float
    next_visit: date | None = None

@dataclass
class Medication:
    pet: Pet
    start_date: date
    end_date: date | None
    drug_name: str
    dosage: str
    frequency: str
    notes: str = ""

@dataclass
class WeightRecord:
    pet: Pet
    date: date
    weight_grams: float
    notes: str = ""
