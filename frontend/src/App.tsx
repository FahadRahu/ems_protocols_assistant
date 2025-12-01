import { useEffect, useState } from 'react';
import { useBundleStore } from './stores/bundleStore';
import { OfflineStorage } from './services/offlineStorage';

function App() {
  const [isOnline, setIsOnline] = useState(navigator.onLine);
  const { bundle, isLoading, error } = useBundleStore();

  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  return (
    <div className="min-h-screen bg-vp-darker text-white p-4">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-vp-accent">VitalPath</h1>
        <p className="text-gray-400">EMS Clinical Decision Support</p>
        <div className="mt-2 flex items-center gap-2">
          <span
            className={`w-3 h-3 rounded-full ${
              isOnline ? 'bg-vp-success' : 'bg-vp-warning'
            }`}
          />
          <span className="text-sm text-gray-400">
            {isOnline ? 'Online' : 'Offline Mode'}
          </span>
        </div>
      </header>

      <main>
        {isLoading && (
          <div className="text-center py-12">
            <p className="text-gray-400">Loading protocol bundle...</p>
          </div>
        )}

        {error && (
          <div className="bg-vp-danger/20 border border-vp-danger rounded-lg p-4">
            <p className="text-vp-danger">Error: {error}</p>
          </div>
        )}

        {bundle && (
          <div className="space-y-4">
            <div className="bg-vp-dark rounded-lg p-4">
              <h2 className="text-xl font-semibold mb-2">Bundle Info</h2>
              <p className="text-gray-400">
                Jurisdiction: {bundle.meta.jurisdiction}
              </p>
              <p className="text-gray-400">Version: {bundle.meta.version}</p>
              <p className="text-gray-400">
                Protocols: {bundle.protocols.length}
              </p>
            </div>

            <div className="bg-vp-dark rounded-lg p-4">
              <h2 className="text-xl font-semibold mb-2">Medical Control</h2>
              <ul className="space-y-2">
                {bundle.meta.medical_control.contacts.map((contact, idx) => (
                  <li key={idx} className="text-gray-400">
                    <span className="font-medium text-white">
                      {contact.facility}
                    </span>
                    <br />
                    📞 {contact.phone}
                    {contact.radio_channel && ` | 📻 ${contact.radio_channel}`}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}

        {!bundle && !isLoading && !error && (
          <div className="text-center py-12">
            <p className="text-gray-400">No protocol bundle loaded.</p>
            <p className="text-sm text-gray-500 mt-2">
              Connect to the backend to download protocols.
            </p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
