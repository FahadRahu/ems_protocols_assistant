FahadRahu: @workspace 

Workspace: Enable Claude Sonnet 4.5 for all clients
[object Object]

FahadRahu: @workspace Enable: "Enable Claude Sonnet 4.5 for all clients"

Workspace: Enable Claude Opus 4.5 (Preview) for all clients
[object Object]

FahadRahu: @workspace Enable: "Enable Claude Opus 4.5 (Preview) for all clients"

Workspace: Collecting workspace informationLooking at your workspace, I can see you're building an EMS Protocol Assistant application for Prince William County. Let me provide an overview of how your project is structured:

## Project Overview

This is a Python-based clinical decision support tool that guides EMS personnel through emergency protocols and procedures.

### Core Architecture

**Entry Point:** main.py - Collects patient demographics and runs through the General Patient Care Protocol

**Domain Model:** domain.py - Defines `Patient`, `Vitals`, `AgeGroup`, and `Complaint` dataclasses/enums

**Rules Engine:** engine.py - Evaluates patient data against protocol rules using the `evaluate_rules` function

### Key Directories

| Directory | Purpose |
|-----------|---------|
| protocols | Medical protocol definitions (allergic reaction, diabetic emergencies, sepsis, etc.) |
| procedures | Clinical procedures (blood glucose analysis, airway management, cardiac procedures) |
| data | YAML-based protocol rules in protocols.yaml |
| src | Core domain models and rule engine |

### Import System

You've built a layered import system documented in imports.py:

1. **procedures/** → individual procedure functions
2. **imports.py** → consolidates procedure modules with aliases (`ocp`, `ccp`, `acp`)
3. **protocols/** → imports procedures, defines protocols
4. **imports.py** → consolidates protocols for main.py

### Current State

Based on purpose.md, you're transitioning from a function-based to a **class-based approach**. The `Patient` class in main.py and the dataclasses in domain.py reflect this direction.

Is there a specific area you'd like help with—refactoring, adding new protocols, or completing the class-based transition?

FahadRahu: @workspace /plan #file:outline.md #file:protocol_context.md

You are VitalPath-Architect, an expert Senior Principal Engineer and EMS Subject Matter Expert. I have hired you to architect and build "VitalPath," an offline-first Clinical Decision Support System (CDSS) for Prince William County (PWC) Fire & Rescue.

**YOUR GOAL:**
We are starting Phase 1. Your specific task right now is to analyze my context files and generate a comprehensive development master plan file named `vitalpath_plan.md`.

**CONTEXT FILES:**
1. `outline.md`: This is the Master Design Document I have agreed to. It defines the "Smart Client" architecture (Python Backend for CMS, React PWA for offline logic), the stack (FastAPI, React, Pydantic, Tailwind), and the JSON schema strategy.
2. `protocol_context.md`: This is the raw text of the PWC Patient Care Manual. This is the source of truth for all medical logic.

**CRITICAL ARCHITECTURAL CONSTRAINTS (DO NOT DEVIATE):**
* **Offline-First:** The React frontend must download a JSON bundle and run the protocol matching logic LOCALLY. The backend is ONLY for managing/generating this JSON.
* **Modularity:** Use a "Modular Monolith" structure.
* **Type Safety:** We use Pydantic (Python) and Interfaces (TypeScript) for a unified data schema.
* **Medical Control:** Medical Control contact info must be dynamic (loaded from JSON), not hardcoded.

**INSTRUCTIONS FOR "vitalpath_plan.md":**
Create a markdown file that breaks this project into granular, check-boxable steps. It must include:

## 1. Project Initialization & Standards
- [ ] Define directory structure (monorepo style: /backend, /frontend, /shared-types).
- [ ] Setup Development Environment (Docker Compose, Pre-commit hooks for Ruff/Prettier).
- [ ] Define the "Protocol Schema" (The single source of truth JSON structure).

## 2. Phase 1: Data Engineering (The Foundation)
- [ ] Create Python script `ingest_protocols.py` to parse `protocol_context.md`.
- [ ] Implement the `Protocol` Pydantic model matching the schema in `outline.md`.
- [ ] Task to extract "Acute Coronary Syndrome" as the "Gold Standard" test case.
- [ ] Build the JSON compiler (exports Postgres DB -> `protocols.json`).

## 3. Phase 2: The "Smart Client" Frontend (Logic Engine)
- [ ] Initialize React + Vite + TypeScript PWA.
- [ ] Build the `OfflineLogicEngine` (TypeScript class that takes patient inputs and filters the JSON).
- [ ] Create the "Tactical Interface" (Dark mode, large buttons).
- [ ] Implement the "Admin/Station" view for protocol editing.

## 4. Phase 3: Validation & DevOps
- [ ] Write Unit Tests for the Logic Engine (Input: Chest Pain -> Output: Aspirin).
- [ ] Setup GitHub Actions for CI/CD (Lint -> Build -> Deploy).

**IMMEDIATE ACTION:**
Do not write code yet. Analyze the provided files and generate the `vitalpath_plan.md` file now. Ensure you explicitly reference how we will handle the "Medical Control" dynamic data and the "Admin Panel" requirement in the plan. I am okay with you deleting files and encourage you to do so, I am on another new git branch right now called alpha, so feel free to make changes as necessary

Workspace: Collecting workspace information# VitalPath Development Master Plan

**Version:** 1.0  
**Created:** Phase 1 Initialization  
**Architecture:** Offline-First Clinical Decision Support System  
**Jurisdiction:** Prince William County Fire & Rescue

---

## Executive Summary

This plan transforms the Prince William County Patient Care Manual (PCM) into a real-time, offline-capable clinical decision support tool. The system follows a "Smart Client" architecture where the backend serves as a Content Management System (CMS) for protocol data, while all clinical logic executes locally in the browser via a downloaded JSON bundle.

---

## 1. Project Initialization & Standards

### 1.1 Directory Structure (Monorepo)

- [ ] Create the following directory structure:

```
VitalPath/
├── backend/                    # FastAPI CMS & JSON Compiler
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI entrypoint
│   │   ├── config.py          # Settings (Pydantic BaseSettings)
│   │   ├── models/            # Pydantic domain models
│   │   │   ├── __init__.py
│   │   │   ├── protocol.py    # Protocol, Step, Criteria models
│   │   │   ├── medication.py  # Medication dosing models
│   │   │   └── jurisdiction.py # Medical Control, meta info
│   │   ├── services/          # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── compiler.py    # JSON bundle compiler
│   │   │   └── parser.py      # Protocol text parser
│   │   ├── api/               # Route handlers
│   │   │   ├── __init__.py
│   │   │   ├── protocols.py   # CRUD for protocols
│   │   │   └── bundles.py     # JSON bundle endpoints
│   │   └── db/                # Database layer
│   │       ├── __init__.py
│   │       └── repository.py
│   ├── scripts/
│   │   └── ingest_protocols.py # One-time ingestion script
│   ├── tests/
│   ├── pyproject.toml
│   └── Dockerfile
├── frontend/                   # React PWA (Tactical Interface)
│   ├── src/
│   │   ├── main.tsx
│   │   ├── App.tsx
│   │   ├── engine/            # Offline Logic Engine
│   │   │   ├── ProtocolMatcher.ts
│   │   │   ├── DoseCalculator.ts
│   │   │   └── index.ts
│   │   ├── components/
│   │   │   ├── tactical/      # Field-use components
│   │   │   └── admin/         # Station-use components
│   │   ├── hooks/
│   │   ├── stores/            # Zustand stores
│   │   ├── types/             # TypeScript interfaces
│   │   │   └── protocol.ts    # Mirrors backend models
│   │   └── services/
│   │       └── offlineStorage.ts
│   ├── public/
│   ├── index.html
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── package.json
├── shared/                     # Shared schema definitions
│   ├── schemas/
│   │   └── protocol-schema.json  # JSON Schema (source of truth)
│   └── README.md
├── data/                       # Raw data & compiled bundles
│   ├── raw/
│   │   └── protocol_context.md
│   ├── compiled/
│   │   └── pwc_protocols_v1.json
│   └── README.md
├── docker-compose.yml
├── .pre-commit-config.yaml
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

- [ ] Delete legacy files that conflict with new architecture:
  - protocols directory (replaced by `backend/app/models/`)
  - procedures directory (logic moves to compiled JSON)
  - domain.py (replaced by `backend/app/models/`)
  - engine.py (replaced by `frontend/src/engine/`)
  - main.py (replaced by main.py)
  - demograph_info.py (logic moves to frontend)
  - alternative_system (superseded by new architecture)

### 1.2 Development Environment Setup

- [ ] Create `docker-compose.yml`:
  ```yaml
  services:
    backend:
      build: ./backend
      ports: ["8000:8000"]
      volumes: ["./backend:/app", "./data:/data"]
      environment:
        - DATABASE_URL=postgresql://user:pass@db:5432/vitalpath
    db:
      image: postgres:15-alpine
      environment:
        - POSTGRES_DB=vitalpath
        - POSTGRES_USER=user
        - POSTGRES_PASSWORD=pass
      volumes: ["pgdata:/var/lib/postgresql/data"]
    frontend:
      build: ./frontend
      ports: ["3000:3000"]
      volumes: ["./frontend:/app"]
  volumes:
    pgdata:
  ```

- [ ] Create `.pre-commit-config.yaml`:
  ```yaml
  repos:
    - repo: https://github.com/astral-sh/ruff-pre-commit
      rev: v0.4.4
      hooks:
        - id: ruff
          args: [--fix]
        - id: ruff-format
    - repo: https://github.com/pre-commit/mirrors-prettier
      rev: v3.1.0
      hooks:
        - id: prettier
          types_or: [javascript, typescript, json, yaml, markdown]
  ```

- [ ] Create `backend/pyproject.toml` with dependencies:
  - FastAPI, Uvicorn, Pydantic v2, SQLAlchemy, Alembic
  - pytest, pytest-asyncio, httpx (testing)
  - ruff (linting)

- [ ] Create `frontend/package.json` with dependencies:
  - React 18, Vite, TypeScript
  - TanStack Query, Zustand
  - Tailwind CSS, @tailwindcss/forms
  - vite-plugin-pwa, workbox

### 1.3 Protocol Schema Definition (Single Source of Truth)

- [ ] Create `shared/schemas/protocol-schema.json`:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "vitalpath-protocol-bundle",
  "type": "object",
  "required": ["meta", "protocols", "medications", "procedures"],
  "properties": {
    "meta": {
      "type": "object",
      "required": ["jurisdiction", "version", "effective_date", "medical_control"],
      "properties": {
        "jurisdiction": { "type": "string" },
        "version": { "type": "string" },
        "effective_date": { "type": "string", "format": "date" },
        "revision_date": { "type": "string", "format": "date" },
        "medical_control": {
          "type": "object",
          "required": ["contacts"],
          "properties": {
            "contacts": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["facility", "phone"],
                "properties": {
                  "facility": { "type": "string" },
                  "phone": { "type": "string" },
                  "radio_channel": { "type": "string" }
                }
              }
            },
            "poison_control": { "type": "string" },
            "chemtrec": { "type": "string" }
          }
        }
      }
    },
    "protocols": {
      "type": "array",
      "items": { "$ref": "#/definitions/Protocol" }
    },
    "medications": {
      "type": "array",
      "items": { "$ref": "#/definitions/Medication" }
    },
    "procedures": {
      "type": "array",
      "items": { "$ref": "#/definitions/Procedure" }
    }
  },
  "definitions": {
    "Protocol": {
      "type": "object",
      "required": ["id", "title", "category", "patient_type", "steps"],
      "properties": {
        "id": { "type": "string" },
        "title": { "type": "string" },
        "category": { 
          "type": "string",
          "enum": ["respiratory", "cardiac_arrest", "cardiac_emergency", 
                   "environmental", "hazmat", "medical", "obgyn", 
                   "overdose_poisoning", "pain_management", "trauma"]
        },
        "patient_type": {
          "type": "string",
          "enum": ["adult", "pediatric", "neonate", "all"]
        },
        "tags": { "type": "array", "items": { "type": "string" } },
        "criteria": { "$ref": "#/definitions/Criteria" },
        "steps": { 
          "type": "array", 
          "items": { "$ref": "#/definitions/Step" }
        },
        "cross_references": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "Criteria": {
      "type": "object",
      "properties": {
        "age_min_months": { "type": "integer" },
        "age_max_months": { "type": "integer" },
        "symptoms": { "type": "array", "items": { "type": "string" } },
        "vital_signs": {
          "type": "object",
          "properties": {
            "sbp_below": { "type": "integer" },
            "sbp_above": { "type": "integer" },
            "hr_below": { "type": "integer" },
            "hr_above": { "type": "integer" },
            "spo2_below": { "type": "integer" },
            "gcs_below": { "type": "integer" }
          }
        },
        "exclusions": { "type": "array", "items": { "type": "string" } }
      }
    },
    "Step": {
      "type": "object",
      "required": ["order", "provider_level", "action"],
      "properties": {
        "order": { "type": "integer" },
        "provider_level": {
          "type": "string",
          "enum": ["ALL", "BLS", "ALS", "PARAMEDIC", "OLMC"]
        },
        "action": { "type": "string" },
        "medication": { "$ref": "#/definitions/MedicationDose" },
        "condition": { "type": "string" },
        "contraindications": { "type": "array", "items": { "type": "string" } },
        "notes": { "type": "array", "items": { "type": "string" } },
        "repeat": { "type": "string" },
        "cross_reference": { "type": "string" }
      }
    },
    "MedicationDose": {
      "type": "object",
      "required": ["medication_id", "dose", "route"],
      "properties": {
        "medication_id": { "type": "string" },
        "dose": { "type": "string" },
        "dose_per_kg": { "type": "number" },
        "max_dose": { "type": "string" },
        "route": {
          "type": "string",
          "enum": ["PO", "SL", "IV", "IO", "IM", "IN", "NEB", "ODT", "TOPICAL"]
        },
        "rate": { "type": "string" }
      }
    },
    "Medication": {
      "type": "object",
      "required": ["id", "generic_name", "class"],
      "properties": {
        "id": { "type": "string" },
        "generic_name": { "type": "string" },
        "trade_names": { "type": "array", "items": { "type": "string" } },
        "class": { "type": "string" },
        "mechanism": { "type": "string" },
        "indications": { "type": "array", "items": { "type": "string" } },
        "contraindications": { "type": "array", "items": { "type": "string" } },
        "adult_dosing": { "type": "array", "items": { "$ref": "#/definitions/DosingInfo" } },
        "pediatric_dosing": { "type": "array", "items": { "$ref": "#/definitions/DosingInfo" } }
      }
    },
    "DosingInfo": {
      "type": "object",
      "properties": {
        "indication": { "type": "string" },
        "dose": { "type": "string" },
        "route": { "type": "string" },
        "max_dose": { "type": "string" },
        "notes": { "type": "string" }
      }
    },
    "Procedure": {
      "type": "object",
      "required": ["id", "title", "authorized_personnel", "steps"],
      "properties": {
        "id": { "type": "string" },
        "title": { "type": "string" },
        "type": {
          "type": "string",
          "enum": ["administrative", "clinical_airway", "clinical_cardiac", "clinical_other"]
        },
        "authorized_personnel": { "type": "array", "items": { "type": "string" } },
        "indications": { "type": "array", "items": { "type": "string" } },
        "contraindications": { "type": "array", "items": { "type": "string" } },
        "equipment": { "type": "array", "items": { "type": "string" } },
        "steps": { "type": "array", "items": { "type": "string" } }
      }
    }
  }
}
```

---

## 2. Phase 1: Data Engineering (The Foundation)

### 2.1 Backend Pydantic Models

- [ ] Create `backend/app/models/jurisdiction.py`:

```python
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
```

- [ ] Create `backend/app/models/protocol.py`:

```python
"""
Protocol domain models.
Mirrors the JSON Schema in shared/schemas/protocol-schema.json.
"""
from enum import Enum
from pydantic import BaseModel, Field

class ProviderLevel(str, Enum):
    ALL = "ALL"           # BLS + ALS
    BLS = "BLS"           # Basic Life Support
    ALS = "ALS"           # Advanced Life Support (includes BLS scope)
    PARAMEDIC = "PARAMEDIC"  # Paramedic-only interventions
    OLMC = "OLMC"         # Requires Medical Control order

class PatientType(str, Enum):
    ADULT = "adult"       # >= 18 years per PWC definition
    PEDIATRIC = "pediatric"  # < 18 years
    NEONATE = "neonate"   # Birth to 1 month
    ALL = "all"

class Route(str, Enum):
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
```

- [ ] Create `backend/app/models/medication.py`:

```python
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
```

- [ ] Create `backend/app/models/procedure.py`:

```python
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
```

- [ ] Create `backend/app/models/bundle.py`:

```python
"""
Complete Protocol Bundle - the compiled JSON output.
This is what the frontend downloads for offline use.
"""
from pydantic import BaseModel
from .jurisdiction import JurisdictionMeta
from .protocol import Protocol
from .medication import Medication
from .procedure import Procedure

class ProtocolBundle(BaseModel):
    """
    The complete offline bundle served to the frontend.
    Contains all data needed for clinical decision support.
    """
    meta: JurisdictionMeta
    protocols: list[Protocol]
    medications: list[Medication]
    procedures: list[Procedure]
```

### 2.2 Protocol Ingestion Script

- [ ] Create `backend/scripts/ingest_protocols.py`:

```python
"""
Protocol Ingestion Script
Parses protocol_context.md and generates structured Protocol objects.

Usage: python -m scripts.ingest_protocols --input ../data/raw/protocol_context.md
"""
import re
from pathlib import Path
from app.models.protocol import Protocol, Step, Criteria, ProviderLevel, PatientType
from app.models.bundle import ProtocolBundle
from app.models.jurisdiction import JurisdictionMeta, MedicalControl, MedicalControlContact

# Medical Control contacts from protocol_context.md (page XI)
PWC_MEDICAL_CONTROL = MedicalControl(
    contacts=[
        MedicalControlContact(
            facility="Novant/UVA Haymarket Medical Center",
            phone="571-261-3413",
            radio_channel="59 Charlie"
        ),
        MedicalControlContact(
            facility="Novant/UVA Prince William Medical Center",
            phone="703-396-5260",
            radio_channel="59 Bravo"
        ),
        MedicalControlContact(
            facility="Sentara Northern Virginia Medical Center",
            phone="703-670-0129",
            radio_channel="59 Alpha"
        ),
        MedicalControlContact(
            facility="INOVA Fairfax Hospital",
            phone="703-876-0522",
            radio_channel="59 Delta"
        ),
        MedicalControlContact(
            facility="INOVA Fair Oaks Hospital",
            phone="703-391-0767",
            radio_channel="49 Delta"
        ),
        MedicalControlContact(
            facility="Fauquier Hospital",
            phone="540-316-4911",
            radio_channel="59 Lima"
        ),
        MedicalControlContact(
            facility="Mary Washington Hospital",
            phone="540-373-0348",
            radio_channel="59 November"
        ),
        MedicalControlContact(
            facility="Stafford Hospital",
            phone="540-741-9102",
            radio_channel="59 Mike"
        ),
    ],
    poison_control="1-800-222-1222",
    chemtrec="1-800-424-9300"
)

def create_pwc_meta() -> JurisdictionMeta:
    """Create PWC jurisdiction metadata."""
    return JurisdictionMeta(
        jurisdiction="Prince William County",
        version="2019.1",
        effective_date="2017-01-01",
        revision_date="2019-07-06",
        medical_control=PWC_MEDICAL_CONTROL
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
                cross_reference="general_pcp_adult"
            ),
            Step(
                order=2,
                provider_level=ProviderLevel.ALL,
                action="If not already done, perform 12-lead ECG",
                notes=["Transmit to PCI facility if STEMI criteria present"]
            ),
            Step(
                order=3,
                provider_level=ProviderLevel.ALL,
                action="Administer Aspirin 324 mg PO",
                medication=MedicationDose(
                    medication_id="aspirin",
                    dose="324 mg",
                    route=Route.PO
                ),
                contraindications=["Known allergy", "Active GI bleeding"]
            ),
            Step(
                order=4,
                provider_level=ProviderLevel.ALL,
                action="Administer Nitroglycerin 0.4 mg SL",
                medication=MedicationDose(
                    medication_id="nitroglycerin",
                    dose="0.4 mg",
                    route=Route.SL
                ),
                condition="SBP >= 100 mmHg or MAP >= 65",
                contraindications=[
                    "SBP < 100 mmHg or MAP < 65",
                    "Phosphodiesterase-5 inhibitor use within 48 hours",
                    "Right ventricular or inferior wall MI suspected"
                ],
                repeat="Every 5 minutes, max 3 doses (1.2 mg total)"
            ),
            # ALS Section
            Step(
                order=5,
                provider_level=ProviderLevel.ALS,
                action="Full ALS Assessment and Treatment"
            ),
            Step(
                order=6,
                provider_level=ProviderLevel.ALS,
                action="Establish IV access NS KVO or saline lock"
            ),
            Step(
                order=7,
                provider_level=ProviderLevel.ALS,
                action="Continuous cardiac monitoring with SpO2 and ETCO2"
            ),
            Step(
                order=8,
                provider_level=ProviderLevel.ALS,
                action="If STEMI criteria present, transmit ECG and transport to PCI facility",
                cross_reference="procedure_code_stemi"
            ),
            Step(
                order=9,
                provider_level=ProviderLevel.ALS,
                action="Consider Morphine Sulfate for persistent chest pain",
                medication=MedicationDose(
                    medication_id="morphine",
                    dose="2-4 mg",
                    route=Route.IV,
                    max_dose="10 mg"
                ),
                condition="Pain persists after nitroglycerin",
                contraindications=[
                    "SBP < 90 mmHg or MAP < 65",
                    "Right ventricular or posterior wall MI"
                ],
                repeat="Every 5 minutes PRN"
            ),
            Step(
                order=10,
                provider_level=ProviderLevel.ALS,
                action="For runs of Ventricular Tachycardia (>= 6 consecutive beats)",
                cross_reference="cardiac_wide_complex_tach"
            ),
            # Medical Control Section
            Step(
                order=11,
                provider_level=ProviderLevel.OLMC,
                action="Contact OLMC for any additional orders or questions"
            )
        ],
        cross_references=[
            "general_pcp_adult",
            "procedure_12lead_ecg", 
            "procedure_code_stemi",
            "cardiac_wide_complex_tach"
        ]
    )

# Additional protocol parsers to implement...
```

### 2.3 Gold Standard Test Case

- [ ] Create test for ACS protocol extraction:
  - Input: Raw text from protocol_context.md pages 22-23
  - Output: Valid `Protocol` object matching schema
  - Validate: All 11 steps present, correct provider levels, medication dosing accurate

- [ ] Verify Medical Control is dynamic:
  - Ensure no hardcoded phone numbers in protocol logic
  - Confirm `MedicalControl` object loaded from bundle metadata
  - Test that changing `meta.medical_control` updates UI display

### 2.4 JSON Bundle Compiler

- [ ] Create `backend/app/services/compiler.py`:

```python
"""
JSON Bundle Compiler
Exports database contents to a versioned JSON file for frontend consumption.
"""
import json
from datetime import datetime
from pathlib import Path
from app.models.bundle import ProtocolBundle

class BundleCompiler:
    """Compiles protocol data into offline-ready JSON bundle."""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
    
    def compile(self, bundle: ProtocolBundle) -> Path:
        """
        Compile and save the protocol bundle.
        Returns path to the generated JSON file.
        """
        version = bundle.meta.version.replace(".", "_")
        filename = f"pwc_protocols_v{version}.json"
        output_path = self.output_dir / filename
        
        with open(output_path, "w") as f:
            json.dump(bundle.model_dump(), f, indent=2)
        
        return output_path
    
    def compile_minified(self, bundle: ProtocolBundle) -> Path:
        """Compile minified version for production use."""
        version = bundle.meta.version.replace(".", "_")
        filename = f"pwc_protocols_v{version}.min.json"
        output_path = self.output_dir / filename
        
        with open(output_path, "w") as f:
            json.dump(bundle.model_dump(), f, separators=(',', ':'))
        
        return output_path
```

### 2.5 FastAPI Endpoints

- [ ] Create `backend/app/api/bundles.py`:

```python
"""
Bundle API endpoints.
Serves the compiled JSON bundle to the frontend PWA.
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter(prefix="/api/v1/bundles", tags=["bundles"])

BUNDLE_DIR = Path("/data/compiled")

@router.get("/latest")
async def get_latest_bundle():
    """
    Get the latest protocol bundle.
    Frontend calls this on startup to check for updates.
    """
    bundles = sorted(BUNDLE_DIR.glob("pwc_protocols_v*.json"), reverse=True)
    if not bundles:
        raise HTTPException(status_code=404, detail="No bundles available")
    
    return FileResponse(
        bundles[0],
        media_type="application/json",
        headers={"Cache-Control": "max-age=3600"}
    )

@router.get("/version")
async def get_bundle_version():
    """Get current bundle version without downloading full bundle."""
    bundles = sorted(BUNDLE_DIR.glob("pwc_protocols_v*.json"), reverse=True)
    if not bundles:
        raise HTTPException(status_code=404, detail="No bundles available")
    
    # Extract version from filename
    version = bundles[0].stem.replace("pwc_protocols_v", "").replace("_", ".")
    return {"version": version, "filename": bundles[0].name}
```

---

## 3. Phase 2: The "Smart Client" Frontend

### 3.1 TypeScript Interfaces (Mirror Backend Models)

- [ ] Create `frontend/src/types/protocol.ts`:

```typescript
/**
 * Protocol type definitions.
 * These MUST mirror backend/app/models/ exactly.
 * Source of truth: shared/schemas/protocol-schema.json
 */

export type ProviderLevel = 'ALL' | 'BLS' | 'ALS' | 'PARAMEDIC' | 'OLMC';
export type PatientType = 'adult' | 'pediatric' | 'neonate' | 'all';
export type Route = 'PO' | 'SL' | 'IV' | 'IO' | 'IM' | 'IN' | 'NEB' | 'ODT' | 'TOPICAL';

export interface MedicalControlContact {
  facility: string;
  phone: string;
  radio_channel?: string;
}

export interface MedicalControl {
  contacts: MedicalControlContact[];
  poison_control: string;
  chemtrec: string;
}

export interface JurisdictionMeta {
  jurisdiction: string;
  version: string;
  effective_date: string;
  revision_date?: string;
  medical_control: MedicalControl;
}

export interface VitalSignCriteria {
  sbp_below?: number;
  sbp_above?: number;
  map_below?: number;
  hr_below?: number;
  hr_above?: number;
  spo2_below?: number;
  gcs_below?: number;
}

export interface Criteria {
  age_min_months?: number;
  age_max_months?: number;
  symptoms?: string[];
  vital_signs?: VitalSignCriteria;
  exclusions?: string[];
}

export interface MedicationDose {
  medication_id: string;
  dose: string;
  dose_per_kg?: number;
  max_dose?: string;
  route: Route;
  rate?: string;
}

export interface Step {
  order: number;
  provider_level: ProviderLevel;
  action: string;
  medication?: MedicationDose;
  condition?: string;
  contraindications?: string[];
  notes?: string[];
  repeat?: string;
  cross_reference?: string;
}

export interface Protocol {
  id: string;
  title: string;
  category: string;
  patient_type: PatientType;
  tags: string[];
  criteria?: Criteria;
  steps: Step[];
  cross_references?: string[];
}

export interface ProtocolBundle {
  meta: JurisdictionMeta;
  protocols: Protocol[];
  medications: Medication[];
  procedures: Procedure[];
}
```

### 3.2 Offline Logic Engine

- [ ] Create `frontend/src/engine/ProtocolMatcher.ts`:

```typescript
/**
 * Offline Protocol Matching Engine
 * 
 * This is the CORE of VitalPath's offline capability.
 * All matching logic runs locally in the browser using the downloaded JSON bundle.
 * 
 * NO API CALLS are made during protocol matching.
 */

import type { Protocol, ProtocolBundle, ProviderLevel, PatientType } from '../types/protocol';

export interface PatientInput {
  ageMonths: number;
  patientType: PatientType;
  chiefComplaint: string;
  symptoms: string[];
  vitals: {
    sbp?: number;
    dbp?: number;
    hr?: number;
    rr?: number;
    spo2?: number;
    gcs?: number;
    temp?: number;
    etco2?: number;
    bgl?: number;
  };
}

export interface MatchedProtocol {
  protocol: Protocol;
  matchScore: number;
  matchReasons: string[];
}

export class ProtocolMatcher {
  private bundle: ProtocolBundle;

  constructor(bundle: ProtocolBundle) {
    this.bundle = bundle;
  }

  /**
   * Find all protocols matching the patient presentation.
   * Returns protocols sorted by relevance score.
   */
  match(input: PatientInput): MatchedProtocol[] {
    const matches: MatchedProtocol[] = [];

    for (const protocol of this.bundle.protocols) {
      const result = this.scoreProtocol(protocol, input);
      if (result.matchScore > 0) {
        matches.push(result);
      }
    }

    // Sort by score descending
    return matches.sort((a, b) => b.matchScore - a.matchScore);
  }

  /**
   * Filter protocol steps by provider certification level.
   * EMT sees only ALL/BLS steps. Paramedic sees all steps.
   */
  filterStepsByLevel(protocol: Protocol, userLevel: ProviderLevel): Protocol {
    const levelHierarchy: Record<ProviderLevel, number> = {
      'ALL': 0,
      'BLS': 1,
      'ALS': 2,
      'PARAMEDIC': 3,
      'OLMC': 4,
    };

    const userLevelNum = levelHierarchy[userLevel];

    return {
      ...protocol,
      steps: protocol.steps.filter(step => {
        const stepLevelNum = levelHierarchy[step.provider_level];
        // User can see steps at or below their level
        // Exception: OLMC steps are always visible (need to know when to call)
        return stepLevelNum <= userLevelNum || step.provider_level === 'OLMC';
      }),
    };
  }

  private scoreProtocol(protocol: Protocol, input: PatientInput): MatchedProtocol {
    let score = 0;
    const reasons: string[] = [];

    // Patient type match (required)
    if (protocol.patient_type !== 'all' && protocol.patient_type !== input.patientType) {
      return { protocol, matchScore: 0, matchReasons: [] };
    }

    // Tag/symptom matching
    const inputTerms = [
      input.chiefComplaint.toLowerCase(),
      ...input.symptoms.map(s => s.toLowerCase()),
    ];

    for (const tag of protocol.tags) {
      if (inputTerms.some(term => term.includes(tag) || tag.includes(term))) {
        score += 10;
        reasons.push(`Matches tag: ${tag}`);
      }
    }

    // Criteria matching
    if (protocol.criteria) {
      // Age criteria
      if (protocol.criteria.age_min_months && input.ageMonths >= protocol.criteria.age_min_months) {
        score += 5;
      }

      // Vital sign criteria
      if (protocol.criteria.vital_signs && input.vitals) {
        const vs = protocol.criteria.vital_signs;
        
        if (vs.sbp_below && input.vitals.sbp && input.vitals.sbp < vs.sbp_below) {
          score += 15;
          reasons.push(`SBP ${input.vitals.sbp} < ${vs.sbp_below}`);
        }
        if (vs.spo2_below && input.vitals.spo2 && input.vitals.spo2 < vs.spo2_below) {
          score += 15;
          reasons.push(`SpO2 ${input.vitals.spo2}% < ${vs.spo2_below}%`);
        }
      }

      // Symptom criteria
      if (protocol.criteria.symptoms) {
        for (const symptom of protocol.criteria.symptoms) {
          if (inputTerms.some(term => term.includes(symptom))) {
            score += 8;
            reasons.push(`Symptom match: ${symptom}`);
          }
        }
      }
    }

    return { protocol, matchScore: score, matchReasons: reasons };
  }

  /**
   * Get Medical Control contact for the jurisdiction.
   * This is DYNAMIC - loaded from the bundle, never hardcoded.
   */
  getMedicalControl() {
    return this.bundle.meta.medical_control;
  }

  /**
   * Get bundle version info.
   */
  getBundleInfo() {
    return {
      jurisdiction: this.bundle.meta.jurisdiction,
      version: this.bundle.meta.version,
      effectiveDate: this.bundle.meta.effective_date,
    };
  }
}
```

- [ ] Create `frontend/src/engine/DoseCalculator.ts`:

```typescript
/**
 * Pediatric Dose Calculator
 * 
 * Calculates weight-based dosing for pediatric patients.
 * Uses Broselow tape logic where applicable.
 */

import type { MedicationDose, Medication } from '../types/protocol';

export interface DoseResult {
  calculatedDose: string;
  maxDose?: string;
  warnings: string[];
}

export class DoseCalculator {
  private medications: Map<string, Medication>;

  constructor(medications: Medication[]) {
    this.medications = new Map(medications.map(m => [m.id, m]));
  }

  /**
   * Calculate pediatric dose based on weight.
   */
  calculatePediatricDose(
    medicationDose: MedicationDose,
    weightKg: number
  ): DoseResult {
    const warnings: string[] = [];

    if (!medicationDose.dose_per_kg) {
      return {
        calculatedDose: medicationDose.dose,
        maxDose: medicationDose.max_dose,
        warnings: ['No weight-based dosing available'],
      };
    }

    const calculatedMg = medicationDose.dose_per_kg * weightKg;
    let finalDose = calculatedMg;

    // Check against max dose
    if (medicationDose.max_dose) {
      const maxMg = this.parseDose(medicationDose.max_dose);
      if (calculatedMg > maxMg) {
        finalDose = maxMg;
        warnings.push(`Dose capped at max: ${medicationDose.max_dose}`);
      }
    }

    return {
      calculatedDose: `${finalDose.toFixed(1)} mg`,
      maxDose: medicationDose.max_dose,
      warnings,
    };
  }

  private parseDose(doseString: string): number {
    const match = doseString.match(/(\d+\.?\d*)/);
    return match ? parseFloat(match[1]) : 0;
  }
}
```

### 3.3 PWA Setup & Offline Storage

- [ ] Configure `vite.config.ts` for PWA:

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'robots.txt'],
      manifest: {
        name: 'VitalPath - EMS Protocol Assistant',
        short_name: 'VitalPath',
        description: 'Offline-first clinical decision support for EMS',
        theme_color: '#1a1a2e',
        background_color: '#1a1a2e',
        display: 'standalone',
        icons: [
          { src: '/icon-192.png', sizes: '192x192', type: 'image/png' },
          { src: '/icon-512.png', sizes: '512x512', type: 'image/png' },
        ],
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg,json}'],
        runtimeCaching: [
          {
            urlPattern: /\/api\/v1\/bundles\/latest/,
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'protocol-bundle',
              expiration: { maxAgeSeconds: 86400 }, // 24 hours
            },
          },
        ],
      },
    }),
  ],
});
```

- [ ] Create `frontend/src/services/offlineStorage.ts`:

```typescript
/**
 * Offline Storage Service
 * 
 * Manages the protocol bundle in IndexedDB for offline access.
 */

import type { ProtocolBundle } from '../types/protocol';

const DB_NAME = 'vitalpath';
const STORE_NAME = 'bundles';
const BUNDLE_KEY = 'current';

export class OfflineStorage {
  private db: IDBDatabase | null = null;

  async init(): Promise<void> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(DB_NAME, 1);
      
      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve();
      };
      
      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;
        db.createObjectStore(STORE_NAME);
      };
    });
  }

  async saveBundle(bundle: ProtocolBundle): Promise<void> {
    if (!this.db) await this.init();
    
    return new Promise((resolve, reject) => {
      const tx = this.db!.transaction(STORE_NAME, 'readwrite');
      const store = tx.objectStore(STORE_NAME);
      const request = store.put(bundle, BUNDLE_KEY);
      
      request.onerror = () => reject(request.error);
      request.onsuccess = () => resolve();
    });
  }

  async loadBundle(): Promise<ProtocolBundle | null> {
    if (!this.db) await this.init();
    
    return new Promise((resolve, reject) => {
      const tx = this.db!.transaction(STORE_NAME, 'readonly');
      const store = tx.objectStore(STORE_NAME);
      const request = store.get(BUNDLE_KEY);
      
      request.onerror = () => reject(request.error);
      request.onsuccess = () => resolve(request.result || null);
    });
  }

  async getBundleVersion(): Promise<string | null> {
    const bundle = await this.loadBundle();
    return bundle?.meta.version || null;
  }
}
```

### 3.4 Tactical Interface Components

- [ ] Create `frontend/src/components/tactical/PatientIntake.tsx`:
  - Large touch targets (min 48x48px)
  - Dark mode optimized
  - Step-through wizard: Demographics → Nature → Complaint → Vitals

- [ ] Create `frontend/src/components/tactical/GamePlan.tsx`:
  - Displays matched protocols
  - Filters steps by user's certification level
  - Highlights critical warnings
  - Shows cross-references as tappable links

- [ ] Create `frontend/src/components/tactical/MedicalControlCard.tsx`:
  - Displays OLMC contacts from bundle (DYNAMIC, not hardcoded)
  - One-tap to call functionality

- [ ] Create `frontend/src/components/tactical/CodeTimer.tsx`:
  - One-tap "Code Start" button
  - Announces 2-minute intervals (per HPCPR protocol)
  - Tracks compressions/ventilations

### 3.5 Admin Panel Components

- [ ] Create `frontend/src/components/admin/ProtocolEditor.tsx`:
  - Form-based protocol editing
  - Step reordering via drag-and-drop
  - Medication dose validation

- [ ] Create `frontend/src/components/admin/VersionManager.tsx`:
  - Shows "Active" vs "Draft" protocol sets
  - Diff view between versions
  - Publish button (triggers bundle recompilation)

- [ ] Create `frontend/src/components/admin/BundleStatus.tsx`:
  - Current bundle version
  - Last sync time
  - Force refresh button

---

## 4. Phase 3: Validation & DevOps

### 4.1 Unit Tests

- [ ] Backend tests (`backend/tests/`):
  - `test_models.py`: Validate Pydantic model serialization
  - `test_parser.py`: Test ACS protocol extraction accuracy
  - `test_compiler.py`: Verify JSON bundle output

- [ ] Frontend tests (`frontend/src/__tests__/`):
  - `ProtocolMatcher.test.ts`: 
    ```typescript
    test('chest pain matches ACS protocol', () => {
      const matcher = new ProtocolMatcher(testBundle);
      const input: PatientInput = {
        ageMonths: 600, // 50 years
        patientType: 'adult',
        chiefComplaint: 'chest pain',
        symptoms: ['diaphoresis', 'shortness of breath'],
        vitals: { sbp: 110, hr: 88, spo2: 95 },
      };
      
      const matches = matcher.match(input);
      expect(matches[0].protocol.id).toBe('cardiac_acs_adult');
      expect(matches[0].protocol.steps.some(s => 
        s.medication?.medication_id === 'aspirin'
      )).toBe(true);
    });
    ```
  - `DoseCalculator.test.ts`: Pediatric weight-based calculations

### 4.2 CI/CD Pipeline

- [ ] Create `.github/workflows/ci.yml`:

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, alpha]
  pull_request:
    branches: [main]

jobs:
  lint-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install ruff
      - run: ruff check backend/
      - run: ruff format --check backend/

  lint-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: cd frontend && npm ci
      - run: cd frontend && npm run lint
      - run: cd frontend && npm run type-check

  test-backend:
    runs-on: ubuntu-latest
    needs: lint-backend
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -e backend/[test]
      - run: pytest backend/tests/ -v

  test-frontend:
    runs-on: ubuntu-latest
    needs: lint-frontend
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: cd frontend && npm ci
      - run: cd frontend && npm test

  build:
    runs-on: ubuntu-latest
    needs: [test-backend, test-frontend]
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker images
        run: docker compose build
      - name: Push to ECR
        # AWS deployment steps...
```

---

## 5. Critical Implementation Notes

### 5.1 Medical Control Handling

**IMPORTANT:** Medical Control contact information is NEVER hardcoded in application logic.

- **Source:** protocol_context.md, page XI (Medical Control Contact)
- **Storage:** `bundle.meta.medical_control` object in JSON
- **Access:** Via `ProtocolMatcher.getMedicalControl()` method
- **Display:** `MedicalControlCard` component reads from bundle state

If PWC updates their OLMC phone numbers:
1. Update `backend/scripts/ingest_protocols.py` → `PWC_MEDICAL_CONTROL`
2. Recompile bundle
3. Frontend auto-updates via Service Worker

### 5.2 Offline-First Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     BACKEND (CMS)                          │
│  ┌─────────────┐    ┌─────────────┐    ┌──────────────┐   │
│  │  Postgres   │───>│  Compiler   │───>│ JSON Bundle  │   │
│  │  (Protocols)│    │             │    │              │   │
│  └─────────────┘    └─────────────┘    └──────┬───────┘   │
└──────────────────────────────────────────────│───────────┘
                                               │
                        ┌──────────────────────▼───────────┐
                        │         API: /bundles/latest     │
                        └──────────────────────┬───────────┘
                                               │
        ┌──────────────────────────────────────▼───────────────┐
        │                  FRONTEND (PWA)                      │
        │  ┌────────────┐    ┌────────────┐    ┌────────────┐ │
        │  │ Service    │───>│ IndexedDB  │───>│ Protocol   │ │
        │  │ Worker     │    │ (Bundle)   │    │ Matcher    │ │
        │  └────────────┘    └────────────┘    └────────────┘ │
        │                                             │        │
        │  ┌──────────────────────────────────────────▼──────┐│
        │  │              UI (React)                         ││
        │  │  ┌──────────┐  ┌──────────┐  ┌──────────┐      ││
        │  │  │ Intake   │  │ GamePlan │  │ OLMC Card│      ││
        │  │  └──────────┘  └──────────┘  └──────────┘      ││
        │  └─────────────────────────────────────────────────┘│
        └─────────────────────────────────────────────────────┘
                            │
                            ▼
                    [NO NETWORK REQUIRED]
                    [ALL LOGIC RUNS LOCAL]
```

### 5.3 Protocol Extraction Priority

Based on protocol_context.md analysis, extract protocols in this order:

**Phase 1A (Core Medical):**
1. General Patient Care Protocol - Adult (p. 1-4)
2. Cardiac Emergencies: Acute Coronary Syndrome (p. 22-23) ★ Gold Standard
3. Respiratory Emergencies: Dyspnea (p. 5-6)
4. Medical: Diabetic Emergencies (p. 45)
5. Cardiac Arrest: General Approach (p. 15-16)

**Phase 1B (Trauma):**
6. General Patient Care Protocol - Adult Trauma (p. 63-64)
7. Trauma: Burns (p. 66-67)
8. Trauma Triage Criteria (p. 158-159)

**Phase 1C (Pediatric):**
9. General Patient Care Protocol - Pediatric (p. 76-79)
10. Pediatric Cardiac Arrest (p. 87-94)

---

## 6. Files to Delete (Legacy Cleanup)

Per the new architecture, these files from the current workspace should be removed:

```bash
# Legacy protocol/procedure system (replaced by JSON bundle)
rm -rf protocols/
rm -rf procedures/
rm -rf src/

# Legacy entry points (replaced by backend/frontend apps)
rm main.py
rm demograph_info.py

# Legacy tests (new test structure)
rm -rf tests/alternative_system/

# Data files that will be regenerated
rm data/protocols.yaml
```

**Keep:**
- protocol_context.md → Move to `data/raw/`
- outline.md → Reference document
- README.md → Update with new architecture
- .gitignore → Update for new structure

---

## 7. Success Criteria

### Phase 1 Complete When:
- [ ] ACS protocol extracts correctly from protocol_context.md
- [ ] JSON bundle compiles with valid schema
- [ ] Bundle includes dynamic Medical Control data
- [ ] `pytest backend/tests/` passes 100%

### Phase 2 Complete When:
- [ ] PWA loads bundle into IndexedDB
- [ ] Protocol matching works offline (airplane mode test)
- [ ] EMT user sees only BLS-appropriate steps
- [ ] Medical Control card displays correct facility contacts

### Phase 3 Complete When:
- [ ] CI/CD pipeline green on all PRs
- [ ] Admin can edit protocol and publish new bundle
- [ ] Frontend auto-updates bundle via Service Worker

---

*This plan is the single source of truth for VitalPath development. All implementation should reference this document.*