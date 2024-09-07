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
    print('Ensure that the patient\'s airway is intact. \n'
          'If the patient is not breathing, consider positive pressure ventilation. \n\n'
          'Check: Lung Sounds, Respiratory Rate, Work of Breathing, SpO2/EtCO2')
    spo2_status_fulfillment_check = False
    while not spo2_status_fulfillment_check:
        spo2_status = input('Enter Patient\'s SpO2 as a percentage (0-100). \n'
                            'If you need a table of the meaning of different value, type "help" \n'
                            'If you would like to skip this step, and the patient is not hypoxic, enter "100" \n\n'
                            'Enter patient SpO2:')