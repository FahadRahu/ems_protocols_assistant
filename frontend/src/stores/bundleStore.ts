/**
 * Bundle Store
 *
 * Zustand store for managing the protocol bundle state.
 */

import { create } from 'zustand';
import type { ProtocolBundle } from '../types/protocol';
import { offlineStorage } from '../services/offlineStorage';

interface BundleState {
  bundle: ProtocolBundle | null;
  isLoading: boolean;
  error: string | null;
  lastSync: Date | null;

  // Actions
  loadBundle: () => Promise<void>;
  fetchBundle: () => Promise<void>;
  clearBundle: () => Promise<void>;
}

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const useBundleStore = create<BundleState>((set, get) => ({
  bundle: null,
  isLoading: false,
  error: null,
  lastSync: null,

  /**
   * Load bundle from IndexedDB (offline storage)
   */
  loadBundle: async () => {
    set({ isLoading: true, error: null });
    try {
      const bundle = await offlineStorage.loadBundle();
      set({ bundle, isLoading: false });
    } catch (err) {
      set({
        error: err instanceof Error ? err.message : 'Failed to load bundle',
        isLoading: false,
      });
    }
  },

  /**
   * Fetch bundle from API and save to IndexedDB
   */
  fetchBundle: async () => {
    set({ isLoading: true, error: null });
    try {
      const response = await fetch(`${API_BASE}/api/v1/bundles/latest`);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      const bundle: ProtocolBundle = await response.json();

      // Save to IndexedDB for offline access
      await offlineStorage.saveBundle(bundle);

      set({ bundle, isLoading: false, lastSync: new Date() });
    } catch (err) {
      // If fetch fails, try loading from cache
      const cached = await offlineStorage.loadBundle();
      if (cached) {
        set({
          bundle: cached,
          isLoading: false,
          error: 'Using cached bundle (offline)',
        });
      } else {
        set({
          error: err instanceof Error ? err.message : 'Failed to fetch bundle',
          isLoading: false,
        });
      }
    }
  },

  /**
   * Clear the stored bundle
   */
  clearBundle: async () => {
    await offlineStorage.clearBundle();
    set({ bundle: null, lastSync: null });
  },
}));
