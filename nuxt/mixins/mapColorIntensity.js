export default {
  methods: {
    mapColorIntensity(val, tertileName) {
      const tertiles = this.tertiles[this.covidVariable]
      const tertileVal = tertiles[tertileName]

      let subtractor
      if (val <= tertiles.first) {
        subtractor = 0
      } else if (val <= tertiles.second) {
        subtractor = tertiles['first']
      } else {
        subtractor = tertiles['second']
      }

      // Different categories have different base hues:
      let baseHue
      if (tertileName === 'first') {
        baseHue = 30
      } else if (tertileName === 'second') {
        baseHue = 150
      } else {
        baseHue = 270
      }

      const intensity = (val - subtractor) / (tertileVal - subtractor)
      // const hue = this.$store.state.colorblind ? 0 : 90 - intensity * 90

      const degreeSpan = 90

      const hue = baseHue + intensity * degreeSpan

      // const saturation = 30 + intensity * 60
      const saturation = 50 + intensity * 20

      const lightness = 20 + intensity * 30

      return `hsl(${hue}, ${saturation}%, ${lightness}%)`
    },
  },
}
