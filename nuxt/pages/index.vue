<template>
  <v-container
    class="page-container"
    :class="{ 'no-transition': !transitions }"
    pa-0
    ma-0
    fluid
  >
    <v-row>
      <v-col cols="2">
        <input
          type="checkbox"
          class="transitions-checkbox"
          value="transitions"
          v-model="transitions"
        />
      </v-col>
      <v-col cols="8">
        <World class="map" />
      </v-col>
      <v-col cols="2">
        <div class="test"></div>
      </v-col>
    </v-row>
    <!-- <v-col></v-col> -->
    <v-row>
      <Timeline class="timeline" />
    </v-row>
  </v-container>
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
}

.test {
  background: hotpink;
  height: 100%;
}
</style>
