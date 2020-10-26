<template>
  <div class="world-container" :class="{ 'no-transition': !transitions }">
    <World />
    <Timeline />
  </div>
</template>

<script>
export default {
  data() {
    return {
      transitions: true,
    }
  },

  methods: {},

  head() {
    return {
      title: 'COVID-19 Heatmap',
    }
  },
}
</script>

<style lang="scss">
.world-container {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;

  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
