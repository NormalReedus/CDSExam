<template>
  <div class="map-container">
    <transition name="title" mode="out-in">
      <h2 class="map-title" :key="currentDate">{{ currentDate }}</h2>
    </transition>
    <WorldSvg />
  </div>
</template>

<script>
export default {
  computed: {
    currentDate() {
      return this.$store.getters.currentCovidData.date
    },
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

.title-enter-active,
.title-leave-active {
  transition: all 200ms cubic-bezier(0.175, 0.885, 0.32, 1.275);
  transform: translateX(0);
}
.title-enter,
.title-leave-to {
  transform: translateX(-200%);
  opacity: 0;
}
</style>
