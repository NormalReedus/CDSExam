<template>
  <div class="map-container">
    <h2 class="map-title">
      {{ currentCovidData.date }}
    </h2>
    <WorldSvg />
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import mapColorIntensity from '@/mixins/mapColorIntensity.js'

export default {
  mixins: [mapColorIntensity],
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
    ...mapGetters(['currentCovidData', 'maxVal']),

    prettyVariable() {
      if (this.covidVariable === 'casesPer10k') {
        return 'cases per 10k.'
      } else if (this.covidVariable === 'deathsPer10k') {
        return 'deaths per 10k.'
      } else {
        return this.covidVariable + '.'
      }
    },

    covidVariable() {
      return this.$store.state.covidVariable
    },
  },

  methods: {
    updateMap() {
      const noDataAreas = Object.assign({}, this.geoSvgs)

      for (const record of this.currentCovidData.data) {
        const element = this.geoSvgs[record.geoId]

        if (!element) continue

        delete noDataAreas[record.geoId]

        const recordValue = record[this.covidVariable]

        element.style.fill = this.mapColorIntensity(recordValue, this.maxVal)

        // Underscores to spaces:
        const titleText = `${record.countriesAndTerritories} - ${
          record[this.covidVariable]
        } ${this.prettyVariable}`.replace(/_/g, ' ')
        element.firstChild.textContent = titleText
      }

      // Reset colors and title of all svgs with no data point:
      for (const element of Object.values(noDataAreas)) {
        element.style.fill = '#5e5e78'

        element.firstChild.textContent = element.firstChild.textContent.split(
          ' - '
        )[0]
      }
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

  position: absolute;
}
</style>
