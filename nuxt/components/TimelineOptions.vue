<template>
  <div>
    <h3 class="timeline-options__title">Timeline speed:</h3>
    <v-radio-group
      class="timeline-options__radios"
      v-model="timelineSpeedModifier"
      row
    >
      <v-radio label="Off" :value="0" color="red"></v-radio>
      <v-radio label="Slow" :value="1" color="red"></v-radio>
      <v-radio label="Fast" :value="2" color="red"></v-radio>
    </v-radio-group>
  </div>
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
    ...mapMutations(['setCurrentDataIndex']),

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
.timeline-options {
  &__radios {
    margin-top: 0;
  }

  &__title {
    text-align: center;
  }
}
</style>