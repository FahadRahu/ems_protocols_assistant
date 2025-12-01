Project VitalPath: Master Design Document'

This is my current working outline of what the app "Vital Path" is. 

1. Executive Summary
VitalPath is an offline-first Clinical Decision Support System (CDSS) for EMS providers. Unlike static PDF viewers, it acts as a dynamic "Game Plan" generator. A provider inputs patient variables (Age, Gender, Complaint, Vitals), and the system filters the massive protocol database to present only the relevant treatment steps, warnings, and medication dosages specific to their certification level (BLS/ALS).

Primary Jurisdiction: Prince William County (PWC), VA. Primary Constraint: Must function 100% offline after initial load.

2. Technical Architecture (The "Smart Client" Model)
A. The Stack
Backend (Management & Source of Truth):

Language: Python 3.11+

Framework: FastAPI (Modular Monolith structure).

Database: PostgreSQL (Stores raw protocol data, version history, admin users).

Role: Acts as the "Headquarters." Administers protocol updates and serves a compiled protocols.json bundle to the frontend.

Frontend (The Field App):

Framework: React (Vite + TypeScript).

Architecture: PWA (Progressive Web App) with Service Workers for offline caching.

State Management: TanStack Query (React Query) + Zustand.

Logic Engine: A TypeScript-based inference engine that runs locally in the browser.

Data Structure (The Protocol Schema):

Protocols are defined in YAML/JSON with strict schemas (using Pydantic models in Python and Interfaces in TS).

Medical Control: Not hardcoded. Defined as a distinct medical_control_contact object within the JSON configuration for the specific county.

B. DevOps & Infrastructure
Containerization: Docker for Backend (API) and Frontend (Nginx serving static build).

Orchestration: AWS ECS (Fargate).

CI/CD: GitHub Actions (Linting -> Testing -> Build -> Deploy).

3. Feature Specifications
Core 1: The "Tactical" Interface (Field Use)
One-Handed Input: Large tap targets. Dark mode default.

Dynamic Intake Form:

Step 1: Demographics (Adult/Ped/Infant toggle).

Step 2: Nature (Medical/Trauma).

Step 3: Chief Complaint (Searchable dropdown tags, e.g., "Chest Pain", "Burn").

Step 4: Critical Vitals (BP, HR, SpO2).

The Game Plan (Output):

Priority Alerts: "Meets Trauma Triage Criteria" (Red Banner).

Filtered Steps: If User = EMT, hide "Intubation". Show "Assist ALS".

Calculators: Auto-calculate Pediatric Epi dose based on input weight (using Broselow logic from PWC reference).

Timer: One-tap "Code Start" timer for Cardiac Arrest.

Core 2: The Admin Panel (Station Use)
Protocol Editor: A web form to edit specific steps without touching code.

Version Control:

"Active Protocol Set: PWC 2019v2".

"Draft Protocol Set: PWC 2024 Updates".

Release Button: Compiles the database into a new protocols_v2.json and pushes it to the PWA.

4. The Data Model (JSON Schema Strategy)
We will structure the PWC PDF into this format. Your AI agent should be instructed to generate data matching this schema:

{
  "meta": {
    "jurisdiction": "Prince William County",
    "version": "2019.1",
    "last_updated": "2023-10-27",
    "medical_control": {
      "default_phone": "703-555-0123",
      "radio_channel": "5 Alpha"
    }
  },
  "protocols": [
    {
      "id": "cardiac_01",
      "title": "Acute Coronary Syndrome",
      "type": "Medical",
      "tags": ["chest pain", "stemi", "heart attack"],
      "criteria": {
        "age_min": 18,
        "symptoms": ["chest_pain", "dyspnea"]
      },
      "steps": [
        {
          "role": "ALL",
          "action": "Administer Aspirin 324mg PO",
          "contraindications": ["Allergy", "GI Bleed"]
        },
        {
          "role": "ALS",
          "action": "12-Lead ECG",
          "note": "Transmit to facility immediately."
        },
        {
          "role": "ALS",
          "action": "Nitroglycerin 0.4mg SL",
          "condition": "SBP > 100",
          "repeat": "Every 5 mins x3"
        }
      ]
    }
  ]
}

5. System Prompt for Your AI Agent
Copy and paste the text below into your VS Code / Cursor / Windsurf AI chat to start the project. This gives it the "Context" it needs to be an expert engineer.

ROLE DEFINITION: You are a Senior Full-Stack Engineer and EMS subject matter expert. You are building VitalPath, a Clinical Decision Support System for First Responders. Your goal is to build a high-reliability, offline-first web application.

CORE CONSTRAINTS:

Architecture: Modular Monolith.

Backend: Python (FastAPI). Used for data management and serving the Protocol Bundle.

Frontend: React (TypeScript + Vite). Used for the UI and the Client-Side Decision Logic.

Offline Requirement: The decision logic MUST run in the browser (TypeScript) using a downloaded JSON bundle. The app cannot rely on API calls during a rescue.

Styling: Tailwind CSS (Mobile-first, high contrast, dark mode optimized).

DATA SOURCE: We are using the "Prince William County Patient Care Manual". All protocols generated must be strictly based on the provided PDF text.

CODING STANDARDS:

Python: Strict type hints, Pydantic models for everything, Pytest for testing.

TypeScript: Strict mode, Interfaces for all data models.

Documentation: Every major function must have a docstring explaining the clinical reasoning (if applicable).

PHASE 1 GOAL: THE DATA FOUNDATION We need to create the backend structure that converts unstructured PDF text into our strict JSON Schema.

TASK 1: Create the project structure:

/backend: FastAPI app

/frontend: React app

/data: Folder for raw PDF and processed JSON.

TASK 2: Define the Pydantic Models (Python) and TypeScript Interfaces that represent a Protocol. It must include fields for: ID, Title, Certification Level (BLS/ALS/OMD), Inclusion Criteria (Signs/Symptoms), Exclusion Criteria, and an ordered list of Steps.

TASK 3: Write a script to "mock" the extraction of the Adult Chest Pain (Acute Coronary Syndrome) protocol from the context I will provide, fitting it into that Pydantic model, and saving it as pwc_protocols.json.
