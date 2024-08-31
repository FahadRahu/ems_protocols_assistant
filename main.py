import demograph_info

import string


def main():
    # Greet User
    print("Welcome to the Prince William County EMS Protocol Assistant.\n"
          "This tool guides users on what procedures and variables to be aware of in the context of their emergency.\n"
          "This tool is incomplete and should not be used as clinical/legal advice/aid in any way\n\n")

    emergency_type = input("Enter the type of emergency: ")  # Nature of the Emergency
    demograph_info.demographic_choice() # Patient Demographics


if __name__ == "__main__":
    main()
print("This is the end")
