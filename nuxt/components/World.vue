<template>
  <div class="map-container">
    <h1 class="map-title" @click="test">Year 3000</h1>
    <WorldSvg />
  </div>
</template>

<script>
// Fuck yes:
import mock from '@/data/mock.json'

export default {
  methods: {
    test() {
      const geoSvgs = this.$store.state.geoSvgs

      mock[0].records.forEach((rec) => {
        geoSvgs[rec.geoId].style.fill = 'crimson'
        // geoSvgs[rec.geoId].style.fill = 'crimson'
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.map-title {
  margin-bottom: 2rem;

  font-family: var(--heading-font);
  font-weight: var(--heading-weight);
}
</style>
