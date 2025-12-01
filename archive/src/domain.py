# src/domain.py
"""
Defines the shape of Patient data used throughout the system.
Includes enums for AgeGroup and Complaint, and dataclasses for Vitals and Patient.
Patient and Vitals are “dumb” containers—no policy logic here.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

class AgeGroup(Enum):
    PEDIATRIC = auto()
    ADULT = auto()

class Complaint(Enum):
    UNKNOWN = auto()
    CHEST_PAIN = auto()
    STROKE = auto()
    TRAUMA = auto()
    DIFFICULTY_BREATHING = auto()

@dataclass
class Vitals:
    # Could've been written as:
    # hr: int | None = None
    hr: Optional[int] = None
    rr: Optional[int] = None
    sbp: Optional[int] = None  # systolic BP
    spo2: Optional[int] = None
    gcs: Optional[int] = None

@dataclass
class Patient:
    age_group: AgeGroup = AgeGroup.ADULT
    complaint: Complaint = Complaint.UNKNOWN
    vitals: Vitals = field(default_factory=Vitals)
    is_unresponsive: bool = False
    has_chest_pain: bool = False
    has_focal_neuro_deficit: bool = False
