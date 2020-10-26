<template>
  <div class="page-container" :class="{ 'no-transition': !transitions }">
    <div class="test"></div>
    <World class="map" />
    <Timeline class="timeline" />
    <input
      type="checkbox"
      class="transitions-checkbox"
      value="transitions"
      v-model="transitions"
    />
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
.page-container {
  min-height: 100vh;
  text-align: center;

  display: grid;
  grid-template-columns: 1fr 6fr 1fr;
  grid-template-rows: 6fr 1fr;
}

.test {
  background: hotpink;
  grid-area: 1 / 1 / 2 / 2;
}

.map {
  grid-area: 1 / 2 / 1 / 3;
}

.timeline {
  grid-area: 2 / 1 / 2 / 4;
}

.transitions-checkbox {
  grid-area: 1 / 3 / 2 / 4;
}
</style>
