# Patient Demographics
def demographic_choice():
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

# Learning note - Don't call the def function at the end of the script, you do that in the main.py when you use it.
# Trying to call it in this file then importing it over to the main file will just make this start to run first.