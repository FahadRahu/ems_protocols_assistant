# Data Directory

This directory contains raw protocol data and compiled JSON bundles.

## Structure

```
data/
├── raw/                    # Source documents
│   └── protocol_context.md # PWC Patient Care Manual (raw text)
├── compiled/               # Output bundles (generated)
│   └── pwc_protocols_v*.json
└── README.md
```

## Workflow

1. **Raw data** is placed in `raw/`
2. Run ingestion script: `python -m backend.scripts.ingest_protocols`
3. Compiled bundles are output to `compiled/`
4. Frontend downloads bundle from API endpoint

## Notes

- Never edit files in `compiled/` directly
- The `protocol_context.md` is the source of truth for all medical content
- Version numbers follow the PCM revision dates
