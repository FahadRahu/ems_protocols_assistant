"""
Protocol Ingestion Script
Parses protocol_context.md and generates structured Protocol objects.

Usage: python -m scripts.ingest_protocols --input ../data/raw/protocol_context.md
"""
import argparse
from pathlib import Path

from app.models.bundle import ProtocolBundle
from app.models.jurisdiction import (
    JurisdictionMeta,
    MedicalControl,
    MedicalControlContact,
)
from app.models.protocol import (
    Criteria,
    MedicationDose,
    PatientType,
    Protocol,
    ProviderLevel,
    Route,
    Step,
)
from app.services.compiler import BundleCompiler

# =============================================================================
# PWC Medical Control Contacts (from protocol_context.md, page XI)
# These are DYNAMIC and loaded from the bundle, never hardcoded in app logic
# =============================================================================
PWC_MEDICAL_CONTROL = MedicalControl(
    contacts=[
        MedicalControlContact(
            facility="Novant/UVA Haymarket Medical Center",
            phone="571-261-3413",
            radio_channel="59 Charlie",
        ),
        MedicalControlContact(
            facility="Novant/UVA Prince William Medical Center",
            phone="703-396-5260",
            radio_channel="59 Bravo",
        ),
        MedicalControlContact(
            facility="Sentara Northern Virginia Medical Center",
            phone="703-670-0129",
            radio_channel="59 Alpha",
        ),
        MedicalControlContact(
            facility="INOVA Fairfax Hospital",
            phone="703-876-0522",
            radio_channel="59 Delta",
        ),
        MedicalControlContact(
            facility="INOVA Fair Oaks Hospital",
            phone="703-391-0767",
            radio_channel="49 Delta",
        ),
        MedicalControlContact(
            facility="Fauquier Hospital",
            phone="540-316-4911",
            radio_channel="59 Lima",
        ),
        MedicalControlContact(
            facility="Mary Washington Hospital",
            phone="540-373-0348",
            radio_channel="59 November",
        ),
        MedicalControlContact(
            facility="Stafford Hospital",
            phone="540-741-9102",
            radio_channel="59 Mike",
        ),
    ],
    poison_control="1-800-222-1222",
    chemtrec="1-800-424-9300",
)


def create_pwc_meta() -> JurisdictionMeta:
    """Create PWC jurisdiction metadata."""
    return JurisdictionMeta(
        jurisdiction="Prince William County",
        version="2019.1",
        effective_date="2017-01-01",
        revision_date="2019-07-06",
        medical_control=PWC_MEDICAL_CONTROL,
    )


def parse_acute_coronary_syndrome() -> Protocol:
    """
    Gold Standard Test Case: Acute Coronary Syndrome (ACS)
    Source: protocol_context.md, pages 22-23
    """
    return Protocol(
        id="cardiac_acs_adult",
        title="Cardiac Emergencies: Acute Coronary Syndrome",
        category="cardiac_emergency",
        patient_type=PatientType.ADULT,
        tags=["chest pain", "stemi", "heart attack", "mi", "cardiac", "acs"],
        criteria=Criteria(
            age_min_months=216,  # 18 years
            symptoms=["chest_pain", "dyspnea", "diaphoresis", "nausea"],
        ),
        steps=[
            # All Providers Section
            Step(
                order=1,
                provider_level=ProviderLevel.ALL,
                action="General Patient Care Protocol – Adult",
                cross_reference="general_pcp_adult",
            ),
            Step(
                order=2,
                provider_level=ProviderLevel.ALL,
                action="If not already done, perform 12-lead ECG",
                notes=["Transmit to PCI facility if STEMI criteria present"],
            ),
            Step(
                order=3,
                provider_level=ProviderLevel.ALL,
                action="Administer Aspirin 324 mg PO",
                medication=MedicationDose(
                    medication_id="aspirin",
                    dose="324 mg",
                    route=Route.PO,
                ),
                contraindications=["Known allergy", "Active GI bleeding"],
            ),
            Step(
                order=4,
                provider_level=ProviderLevel.ALL,
                action="Administer Nitroglycerin 0.4 mg SL",
                medication=MedicationDose(
                    medication_id="nitroglycerin",
                    dose="0.4 mg",
                    route=Route.SL,
                ),
                condition="SBP >= 100 mmHg or MAP >= 65",
                contraindications=[
                    "SBP < 100 mmHg or MAP < 65",
                    "Phosphodiesterase-5 inhibitor use within 48 hours",
                    "Right ventricular or inferior wall MI suspected",
                ],
                repeat="Every 5 minutes, max 3 doses (1.2 mg total)",
            ),
            # ALS Section
            Step(
                order=5,
                provider_level=ProviderLevel.ALS,
                action="Full ALS Assessment and Treatment",
            ),
            Step(
                order=6,
                provider_level=ProviderLevel.ALS,
                action="Establish IV access NS KVO or saline lock",
            ),
            Step(
                order=7,
                provider_level=ProviderLevel.ALS,
                action="Continuous cardiac monitoring with SpO2 and ETCO2",
            ),
            Step(
                order=8,
                provider_level=ProviderLevel.ALS,
                action="If STEMI criteria present, transmit ECG and transport to PCI facility",
                cross_reference="procedure_code_stemi",
            ),
            Step(
                order=9,
                provider_level=ProviderLevel.ALS,
                action="Consider Morphine Sulfate for persistent chest pain",
                medication=MedicationDose(
                    medication_id="morphine",
                    dose="2-4 mg",
                    route=Route.IV,
                    max_dose="10 mg",
                ),
                condition="Pain persists after nitroglycerin",
                contraindications=[
                    "SBP < 90 mmHg or MAP < 65",
                    "Right ventricular or posterior wall MI",
                ],
                repeat="Every 5 minutes PRN",
            ),
            Step(
                order=10,
                provider_level=ProviderLevel.ALS,
                action="For runs of Ventricular Tachycardia (>= 6 consecutive beats)",
                cross_reference="cardiac_wide_complex_tach",
            ),
            # Medical Control Section
            Step(
                order=11,
                provider_level=ProviderLevel.OLMC,
                action="Contact OLMC for any additional orders or questions",
            ),
        ],
        cross_references=[
            "general_pcp_adult",
            "procedure_12lead_ecg",
            "procedure_code_stemi",
            "cardiac_wide_complex_tach",
        ],
    )


def main():
    """Main entry point for protocol ingestion."""
    parser = argparse.ArgumentParser(description="Ingest protocols from source document")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("../data/raw/protocol_context.md"),
        help="Path to the protocol source document",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("../data/compiled"),
        help="Output directory for compiled bundles",
    )
    args = parser.parse_args()
    
    print(f"📖 Reading protocols from: {args.input}")
    print(f"📦 Output directory: {args.output}")
    
    # Create the bundle with Gold Standard test case
    meta = create_pwc_meta()
    acs_protocol = parse_acute_coronary_syndrome()
    
    bundle = ProtocolBundle(
        meta=meta,
        protocols=[acs_protocol],
        medications=[],  # TODO: Parse medications
        procedures=[],   # TODO: Parse procedures
    )
    
    # Compile the bundle
    compiler = BundleCompiler(args.output)
    output_path = compiler.compile(bundle)
    
    print(f"✅ Bundle compiled: {output_path}")
    print(f"   - Protocols: {len(bundle.protocols)}")
    print(f"   - Medications: {len(bundle.medications)}")
    print(f"   - Procedures: {len(bundle.procedures)}")
    print(f"   - Medical Control Contacts: {len(bundle.meta.medical_control.contacts)}")


if __name__ == "__main__":
    main()
