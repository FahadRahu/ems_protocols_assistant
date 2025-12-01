# VitalPath

**Offline-First Clinical Decision Support System for EMS**

VitalPath transforms the Prince William County Patient Care Manual into a real-time, offline-capable clinical decision support tool for EMS providers.

## 🏗️ Architecture

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

## 📁 Project Structure

```
VitalPath/
├── backend/          # FastAPI CMS & JSON Compiler
├── frontend/         # React PWA (Tactical Interface)
├── shared/           # JSON Schema (source of truth)
├── data/             # Raw protocols & compiled bundles
├── archive/          # Legacy code (preserved)
└── docs/             # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- Docker & Docker Compose (optional)

### Development

**Backend:**
```bash
cd backend
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**With Docker:**
```bash
docker compose up
```

## 📋 Key Features

- **Offline-First**: Works without network after initial bundle download
- **Provider-Level Filtering**: EMT vs Paramedic scope of practice
- **Dynamic Medical Control**: OLMC contacts loaded from JSON, never hardcoded
- **Tactical Interface**: Dark mode, large touch targets for field use
- **PWA**: Installable on mobile devices

## 📖 Documentation

- [Development Plan](vitalpath_plan.md) - Comprehensive development roadmap
- [Design Document](outline.md) - Architecture and stack decisions
- [Protocol Source](data/raw/protocol_context.md) - PWC Patient Care Manual

## 🧪 Testing

```bash
# Backend
cd backend && pytest tests/ -v

# Frontend
cd frontend && npm test
```

## 📄 License

Proprietary - Prince William County Fire & Rescue

---

## Legacy Documentation

> **Note:** The content below is from the original prototype and is preserved for reference.
> The new architecture uses a different structure. See `archive/` for legacy code.

        a. There are ups and downs to using this method instead of 3B:

            I. Benefits:
                i. You have access to ANY AND ALL functions in procedures/import.py
                ii. It's more consistent since everything is prefaced as
                    {shorter_name_for_imports.py}.{shorter_name_for_file_name_in_procedures/}.{function_name}
                    shorter_name_for_imports.py = STAYS THE SAME THE ENTIRE TIME WHEN REFERENCING
                    shorter_name_for_file_name_in_procedures/ = NAME OF FILE THE FUNCTION YOU WANT TO CALL IS FROM
                    function_name = SIMPLY THE NAME OF THE FUNCTION YOU ARE CALLING
                iii. Better for scalability - If I end up adding more functions to procedures/{file_name}.py,
                        it's automatically imported to protocols/{file_name}.py

            II. Disadvantages:
                i. Less Explicit and Less Clear to developer looking at a file in protocols/
                    1. For example, if you are looking at medical_protocols.py, it's not super clear where functions
                        are coming from, you'd likely have to look at procedures/import.py to understand what's going on
                ii. You CANNOT have any functions with the same name in any file located in the protocols directory
                    1. To be honest, I'm not entirely sure if that's true, but with everything consolidated,
                        functions should all have their own independent name, that's the plan to begin with,
                        but if you have very basic functions to do something, it's name needs to be unique.
                iii. Importing entire modules can increase the amount of memory you use, decreasing performance.

        b. I'll likely end up using this system to begin with, but I'll add an alternative option in 3B. Using this
            method allows me to import the entire module rather than independently typing every function I use,
            it's also great for scaleability if I add more functions to a file in procedures/

        c. ALTERNATIVE - DIRECT CALLING METHOD:

            I. Instead of calling as:
            (from 'procedures' import 'imports' as {shorter_name_for_procedure/imports.py})
                i. This forces you to call functions as
                {shorter_name_for_procedure/imports.py}.{shorter_name_for_file_name_in_procedures/}.{function_name}
                for example - proc_imports.ocp.blood_glucose_analysis()

            II. NEW METHOD OF DIRECT ACCESS CALLING:
            (from procedures.imports import {shorter_name_for_file_name_in_procedures/.py})
            For example - from procedures.imports import ocp
                i. This forces you to call functions as
                {shorter_name_for_file_name_in_procedures/.py}.{function_name}
                for example - ocp.blood_glucose_analysis()

    B. To utilize specific functions from procedures/{file_name}.py instead of importing the entire module,
        you need to use this format on your protocols/{file_name}.py:
        (from 'procedures.imports' import {function_name}, {shorter_name_for_protocols/file_name.py}
        ****Keep in mind, you need to use the short name you chose for the FILE, NOT the imports.py ^^^^^^^

        a. Benefits and Disadvantages:

            I. Advantages:
                i. Decrease Memory Footprint - it marginally improves performance, possibly boosts performance
                ii. Easy to call functions - You just write the function name, it's as simple as that
                    1. i.e. if you have a function in "other_clinical_procedures.py" located in procedures/
                        called "blood_glucose_analysis()", instead of prefacing with so many words like 3A, you
                        just type "blood_glucose_analysis()" and the function is called!

            II. Disadvantages:
                i. Read 3-A-a-I
                ii. The biggest issue is scalability, though it's not truly THAT big of a concern, you would just need
                    to always add a new line to protocols/{file_name}.py importing the new function you wrote in
                    procedures/{file_name}.py

4. [protocols/imports.py]: Consolidate all the protocol files and their functions here, this is the PRIMARY
    imports.py file we call on main.py

    A. To import PARTICULAR FUNCTIONS - USE THE FOLLOWING FORMAT:

        from protocols.{file_name} import ({function_1}, {function_2}, {function_3}, etc.)

        for example - if you want PARTICULAR FUNCTIONS in protocols/{file_name} imported -
        ON PROTOCOLS/IMPORT.PY YOU WRITE:

        from protocols.medical import (
            abdominal_pain,
            allergic_reaction,
            diabetic_emergencies,
        )
        (calling this function on main.py is simple, you literally just call the function name, no preface)

    B. To import THE ENTIRE MODULE - USE THE FOLLOWING FORMAT:

        from protocols import {file_name} ****optional: you can use "as" to shorten file_names

        for example, if you want to import the ENTIRE MODULE - ON PROTOCOLS/IMPORT.PY YOU WRITE:
        from protocols import medical_protocols

        (calling this function on main.py is longer:
        if on main.py you import the entire protocols/imports.py as:
        (from protocols import imports as prot_imports)
        you would have to call it in main.py as:
        (prot_imports.medical.bls_adult_alt_mental_status_syncope())

    C. Consider adding an __all__ variable, it's supposed to make imports easy into main.py, though, this is for
        importing particular functions.

        # Export the modules and functions - this supposedly makes for easy imports in main.py
        __all__ = [
            "medical",
            "bls_adult_alt_mental_status_syncope",
            etc.
            ]

5. [main.py]: Finally, import you primary imports.py file for access to everything

    A. Use this format:
        from 'protocols' import 'imports' as prot_imports.

        a. To call a function it's long, but this is what you'd write:
            prot_imports.medical.bls_adult_alt_mental_status_syncope()