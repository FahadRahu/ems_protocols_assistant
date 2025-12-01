"""
Medication reference models.
Source: protocol_context.md, "Pharmacology" section (pages 242-290)
"""
from pydantic import BaseModel, Field


class DosingInfo(BaseModel):
    """Dosing information for a specific indication."""
    indication: str
    dose: str
    route: str
    max_dose: str | None = None
    notes: str | None = None


class Medication(BaseModel):
    """
    Complete medication reference.
    Includes pharmacology info from PWC PCM Pharmacology section.
    """
    id: str
    generic_name: str
    trade_names: list[str] = Field(default_factory=list)
    drug_class: str
    mechanism: str | None = None
    indications: list[str] = Field(default_factory=list)
    contraindications: list[str] = Field(default_factory=list)
    adult_dosing: list[DosingInfo] = Field(default_factory=list)
    pediatric_dosing: list[DosingInfo] = Field(default_factory=list)
