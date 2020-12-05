<template>
  <v-container
    class="page-container"
    :class="{ 'no-transition': !transitions }"
    pa-0
    ma-0
    fluid
  >
    <v-progress-circular
      class="loader"
      v-if="loading"
      indeterminate
      color="red"
      size="70"
      width="7"
    ></v-progress-circular>

    <MaxInfo />

    <v-row>
      <v-col cols="3" class="pl-6 d-flex flex-column justify-space-between">
        <Legend />
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
import MaxInfo from '../components/MaxInfo.vue'
export default {
  components: { MaxInfo },
  computed: {
    transitions() {
      return this.$store.state.transitions
    },

    loading() {
      return this.$store.state.loading
    },
  },

  methods: {
    callUpdateMap() {
      this.$refs.world.updateMap()
    },
  },
}
</script>

<style lang="scss">
.page-container {
  min-height: 100vh;
}

.loader {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
