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
    elif avpu_status == 'U':
        avpu_score = 1
    else:
        print('We failed somehow in the AVPU check, I\'m not sure how you got here')

    print('')
    return avpu_score


def general_cardiac():  # All this checks is if the patient has a pulse

    print('Check for a central pulse.')
    pulse_presence = input('Does the patient have a pulse (Y/N): ')  # Key Variable for function
    pulse_presence = pulse_presence.upper()

    while pulse_presence not in ['Y', 'N']:
        print('Invalid input, enter Y/N\n')
        pulse_presence = input('Does the patient have a pulse (Y/N): ')
        pulse_presence = pulse_presence.upper()

    if pulse_presence == 'N':
        pulse_status = False
        # GO TO CPR - UNCODED PROTOCOL
        print('Refer to Cardiac Arrest: General Approach\n')
        print('Start CPR')
        print('High Performance CPR if indicated - start continuous chest compressions \n'
              'Place Patient on an OPA and NRB at 15 LPM until resources allow \n'
              'Once you have resources (people) available, start positive pressure ventilation with bag-valve mask')
        pass

    elif pulse_presence == 'Y':
        pulse_status = True
        print('')
        print('Assess the patient\'s perfusion: \n'
              'Measure Heart Rate, Skin Color, Capillary Refill, Quality of Pulses')

    else:
        print('This shouldn\'t happen - Error in General Cardiac')

    return pulse_status


def general_respiratory():  # Checks airway_status (boolean), and SpO2 status (int or NoneType)
    # global spo2_status  - <<-- What is the purpose of making this global

    # Check if the Patient has an Intact Airway:
    print('Ensure that the patient\'s airway is intact. \n\n'
          'If the patient is not breathing, consider positive pressure ventilation. \n'
          'Check: Lung Sounds, Respiratory Rate, Work of Breathing, SpO2/EtCO2\n')

    airway_status_check = False

    while not airway_status_check:
        airway_status_input = input('Does the patient have an intact airway? \n'
                                    'Enter Y/N, or "help" for common incubation references: ').strip().upper()
        print('')

        # If User enters 'help'
        if airway_status_input == 'HELP':
            print('Reference Table for Indications for Intubation: \n'
                  'No Signs of Respiratory Failure - Hypoxic or Hypercapic \n'
                  'Apneic \n'
                  'Reduced Level of Consciousness / GCS \u2264 8 \n'
                  'Sudden Change of Mental Status \n'
                  'Airway Injury or Impending Airway Compromise \n'
                  'Risk of Aspiration \n'
                  'Trauma to the Larynx or Penetrating Injuries to Neck, Abdomen, and Chest \n')

        # If the Patient does have an intact airway:
        elif airway_status_input == 'Y':
            spo2_status_fulfillment_check = False

            # All this below is assuming the airway is intact
            while not spo2_status_fulfillment_check:
                spo2_status = input('Enter Patient SpO2% (0-100) or type "help": ').strip()

                if spo2_status.isdigit() and 0 <= int(spo2_status) <= 100:
                    spo2_status = int(spo2_status)
                    spo2_status_fulfillment_check = True

                    if 92 <= spo2_status <= 100:
                        print('Normal SpO2 Range, consider O2 by Nasal Cannula if necessary')
                    elif 90 <= spo2_status < 92:
                        print('Mild Hypoxia - Administer O2 on Nasal Cannula at 2-6 LPM')
                    elif 86 <= spo2_status < 90:
                        print('Moderate Hypoxia - Administer O2 on Non-Rebreather at 12-15 LPM')
                    elif spo2_status < 86:
                        print('Severe Hypoxia - Administer O2 on CPAP/BVM/LTA(King Airway) '
                              'with adjuncts as necessary')
                    else:
                        print('There\'s been an error, try again')
                        spo2_status_fulfillment_check = False
                    print('Always check perfusion and for cyanosis if false SpO2% is suspected. \n')

                elif spo2_status.isalpha():

                    if spo2_status.upper() == 'HELP':
                        print('Reference Table for SpO2 readings: \n\n'
                              '92% - 100%: Normal SpO2 Range, consider O2 by Nasal Cannula if necessary \n'
                              '90% - 91%: Mild Hypoxia - Administer O2 on Nasal Cannula at 2-6 LPM \n'
                              '86% - 89%: Moderate Hypoxia - Administer O2 on Non-Rebreather at 12-15 LPM \n'
                              '<86%: Severe Hypoxia - Administer O2 on CPAP/BVM/LTA(King Airway) '
                              'with adjuncts as necessary \n')
                        # spo2_status_fulfillment_check = False

                    else:
                        print('There\'s been an error, try again \n')
                        # spo2_status_fulfillment_check = False

                else:
                    print('Invalid input, try again\n')

            airway_status = True
            airway_status_check = True
            return airway_status, spo2_status

        # If the patient does not have an intact airway
        elif airway_status_input == 'N':
            print('Intubate Patient: Administer 15 LPM O2 with Bag-Valve-Mask or LTA (King Airway) \n'
                  'Check the patient\'s pulse frequently.\n'
                  'Administer CPR if pulse is weak or absent and if pulse is less than 60 bpm. \n')

            airway_status = False
            airway_status_check = True
            spo2_status = None
            return airway_status, spo2_status

        else:
            print('Broken Code in General Respiratory Block - This shouldn\'t happen')

# 1. ** insert Medical: Allergic Reaction Protocol

# 2. ** insert Clinical Procedure: Selective Spinal Motion Restriction (SSMR)

# 3. ** insert General Patient Care Protocol ‐ Adult Trauma.

# 4. Obtain SAMPLE and OPQRST

# 5. Evaluate	pupillary	reaction,	motor	function,	sensation	and	GCS.

# 6. Assess for the possibility of a stroke

# 7. Record Vitals [LOC, HR, RR, Skin (Color, Condition, Temp), BP, BGL, SPO2, and ETCO2]
# Record Every 5 minutes if pt is critical, or 15 minutes for non-critical

# 8. Consider 12 Lead - Possibly make its own file

# 9. ** insert Clinical Procedure: Blood Glucose Analysis

# 10. ** insert Medical: Diabetic Emergencies - for BOTH hypo/hyperglycemia

# 11. Consider Zofran for nausea

# 12. Consider Naloxone 2mg IN for suspected opiate overdose

# 13. Transport Patient and minimize on-scene time
