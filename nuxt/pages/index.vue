<template>
  <v-container
    class="page-container"
    :class="{ 'no-transition': !transitions }"
    pa-0
    ma-0
    fluid
  >
    <v-row>
      <v-col cols="3" class="pl-6 d-flex flex-column justify-space-between">
        <Settings @updateMap="callUpdateMap" />
        <TimelineOptions />
      </v-col>
      <v-col cols="9 pr-6">
        <World class="map" ref="world" />
        <Timeline class="timeline" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  computed: {
    transitions() {
      return this.$store.state.transitions
    },
  },

  methods: {
    callUpdateMap() {
      this.$refs.world.updateMap()
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
.page-container {
  min-height: 100vh;
}

.test {
  background: hotpink;
  height: 100%;
}
</style>
