from procedures import other_clinical_procedures


# BOTH Adult and Pediatric Protocols Available:
def bls_adult_allergic_reaction():
    """Protocol for altered mental status - needs functions [i.e. was a 12-lead performed? Did you take BGl?]
    :return: Nothing as of right now
    Plans: Need to add functions to return if any interventions were performed.
    """
    print(f"1. Follow the General Patient Care Protocol for Adult patients.\n"
          "2. Assist the patient in self-administration of their prescribed epinephrine auto-injector "
          "(Epi-Pen/Epi-Pen Jr.)\n"
          "3. If wheezing is present: Administer Albuterol 2.5 mg via nebulizer - "
          "repeat once in 5 minutes if indicated")

def bls_pediatric_allergic_reaction():
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


def bls_adult_diabetic_emergencies(local_age_type, bgl):
    """Protocol = Adult Diabetic Emergencies
    Why Unfinished?: Nothing is coded - Need to  add function if Oral Glucose Gel or sugar was administered
    :return: Nothing as of right now
    Plans: Need to code the protocol, need to return whether oral glucose or sugary food/bev was given
    Other Notes: For now, I'll leave it as 'print{whatever the protocol is}' and make it more complex later.
    Hypoglycemia in ALL ADULTS IS <= 60 mg/dL
    Hyperglycemia in ALL ADULTS IS >= 250 mg/dL
    """

    # Skipping the following line since so many protocols say it, repeating it is redundant.
    # print("Follow the General Patient Care Protocol for Adult/Pediatric patients")

    if local_age_type == 'Adult':
        if bgl < 60:
            print('Patient is experiencing Hypoglycemic:\n')
            print('1. Consider administering Oral Glucose Gel 15 g, '
                  'OR glucose containing beverage (e.g. orange-juice).\n'
                  '2. Patient MUST be fully alert/oriented and able to maintain airway to (self)administer gel/drink.')
        elif bgl > 250:
            print('Patient is experiencing Hyperglycemia: \n'
                  'May potentially be experiencing life-threatening condition: Diabetic Ketoacidosis\n\n'
                  '1. Strongly recommend ALS on scene/ALS Intercept if time permits\n'
                  '2. Rapid Transport to hospital if ALS intervention cannot be reached within timely manner. ')
        else:
            print('Patient\'s reported Blood Glucose measurement is a normal range')
    else:
        if local_age_type is None:
            print('Error in bls_adult_diabetic_emergencies function, argument for "local_age_type" is None')
        elif local_age_type is not None:
            print('Error in bls_adult_diabetic_emergencies function, argument for '
                  '"local_age_type" is something other than "Adult"')
        else:
            print('Error in bls_adult_diabetic_emergencies, argument for "local_age_type" did not successfully compute,'
                  'I\'m not sure how you got here.')


def bls_pediatric_diabetic_emergencies(local_age_type, bgl):
    """Protocol = Pediatric Diabetic Emergencies
    Why Unfinished?: Nothing is coded - Need to add function if Oral Glucose Gel or sugar was administered
    :return: Nothing as of right now
    Plans: Need to code the protocol, need to return whether oral glucose or sugary food/bev was given
    Other Notes: For now, I'll leave it as 'print{whatever the protocol is}' and make it more complex later.
    Hypoglycemia in a neonate is <= 40 mg/dL
    Hypoglycemia in ALL OTHER PEDIATRICS is <= 60 mg/dL
    Hyperglycemia in ALL PEDIATRICS is >= 250 mg/dL
    """

    # Skipping the following line since so many protocols say it, repeating it is redundant.
    # print("Follow the General Patient Care Protocol for Adult/Pediatric patients")

    if local_age_type in ['Child', 'Infant']:
        if bgl < 60:
            print('Patient is experiencing Hypoglycemia:\n')
            print('1. Consider administering Oral Glucose Gel 15 g, '
                  'OR glucose containing beverage (e.g. orange-juice) if age-appropriate.\n'
                  '2. Patient MUST be fully alert/oriented and able to maintain airway to (self)administer gel/drink.')
        elif bgl > 250:
            print('Patient is experiencing Hyperglycemia: \n'
                  'May potentially be experiencing life-threatening condition: Diabetic Ketoacidosis\n\n'
                  '1. Strongly recommend ALS on scene/ALS Intercept if time permits\n'
                  '2. Rapid Transport to hospital if ALS intervention cannot be reached within timely manner. ')
        else:
            print('Patient\'s reported Blood Glucose measurement is a normal range')

    elif local_age_type == 'Neonate':
        if bgl < 40:
            print('Patient is experiencing Hypoglycemia: \n')
            print('1. Strongly recommend ALS on scene/ALS Intercept if time permits\n'
                  '2. Rapid Transport to hospital if ALS intervention cannot be reached within timely manner. ')
        elif bgl > 250:
            print('Patient is experiencing Hyperglycemia: \n'
                  'May potentially be experiencing life-threatening condition: Diabetic Ketoacidosis\n\n'
                  '1. Strongly recommend ALS on scene/ALS Intercept if time permits\n'
                  '2. Rapid Transport to hospital if ALS intervention cannot be reached within timely manner. ')
        else:
            print('Patient\'s reported Blood Glucose measurement is a normal range')

    else:
        if local_age_type is None:
            print('Error in bls_pediatric_diabetic_emergencies function, argument for "local_age_type" is None')
        elif local_age_type is not None:
            print('Error in bls_pediatric_diabetic_emergencies function, argument for '
                  '"local_age_type" is something other than "Adult"')
        else:
            print('Error in bls_pediatric_diabetic_emergencies, argument for '
                  '"local_age_type" did not successfully compute,'
                  'I\'m not sure how you got here.')


def bls_adult_seizure():
    """
    Protocol: Medical: Seizure
    :return: Nothing, simple procedure
    Plans: Consider writing how an EMT can treat this type of patient.
    Other Notes:
    """
    print("Protect the patient from injury/injuring themselves.")


def bls_pediatric_seizure():
    """
    Protocol: Medical: Seizure
    :return: Nothing, simple procedure
    Plans: Consider writing how an EMT can treat this type of patient.
    Other Notes:
    """
    print("Protect the patient from injury/injuring themselves. \n"
          "Obtain a Blood Glucose Measurement if you haven\'t already\n"
          "Providing Oxygen via Nasal Cannula (NC) is sufficient so long as patient is not actively seizing "
          "or having signs/sympotoms of respiratory distress.")


# UNFINISHED
def bls_adult_sepsis():
    """
    Protocol: Medical: Sepsis
    :return: Nothing
    Plans: Check existing user data in main.py and base output on that, Sepsis Check Status (Postitive or Negative)
    Other Notes:
    """
    print('Notify hospital of a "CODE SEPSIS" during transport prior to arrival')
    print('To meet sepsis criteria, the patient must meet the following criteria:\n'
          '\t1. Suspected Infection\n'
          '\t2. TWO or more of the following: \n'
          '\t\ta. Fever (>100.4) or Hypothermia (<96.8)\n'
          '\t\tb. Elevated Respiratory Rate (>20)\n'
          '\t\tc. Heart Rate > 90\n'
          '\t\td. ETCO2 < 30 mmHg')


def bls_pediatric_sepsis(age=None, age_type=None):
    """
    Protocol: Medical: Sepsis
    :return: Nothing
    Plans: Check existing user data in main.py and base output on that, Sepsis Check Status (Postitive or Negative)
    Other Notes: Pediatric has age specific vitals - heart rate, resp rate, and blood pressure
    """

    if age_type == 'Neonate':
        patient_age = age / 365
    elif age_type == 'Infant':
        patient_age = age / 12
    elif age_type == 'Child':
        patient_age = age
    else:
        print("Issue with interpreting age_type")
        patient_age = age

    pediatric_vitals = {
        "0D-1W": {"heart_rate": ("<100", ">180"), "resp_rate": ">50", "SBP": "<60"},
        "1W-1M": {"heart_rate": ("<100", ">180"), "resp_rate": ">40", "SBP": "<70"},
        "1M-1Y": {"heart_rate": ("<90", "<180"), "resp_rate": ">34", "SBP": "<70"},
        "2Y-5Y": {"heart_rate": ">140", "resp_rate": ">22", "SBP": "70 + 2*age"},
        "6Y-12Y": {"heart_rate": ">130", "resp_rate": ">18", "SBP": "70 + 2*age"},
        "13Y-<18Y": {"heart_rate": ">110", "resp_rate": ">14", "SBP": "<90"}
    }

    if 0 <= patient_age < 1 / 52:
        age_category = "0D-1W"
    elif 1 / 52 <= patient_age < 1 / 12:
        age_category = "1W-1M"
    elif 1 / 12 <= patient_age < 1:
        age_category = "1M-1Y"
    elif 2 <= patient_age < 5:
        age_category = "2Y-5Y"
    elif 6 <= patient_age < 12:
        age_category = "6Y-12Y"
    elif 13 <= patient_age < 18:
        age_category = "13Y-<18Y"
    else:
        raise ValueError("Age out of pediatric range")

    print('Notify hospital of a "CODE SEPSIS" during transport prior to arrival')
    print('To meet sepsis criteria, the patient must meet the following criteria:\n'
          '\t1. Suspected Infection\n'
          '\t2. TWO or more of the following: \n'
          '\t\ta. Fever (>100.4) or Hypothermia (<96.8)\n'
          '\t\tb. Elevated Respiratory Rate (>20)\n'
          '\t\tc. Heart Rate > 90\n'
          '\t\td. ETCO2 < 30 mmHg\n')

    vitals = pediatric_vitals.get(age_category)

    print(f"Vital signs for age category '{age_category}':")
    for parameter, value in vitals.items():
        if isinstance(value, tuple):
            value = " to ".join(value)  # Format range nicely for tuple values
        print(f"  {parameter.replace('_', ' ').title()}: {value}")

# ONLY Adult Protocols Available:


# ONLY Pediatric Protocols Available:
