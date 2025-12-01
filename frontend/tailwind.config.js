/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // VitalPath brand colors - dark tactical theme
        'vp-dark': '#1a1a2e',
        'vp-darker': '#0f0f1a',
        'vp-accent': '#e94560',
        'vp-success': '#16a34a',
        'vp-warning': '#eab308',
        'vp-danger': '#dc2626',
      },
      fontFamily: {
        'tactical': ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
