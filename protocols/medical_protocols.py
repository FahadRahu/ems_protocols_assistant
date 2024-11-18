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


def bls_adult_diabetic_emergencies(local_age_type, bgl):
    """Protocol = Adult Diabetic Emergencies
    Why Unfinished?: Nothing is coded - Need to add function if Oral Glucose Gel or sugar was administered
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


# ONLY Adult Protocols Available:


# ONLY Pediatric Protocols Available:
