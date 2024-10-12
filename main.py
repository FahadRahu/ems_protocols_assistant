import demograph_info
from protocols import GeneralPCP_Adult
import string


def main():
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
    pt_report['Sex'] = pt_sex = demograph_info.pt_sex()
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
print("This is the end")
