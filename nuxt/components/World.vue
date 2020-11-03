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
  data() {
    return {
      loading: true,
    }
  },

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
      const noDataAreas = Object.assign({}, this.geoSvgs)

      for (const record of this.currentCovidData.data) {
        const element = this.geoSvgs[record.geoId]
        const covidVariable = this.$store.state.covidVariable

        if (!element) continue

        delete noDataAreas[record.geoId]

        // Set colour intensity:
        element.style.fill = this.mapColorIntensity(
          record[covidVariable],
          this.$store.state.covidMaxVals[covidVariable]
        )

        // Underscores to spaces:
        const titleText = `${record.countriesAndTerritories} - ${record[covidVariable]} ${covidVariable}`.replace(
          /_/g,
          ' '
        )
        element.firstChild.textContent = titleText
      }

      for (const element of Object.values(noDataAreas)) {
        element.style.fill = '#A1A1B5'
      }
    },

    mapColorIntensity(val, maxVal) {
      const intensity = val / maxVal
      const hue = this.$store.state.colorblind ? 0 : 90 - intensity * 90
      // const hue = 0
      const saturation = 30 + intensity * 60
      // const saturation = 80
      // const lightness = 15 + intensity * 70
      const lightness = 20 + intensity * 20

      return `hsl(${hue}, ${saturation}%, ${lightness}%)`
    },
  },

  mounted() {
    this.updateMap()
    this.$store.commit('stopLoader')
  },
}
</script>

<style lang="scss" scoped>
.map-title {
  color: var(--text-color);

  // font-weight: var(--heading-weight);

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
