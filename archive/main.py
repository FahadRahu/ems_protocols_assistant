#!/usr/bin/python

# IMPORTS:

# Python imports
import string
# Primary directory imports
import demograph_info
# Protocols/ directory imports
from protocols import imports as prot_imports, GeneralPCP_Adult

# Procedures/ directory imports
# Shouldn't need "from procedures import other_clinical_procedures"


def main():
    class Patient:

        # Initialize Class - set parameters for object [self] to None
        def __init__(self):
            self.conditions = {}  # <-- This serves as a dictionary for a final patient report

        # Method to add key/value pairs to self.conditions dictionary
        def update_condition(self, key, value):
            self.conditions[key] = value

    # Greet User
    print("Welcome to the Prince William County EMS Protocol Assistant!\n\n"
          "This tool guides users on what procedures and variables to be aware of in the context of their emergency.\n"
          "This tool is incomplete and should not be used as clinical/legal advice/aid in any way\n\n")

    # Create Empty Dict for Patient Info:
    pt_report = {}

    # Nature of the Emergency
    emergency_type = input("Enter the type of emergency: ")
    print('')

    # Patient Demographics
    pt_report['Sex'] = demograph_info.pt_sex()
    pt_report.update(zip(['Global Age Type', 'Local Age Type', 'Age', 'Age Measurement'],
                         demograph_info.pt_age_check()))

    # General Patient Care - Adult
    GeneralPCP_Adult.avpu_check()
    GeneralPCP_Adult.general_cardiac()
    GeneralPCP_Adult.general_respiratory()

    for key, value in pt_report.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    main()
print('')
print("This is the very end")
