"""
Jurisdiction and Medical Control configuration.
These values are DYNAMIC - loaded from the JSON bundle, never hardcoded.
Source: protocol_context.md, "Preliminary Information: Medical Control Contact"
"""
from pydantic import BaseModel


class MedicalControlContact(BaseModel):
    """Individual OLMC facility contact."""
    facility: str
    phone: str
    radio_channel: str | None = None


class MedicalControl(BaseModel):
    """
    Dynamic Medical Control configuration.
    Per PWC PCM: Contact OLMC for any additional orders.
    """
    contacts: list[MedicalControlContact]
    poison_control: str = "1-800-222-1222"  # RPCC per PWC protocol
    chemtrec: str = "1-800-424-9300"


class JurisdictionMeta(BaseModel):
    """Bundle metadata - identifies protocol set and version."""
    jurisdiction: str
    version: str
    effective_date: str
    revision_date: str | None = None
    medical_control: MedicalControl
