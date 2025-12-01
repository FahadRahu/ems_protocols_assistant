import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'robots.txt'],
      manifest: {
        name: 'VitalPath - EMS Protocol Assistant',
        short_name: 'VitalPath',
        description: 'Offline-first clinical decision support for EMS',
        theme_color: '#1a1a2e',
        background_color: '#1a1a2e',
        display: 'standalone',
        icons: [
          { src: '/icon-192.png', sizes: '192x192', type: 'image/png' },
          { src: '/icon-512.png', sizes: '512x512', type: 'image/png' },
        ],
      },
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg,json}'],
        runtimeCaching: [
          {
            urlPattern: /\/api\/v1\/bundles\/latest/,
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'protocol-bundle',
              expiration: { maxAgeSeconds: 86400 }, // 24 hours
            },
          },
        ],
      },
    }),
  ],
});
