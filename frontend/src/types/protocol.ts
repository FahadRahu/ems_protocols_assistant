/**
 * Protocol type definitions.
 * These MUST mirror backend/app/models/ exactly.
 * Source of truth: shared/schemas/protocol-schema.json
 */

export type ProviderLevel = 'ALL' | 'BLS' | 'ALS' | 'PARAMEDIC' | 'OLMC';
export type PatientType = 'adult' | 'pediatric' | 'neonate' | 'all';
export type Route = 'PO' | 'SL' | 'IV' | 'IO' | 'IM' | 'IN' | 'NEB' | 'ODT' | 'TOPICAL';

export interface MedicalControlContact {
  facility: string;
  phone: string;
  radio_channel?: string;
}

export interface MedicalControl {
  contacts: MedicalControlContact[];
  poison_control: string;
  chemtrec: string;
}

export interface JurisdictionMeta {
  jurisdiction: string;
  version: string;
  effective_date: string;
  revision_date?: string;
  medical_control: MedicalControl;
}

export interface VitalSignCriteria {
  sbp_below?: number;
  sbp_above?: number;
  map_below?: number;
  hr_below?: number;
  hr_above?: number;
  spo2_below?: number;
  gcs_below?: number;
  etco2_below?: number;
  etco2_above?: number;
}

export interface Criteria {
  age_min_months?: number;
  age_max_months?: number;
  symptoms?: string[];
  vital_signs?: VitalSignCriteria;
  exclusions?: string[];
}

export interface MedicationDose {
  medication_id: string;
  dose: string;
  dose_per_kg?: number;
  max_dose?: string;
  route: Route;
  rate?: string;
}

export interface Step {
  order: number;
  provider_level: ProviderLevel;
  action: string;
  medication?: MedicationDose;
  condition?: string;
  contraindications?: string[];
  notes?: string[];
  repeat?: string;
  cross_reference?: string;
}

export interface Protocol {
  id: string;
  title: string;
  category: string;
  patient_type: PatientType;
  tags: string[];
  criteria?: Criteria;
  steps: Step[];
  cross_references?: string[];
}

export interface DosingInfo {
  indication: string;
  dose: string;
  route: string;
  max_dose?: string;
  notes?: string;
}

export interface Medication {
  id: string;
  generic_name: string;
  trade_names: string[];
  drug_class: string;
  mechanism?: string;
  indications: string[];
  contraindications: string[];
  adult_dosing: DosingInfo[];
  pediatric_dosing: DosingInfo[];
}

export interface Procedure {
  id: string;
  title: string;
  procedure_type: string;
  authorized_personnel: string[];
  indications: string[];
  contraindications: string[];
  equipment: string[];
  steps: string[];
}

export interface ProtocolBundle {
  meta: JurisdictionMeta;
  protocols: Protocol[];
  medications: Medication[];
  procedures: Procedure[];
}
