<template>
  <div class="map-container">
    <!-- <transition name="title" mode="out-in"> -->
    <h2 class="map-title" :key="currentCovidData.date">
      {{ currentCovidData.date }}
    </h2>
    <!-- </transition> -->
    <WorldSvg />
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
  watch: {
    currentCovidData(newData, oldData) {
      this.updateMap(newData)
    },
  },

  computed: {
    ...mapState(['geoSvgs']),
    ...mapGetters(['currentCovidData']),
  },

  methods: {
    updateMap() {
      for (const record of this.currentCovidData.data) {
        const element = this.geoSvgs[record.geoId]

        if (!element) continue

        // Set colour intensity:
        element.style.fill = this.mapColorIntensity(
          record.cases,
          this.$store.state.covidMaxVals.cases
        )

        // Underscores to spaces:
        const titleText = `${record.countriesAndTerritories} - ${record.cases} cases`.replace(
          /_/g,
          ' '
        )
        element.firstChild.textContent = titleText
      }
    },

    mapColorIntensity(val, maxVal) {
      const intensity = val / maxVal
      const hue = 0
      const saturation = 50 + intensity * 50
      const lightness = 5 + intensity * 50

      // const hue = 100 - intensity * 100
      // const saturation = intensity * 100
      // const lightness = 50

      return `hsl(${hue}, ${saturation}%, ${lightness}%)`
    },
  },

  mounted() {
    this.updateMap()
  },
}
</script>

<style lang="scss" scoped>
.map-title {
  margin-bottom: 2rem;

  color: var(--text-color);

  font-family: var(--heading-font);
  font-weight: var(--heading-weight);

  position: absolute;
}

// .title-enter-active,
// .title-leave-active {
//   transition: all 200ms cubic-bezier(0.175, 0.885, 0.32, 1.275);
//   transform: translateX(0);
// }
// .title-enter,
// .title-leave-to {
//   transform: translateX(-200%);
//   opacity: 0;
// }
</style>
