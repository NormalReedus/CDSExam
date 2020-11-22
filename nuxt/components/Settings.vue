<template>
  <v-card elevation="4">
    <v-card-title class="justify-center">Settings</v-card-title>

    <v-divider class="mx-16"></v-divider>

    <v-card-subtitle>Aesthetics:</v-card-subtitle>
    <v-card-text>
      <v-switch
        :disabled="loading"
        v-model="transitions"
        label="Animations"
        color="red"
      ></v-switch>
      <v-switch
        :disabled="loading"
        v-model="altColorMode"
        label="Alt. color mode"
        color="red"
      ></v-switch>
    </v-card-text>

    <v-divider class="mx-4" />
    <v-card-subtitle>Legend limits:</v-card-subtitle>
    <v-card-text>
      <v-radio-group v-model="perDate" :disabled="loading">
        <v-radio label="Single date" :value="true" color="red"></v-radio>
        <v-radio label="All time" :value="false" color="red"></v-radio>
      </v-radio-group>
    </v-card-text>

    <v-card-subtitle>Variable to display:</v-card-subtitle>
    <v-card-text>
      <v-radio-group
        v-model="covidVariable"
        @change="hideMaxInfo"
        :disabled="loading"
      >
        <v-radio label="Cases" value="cases" color="red"></v-radio>
        <v-radio label="Deaths" value="deaths" color="red"></v-radio>
        <v-radio
          label="Cases per 10k."
          value="cases_per_10k"
          color="red"
        ></v-radio>
        <v-radio
          label="Deaths per 10k."
          value="deaths_per_10k"
          color="red"
        ></v-radio>
      </v-radio-group>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  computed: {
    loading() {
      return this.$store.state.loading
    },

    perDate: {
      get() {
        return this.$store.state.perDate
      },
      set(val) {
        this.$store.commit('setPerDate', val)
        this.$emit('updateMap')
      },
    },

    transitions: {
      get() {
        return this.$store.state.transitions
      },
      set(val) {
        this.$store.commit('setTransitions', val)
      },
    },
    altColorMode: {
      get() {
        return this.$store.state.altColorMode
      },
      set(val) {
        this.$store.commit('setColorMode', val)
        this.$emit('updateMap')
      },
    },
    covidVariable: {
      get() {
        return this.$store.state.covidVariable
      },
      set(val) {
        this.$store.commit('setCovidVariable', val)
        this.$emit('updateMap')
      },
    },
  },

  methods: {
    ...mapMutations(['hideMaxInfo']),
  },
}
</script>

<style lang="scss" scoped>
.v-input {
  margin-top: 0;
}

.v-card__text {
  padding-bottom: 0;
}
</style>