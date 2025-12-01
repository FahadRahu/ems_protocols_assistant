"""
Clinical and Administrative Procedure models.
Source: protocol_context.md, "Procedures" section
"""
from pydantic import BaseModel, Field


class Procedure(BaseModel):
    """
    Clinical or Administrative Procedure.
    Maps to PWC PCM procedure format.
    """
    id: str
    title: str
    procedure_type: str  # administrative, clinical_airway, clinical_cardiac, clinical_other
    authorized_personnel: list[str]  # ["ALS", "BLS"]
    indications: list[str] = Field(default_factory=list)
    contraindications: list[str] = Field(default_factory=list)
    equipment: list[str] = Field(default_factory=list)
    steps: list[str] = Field(default_factory=list)
