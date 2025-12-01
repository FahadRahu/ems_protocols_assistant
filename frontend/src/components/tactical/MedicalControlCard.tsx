/**
 * Medical Control Card Component
 * 
 * Displays OLMC contacts from the bundle.
 * These are DYNAMIC - loaded from JSON, never hardcoded.
 */

import type { MedicalControl } from '../../types/protocol';

interface MedicalControlCardProps {
  medicalControl: MedicalControl;
}

export function MedicalControlCard({ medicalControl }: MedicalControlCardProps) {
  const handleCall = (phone: string) => {
    window.location.href = `tel:${phone.replace(/\D/g, '')}`;
  };

  return (
    <div className="bg-vp-dark rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4 text-vp-accent">
        📞 Medical Control
      </h2>
      
      <div className="space-y-3">
        {medicalControl.contacts.map((contact, idx) => (
          <button
            key={idx}
            onClick={() => handleCall(contact.phone)}
            className="w-full text-left bg-vp-darker hover:bg-vp-darker/70 
                       rounded-lg p-4 transition-colors"
          >
            <div className="font-medium text-white">{contact.facility}</div>
            <div className="text-sm text-gray-400 mt-1">
              📞 {contact.phone}
              {contact.radio_channel && (
                <span className="ml-3">📻 {contact.radio_channel}</span>
              )}
            </div>
          </button>
        ))}
      </div>

      <div className="mt-6 pt-4 border-t border-gray-700 space-y-2">
        <button
          onClick={() => handleCall(medicalControl.poison_control)}
          className="w-full btn-secondary"
        >
          ☠️ Poison Control: {medicalControl.poison_control}
        </button>
        <button
          onClick={() => handleCall(medicalControl.chemtrec)}
          className="w-full btn-secondary"
        >
          ⚗️ CHEMTREC: {medicalControl.chemtrec}
        </button>
      </div>
    </div>
  );
}
