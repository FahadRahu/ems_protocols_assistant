# VitalPath Development Timeline & Journal

**Project:** VitalPath - Offline-First Clinical Decision Support System  
**Repository:** `ems_protocols_assistant`  
**Owner:** FahadRahu  
**Current Branch:** `alpha`  
**Default Branch:** `main`  

---

## Entry #1: The Great Restructuring

**Date:** November 30, 2025  
**Branch:** `alpha`  
**Commit Status:** Uncommitted (5 additions, 23 deletions staged)

---

### Executive Summary

Today marks the transformation of a Python-only EMS protocol assistant into a full-stack, offline-first Clinical Decision Support System (CDSS) called **VitalPath**. The session involved two major phases:

1. **Planning Phase**: Generated a comprehensive 1,650+ line development master plan (`vitalpath_plan.md`)
2. **Execution Phase**: Restructured the entire workspace—archiving legacy code and creating a complete monorepo skeleton with functional code

The goal: Build a "Smart Client" architecture where a FastAPI backend serves as a CMS/JSON compiler, while a React PWA runs all protocol matching logic locally and offline.

---

### Background: What Existed Before

The original project was a Python-based EMS Protocol Assistant for Prince William County Fire & Rescue. It had:

```
Original Structure:
├── main.py                 # Entry point collecting patient demographics
├── demograph_info.py       # Patient demographic collection
├── domain.py               # Patient, Vitals, AgeGroup dataclasses
├── engine.py               # Rules evaluation engine
├── protocols/              # Medical protocol definitions
│   ├── GeneralPCP_Adult.py
│   ├── medical_protocols.py
│   └── imports.py
├── procedures/             # Clinical procedures
│   ├── admin_procedures.py
│   ├── airway_clinical_procedures.py
│   ├── cardiac_clinical_procedures.py
│   ├── other_clinical_procedures.py
│   └── imports.py
├── src/
│   ├── domain.py
│   └── engine.py
├── tests/
│   └── alternative_system/
├── utils/
│   ├── helpers.py
│   └── logger.py
└── data/
    └── protocols.yaml
```

**Problems with the old architecture:**
- Python-only meant no offline mobile capability
- Protocol logic was hardcoded in Python functions
- Medical Control phone numbers were scattered/hardcoded
- No separation between data management and clinical logic
- Not deployable as a PWA for field use

---

### The New Architecture: Smart Client

```
┌─────────────────────────────────────────────────────────────┐
│                     BACKEND (CMS)                          │
│  ┌─────────────┐    ┌─────────────┐    ┌──────────────┐   │
│  │  Postgres   │───>│  Compiler   │───>│ JSON Bundle  │   │
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
        └─────────────────────────────────────────────────────┘
                            │
                            ▼
                    [NO NETWORK REQUIRED]
```

**Key Principle:** The backend compiles protocols into a JSON bundle. The frontend downloads this bundle once, stores it in IndexedDB, and runs ALL clinical logic locally. After initial sync, the app works completely offline.

---

### Phase 1: Planning (`vitalpath_plan.md`)

**File Created:** `vitalpath_plan.md`  
**Lines:** ~1,650  
**Purpose:** Comprehensive development roadmap with checkboxable tasks

This master plan document serves as the single source of truth for development. It includes:

1. **Project Initialization & Standards** (Section 1)
   - Directory structure definition
   - Development environment setup (Docker, pre-commit hooks)
   - Protocol schema definition

2. **Data Engineering Foundation** (Section 2)
   - Backend Pydantic models
   - Protocol ingestion script design
   - JSON bundle compiler architecture

3. **Smart Client Frontend** (Section 3)
   - TypeScript interfaces mirroring backend
   - Offline Logic Engine design
   - Tactical interface components
   - Admin panel components

4. **Validation & DevOps** (Section 4)
   - Unit test strategy
   - CI/CD pipeline configuration

5. **Critical Implementation Notes** (Section 5)
   - Medical Control handling (MUST be dynamic)
   - Offline-first architecture diagrams
   - Protocol extraction priority

---

### Phase 2: The Great Restructuring

#### Step 1: Archive Legacy Code

Instead of deleting the old code (preserving git history and reference material), all legacy files were moved to an `archive/` directory:

**Files Archived:**
| Original Location | New Location | Reason |
|-------------------|--------------|--------|
| `main.py` | `archive/main.py` | Entry point replaced by FastAPI |
| `demograph_info.py` | `archive/demograph_info.py` | Logic moves to React frontend |
| `protocols/` | `archive/protocols/` | Replaced by JSON bundle system |
| `procedures/` | `archive/procedures/` | Logic encoded in JSON, not Python |
| `src/` | `archive/src/` | Domain models replaced by Pydantic |
| `tests/` | `archive/tests/` | New test structure created |
| `utils/` | `archive/utils/` | Utilities consolidated elsewhere |

**Archive README created:** `archive/README.md` explains why these files exist and that they should not be used in new development.

---

#### Step 2: Create Backend Structure

**Directory:** `backend/`

##### `backend/pyproject.toml`
**Purpose:** Python package configuration with all dependencies  
**Key Dependencies:**
- `fastapi` - Web framework for API
- `uvicorn` - ASGI server
- `pydantic` v2 - Data validation
- `sqlalchemy` - ORM for PostgreSQL
- `alembic` - Database migrations
- `pytest`, `httpx` - Testing
- `ruff` - Linting

##### `backend/Dockerfile`
**Purpose:** Container configuration for backend service  
**Base Image:** `python:3.11-slim`  
**Exposes:** Port 8000

##### `backend/app/__init__.py`
**Purpose:** Package marker, empty file

##### `backend/app/main.py`
**Purpose:** FastAPI application entry point  
**Key Features:**
- Lifespan context manager for startup/shutdown
- CORS middleware configured for frontend
- API routers mounted at `/api/v1/`
- Root health check endpoint

##### `backend/app/config.py`
**Purpose:** Configuration management using Pydantic BaseSettings  
**Environment Variables:**
- `DATABASE_URL` - PostgreSQL connection string
- `BUNDLE_DIR` - Path to compiled JSON bundles
- `DEBUG` - Debug mode toggle
- `CORS_ORIGINS` - Allowed frontend origins

---

#### Step 3: Create Backend Models

**Directory:** `backend/app/models/`

##### `backend/app/models/__init__.py`
**Purpose:** Re-exports all models for clean imports  
**Exports:** All Pydantic models from protocol, jurisdiction, medication, procedure, bundle modules

##### `backend/app/models/protocol.py`
**Purpose:** Core protocol domain models  
**Classes:**
- `ProviderLevel` (Enum): ALL, BLS, ALS, PARAMEDIC, OLMC
- `PatientType` (Enum): adult, pediatric, neonate, all
- `Route` (Enum): PO, SL, IV, IO, IM, IN, NEB, ODT, TOPICAL
- `VitalSignCriteria`: Thresholds for protocol matching (SBP, HR, SpO2, GCS, EtCO2)
- `Criteria`: Inclusion/exclusion criteria
- `MedicationDose`: Dosing within a step
- `Step`: Individual treatment step with provider level, action, conditions
- `Protocol`: Complete protocol definition

**Critical Design Decision:** The `Step` model includes `provider_level` which allows filtering steps by EMT vs Paramedic scope of practice.

##### `backend/app/models/jurisdiction.py`
**Purpose:** Medical Control and jurisdiction metadata  
**Classes:**
- `MedicalControlContact`: Individual OLMC facility (facility, phone, radio_channel)
- `MedicalControl`: All contacts + poison control + CHEMTREC
- `JurisdictionMeta`: Bundle metadata (jurisdiction, version, effective_date, medical_control)

**CRITICAL:** Medical Control contacts are DYNAMIC. They load from JSON, never hardcoded in application logic. This allows updating phone numbers by recompiling the bundle without code changes.

##### `backend/app/models/medication.py`
**Purpose:** Medication reference data  
**Classes:**
- `DosingInfo`: Indication-specific dosing
- `Medication`: Complete drug reference (generic name, trade names, class, mechanism, contraindications, adult/pediatric dosing)

##### `backend/app/models/procedure.py`
**Purpose:** Clinical and administrative procedures  
**Classes:**
- `Procedure`: Procedure definition (id, title, type, authorized personnel, indications, contraindications, equipment, steps)

##### `backend/app/models/bundle.py`
**Purpose:** The complete offline bundle structure  
**Classes:**
- `ProtocolBundle`: Contains meta, protocols, medications, procedures - this is what gets serialized to JSON and downloaded by the frontend

---

#### Step 4: Create Backend Services

**Directory:** `backend/app/services/`

##### `backend/app/services/__init__.py`
**Purpose:** Re-exports services

##### `backend/app/services/compiler.py`
**Purpose:** JSON bundle compilation  
**Classes:**
- `BundleCompiler`: Takes a ProtocolBundle and outputs versioned JSON files
  - `compile()`: Pretty-printed JSON for development
  - `compile_minified()`: Minified JSON for production
  - Generates SHA-256 hash for bundle integrity verification

##### `backend/app/services/parser.py`
**Purpose:** Protocol text parsing (stub for future implementation)  
**Classes:**
- `ProtocolParser`: Will parse `protocol_context.md` into structured Protocol objects

---

#### Step 5: Create Backend API Routes

**Directory:** `backend/app/api/`

##### `backend/app/api/__init__.py`
**Purpose:** Re-exports routers

##### `backend/app/api/bundles.py`
**Purpose:** Bundle download endpoints  
**Endpoints:**
- `GET /api/v1/bundles/latest`: Returns the most recent compiled JSON bundle
- `GET /api/v1/bundles/version`: Returns version info without full download (for update checking)

##### `backend/app/api/protocols.py`
**Purpose:** Protocol CRUD operations (stubs)  
**Endpoints:**
- `GET /api/v1/protocols/`: List all protocols
- `GET /api/v1/protocols/{id}`: Get single protocol
- `POST /api/v1/protocols/`: Create protocol (admin)
- `PUT /api/v1/protocols/{id}`: Update protocol (admin)
- `DELETE /api/v1/protocols/{id}`: Delete protocol (admin)

---

#### Step 6: Create Backend Database Layer

**Directory:** `backend/app/db/`

##### `backend/app/db/__init__.py`
**Purpose:** Package marker

##### `backend/app/db/repository.py`
**Purpose:** Database access layer (stub)  
**Classes:**
- `ProtocolRepository`: Future CRUD operations for PostgreSQL

---

#### Step 7: Create Ingestion Script

**File:** `backend/scripts/ingest_protocols.py`

**Purpose:** One-time script to parse `protocol_context.md` and generate the initial protocol bundle

**Key Contents:**
1. **PWC_MEDICAL_CONTROL**: All 8 Prince William County Medical Control facilities with phone numbers:
   - Sentara Northern Virginia Medical Center
   - Novant Health UVA Health System Haymarket Medical Center
   - Novant Health UVA Health System Prince William Medical Center
   - Reston Hospital Center
   - Inova Fair Oaks Hospital
   - Inova Fairfax Medical Campus
   - Fauquier Hospital
   - Spotsylvania Regional Medical Center
   - Plus: Poison Control (1-800-222-1222) and CHEMTREC (1-800-424-9300)

2. **Gold Standard Protocol**: Complete Acute Coronary Syndrome (ACS) protocol with all 11 steps:
   - Step 1: Oxygen therapy (ALL providers)
   - Step 2: Cardiac monitoring (ALL)
   - Step 3: 12-lead ECG (ALL)
   - Step 4: IV access (ALS)
   - Step 5: Aspirin 324mg (ALL)
   - Step 6: Nitroglycerin (ALS, with SBP condition)
   - Step 7: Pain reassessment (ALS)
   - Step 8: Fentanyl for pain (PARAMEDIC)
   - Step 9: STEMI alert/transport (ALL)
   - Step 10: Notify destination (ALL)
   - Step 11: Additional orders (OLMC)

3. **Bundle Generation**: Creates `pwc_protocols_v1.json` in `data/compiled/`

---

#### Step 8: Create Backend Tests

**File:** `backend/tests/test_models.py`

**Purpose:** Validate Pydantic model serialization and behavior  
**Tests:**
- Protocol creation and serialization
- Step ordering
- Provider level enum handling
- Medical Control structure

---

#### Step 9: Create Frontend Structure

**Directory:** `frontend/`

##### `frontend/package.json`
**Purpose:** Node.js package configuration  
**Key Dependencies:**
- `react` 18, `react-dom` 18 - UI framework
- `@tanstack/react-query` - Server state management
- `zustand` - Client state management
- `react-router-dom` - Routing

**Dev Dependencies:**
- `vite` - Build tool
- `typescript` - Type safety
- `tailwindcss`, `postcss`, `autoprefixer` - Styling
- `vite-plugin-pwa` - PWA support
- `@testing-library/react`, `vitest` - Testing

##### `frontend/index.html`
**Purpose:** HTML entry point  
**Features:** PWA meta tags, theme-color for mobile

##### `frontend/vite.config.ts`
**Purpose:** Vite build configuration  
**Features:**
- React plugin
- PWA plugin with workbox configuration
- Service worker registration
- Offline caching strategy

##### `frontend/tsconfig.json`
**Purpose:** TypeScript compiler configuration  
**Settings:** Strict mode, ES2020 target, React JSX

##### `frontend/tsconfig.node.json`
**Purpose:** TypeScript config for Node.js files (vite.config.ts)

##### `frontend/tailwind.config.js`
**Purpose:** Tailwind CSS configuration  
**Customizations:**
- Dark mode enabled
- Custom colors for EMS (priority red, caution yellow, safe green)
- Extended spacing for large touch targets

##### `frontend/postcss.config.js`
**Purpose:** PostCSS configuration for Tailwind

---

#### Step 10: Create Frontend Source Files

**Directory:** `frontend/src/`

##### `frontend/src/main.tsx`
**Purpose:** React application entry point  
**Features:** StrictMode, QueryClient provider

##### `frontend/src/App.tsx`
**Purpose:** Main application component  
**Features:** Routing setup, layout structure

##### `frontend/src/index.css`
**Purpose:** Global styles  
**Features:** Tailwind directives, dark mode defaults, large touch target utilities

---

#### Step 11: Create Frontend Types

**Directory:** `frontend/src/types/`

##### `frontend/src/types/protocol.ts`
**Purpose:** TypeScript interfaces mirroring backend Pydantic models  
**Interfaces:**
- `ProviderLevel`, `PatientType`, `Route` - Type unions
- `MedicalControlContact`, `MedicalControl`, `JurisdictionMeta`
- `VitalSignCriteria`, `Criteria`
- `MedicationDose`, `Step`, `Protocol`
- `Medication`, `DosingInfo`
- `Procedure`
- `ProtocolBundle`

**CRITICAL:** These interfaces MUST stay in sync with backend models. The JSON Schema in `shared/schemas/` is the source of truth.

##### `frontend/src/types/index.ts`
**Purpose:** Re-exports all types

---

#### Step 12: Create Frontend Engine (The Core Logic)

**Directory:** `frontend/src/engine/`

##### `frontend/src/engine/ProtocolMatcher.ts`
**Purpose:** Offline protocol matching - THE HEART OF VITALPATH  
**Classes:**
- `ProtocolMatcher`: Takes patient input, returns matched protocols with scores

**Key Methods:**
- `match(input: PatientInput)`: Scores all protocols against patient presentation
- `filterStepsByLevel(protocol, userLevel)`: Filters steps by EMT/Paramedic certification
- `getMedicalControl()`: Returns OLMC contacts from bundle (DYNAMIC!)
- `getVersion()`: Returns bundle version info

**Matching Algorithm:**
1. Filter by patient type (adult/pediatric)
2. Score by symptom matches
3. Score by chief complaint tags
4. Score by vital sign criteria
5. Return sorted by match score

##### `frontend/src/engine/DoseCalculator.ts`
**Purpose:** Pediatric weight-based dose calculations  
**Classes:**
- `DoseCalculator`: Calculates doses from mg/kg with max dose limits

**Key Methods:**
- `calculate(dose: MedicationDose, weightKg: number)`: Returns calculated dose with warnings

##### `frontend/src/engine/index.ts`
**Purpose:** Re-exports engine classes

---

#### Step 13: Create Frontend Services

**Directory:** `frontend/src/services/`

##### `frontend/src/services/offlineStorage.ts`
**Purpose:** IndexedDB wrapper for offline bundle persistence  
**Classes:**
- `OfflineStorage`: Manages protocol bundle in IndexedDB

**Key Methods:**
- `init()`: Opens/creates database
- `saveBundle(bundle)`: Stores bundle with timestamp
- `getBundle()`: Retrieves stored bundle
- `getBundleVersion()`: Gets version without loading full bundle
- `clearBundle()`: Removes stored data

##### `frontend/src/services/index.ts`
**Purpose:** Re-exports services

---

#### Step 14: Create Frontend Stores

**Directory:** `frontend/src/stores/`

##### `frontend/src/stores/bundleStore.ts`
**Purpose:** Zustand store for bundle state management  
**State:**
- `bundle`: Current protocol bundle (or null)
- `isLoading`: Loading state
- `error`: Error state
- `lastSync`: Last sync timestamp

**Actions:**
- `loadBundle()`: Load from IndexedDB or fetch from API
- `refreshBundle()`: Force refresh from API
- `clearBundle()`: Clear local storage

##### `frontend/src/stores/index.ts`
**Purpose:** Re-exports stores

---

#### Step 15: Create Frontend Components

**Directory:** `frontend/src/components/`

##### Tactical Components (`frontend/src/components/tactical/`)

**Purpose:** Field-use interface components designed for:
- Dark environments (dark mode default)
- Gloved operation (large 48x48px touch targets)
- Quick access (minimal navigation depth)

| File | Purpose |
|------|---------|
| `PatientIntake.tsx` | Step-through wizard for patient information |
| `GamePlan.tsx` | Displays matched protocols with filtered steps |
| `MedicalControlCard.tsx` | OLMC contacts loaded from bundle (DYNAMIC!) |
| `CodeTimer.tsx` | Cardiac arrest timer with medication tracking |
| `index.ts` | Re-exports |

##### Admin Components (`frontend/src/components/admin/`)

**Purpose:** Station-use interface for protocol management

| File | Purpose |
|------|---------|
| `ProtocolEditor.tsx` | Form-based protocol editing |
| `BundleStatus.tsx` | Current version, sync status, refresh button |
| `index.ts` | Re-exports |

##### `frontend/src/components/index.ts`
**Purpose:** Re-exports all component directories

---

#### Step 16: Create Frontend Hooks

**Directory:** `frontend/src/hooks/`

##### `frontend/src/hooks/hooks.ts`
**Purpose:** Custom React hooks  
**Hooks:**
- `useBundle()`: Access bundle from store
- `useProtocolMatcher()`: Get matcher instance for current bundle
- `useMedicalControl()`: Access OLMC contacts (convenience hook)

##### `frontend/src/hooks/index.ts`
**Purpose:** Re-exports hooks

---

#### Step 17: Create Shared Schema

**Directory:** `shared/`

##### `shared/schemas/protocol-schema.json`
**Purpose:** JSON Schema - THE SINGLE SOURCE OF TRUTH  
**Defines:**
- Complete bundle structure
- All model definitions
- Validation rules
- Enum values

This schema is used to:
1. Validate compiled JSON bundles
2. Generate TypeScript types (optional)
3. Document the data contract between backend and frontend

##### `shared/README.md`
**Purpose:** Explains the shared schema directory

---

#### Step 18: Create Data Directory

**Directory:** `data/`

##### `data/README.md`
**Purpose:** Documents the data directory structure  
**Subdirectories:**
- `raw/`: Source documents (protocol_context.md)
- `compiled/`: Generated JSON bundles

---

#### Step 19: Create DevOps Configuration

##### `docker-compose.yml`
**Purpose:** Development environment orchestration  
**Services:**
- `backend`: FastAPI on port 8000
- `frontend`: Vite dev server on port 5173
- `db`: PostgreSQL on port 5432
**Volumes:**
- `pgdata`: Persistent database storage

##### `.pre-commit-config.yaml`
**Purpose:** Git pre-commit hooks for code quality  
**Hooks:**
- `ruff`: Python linting and formatting
- `prettier`: TypeScript/JSON formatting
- `trailing-whitespace`: Remove trailing spaces
- `end-of-file-fixer`: Ensure newline at EOF
- `check-yaml`: Validate YAML syntax

##### `.github/workflows/ci.yml`
**Purpose:** GitHub Actions CI/CD pipeline  
**Jobs:**
1. `lint-backend`: Run ruff on Python code
2. `lint-frontend`: Run ESLint and Prettier
3. `test-backend`: Run pytest
4. `test-frontend`: Run vitest
5. `build`: Build frontend for production

---

#### Step 20: Update Root Documentation

##### `README.md`
**Purpose:** Updated project documentation  
**Sections:**
- Architecture diagram
- Project structure
- Quick start guide
- Development commands
- Testing instructions
- Legacy documentation preserved at bottom

---

### Summary of All Files Created

| Category | Count | Files |
|----------|-------|-------|
| Backend Models | 6 | `__init__.py`, `protocol.py`, `jurisdiction.py`, `medication.py`, `procedure.py`, `bundle.py` |
| Backend Services | 3 | `__init__.py`, `compiler.py`, `parser.py` |
| Backend API | 3 | `__init__.py`, `bundles.py`, `protocols.py` |
| Backend DB | 2 | `__init__.py`, `repository.py` |
| Backend Root | 5 | `__init__.py`, `main.py`, `config.py`, `pyproject.toml`, `Dockerfile` |
| Backend Scripts | 1 | `ingest_protocols.py` |
| Backend Tests | 2 | `__init__.py`, `test_models.py` |
| Frontend Config | 6 | `package.json`, `index.html`, `vite.config.ts`, `tsconfig.json`, `tsconfig.node.json`, `tailwind.config.js`, `postcss.config.js` |
| Frontend Source | 3 | `main.tsx`, `App.tsx`, `index.css` |
| Frontend Types | 2 | `protocol.ts`, `index.ts` |
| Frontend Engine | 3 | `ProtocolMatcher.ts`, `DoseCalculator.ts`, `index.ts` |
| Frontend Services | 2 | `offlineStorage.ts`, `index.ts` |
| Frontend Stores | 2 | `bundleStore.ts`, `index.ts` |
| Frontend Hooks | 2 | `hooks.ts`, `index.ts` |
| Frontend Components | 8 | `PatientIntake.tsx`, `GamePlan.tsx`, `MedicalControlCard.tsx`, `CodeTimer.tsx`, `ProtocolEditor.tsx`, `BundleStatus.tsx`, 2x `index.ts` |
| Shared | 2 | `protocol-schema.json`, `README.md` |
| Data | 1 | `README.md` |
| DevOps | 3 | `docker-compose.yml`, `.pre-commit-config.yaml`, `ci.yml` |
| Archive | 1 | `README.md` |
| Root | 1 | `README.md` (updated) |

**Total New Files:** ~55 files

---

### Critical Design Decisions Explained

#### 1. Why Archive Instead of Delete?
- Preserves git history for reference
- Allows comparison between old and new approaches
- Legacy code may have useful snippets
- No data loss if we need to reference something

#### 2. Why Monorepo Structure?
- Shared types between frontend and backend
- Single git repository for atomic commits
- Easier to maintain version alignment
- Simpler CI/CD pipeline

#### 3. Why Pydantic v2?
- Performance improvements over v1
- Better JSON Schema generation
- Native support for TypeScript-like validation
- Model serialization matches TypeScript interfaces

#### 4. Why Zustand Over Redux?
- Simpler API, less boilerplate
- Works well with React Query
- Better TypeScript support
- Smaller bundle size

#### 5. Why IndexedDB Over localStorage?
- Larger storage limits (localStorage is 5-10MB)
- Protocol bundles can be large
- Better for structured data
- Async API doesn't block main thread

#### 6. Why Dynamic Medical Control?
- Phone numbers change
- New facilities get added
- Different jurisdictions have different contacts
- Updating bundle is easier than deploying code changes

---

### Next Steps: Immediate Goals

#### Phase 1 Completion Checklist

- [ ] **Install Dependencies**
  ```bash
  # Backend
  cd backend
  pip install -e ".[dev]"
  
  # Frontend
  cd frontend
  npm install
  ```

- [ ] **Run Ingestion Script**
  ```bash
  cd backend
  python -m scripts.ingest_protocols
  ```
  This will generate `data/compiled/pwc_protocols_v1.json`

- [ ] **Start Backend**
  ```bash
  cd backend
  uvicorn app.main:app --reload
  ```

- [ ] **Start Frontend**
  ```bash
  cd frontend
  npm run dev
  ```

- [ ] **Verify Bundle API**
  ```bash
  curl http://localhost:8000/api/v1/bundles/version
  ```

- [ ] **Run Tests**
  ```bash
  # Backend
  cd backend && pytest tests/ -v
  
  # Frontend
  cd frontend && npm test
  ```

#### Additional Protocols to Extract

After ACS (Gold Standard) is validated, extract in this order:

1. **General Patient Care Protocol - Adult** (p. 1-4)
2. **Dyspnea** (p. 5-6)
3. **Diabetic Emergencies** (p. 45)
4. **Cardiac Arrest - General Approach** (p. 15-16)
5. **General Patient Care Protocol - Adult Trauma** (p. 63-64)
6. **Burns** (p. 66-67)
7. **General Patient Care Protocol - Pediatric** (p. 76-79)
8. **Pediatric Cardiac Arrest** (p. 87-94)

#### Frontend Integration Tasks

1. Wire up `PatientIntake` to `ProtocolMatcher`
2. Display `GamePlan` with matched protocols
3. Test offline mode (airplane mode test)
4. Verify Medical Control card shows bundle contacts
5. Test provider level filtering (EMT vs Paramedic view)

---

### Notes for Future Entries

When adding new journal entries, include:

1. **Date and branch**
2. **What was changed** (files added/modified/deleted)
3. **Why it was changed** (the problem being solved)
4. **How it works** (technical explanation)
5. **Testing performed** (how it was validated)
6. **Next steps** (what comes after)

---

### Appendix: Tech Stack Quick Reference

| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| Backend Framework | FastAPI | Latest | API server |
| Backend Validation | Pydantic | v2 | Data models |
| Backend ORM | SQLAlchemy | Latest | Database access |
| Database | PostgreSQL | 15 | Persistent storage |
| Frontend Framework | React | 18 | UI library |
| Frontend Build | Vite | Latest | Build tool |
| Frontend Language | TypeScript | Latest | Type safety |
| Frontend Styling | Tailwind CSS | Latest | Utility CSS |
| Frontend State | Zustand | Latest | Client state |
| Frontend Data | TanStack Query | Latest | Server state |
| PWA | vite-plugin-pwa | Latest | Offline support |
| Container | Docker | Latest | Deployment |
| CI/CD | GitHub Actions | N/A | Automation |
| Python Linting | Ruff | Latest | Code quality |
| JS Formatting | Prettier | Latest | Code style |

---

*This timeline document will be updated with each significant development session. It serves as both a changelog and a technical reference for the VitalPath project.*

---

**End of Entry #1**
