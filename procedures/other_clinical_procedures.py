def blood_glucose_analysis():
    # This function has 3 functions: relay indications, relay procedure, obtain BGl in mg/dL
    # This DOES NOT evaluate what values mean, that is going to get explained in the medical_protocols.py protocol

    # Establish Indications for procedure as a list
    bgl_indications = ['Known diabetic history',
                       'Altered/Change in mental status, or not showing typical normal behavior',
                       'Patient is suspected to be under the influence of drugs/alcohol, or overdose patients',
                       'Syncopal episode (fainting)',
                       'Seizure',
                       'Stroke or Sepsis',
                       'Liver dysfunction to any degree',
                       'Dialysis Patients',
                       'Provider Discretion']

    # Establish Procedure for taking BGl as a list
    bgl_procedure = ['Gather and prepare equipment - alcohol wipe, lancet, 4x4 gauze (or similar), '
                     'glucometer equipment and strips',
                     'Clean patient sample area with alcohol wipe',
                     'Use lancet - use with great caution - discard in sharps box',
                     'Clean initial blood released with 4x4 gauze pad (or other similar clean pad)',
                     'Place the correct amount of blood on reagent strip/site on '
                     'glucometer per glucometer instructions',
                     'Time the analysis as advised by manufacturer',
                     'Document glucometer reading, treat patient as indicated given measurement \n'
                     '  ---(Consider error if patient symptoms are discordant with readings, '
                     'use different glucometer if necessary)',
                     'Repeat glucose analysis for reassessment after treatment if indicated for change/per protocol']

    # May as well store the following as a variable, we'll be re-using these options frequently
    accepted_responses = ['y', 'n', 'yes', 'no']

    take_bgl_indication_response = input('Would you like to see indications for '
                                         'taking a Blood Glucose Measurement? (y/n): ')
    # Loop to check whether user enters (y/n) for receiving indications
    while True:
        if take_bgl_indication_response.lower() not in accepted_responses:
            take_bgl_indication_response = input('Invalid response, would you like to see '
                                                 'indications for taking a Blood Glucose Measurement? (y/n): ')
            continue
        else:
            break  # <-- Check to see later if 'break' is appropriate to break while loop, is there a better way?

    # Only need the if statement to check whether response was 'y'/'yes', adding 'else' would be redundant
    if take_bgl_indication_response.lower() in ['y', 'yes']:
        print('\nBlood Glucose Analysis Indications:\n')
        n = 1
        for indication in bgl_indications:
            print(str(n) + '.', indication)
            n += 1

    take_bgl_procedure_response = input('\nWould you like to see the procedure for '
                                        'taking a Blood Glucose Measurement? (y/n): ')
    # Same loop as earlier, check whether user enters (y/n) for receiving procedure
    while True:
        if take_bgl_procedure_response.lower() not in accepted_responses:
            take_bgl_procedure_response = input('Invalid response, would you like to see '
                                                'the procedure for taking a Blood Glucose Measurement? (y/n): ')
            continue
        else:
            break

    # Create a for loop to show the procedure if user chooses to see it, used enumerate unlike bgl_indication case
    if take_bgl_procedure_response.lower() in ['y', 'yes']:
        print('\nBlood Glucose Analysis Procedure:\n')
        for i, step in enumerate(bgl_procedure, start=1):
            print(str(i) + '.', step)

    # Third section to check whether user actually obtained a Blood Glucose Measurement
    bgl_measurement_response = input('\nDid you obtain a blood glucose measurement? (y/n): ')
    while True:
        if bgl_measurement_response.lower() not in accepted_responses:
            bgl_measurement_response = input('Invalid response, did you obtain a blood glucose measurement? (y/n): ')
            continue
        else:
            break
    if bgl_measurement_response.lower() in ['y', 'yes']:
        while True:
            bgl_measure = input('What was the Blood Glucose Measurement in mg/dL: ')
            try:
                bgl_measure = float(bgl_measure)
                if 0 <= bgl_measure <= 1000:
                    bgl_measure = round(bgl_measure, 2)
                    print(f'Your reported Blood Glucose is {bgl_measure} mg/dL')
                    break
                else:
                    print('Measurement out of range, this tool only accepts 0-1000 mg/dL\n')
            except ValueError:
                print('Invalid Measurement, please enter an appropriate numerical value \n')
                continue
    else:
        bgl_measure = None

    return bgl_measure
