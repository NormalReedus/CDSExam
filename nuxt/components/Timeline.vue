<template>
  <div class="date-slider-container">
    <TimelineOptions />

    <h6 class="date-slider__date">{{ covidRecords[0].date }}</h6>
    <!-- <input
      class="date-slider__input"
      type="range"
      min="0"
      :max="covidRecords.length - 1"
      @change="currentDataIndex = $event.target.value"
      :value="currentDataIndex"
      :title="currentCovidData.date"
    /> -->
    <v-slider
      min="0"
      :max="covidRecords.length - 1"
      @end="currentDataIndex = $event"
      :value="currentDataIndex"
      :title="currentCovidData.date"
      thumb-color="red"
      thumb-label
      thumb-size="0"
    >
      <template v-slot:thumb-label="{ value }">
        {{ covidRecords[value].date }}
      </template>
    </v-slider>
    <h6 class="date-slider__date">
      {{ covidRecords[covidRecords.length - 1].date }}
    </h6>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex'

export default {
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
  },

  methods: {
    ...mapMutations(['setCurrentDataIndex']),
  },
}
</script>

<style lang="scss" scoped>
.date-slider {
  &-container {
    display: flex;
    align-items: center;

    width: 100%;
    padding: 0 2rem;
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