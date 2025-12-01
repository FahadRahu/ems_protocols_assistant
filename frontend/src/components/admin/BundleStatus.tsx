/**
 * Bundle Status Component
 * 
 * Shows current bundle version and sync status.
 */

import { useBundleStore } from '../../stores/bundleStore';

export function BundleStatus() {
  const { bundle, isLoading, lastSync, fetchBundle } = useBundleStore();

  return (
    <div className="bg-white dark:bg-vp-dark rounded-lg p-6">
      <h2 className="text-xl font-semibold mb-4">Bundle Status</h2>
      
      {bundle ? (
        <div className="space-y-2 text-sm">
          <p>
            <span className="text-gray-500">Version:</span>{' '}
            <span className="font-mono">{bundle.meta.version}</span>
          </p>
          <p>
            <span className="text-gray-500">Jurisdiction:</span>{' '}
            {bundle.meta.jurisdiction}
          </p>
          <p>
            <span className="text-gray-500">Protocols:</span>{' '}
            {bundle.protocols.length}
          </p>
          <p>
            <span className="text-gray-500">Medications:</span>{' '}
            {bundle.medications.length}
          </p>
          {lastSync && (
            <p>
              <span className="text-gray-500">Last Sync:</span>{' '}
              {lastSync.toLocaleString()}
            </p>
          )}
        </div>
      ) : (
        <p className="text-gray-500">No bundle loaded</p>
      )}

      <button
        onClick={() => fetchBundle()}
        disabled={isLoading}
        className="mt-4 btn-primary w-full"
      >
        {isLoading ? 'Syncing...' : '🔄 Sync Bundle'}
      </button>
    </div>
  );
}
