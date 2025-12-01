# src/engine.py
"""
Engine to evaluate patient against protocol rules.
Given a Patient, returns list of matched Rules (highest priority first).
    1. Iterate over RULES.
    2. For each rule, check if all predicates (small functions like is_adult, sbp_below(90)) 
        in "when" are True for the patient.
    3. If all predicates pass → that rule “matches.”
    4. Return list of matched rules sorted by priority (highest first).

"""
from typing import List
from domain import Patient
from protocols import RULES

def evaluate_rules(patient: Patient):
    matches = []
    for rule in RULES:
        if all(pred(patient) for pred in rule["when"]):
            matches.append(rule)
    # Sort by priority (desc) so most critical shows first
    matches.sort(key=lambda r: r["priority"], reverse=True)
    return matches
