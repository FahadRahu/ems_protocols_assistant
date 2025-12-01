"""
Tests for Pydantic domain models.
"""
import pytest

from app.models import (
    Criteria,
    JurisdictionMeta,
    MedicalControl,
    MedicalControlContact,
    MedicationDose,
    PatientType,
    Protocol,
    ProtocolBundle,
    ProviderLevel,
    Route,
    Step,
)


class TestMedicalControl:
    """Tests for Medical Control models."""
    
    def test_medical_control_contact_creation(self):
        """Test creating a Medical Control contact."""
        contact = MedicalControlContact(
            facility="Test Hospital",
            phone="555-123-4567",
            radio_channel="59 Alpha",
        )
        assert contact.facility == "Test Hospital"
        assert contact.phone == "555-123-4567"
        assert contact.radio_channel == "59 Alpha"
    
    def test_medical_control_with_defaults(self):
        """Test Medical Control with default values."""
        control = MedicalControl(
            contacts=[
                MedicalControlContact(facility="Test", phone="555-0000")
            ]
        )
        assert control.poison_control == "1-800-222-1222"
        assert control.chemtrec == "1-800-424-9300"


class TestProtocol:
    """Tests for Protocol models."""
    
    def test_protocol_creation(self):
        """Test creating a basic protocol."""
        protocol = Protocol(
            id="test_protocol",
            title="Test Protocol",
            category="medical",
            patient_type=PatientType.ADULT,
            steps=[
                Step(
                    order=1,
                    provider_level=ProviderLevel.ALL,
                    action="Test action",
                )
            ],
        )
        assert protocol.id == "test_protocol"
        assert len(protocol.steps) == 1
    
    def test_step_with_medication(self):
        """Test creating a step with medication dosing."""
        step = Step(
            order=1,
            provider_level=ProviderLevel.ALS,
            action="Administer medication",
            medication=MedicationDose(
                medication_id="aspirin",
                dose="324 mg",
                route=Route.PO,
            ),
        )
        assert step.medication is not None
        assert step.medication.dose == "324 mg"


class TestProtocolBundle:
    """Tests for the complete protocol bundle."""
    
    def test_bundle_serialization(self):
        """Test that a bundle can be serialized to JSON."""
        bundle = ProtocolBundle(
            meta=JurisdictionMeta(
                jurisdiction="Test County",
                version="1.0",
                effective_date="2024-01-01",
                medical_control=MedicalControl(
                    contacts=[
                        MedicalControlContact(facility="Test", phone="555-0000")
                    ]
                ),
            ),
            protocols=[],
            medications=[],
            procedures=[],
        )
        
        # Should not raise
        json_data = bundle.model_dump_json()
        assert "Test County" in json_data
