# Shared Schemas

This directory contains the JSON Schema definitions that serve as the **single source of truth** for data structures across the VitalPath project.

## Files

- `protocol-schema.json` - The complete protocol bundle schema

## Usage

### Python (Backend)
The Pydantic models in `backend/app/models/` are derived from this schema and should mirror it exactly.

### TypeScript (Frontend)
The TypeScript interfaces in `frontend/src/types/protocol.ts` are derived from this schema and should mirror it exactly.

## Validation

To validate a protocol bundle against this schema:

```bash
# Using ajv-cli
npx ajv validate -s protocol-schema.json -d ../data/compiled/pwc_protocols_v2019_1.json
```

## Making Changes

1. Update `protocol-schema.json` first
2. Update `backend/app/models/*.py` to match
3. Update `frontend/src/types/protocol.ts` to match
4. Run tests to ensure consistency
