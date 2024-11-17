from procedures import other_clinical_procedures


# BOTH Adult and Pediatric Protocols Available:
def bls_adult_medical_allergic_reaction():
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


# Unfinished - Needs functions to refer to many different protocols.
def bls_adult_alt_mental_status_syncope():
    print("Follow the advice consistent with the General Patient Care Protocol - Adult\n")
    print("Obtain Blood Glucose Level - Refer to Medical: Diabetic Emergencies")
    print("Obtain a 12-Lead ECG - \n"
          "If head injury is suspected - refer to Trauma: Head Injuries.\n"
          "If severely agitated and/or violent - refer to Medical: Behavioral Emergencies/Excited Delirium\n"
          "If sepsis is suspected (high in age, high risk for infection, febrile/showing fever symptoms - "
          "refer to - Medical: Sepsis\n"
          "If you suspect poisoning - refer to Overdose and Poisoning: General Approach")

other_clinical_procedures.blood_glucose_analysis()

# ONLY Adult Protocols Available:


# ONLY Pediatric Protocols Available:
