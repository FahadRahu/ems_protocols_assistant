/**
 * Offline Protocol Matching Engine
 *
 * This is the CORE of VitalPath's offline capability.
 * All matching logic runs locally in the browser using the downloaded JSON bundle.
 *
 * NO API CALLS are made during protocol matching.
 */

import type {
  Protocol,
  ProtocolBundle,
  ProviderLevel,
  PatientType,
} from '../types/protocol';

export interface PatientInput {
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
    temp?: number;
    etco2?: number;
    bgl?: number;
  };
}

export interface MatchedProtocol {
  protocol: Protocol;
  matchScore: number;
  matchReasons: string[];
}

export class ProtocolMatcher {
  private bundle: ProtocolBundle;

  constructor(bundle: ProtocolBundle) {
    this.bundle = bundle;
  }

  /**
   * Find all protocols matching the patient presentation.
   * Returns protocols sorted by relevance score.
   */
  match(input: PatientInput): MatchedProtocol[] {
    const matches: MatchedProtocol[] = [];

    for (const protocol of this.bundle.protocols) {
      const result = this.scoreProtocol(protocol, input);
      if (result.matchScore > 0) {
        matches.push(result);
      }
    }

    // Sort by score descending
    return matches.sort((a, b) => b.matchScore - a.matchScore);
  }

  /**
   * Filter protocol steps by provider certification level.
   * EMT sees only ALL/BLS steps. Paramedic sees all steps.
   */
  filterStepsByLevel(
    protocol: Protocol,
    userLevel: ProviderLevel
  ): Protocol {
    const levelHierarchy: Record<ProviderLevel, number> = {
      ALL: 0,
      BLS: 1,
      ALS: 2,
      PARAMEDIC: 3,
      OLMC: 4,
    };

    const userLevelNum = levelHierarchy[userLevel];

    return {
      ...protocol,
      steps: protocol.steps.filter((step) => {
        const stepLevelNum = levelHierarchy[step.provider_level];
        // User can see steps at or below their level
        // Exception: OLMC steps are always visible (need to know when to call)
        return stepLevelNum <= userLevelNum || step.provider_level === 'OLMC';
      }),
    };
  }

  private scoreProtocol(
    protocol: Protocol,
    input: PatientInput
  ): MatchedProtocol {
    let score = 0;
    const reasons: string[] = [];

    // Patient type match (required)
    if (
      protocol.patient_type !== 'all' &&
      protocol.patient_type !== input.patientType
    ) {
      return { protocol, matchScore: 0, matchReasons: [] };
    }

    // Tag/symptom matching
    const inputTerms = [
      input.chiefComplaint.toLowerCase(),
      ...input.symptoms.map((s) => s.toLowerCase()),
    ];

    for (const tag of protocol.tags) {
      if (inputTerms.some((term) => term.includes(tag) || tag.includes(term))) {
        score += 10;
        reasons.push(`Matches tag: ${tag}`);
      }
    }

    // Criteria matching
    if (protocol.criteria) {
      // Age criteria
      if (
        protocol.criteria.age_min_months &&
        input.ageMonths >= protocol.criteria.age_min_months
      ) {
        score += 5;
      }

      // Vital sign criteria
      if (protocol.criteria.vital_signs && input.vitals) {
        const vs = protocol.criteria.vital_signs;

        if (vs.sbp_below && input.vitals.sbp && input.vitals.sbp < vs.sbp_below) {
          score += 15;
          reasons.push(`SBP ${input.vitals.sbp} < ${vs.sbp_below}`);
        }
        if (
          vs.spo2_below &&
          input.vitals.spo2 &&
          input.vitals.spo2 < vs.spo2_below
        ) {
          score += 15;
          reasons.push(`SpO2 ${input.vitals.spo2}% < ${vs.spo2_below}%`);
        }
      }

      // Symptom criteria
      if (protocol.criteria.symptoms) {
        for (const symptom of protocol.criteria.symptoms) {
          if (inputTerms.some((term) => term.includes(symptom))) {
            score += 8;
            reasons.push(`Symptom match: ${symptom}`);
          }
        }
      }
    }

    return { protocol, matchScore: score, matchReasons: reasons };
  }

  /**
   * Get Medical Control contact for the jurisdiction.
   * This is DYNAMIC - loaded from the bundle, never hardcoded.
   */
  getMedicalControl() {
    return this.bundle.meta.medical_control;
  }

  /**
   * Get bundle version info.
   */
  getBundleInfo() {
    return {
      jurisdiction: this.bundle.meta.jurisdiction,
      version: this.bundle.meta.version,
      effectiveDate: this.bundle.meta.effective_date,
    };
  }
}
