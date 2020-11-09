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

    <!-- <div class="map-legend-category-container">
          <p class="map-legend__category-label">
            {{ legendLabels.firstEnd }}
          </p>
          <div
            :style="legendColors.first"
            class="map-legend__category-colors elevation-4"
          ></div>
          <p class="map-legend__category-label">
            {{ legendLabels.firstStart }}
          </p>
        </div>

        <div class="map-legend-category-container">
          <p class="map-legend__category-label">
            {{ legendLabels.secondEnd }}
          </p>
          <div
            :style="legendColors.second"
            class="map-legend__category-colors elevation-4"
          ></div>
          <p class="map-legend__category-label">
            {{ legendLabels.secondStart }}
          </p>
        </div>

        <div class="map-legend-category-container">
          <p class="map-legend__category-label">
            {{ legendLabels.maxEnd }}
          </p>
          <div
            :style="legendColors.max"
            class="map-legend__category-colors elevation-4"
          ></div>
          <p class="map-legend__category-label">
            {{ legendLabels.maxStart }}
          </p>
        </div> -->
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

    tertiles() {
      return this.$store.state.covidTertiles
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

      // const { first, second, max } = this.tertiles[this.covidVariable]
      // let labels

      // if (
      //   this.covidVariable === 'cases_per_cap' ||
      //   this.covidVariable === 'deaths_per_cap'
      // ) {
      //   const decimals = this.covidVariable === 'cases_per_cap' ? 4 : 6

      //   labels = {
      //     firstStart: 0,
      //     firstEnd: first.toFixed(decimals),
      //     secondStart: first.toFixed(decimals),
      //     secondEnd: second.toFixed(decimals),
      //     maxStart: first.toFixed(decimals),
      //     maxEnd: max.toFixed(decimals),
      //   }
      // } else {
      //   labels = {
      //     firstStart: 0,
      //     firstEnd: Math.round(first),
      //     secondStart: Math.round(first) + 1,
      //     secondEnd: Math.round(second),
      //     maxStart: Math.round(second) + 1,
      //     maxEnd: Math.round(max),
      //   }
      // }

      // return labels
    },

    legendColors() {
      // return {
      //   first: {
      //     background: `linear-gradient(0deg, ${this.mapColorIntensity(
      //       0,
      //       'first'
      //     )}, ${this.mapColorIntensity(
      //       this.tertiles[this.covidVariable].first,
      //       'first'
      //     )})`,
      //   },
      //   second: {
      //     background: `linear-gradient(0deg, ${this.mapColorIntensity(
      //       this.tertiles[this.covidVariable].first,
      //       'second'
      //     )}, ${this.mapColorIntensity(
      //       this.tertiles[this.covidVariable].second,
      //       'second'
      //     )})`,
      //   },
      //   max: {
      //     background: `linear-gradient(0deg, ${this.mapColorIntensity(
      //       this.tertiles[this.covidVariable].second,
      //       'max'
      //     )}, ${this.mapColorIntensity(
      //       this.tertiles[this.covidVariable].max,
      //       'max'
      //     )})`,
      //   },
      // }

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
  // display: flex;
  // justify-content: space-between;
  // align-items: center;
  &-labels {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  &__indicator {
    height: 35%;
    border-radius: 5px;
  }

  // &-category-container {
  //   width: 100%;
  //   display: flex;
  //   flex-direction: column;
  // }

  // &__category-colors {
  //   margin: 0 auto;
  //   height: 100px;
  //   width: 50%;
  //   flex-grow: 1;
  //   border-radius: 5px;
  // }

  // &__category-label {
  //   text-align: center;
  //   margin: 0;
  // }
}

.map-categoricals {
  display: flex;
  justify-content: space-around;
  align-items: center;

  &__indicator {
    height: 35px;
    // width: 30%;
    width: 100%;
    background: red;
    border-radius: 5px;
  }

  &__no-data {
    background: darkslategray;
  }
}

.map-categorical-container {
  min-width: 35%;
}

.v-card__text:not(:last-of-type) {
  padding-bottom: 0;
}
</style>