"""
Complete Protocol Bundle - the compiled JSON output.
This is what the frontend downloads for offline use.
"""
from pydantic import BaseModel

from .jurisdiction import JurisdictionMeta
from .medication import Medication
from .procedure import Procedure
from .protocol import Protocol


class ProtocolBundle(BaseModel):
    """
    The complete offline bundle served to the frontend.
    Contains all data needed for clinical decision support.
    """
    meta: JurisdictionMeta
    protocols: list[Protocol]
    medications: list[Medication]
    procedures: list[Procedure]
