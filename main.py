import demograph_info

import string


def main():
    # Greet User
    print("Welcome to the Prince William County EMS Protocol Assistant.\n"
          "This tool guides users on what procedures and variables to be aware of in the context of their emergency.\n"
          "This tool is incomplete and should not be used as clinical/legal advice/aid in any way\n\n")

    # Nature of the Emergency
    emergency_type = input("Enter the type of emergency: ")
    print('')

    # Patient Demographics
    demograph_info.pt_sex()
    demograph_info.pt_age_check()


if __name__ == "__main__":
    main()
print("This is the end")
