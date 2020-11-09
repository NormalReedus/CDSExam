export default {
  methods: {
    mapColorIntensity(val, maxVal) {
      let intensity = val / maxVal
      if (intensity > 1) intensity = 1

      const maxHue = 270
      const baseHue = 90
      let hue
      if (this.$store.state.altColorMode) {
        // Green -> blue -> red
        hue = baseHue + intensity * maxHue
      } else {
        // Blue -> green -> red
        hue = maxHue - intensity * maxHue
      }

      const saturation = 40 + intensity * 60

      let lightness
      if (intensity <= 0) {
        lightness = 20
      } else {
        lightness = 30 + intensity * 30
      }

      return `hsl(${hue}, ${saturation}%, ${lightness}%)`
    },
  },
}
