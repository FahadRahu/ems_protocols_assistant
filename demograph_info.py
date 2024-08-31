# Patient Demographics
def demographic_choice():

    def global_age_data(): # All Patient Age Related Questions Here
        print('Is the patient less than or equal to 1 Years Old?')
        neo_or_inf_check = input('Enter Y/N: ')
        while neo_or_inf_check not in ['Y', 'y','yes' 'N', 'n', 'no']:
            print('Please enter Y/N')
            neo_or_inf_check = input('Enter Y/N: ')
        if neo_or_inf_check in ['Y', 'y', 'yes']:
            neo_or_inf_check = True

        def age_number_months():
        def age_number_years(): # Get the age of the patient in years (Not Neonate or Infant >= 1-Year-Old
            """
This function is only utilized if the patient is a Child or Adult - Neonate and Infants are special exceptions
            """
            age_of_pt = (input("Enter age of patient: "))
            print('')
            try:
                age_of_pt = int(age_of_pt)
            except ValueError:
                print('Please enter the age as a whole number')
                age_of_pt = input('Enter age again: ')
                print('')
                while not isinstance(age_of_pt, int):  # First time using 'isinstance()' replaced from type != int
                    print('Please enter an integer.')
                    age_of_pt = input('Enter age again: ')
                    print('')
                    try:
                        age_of_pt = int(age_of_pt)
                    except ValueError:
                        pass
            finally:
                print(f'Patient Age: {age_of_pt}')     
        age_number_years()

    global_age_data()

    def pt_sex():  # Patient's sex (M/F)
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
        return sex_of_pt

    pt_sex()


demographic_choice()

# Learning note - Don't call the def function at the end of the script, you do that in the main.py when you use it.
# Trying to call it in this file then importing it over to the main file will just make this start to run first.

# Unused/Disabled Code:

# Earlier Placed at Line 3: (Gives user the option to choose to add demographic info or not - now its required)
# print('Are you willing to enter patient demographics?')
# demographic_choice = input('Enter Y/N: ')
# while demographic_choice.upper() not in ['Y', 'y', 'N', 'n']:
# demographic_choice = input('There was an issue with the input, enter Y/N: ')
# if demographic_choice == 'Y' or demographic_choice == 'y':
# print('')
# ...
# elif demographic_choice == 'N' or demographic_choice == 'n':
# print('No problem, let\'s move on. ')
# else:
# print('There\'s an error with the input, let\'s move on. ')
