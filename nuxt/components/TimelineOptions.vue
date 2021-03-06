<template>
  <v-card elevation="4">
    <v-card-title class="justify-center">Timeline speed</v-card-title>
    <v-divider class="mx-16"></v-divider>
    <v-card-text>
      <v-radio-group
        :disabled="loading"
        dense
        class="timeline-options__radios d-flex"
        v-model="timelineSpeedModifier"
        @change="hideMaxInfo"
        row
      >
        <v-radio label="Off" :value="0" color="red" class="mx-auto"></v-radio>
        <v-radio label="Slow" :value="1" color="red" class="mx-auto"></v-radio>
        <v-radio label="Fast" :value="2" color="red" class="mx-auto"></v-radio>
      </v-radio-group>
    </v-card-text>
  </v-card>
</template>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex'

export default {
  data() {
    return {
      // Vue internals use '_', so we have to access through this.$data:
      _timelineSpeedModifier: 0,
      _runningTimeoutId: null,
    }
  },

  computed: {
    ...mapState(['covidRecords']),
    ...mapGetters(['currentCovidData']),

    loading() {
      return this.$store.state.loading
    },

    currentDataIndex: {
      get() {
        return this.$store.state.currentDataIndex
      },

      set(index) {
        this.setCurrentDataIndex(index)
      },
    },

    timelineSpeedModifier: {
      get() {
        return this.$data._timelineSpeedModifier
      },

      // Gets called like a watcher when radiobtn value changes
      set(modifier) {
        // Timeline will call itself when running, so we only want to run it if current status is not running:
        if (this.$data._timelineSpeedModifier == 0) {
          // We have to set modifier before running timeline (otherwise it will stop itself since modifier is 0):
          this.$data._timelineSpeedModifier = modifier

          // Avoid multiple timelines running at the same time:
          clearTimeout(this.$data._runningTimeoutId)
          this.autoTimeline()
        } else {
          // If timeline is already running, we just adjust the modifier, which will change the speed next tick:
          this.$data._timelineSpeedModifier = modifier
        }
      },
    },
  },

  methods: {
    ...mapMutations(['setCurrentDataIndex', 'hideMaxInfo']),

    autoTimeline() {
      if (this.$data._timelineSpeedModifier == 0) return

      if (this.currentDataIndex == this.covidRecords.length - 1) {
        this.currentDataIndex = 0
      } else {
        this.currentDataIndex++
      }

      this.$data._runningTimeoutId = setTimeout(
        this.autoTimeline,
        process.env.timelineBaseSpeed / this.$data._timelineSpeedModifier
      )
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