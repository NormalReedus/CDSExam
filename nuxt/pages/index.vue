<template>
  <div class="world-container" :class="{ 'no-transition': !transitions }">
    <World />
    <div class="date-slider-container">
      <!-- <Radios /> -->
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
      <h6 class="date-slider__date">{{ covidRecords[0].date }}</h6>
      <input
        class="date-slider__input"
        type="range"
        min="0"
        :max="covidRecords.length - 1"
        @change="currentDataIndex = $event.target.value"
        :value="currentDataIndex"
        :title="currentCovidData.date"
      />
      <h6 class="date-slider__date">
        {{ covidRecords[covidRecords.length - 1].date }}
      </h6>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {
  data() {
    return {
      transitions: true,
      // Vue internals use '_', so we have to access through this.$data:
      _timelineSpeedModifier: 0,
      _runningTimeoutId: null,
    }
  },

  computed: {
    ...mapState(['covidRecords', 'geoSvgs']),
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
          this.useTimeline()
        } else {
          // If timeline is already running, we just adjust the modifier, which will change the speed next tick:
          this.$data._timelineSpeedModifier = modifier
        }
      },
    },
  },

  watch: {
    currentCovidData(newData, oldData) {
      this.updateMap(newData)
    },
  },

  methods: {
    ...mapMutations(['setCurrentDataIndex']),

    updateMap() {
      for (const record of this.currentCovidData.data) {
        const element = this.geoSvgs[record.geoId]

        if (!element) continue

        // Set colour intensity:
        element.style.fill = this.mapColorIntensity(
          record.cases,
          this.$store.state.covidMaxVals.cases
        )

        // Edit title:
        const titleText = `${record.countriesAndTerritories} - ${record.cases} cases`.replace(
          /_/g,
          ' '
        )
        element.firstChild.textContent = titleText
      }
    },

    mapColorIntensity(val, maxVal) {
      const intensity = val / maxVal
      const hue = 0
      const saturation = 50 + intensity * 50
      const lightness = 5 + intensity * 50

      // const hue = 100 - intensity * 100
      // const saturation = intensity * 100
      // const lightness = 50

      return `hsl(${hue}, ${saturation}%, ${lightness}%)`
    },

    useTimeline() {
      if (this.$data._timelineSpeedModifier == 0) return

      if (this.currentDataIndex == this.covidRecords.length - 1) {
        this.currentDataIndex = 0
      } else {
        this.currentDataIndex++
      }

      this.$data._runningTimeoutId = setTimeout(
        this.useTimeline,
        process.env.timelineBaseSpeed / this.$data._timelineSpeedModifier
      )
    },
  },

  head() {
    return {
      title: 'COVID-19 Heatmap',
    }
  },

  mounted() {
    this.updateMap()
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

.date-slider {
  &-container {
    display: flex;
    align-items: center;

    width: 100%;
    padding: 0 2rem;
  }

  &-options {
    margin-right: 2rem;

    &__label {
      margin-right: 0.5rem;
      font-style: italic;
    }
  }

  &__date {
    font-family: var(--heading-font);
    font-weight: 500;
    transform: rotate(35deg);
  }
}

.date-slider__input {
  flex-grow: 1;
  background: transparent;
  height: 25px;
  -webkit-appearance: none;
  margin: 0 1rem;
  opacity: 0.6;
  transition: opacity 700ms ease;

  &:focus {
    outline: none;

    &::-webkit-slider-runnable-track {
      background: var(--disabled-color);
    }

    &::-ms-fill-lower {
      background: var(--disabled-color);
    }

    &::-ms-fill-upper {
      background: var(--disabled-color);
    }
  }

  &:hover {
    opacity: 1;

    &::-ms-thumb {
      background: red;
      border-color: red;
    }
    &::-webkit-slider-thumb {
      background: red;
      border-color: red;
    }
    &::-moz-range-thumb {
      background: red;
      border-color: red;
    }
  }

  &::-webkit-slider-runnable-track {
    width: 100%;
    height: 5px;
    cursor: pointer;
    animation: 0.2s;
    background: var(--disabled-color);
    border-radius: 1px;
  }

  &::-webkit-slider-thumb {
    box-shadow: 0px 0px 1rem rgba(0, 0, 0, 0.5);
    border: 1px solid var(--danger-color);
    height: 18px;
    width: 18px;
    border-radius: 25px;
    background: var(--danger-color);
    cursor: pointer;
    -webkit-appearance: none;
    margin-top: -7px;
    transition: all 1s ease;
  }

  &::-moz-range-track {
    width: 100%;
    height: 5px;
    cursor: pointer;
    animation: 0.2s;
    background: var(--disabled-color);
    border-radius: 1px;
  }

  &::-moz-range-thumb {
    box-shadow: 0px 0px 1rem rgba(0, 0, 0, 0.5);
    border: 1px solid var(--danger-color);
    height: 18px;
    width: 18px;
    border-radius: 25px;
    background: var(--danger-color);
    cursor: pointer;
    transition: all 1s ease;
  }

  &::-ms-track {
    width: 100%;
    height: 5px;
    cursor: pointer;
    animation: 0.2s;
    background: transparent;
    border-color: transparent;
    color: transparent;
  }

  &::-ms-fill-lower {
    background: var(--disabled-color);
    border-radius: 2px;
  }

  &::-ms-fill-upper {
    background: var(--disabled-color);
    border-radius: 2px;
  }

  &::-ms-thumb {
    margin-top: 1px;
    box-shadow: 0px 0px 1rem rgba(0, 0, 0, 0.5);
    border: 1px solid var(--danger-color);
    height: 18px;
    width: 18px;
    border-radius: 25px;
    background: var(--danger-color);
    cursor: pointer;
    transition: all 1s ease;
  }
}
</style>
