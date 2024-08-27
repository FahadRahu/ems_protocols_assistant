# Import modules from protocols/ and data/
import string


def main():
    # Greet User
    print("Welcome to the Prince William County EMS Protocol Assistant.\n"
          "This tool guides users on what procedures and variables to be aware of in the context of their emergency.\n"
          "This tool is incomplete and should not be used as clinical/legal advice/aid in any way\n\n")

    # Nature of the Emergency
    # Import types of emergency identity from protocols
    emergency_type = input("Enter the type of emergency: ")

    # Patient Demographics - definitely throw this in a separate file and just import it later
    def demographic_info():
        print('Are you willing to enter patient demographics?')
        demographic_choice = input('Enter Y/N: ')
        while demographic_choice.upper() not in ['Y', 'y', 'N', 'n']:
            demographic_choice = input('There was an issue with the input, enter Y/N: ')
        if demographic_choice == 'Y' or demographic_choice == 'y':
            print('')
            sex_of_pt = str(input('Is the patient Male or Female?\n'
                                  '(Enter Male/Female or M/F): '))
            print('')
            while sex_of_pt not in ['Male', 'male', 'Female', 'female', 'M', 'm', 'F', 'f']:
                sex_of_pt = input('There was an error with the input, please enter the patient\'s sex again.\n'
                                  'Enter Male/Female or M/F: ')
                print('')
            if sex_of_pt in ['Male', 'male', 'M', 'm']:
                sex_of_pt = 'Male'
            elif sex_of_pt in ['Female', 'female', 'F', 'f']:
                sex_of_pt = 'Female'
        elif demographic_choice == 'N' or demographic_choice == 'n':
            print('No problem, let\'s move on. ')
        else:
            print('There\'s an error with the input, let\'s move on. ')
    demographic_info()


if __name__ == "__main__":
    main()
print("This is the end")
