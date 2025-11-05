# main.py (simple CLI MVP)
from src.domain import Patient, Vitals, AgeGroup, Complaint
from src.engine import evaluate_rules

def ask_yes_no(prompt: str) -> bool:
    return input(f"{prompt} (y/n): ").strip().lower().startswith("y")

def ask_int(prompt: str):
    txt = input(f"{prompt} (blank to skip): ").strip()
    return int(txt) if txt else None

if __name__ == "__main__":
    # Minimal interactive flow (expand later)
    is_adult = ask_yes_no("Is the patient an adult?")
    complaint_map = {
        "1": Complaint.CHEST_PAIN,
        "2": Complaint.STROKE,
        "3": Complaint.TRAUMA,
        "4": Complaint.DIFFICULTY_BREATHING,
        "": Complaint.UNKNOWN
    }
    print("Chief complaint: [1] Chest pain  [2] Stroke  [3] Trauma  [4] Difficulty breathing")
    complaint = complaint_map.get(input("Choose: ").strip(), Complaint.UNKNOWN)

    vitals = Vitals(
        hr=ask_int("HR"),
        rr=ask_int("RR"),
        sbp=ask_int("Systolic BP"),
        spo2=ask_int("SpO2"),
        gcs=ask_int("GCS"),
    )

    p = Patient(
        age_group=AgeGroup.ADULT if is_adult else AgeGroup.PEDIATRIC,
        complaint=complaint,
        vitals=vitals,
        is_unresponsive=ask_yes_no("Is the patient unresponsive?"),
        has_chest_pain=(complaint == Complaint.CHEST_PAIN),
        has_focal_neuro_deficit=ask_yes_no("Focal neuro deficit present?"),
    )

    matches = evaluate_rules(p)
    if not matches:
        print("\nNo specific protocol matched. Use general assessment and transport per local guidelines.")
    else:
        print("\nRecommended Protocol(s) (highest priority first):\n")
        for r in matches:
            print(f"▶ {r['name']}")
            for step in r["then"]:
                print(f"  - {step}")
            print()
