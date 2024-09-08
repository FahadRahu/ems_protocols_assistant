# General Patient Care Protocol - Adult
def avpu_check():
    print('Input the mental status of the patient:\n'
          'A = Alert & Oriented: Patient is Awake and Alert \n'
          'V = Verbal: Patient Responds to Verbal Stimulus \n'
          'P = Pain: Patient Responds to Painful Stimulus \n'
          'U = Unresponsive: Patient Responds to Unresponsive Stimulus \n')
    avpu_status = input('Enter Patient Mental Status (A/V/P/U): ')
    avpu_status = avpu_status.upper()
    while avpu_status not in ['A', 'V', 'P', 'U']:
        print('Invalid input, enter A/V/P/U\n')
        avpu_status = input('Enter Patient Mental Status (A/V/P/U): ')
        avpu_status = avpu_status.upper()
    if avpu_status == 'A':
        avpu_score = 4
    elif avpu_status == 'V':
        avpu_score = 3
    elif avpu_status == 'P':
        avpu_score = 2
    else:
        avpu_score = 1


def general_cardiac():
    print('Check for a central pulse.')
    pulse_presence = input('Does the patient have a pulse (Y/N): ')
    pulse_presence = pulse_presence.upper()
    while pulse_presence not in ['Y', 'N']:
        print('Invalid input, enter Y/N\n')
        pulse_presence = input('Does the patient have a pulse (Y/N): ')
        pulse_presence = pulse_presence.upper()
    if pulse_presence == 'N':
        # GO TO CPR - UNCODED PROTOCOL
        print('Refer to Cardiac Arrest: General Approach\n')
        print('Start CPR')
        print('High Performance CPR if indicated - start continuous chest compressions \n'
              'Place Patient on an OPA and NRB at 15 LPM until resources allow \n'
              'Once you have resources (people) available, start positive pressure ventilation with bag-valve mask')
        return
    else:
        print('')
        print('Assess the patient\'s perfusion: \n'
              'Measure Heart Rate, Skin Color, Capillary Refill, Quality of Pulses')


def general_respiratory():
    global spo2_status
    print('Ensure that the patient\'s airway is intact. \n\n'
          'If the patient is not breathing, consider positive pressure ventilation. \n'
          'Check: Lung Sounds, Respiratory Rate, Work of Breathing, SpO2/EtCO2\n')
    spo2_status_fulfillment_check = False
    print('Enter Patient\'s SpO2 percentage as an integer (0-100). \n'
          'Type "help" for SpO2 table, to skip this step, if patient is not hypoxic, enter "100"\n'
          'If you suspect a False SpO2 reading, check perfusion and for cyanosis, '
          'and consider administering O2\n')
    # All this below is assuming the airway is intact
    while not spo2_status_fulfillment_check:
        spo2_status = input('Enter Patient SpO2%: ')
        if spo2_status.isdigit() and 0 <= int(spo2_status) <= 100:
            spo2_status_fulfillment_check = True
            spo2_status = int(spo2_status)
            if 92 <= spo2_status <= 100:
                print('Normal SpO2 Range, consider O2 by Nasal Cannula if necessary')
            elif 90 <= spo2_status < 92:
                print('Mild Hypoxia - Administer O2 on Nasal Cannula at 2-6 LPM')
            elif 86 <= spo2_status < 90:
                print('Moderate Hypoxia - Administer O2 on Non-Re-breather at 12-15 LPM')
            elif spo2_status < 86:
                print('Severe Hypoxia - Administer O2 on CPAP/BVM/LTA(King Airway) with adjuncts as necessary')
            else:
                print('There\'s been an error, try again')
                spo2_status_fulfillment_check = False
        elif spo2_status.isalpha():
            if spo2_status.upper() == 'HELP':
                print('Reference Table for SpO2 readings: \n\n'
                      '92% - 100%: Normal SpO2 Range, consider O2 by Nasal Cannula if necessary \n'
                      '90% - 91%: Mild Hypoxia - Administer O2 on Nasal Cannula at 2-6 LPM \n'
                      '86% - 89%: Moderate Hypoxia - Administer O2 on Non-Re-breather at 12-15 LPM \n'
                      '<86%: Severe Hypoxia - Administer O2 on CPAP/BVM/LTA(King Airway) with adjuncts as necessary '
                      '\n')
                # spo2_status_fulfillment_check = False
            else:
                print('There\'s been an error, try again \n')
                # spo2_status_fulfillment_check = False
        else:
            print('Invalid input, try again\n')
