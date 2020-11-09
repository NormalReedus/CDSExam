<template>
  <v-card elevation="4">
    <v-card-title class="justify-center"
      >Legend - {{ legendTitle }}</v-card-title
    >
    <v-divider class="mx-16"></v-divider>
    <v-card-text>
      <div class="map-legend">
        <div class="map-legend-labels">
          <div class="map-legend__label map-legend__min">> 0</div>
          <div class="map-legend__label map-legend__max">
            {{ legendLabel }}
          </div>
        </div>
        <div
          class="map-legend__indicator elevation-4"
          :style="legendColors"
        ></div>
      </div>
    </v-card-text>

    <v-divider class="mx-4" />

    <v-card-text>
      <div class="map-categoricals">
        <div class="map-categorical-container text-center">
          No data
          <div
            class="map-categoricals__no-data map-categoricals__indicator elevation-4"
          ></div>
        </div>
        <div class="map-categorical-container text-center">
          Zero
          <div
            class="map-categoricals__zero map-categoricals__indicator elevation-4"
            :style="zeroColor"
          ></div>
        </div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import mapColorIntensity from '@/mixins/mapColorIntensity.js'

export default {
  mixins: [mapColorIntensity],
  computed: {
    legendTitle() {
      if (this.covidVariable === 'cases') {
        return 'Cases'
      } else if (this.covidVariable === 'deaths') {
        return 'Deaths'
      } else if (this.covidVariable === 'cases_per_cap') {
        return 'Cases per capita'
      } else {
        return 'Deaths per capita'
      }
    },

    maxVals() {
      return this.$store.state.covidMaxVals
    },

    covidVariable() {
      return this.$store.state.covidVariable
    },

    zeroColor() {
      return `background: ${this.mapColorIntensity(0, 1)}`
    },

    legendLabel() {
      const maxLabel = this.maxVals[this.covidVariable]
      if (
        this.covidVariable === 'cases_per_cap' ||
        this.covidVariable === 'deaths_per_cap'
      ) {
        const decimals = this.covidVariable === 'cases_per_cap' ? 4 : 6
        return maxLabel.toFixed(decimals) + '+'
      } else {
        return Math.round(maxLabel) + '+'
      }
    },

    legendColors() {
      return {
        background: `linear-gradient(to right, ${this.mapColorIntensity(
          0.0000001 /* to not show 0 cases on the legend */,
          1
        )}, ${this.mapColorIntensity(0.1, 1)}, ${this.mapColorIntensity(
          0.2,
          1
        )}, ${this.mapColorIntensity(0.3, 1)}, ${this.mapColorIntensity(
          0.4,
          1
        )},${this.mapColorIntensity(0.5, 1)}, ${this.mapColorIntensity(
          0.6,
          1
        )}, ${this.mapColorIntensity(0.7, 1)}, ${this.mapColorIntensity(
          0.8,
          1
        )}, ${this.mapColorIntensity(0.9, 1)}, ${this.mapColorIntensity(
          1,
          1
        )})`,
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.map-legend {
  width: 100%;
  height: 100px;

  &-labels {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__indicator {
    height: 35%;
    border-radius: 5px;
    transition: background 250ms ease;
  }
}

.map-categoricals {
  display: flex;
  justify-content: space-around;
  align-items: center;

  &__indicator {
    height: 35px;
    width: 100%;
    background: red;
    border-radius: 5px;
  }

  &__no-data {
    background: #5e5e78;
  }

  &__zero {
    transition: background 250ms ease;
  }
}

.map-categorical-container {
  min-width: 35%;
}

.v-card__text:not(:last-of-type) {
  padding-bottom: 0;
}
</style>