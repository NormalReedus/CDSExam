<template>
  <div class="date-slider-container my-4">
    <h6 class="date-slider__date">{{ covidRecords[0].date }}</h6>
    <v-slider
      :disabled="loading"
      class="mb-n5"
      min="0"
      :max="covidRecords.length - 1"
      :value="currentDataIndex"
      :title="currentCovidData.date"
      @change="onSlide"
      color="red"
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
  },

  methods: {
    ...mapMutations(['setCurrentDataIndex', 'hideMaxInfo']),
    onSlide(event) {
      this.currentDataIndex = event
      this.hideMaxInfo()
    },
  },
}
</script>

<style lang="scss" scoped>
.date-slider {
  &-container {
    display: flex;
    align-items: center;

    width: 100%;
  }

  &__date {
    transform: rotate(35deg);
  }
}
</style>