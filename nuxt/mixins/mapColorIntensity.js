export default {
  methods: {
    mapColorIntensity(val, maxVal) {
      // const tertiles = this.tertiles[this.covidVariable]
      // const tertileVal = tertiles[tertileName]

      // let subtractor
      // if (val <= tertiles.first) {
      //   subtractor = 0
      // } else if (val <= tertiles.second) {
      //   subtractor = tertiles['first']
      // } else {
      //   subtractor = tertiles['second']
      // }

      // // Different categories have different base hues:
      // let baseHue
      // if (tertileName === 'first') {
      //   baseHue = 30
      // } else if (tertileName === 'second') {
      //   baseHue = 150
      // } else {
      //   baseHue = 270
      // }

      const maxHue = 270
      // const intensity = (val - subtractor) / (tertileVal - subtractor)
      let intensity = val / maxVal
      if (intensity > 1) intensity = 1

      const hue = maxHue - intensity * maxHue

      const saturation = 40 + intensity * 60

      let lightness
      if (intensity <= 0) {
        lightness = 15
      } else {
        lightness = 30 + intensity * 30
      }

      return `hsl(${hue}, ${saturation}%, ${lightness}%)`
    },
  },
}
