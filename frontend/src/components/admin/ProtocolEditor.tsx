/**
 * Protocol Editor Component
 * 
 * Admin interface for editing protocols.
 * Used at the station for protocol management.
 */

import type { Protocol } from '../../types/protocol';

interface ProtocolEditorProps {
  protocol?: Protocol;
  onSave: (protocol: Protocol) => void;
  onCancel: () => void;
}

export function ProtocolEditor({ protocol, onSave, onCancel }: ProtocolEditorProps) {
  // TODO: Implement protocol editing form
  return (
    <div className="bg-white dark:bg-vp-dark rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">
        {protocol ? 'Edit Protocol' : 'New Protocol'}
      </h2>
      <p className="text-gray-500 dark:text-gray-400">
        Protocol editor coming soon...
      </p>
      <div className="mt-6 flex gap-4">
        <button onClick={onCancel} className="btn-secondary">
          Cancel
        </button>
        <button onClick={() => {}} className="btn-primary">
          Save Protocol
        </button>
      </div>
    </div>
  );
}
