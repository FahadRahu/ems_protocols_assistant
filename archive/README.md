# Archive

This directory contains legacy code from the initial prototype phase. These files are preserved for reference but are **no longer active** in the new architecture.

## Contents

- `protocols/` - Original Python protocol definitions
- `procedures/` - Original Python procedure functions
- `src/` - Original domain models and rules engine
- `main.py` - Original CLI entry point
- `demograph_info.py` - Original demographic collection
- `tests/` - Original test files
- `utils/` - Original utility functions
- `protocols.yaml` - Original YAML-based rules

## Why Archived?

The project has transitioned from a Python-only CLI tool to a **Smart Client** architecture:

1. **Backend** (FastAPI) - Protocol CMS and JSON compiler
2. **Frontend** (React PWA) - Offline-first clinical interface

The new architecture enables:
- True offline capability via Service Workers
- Mobile-friendly tactical interface
- Separation of concerns (data management vs clinical logic)

## Reference

If you need to understand the original domain model or protocol logic, these files provide helpful context. The core concepts (Patient, Vitals, Protocol steps) remain similar but are now implemented across Python (backend) and TypeScript (frontend).
