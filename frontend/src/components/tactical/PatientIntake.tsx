/**
 * Patient Intake Component
 * 
 * Step-through wizard for collecting patient information:
 * Demographics → Nature → Complaint → Vitals
 */

import { useState } from 'react';
import type { PatientType } from '../../types/protocol';

interface PatientData {
  ageMonths: number;
  patientType: PatientType;
  chiefComplaint: string;
  symptoms: string[];
  vitals: {
    sbp?: number;
    dbp?: number;
    hr?: number;
    rr?: number;
    spo2?: number;
    gcs?: number;
  };
}

export function PatientIntake() {
  const [step, setStep] = useState(0);
  const [patientData, setPatientData] = useState<Partial<PatientData>>({});

  // TODO: Implement step-through wizard
  return (
    <div className="bg-vp-dark rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Patient Intake</h2>
      <p className="text-gray-400">Step {step + 1} of 4</p>
      {/* TODO: Implement intake form steps */}
    </div>
  );
}
