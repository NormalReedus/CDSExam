<template>
  <div class="container" @click="test">
    <World />
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex'

export default {
  computed: {
    ...mapState(['covidData', 'currentCovidData', 'geoSvgs']),
  },

  watch: {
    currentCovidData(newData, oldData) {
      console.log({ newData, oldData })

      newData.records.forEach((record) => {
        this.geoSvgs[record.geoId].style.fill = this.mapColorOpacity(
          '#ff0000',
          record.number,
          100
        )
      })
    },
  },

  methods: {
    ...mapMutations(['setCurrentCovidData']),

    test() {
      this.setCurrentCovidData(this.covidData[1])
    },

    mapColorOpacity(colorHex, number, max) {
      const opacity = number / max

      const byteOpacity = Math.round(opacity * 255)

      let hexOpacity

      if (opacity * 100 < 7) {
        hexOpacity = '0' + byteOpacity.toString(16)
      } else {
        hexOpacity = byteOpacity.toString(16)
      }

      return colorHex + hexOpacity
    },
  },

  head() {
    return {
      title: 'COVID-19 Heatmap',
    }
  },
}
</script>

<style lang="scss">
.container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
