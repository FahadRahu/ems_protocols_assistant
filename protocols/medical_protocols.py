from procedures import other_clinical_procedures


# BOTH Adult and Pediatric Protocols Available:
def bls_adult_medical_allergic_reaction():
    """Protocol for altered mental status - needs functions [i.e. was a 12-lead performed? Did you take BGl?]
    :return: Nothing as of right now
    Plans: Need to add functions to return if any interventions were performed.
    """
    print(f"1. Follow the General Patient Care Protocol for Adult patients.\n"
          "2. Assist the patient in self-administration of their prescribed epinephrine auto-injector "
          "(Epi-Pen/Epi-Pen Jr.)\n"
          "3. If wheezing is present: Administer Albuterol 2.5 mg via nebulizer - "
          "repeat once in 5 minutes if indicated")


def bls_pediatric_medical_allergic_reaction():
    print(f"1. Follow the General Patient Care Protocol for Pediatric patients.\n"
          "2. Assist the patient in self-administration of their prescribed epinephrine auto-injector "
          "(Epi-Pen/Epi-Pen Jr.)\n"
          "3. If wheezing is present: Administer Albuterol 2.5 mg via nebulizer - "
          "repeat once in 5 minutes if indicated"
          "4. Do not give the patient anything by mouth.")


# UNFINISHED - Needs functions if any interventions were performed.
def bls_adult_alt_mental_status_syncope():
    """Protocol = Adult Altered Mental Status
    Why Unfinished?: Needs functions [i.e. was a 12-lead performed? Did you take BGl?]
    :return: Nothing as of right now
    Plans: Need to add functions to return if any interventions were performed.
    """

    altered_guide = [
        "Follow the advice consistent with the General Patient Care Protocol - Pediatric",
        "Obtain Blood Glucose Level - Refer to Medical: Diabetic Emergencies",
        "Obtain a 12-Lead ECG",
        "If head injury is suspected - refer to Trauma: Head Injuries.",
        "If severely agitated and/or violent - refer to Medical: Behavioral Emergencies/Excited Delirium",
        "If sepsis is suspected (greater age, high risk for infection, febrile/showing fever symptoms - "
        "refer to - Medical: Sepsis",
        "If you suspect poisoning - refer to Overdose and Poisoning: General Approach"
    ]

    for i, guideline in enumerate(altered_guide, start=1):
        print(f"{i}. {guideline}")


# UNFINISHED - Needs functions if any interventions were performed.
def bls_pediatric_alt_mental_status_syncope():
    """Protocol = Pediatric Altered Mental Status
    Why Unfinished?: Needs functions [i.e. was a 12-lead performed? Did you take BGl?]
    :return: Nothing as of right now
    Plans: Need to add functions to return if any interventions were performed.
    """
    altered_guide = [
        "Follow the advice consistent with the General Patient Care Protocol - Pediatric",
        "Obtain Blood Glucose Level - Refer to Medical: Diabetic Emergencies",
        "Obtain a 12-Lead ECG",
        "If head injury is suspected - refer to Trauma: Head Injuries",
        "If sepsis is suspected (greater age, high risk for infection, febrile/showing fever symptoms - "
        "refer to - Medical: Sepsis",
        "If you suspect poisoning - refer to Pediatric Overdose and Poisoning"
    ]
    for i, guideline in enumerate(altered_guide, start=1):
        print(f"{i}. {guideline}")


def bls_adult_diabetic_emergencies(local_age_type):
    """Protocol = Adult Diabetic Emergencies
    Why Unfinished?: Nothing is coded - Need to add function if Oral Glucose Gel or sugar was administered
    :return: Nothing as of right now
    Plans: Need to code the protocol, need to return whether oral glucose or sugary food/bev was given
    Other Notes: For now, I'll leave it as 'print{whatever the protocol is}' and make it more complex later.
    Hypoglycemia in ALL ADULTS IS <= 60 mg/dL
    Hyperglycemia in ALL ADULTS IS >= 250 mg/dL
    """
    pass


def bls_pediatric_diabetic_emergencies(local_age_type):
    """Protocol = Pediatric Diabetic Emergencies
    Why Unfinished?: Nothing is coded - Need to add function if Oral Glucose Gel or sugar was administered
    :return: Nothing as of right now
    Plans: Need to code the protocol, need to return whether oral glucose or sugary food/bev was given
    Other Notes: For now, I'll leave it as 'print{whatever the protocol is}' and make it more complex later.
    Hypoglycemia in a neonate is <= 40 mg/dL
    Hypoglycemia in ALL OTHER PEDIATRICS is <= 60 mg/dL
    Hyperglycemia in ALL PEDIATRICS is >= 250 mg/dL
    """
    pass

# ONLY Adult Protocols Available:


# ONLY Pediatric Protocols Available:
