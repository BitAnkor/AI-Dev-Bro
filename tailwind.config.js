// tailwind.config.js
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/src/**/*.js",
    "./app/routes.py"  // Para detectar clases en tus templates de Flask
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          900: '#0f172a',
          800: '#1e293b',
          700: '#334155',
        },
        accent: {
          500: '#6366f1',
          600: '#4f46e5',
        },
        electric: {
          400: '#22d3ee',
          500: '#06b6d4',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['Fira Code', 'monospace']
      },
      boxShadow: {
        'neumorphic': '8px 8px 15px #0f172a, -8px -8px 15px #1e293b',
        'glass': '0 4px 30px rgba(0, 0, 0, 0.1)'
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    function({ addUtilities }) {
      addUtilities({
        '.glass-effect': {
          'background': 'rgba(15, 23, 42, 0.7)',
          'backdrop-filter': 'blur(10px)',
          'border': '1px solid rgba(255, 255, 255, 0.1)'
        },
        '.text-gradient': {
          'background-clip': 'text',
          '-webkit-background-clip': 'text',
          'color': 'transparent'
        }
      })
    }
  ]
}