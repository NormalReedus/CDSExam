<template>
  <form class="date-slider-options">
    <h3>Timeline speed:</h3>
    <input
      class="date-slider-options__radio"
      type="radio"
      name="speed"
      id="off"
      value="0"
      v-model="timelineSpeedModifier"
      checked
    />
    <label for="off" class="date-slider-options__label">Off</label>
    <input
      class="date-slider-options__radio"
      type="radio"
      name="speed"
      id="slow"
      value="1"
      v-model="timelineSpeedModifier"
    />
    <label for="slow" class="date-slider-options__label">Slow</label>
    <input
      class="date-slider-options__radio"
      type="radio"
      name="speed"
      id="fast"
      value="2"
      v-model="timelineSpeedModifier"
    />
    <label for="fast" class="date-slider-options__label">Fast</label>
  </form>
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
        return this.$tore.state.currentDataIndex
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
.date-slider {
  &-options {
    margin-right: 2rem;

    &__label {
      margin-right: 0.5rem;
      font-style: italic;
    }
  }
}
</style>