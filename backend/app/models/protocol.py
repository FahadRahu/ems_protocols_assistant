"""
Protocol domain models.
Mirrors the JSON Schema in shared/schemas/protocol-schema.json.
"""
from enum import Enum

from pydantic import BaseModel, Field


class ProviderLevel(str, Enum):
    """EMS Provider certification levels."""
    ALL = "ALL"           # BLS + ALS
    BLS = "BLS"           # Basic Life Support
    ALS = "ALS"           # Advanced Life Support (includes BLS scope)
    PARAMEDIC = "PARAMEDIC"  # Paramedic-only interventions
    OLMC = "OLMC"         # Requires Medical Control order


class PatientType(str, Enum):
    """Patient age categories per PWC PCM definitions."""
    ADULT = "adult"       # >= 18 years per PWC definition
    PEDIATRIC = "pediatric"  # < 18 years
    NEONATE = "neonate"   # Birth to 1 month
    ALL = "all"


class Route(str, Enum):
    """Medication administration routes."""
    PO = "PO"      # Per Os (oral)
    SL = "SL"      # Sublingual
    IV = "IV"      # Intravenous
    IO = "IO"      # Intraosseous
    IM = "IM"      # Intramuscular
    IN = "IN"      # Intranasal
    NEB = "NEB"    # Nebulized
    ODT = "ODT"    # Oral Dissolving Tablet
    TOPICAL = "TOPICAL"


class VitalSignCriteria(BaseModel):
    """Vital sign thresholds for protocol matching."""
    sbp_below: int | None = None
    sbp_above: int | None = None
    map_below: int | None = None
    hr_below: int | None = None
    hr_above: int | None = None
    spo2_below: int | None = None
    gcs_below: int | None = None
    etco2_below: int | None = None
    etco2_above: int | None = None


class Criteria(BaseModel):
    """Inclusion/exclusion criteria for protocol matching."""
    age_min_months: int | None = None
    age_max_months: int | None = None
    symptoms: list[str] = Field(default_factory=list)
    vital_signs: VitalSignCriteria | None = None
    exclusions: list[str] = Field(default_factory=list)


class MedicationDose(BaseModel):
    """Specific medication dosing within a step."""
    medication_id: str
    dose: str
    dose_per_kg: float | None = None
    max_dose: str | None = None
    route: Route
    rate: str | None = None


class Step(BaseModel):
    """Individual treatment step within a protocol."""
    order: int
    provider_level: ProviderLevel
    action: str
    medication: MedicationDose | None = None
    condition: str | None = None  # e.g., "SBP > 100"
    contraindications: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    repeat: str | None = None  # e.g., "Every 5 minutes x3"
    cross_reference: str | None = None  # Protocol/Procedure ID


class Protocol(BaseModel):
    """
    Complete EMS Protocol definition.
    Maps to PWC PCM structure: All Providers -> ALS -> Paramedic -> Medical Control
    """
    id: str
    title: str
    category: str
    patient_type: PatientType
    tags: list[str] = Field(default_factory=list)
    criteria: Criteria | None = None
    steps: list[Step]
    cross_references: list[str] = Field(default_factory=list)
