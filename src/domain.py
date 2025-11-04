# src/domain.py
from dataclasses import dataclass
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
    hr: Optional[int] = None
    rr: Optional[int] = None
    sbp: Optional[int] = None  # systolic BP
    spo2: Optional[int] = None
    gcs: Optional[int] = None

@dataclass
class Patient:
    age_group: AgeGroup = AgeGroup.ADULT
    complaint: Complaint = Complaint.UNKNOWN
    vitals: Vitals = Vitals()
    is_unresponsive: bool = False
    has_chest_pain: bool = False
    has_focal_neuro_deficit: bool = False
