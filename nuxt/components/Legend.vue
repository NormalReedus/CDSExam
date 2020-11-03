<template>
  <v-card elevation="4">
    <v-card-title class="justify-center">{{ legendTitle }}</v-card-title>
    <v-divider class="mx-16"></v-divider>
    <v-card-text>
      <div class="map-legend">
        <div class="map-legend-category-container">
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

    tertiles() {
      return this.$store.state.covidTertiles
    },
    covidVariable() {
      return this.$store.state.covidVariable
    },

    legendLabels() {
      const { first, second, max } = this.tertiles[this.covidVariable]
      let labels

      if (
        this.covidVariable === 'cases_per_cap' ||
        this.covidVariable === 'deaths_per_cap'
      ) {
        const decimals = this.covidVariable === 'cases_per_cap' ? 4 : 6

        labels = {
          firstStart: 0,
          firstEnd: first.toFixed(decimals),
          secondStart: first.toFixed(decimals),
          secondEnd: second.toFixed(decimals),
          maxStart: first.toFixed(decimals),
          maxEnd: max.toFixed(decimals),
        }
      } else {
        labels = {
          firstStart: 0,
          firstEnd: Math.round(first),
          secondStart: Math.round(first) + 1,
          secondEnd: Math.round(second),
          maxStart: Math.round(second) + 1,
          maxEnd: Math.round(max),
        }
      }

      return labels
    },

    legendColors() {
      return {
        first: {
          background: `linear-gradient(0deg, ${this.mapColorIntensity(
            0,
            'first'
          )}, ${this.mapColorIntensity(
            this.tertiles[this.covidVariable].first,
            'first'
          )})`,
        },
        second: {
          background: `linear-gradient(0deg, ${this.mapColorIntensity(
            this.tertiles[this.covidVariable].first,
            'second'
          )}, ${this.mapColorIntensity(
            this.tertiles[this.covidVariable].second,
            'second'
          )})`,
        },
        max: {
          background: `linear-gradient(0deg, ${this.mapColorIntensity(
            this.tertiles[this.covidVariable].second,
            'max'
          )}, ${this.mapColorIntensity(
            this.tertiles[this.covidVariable].max,
            'max'
          )})`,
        },
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.map-legend {
  display: flex;
  justify-content: space-between;
  align-items: stretch;

  &-category-container {
    width: 100%;
    display: flex;
    flex-direction: column;
  }

  &__category-colors {
    margin: 0 auto;
    height: 100px;
    width: 50%;
    flex-grow: 1;
    border-radius: 5px;

    background: linear-gradient(0deg, red, blue);
  }

  &__category-label {
    text-align: center;
    margin: 0;
  }
}
</style>