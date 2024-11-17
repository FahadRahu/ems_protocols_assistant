from procedures import (
    admin_procedures as adp,
    other_clinical_procedures as ocp,
    cardiac_clinical_procedures as ccp,
    airway_clinical_procedures as acp
)

# Look into what __all__ does later
# It "exports modules and functions for easy imports elsewhere"
__all__ = [
    "adp",
    "ocp",
    "ccp",
    "acp"
]