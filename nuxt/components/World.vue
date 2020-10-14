<template>
  <div class="map-container">
    <transition name="title">
      <h1 class="map-title">{{ currentDate }}</h1>
    </transition>
    <WorldSvg />
  </div>
</template>

<script>
export default {
  computed: {
    currentDate() {
      return this.$store.state.currentCovidData.date
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
