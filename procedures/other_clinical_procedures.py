def blood_glucose_analysis():
    bgl_indications = ['Known diabetic history',
                       'Altered/Change in mental status, or not showing typical normal behavior',
                       'Patient is suspected to be under the influence of drugs/alcohol, or overdose patients',
                       'Syncopal episode (fainting)',
                       'Seizure',
                       'Stroke or Sepsis',
                       'Liver dysfunction to any degree',
                       'Dialysis Patients',
                       'Provider Discretion']
    print('Blood Glucose Analysis Indications:\n')
    n = 1
    for indication in bgl_indications:
        print(str(n) + '.', indication)
        n += 1
blood_glucose_analysis()