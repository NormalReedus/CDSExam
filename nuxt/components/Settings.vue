<template>
  <v-card elevation="4">
    <v-card-title class="justify-center">Settings</v-card-title>

    <v-divider class="mx-16"></v-divider>

    <v-card-subtitle>Disable/enable animations:</v-card-subtitle>
    <v-card-text>
      <v-checkbox
        v-model="transitions"
        label="Animations"
        color="red"
      ></v-checkbox>
    </v-card-text>

    <v-divider class="mx-4" />

    <v-card-subtitle>Choose a variable to display:</v-card-subtitle>
    <v-card-text>
      <v-radio-group v-model="covidVariable">
        <v-radio label="Cases" value="cases" color="red"></v-radio>
        <v-radio label="Deaths" value="deaths" color="red"></v-radio>
        <v-radio
          label="Cases per cap."
          value="casesPerCap"
          color="red"
          disabled
        ></v-radio>
        <v-radio
          label="Deaths per cap."
          value="deathsPerCap"
          color="red"
          disabled
        ></v-radio>
      </v-radio-group>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  computed: {
    transitions: {
      get() {
        return this.$store.state.transitions
      },
      set(val) {
        this.$store.commit('setTransitions', val)
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