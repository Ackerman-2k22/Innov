/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.{html,js}"],
  theme: {

    backgroundImage: {
      ho: 'url(/Images/lukasz-szmigiel-2ShvY8Lf6l0-unsplash.jpg)',
    },
    extend: {
      colors: {
        "color-primary": "#181D27",
        "color-primary-light": "#CCE5AE",
        "color-primary-dark": "#211F28",
        "color-secondary-dark": "#527410",
        "color-secondary": "#5C9926",
        "color-gray": "#333",
        "color-white": "#EDF3D3",
        "color-blob": "#57714D",
        "color-op": "#7B8436",
        "color-ope": "#0D2847",
      }
    },
    container: {
      center: true,
      padding: {
        DEFAULT:'20px',
        md: "50px"
      }
    }
  },
  plugins: [],
}

