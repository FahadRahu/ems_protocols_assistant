/**
 * Pediatric Dose Calculator
 *
 * Calculates weight-based dosing for pediatric patients.
 * Uses Broselow tape logic where applicable.
 */

import type { MedicationDose, Medication } from '../types/protocol';

export interface DoseResult {
  calculatedDose: string;
  maxDose?: string;
  warnings: string[];
}

export class DoseCalculator {
  private medications: Map<string, Medication>;

  constructor(medications: Medication[]) {
    this.medications = new Map(medications.map((m) => [m.id, m]));
  }

  /**
   * Calculate pediatric dose based on weight.
   */
  calculatePediatricDose(
    medicationDose: MedicationDose,
    weightKg: number
  ): DoseResult {
    const warnings: string[] = [];

    if (!medicationDose.dose_per_kg) {
      return {
        calculatedDose: medicationDose.dose,
        maxDose: medicationDose.max_dose,
        warnings: ['No weight-based dosing available'],
      };
    }

    const calculatedMg = medicationDose.dose_per_kg * weightKg;
    let finalDose = calculatedMg;

    // Check against max dose
    if (medicationDose.max_dose) {
      const maxMg = this.parseDose(medicationDose.max_dose);
      if (calculatedMg > maxMg) {
        finalDose = maxMg;
        warnings.push(`Dose capped at max: ${medicationDose.max_dose}`);
      }
    }

    return {
      calculatedDose: `${finalDose.toFixed(1)} mg`,
      maxDose: medicationDose.max_dose,
      warnings,
    };
  }

  /**
   * Get medication info by ID.
   */
  getMedication(medicationId: string): Medication | undefined {
    return this.medications.get(medicationId);
  }

  private parseDose(doseString: string): number {
    const match = doseString.match(/(\d+\.?\d*)/);
    return match ? parseFloat(match[1]) : 0;
  }
}
