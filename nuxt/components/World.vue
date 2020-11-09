<template>
  <div class="map-container">
    <h2 class="map-title" :key="currentCovidData.date">
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
    ...mapGetters(['currentCovidData']),

    prettyVariable() {
      if (this.covidVariable === 'cases_per_cap') {
        return 'cases per capita.'
      } else if (this.covidVariable === 'deaths_per_cap') {
        return 'deaths per capita.'
      } else {
        return this.covidVariable + '.'
      }
    },

    maxVals() {
      return this.$store.state.covidMaxVals
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

        // Get the tertile interval for the record value:
        // const tertiles = this.tertiles[this.covidVariable]
        const recordValue = record[this.covidVariable]

        // let tertileName
        // if (recordValue <= tertiles.first) {
        //   tertileName = 'first'
        // } else if (recordValue <= tertiles.second) {
        //   tertileName = 'second'
        // } else {
        //   tertileName = 'max'
        // }

        // Set colour intensity:
        // element.style.fill = this.mapColorIntensity(recordValue, tertileName)
        element.style.fill = this.mapColorIntensity(
          recordValue,
          this.maxVals[this.covidVariable]
        )

        // Underscores to spaces:
        const titleText = `${record.countriesAndTerritories} - ${
          record[this.covidVariable]
        } ${this.prettyVariable}`.replace(/_/g, ' ')
        element.firstChild.textContent = titleText
      }

      // Reset colors and title of all svgs with no data point:
      for (const element of Object.values(noDataAreas)) {
        // element.style.fill = '#A1A1B5'
        element.style.fill = 'darkslategray'

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
