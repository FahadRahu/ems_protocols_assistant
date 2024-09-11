# Patient Demographics
def pt_age_check():
    print('Patient Age:\n'
          'If the patient is \u2264 1-Year\'s-old: \n'
          'Type the letter "I" for Infant (Aged 1 month - 12 months) or '
          '"N" for Neonate (0 - 1 month old) respectively. \n')
    pt_age_fulfillment_check = False
    while not pt_age_fulfillment_check:
        pt_age = input('Enter Patient\'s Age: ')
        if pt_age.isdigit():  # Check to see if the input is numeric
            pt_age = int(pt_age)
            if pt_age >= 18:
                pt_age_type_global = 'Adult'
                pt_age_type_local = 'Adult'
                pt_age_fulfillment_check = True
            elif 1 <= pt_age < 18:
                pt_age_type = 'Pediatric'
                pt_age_type_local = 'Child'
                pt_age_fulfillment_check = True
        elif pt_age.isalpha():  # Check to see if input is a letter
            if pt_age.upper() == 'I' or pt_age.upper() == 'INF' or pt_age.upper() == 'INFANT':
                pt_age_type_global = 'Pediatric'
                pt_age_type_local = 'Infant'
                pt_age_fulfillment_check = True
                pt_age_month_check = False
                print('')
                pt_age_months = input('Enter Patient\'s Age in Months: ')
                while not pt_age_month_check:
                    if pt_age_months.isdigit():
                        pt_age_months = int(pt_age_months)
                        if 1 <= pt_age_months <= 12:
                            pt_age_month_check = True
                        else:
                            print('Patient\'s Age in months must be between 1 and 12\n')
                            pt_age_months = input('Enter Patient\'s Age in Months: ')
                    elif ValueError:
                        print('Invalid input, please put how old the infant is in months from 1 - 12\n')
                        pt_age_months = input('Enter Patient\'s Age in Months: ')
                    else:
                        print('There\'s been an error, please enter the '
                              'patient\'s Age in months must be between 1 and 12\n')
                print('done')
            elif pt_age.upper() == 'N' or pt_age.upper() == 'NEO' or pt_age.upper() == 'NEONATE':
                pt_age_type_global = 'Pediatric'
                pt_age_type_local = 'Neonate'
                pt_age_fulfillment_check = True
            else:
                print('Invalid input. Please enter "I", "N", or valid age.\n')
                continue
        else:
            print('Invalid input. Please enter "I", "N", or valid age.\n')
            continue
    print('')


def pt_sex():  # Patient's sex (M/F) THIS WORKS
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
