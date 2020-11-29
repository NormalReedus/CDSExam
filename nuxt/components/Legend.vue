<template>
  <v-card elevation="4">
    <v-card-title class="justify-center">{{ legendTitle }}</v-card-title>
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

    <v-card-text class="d-flex justify-space-between">
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
      <div class="map-categorical-container max-button-container text-center">
        Go to max
        <div @click="maxIndex" class="max-button elevation-4"></div>
      </div>
    </v-card-text>
  </v-card>
</template>

<script>
import mapColorIntensity from '@/mixins/mapColorIntensity.js'
import { mapMutations, mapGetters } from 'vuex'

export default {
  mixins: [mapColorIntensity],
  computed: {
    ...mapGetters(['currentCovidData', 'maxVal']),

    legendTitle() {
      let variable
      if (this.covidVariable === 'cases') {
        variable = 'Cases'
      } else if (this.covidVariable === 'deaths') {
        variable = 'Deaths'
      } else if (this.covidVariable === 'cases_per_10k') {
        variable = 'Cases per 10k'
      } else {
        variable = 'Deaths per 10k'
      }

      let limits
      if (this.$store.state.perDate) {
        limits = 'Single date'
      } else {
        limits = 'All time'
      }

      return variable + ' - ' + limits
    },

    covidVariable() {
      return this.$store.state.covidVariable
    },

    covidRecords() {
      return this.$store.state.covidRecords
    },

    zeroColor() {
      return `background: ${this.mapColorIntensity(0, 1)}`
    },

    perDate() {
      return this.$store.state.perDate
    },

    legendLabel() {
      const maxLabel = this.maxVal

      const andAbove = this.perDate ? '' : '+'

      if (
        this.covidVariable === 'cases_per_10k' ||
        this.covidVariable === 'deaths_per_10k'
      ) {
        const decimals = this.covidVariable === 'cases_per_10k' ? 2 : 3
        return maxLabel.toFixed(decimals) + andAbove
      } else {
        return Math.round(maxLabel) + andAbove
      }
    },

    legendColors() {
      return {
        background: `linear-gradient(to right, ${this.mapColorIntensity(
          0.0000001 /* to not show 0 cases in the legend */,
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
  methods: {
    ...mapMutations(['setCurrentDataIndex', 'setMaxInfo', 'showMaxInfo']),

    maxIndex() {
      const records = this.covidRecords

      const maxInfo = {
        covidVariable: this.covidVariable,
        country: '',
        max: 0,
        date: '',
        index: 0,
      }

      for (let i = 0; i < records.length; i++) {
        const data = records[i].data
        const date = records[i].date

        for (let j = 0; j < data.length; j++) {
          const prop = data[j][this.covidVariable]
          if (prop > maxInfo.max) {
            maxInfo.max = prop
            maxInfo.date = date
            maxInfo.index = i
            maxInfo.geoId = data[j].geoId
            maxInfo.country = data[j].countriesAndTerritories.replace(/_/g, ' ')
          }
        }
      }
      console.table(maxInfo)
      this.setCurrentDataIndex(maxInfo.index)
      this.setMaxInfo(maxInfo)
      this.showMaxInfo()
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
  justify-content: space-evenly;
  align-items: center;
  flex-grow: 2;

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

.max-button-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.max-button {
  width: 40px;
  height: 40px;
  background: radial-gradient(
    farthest-side at 30% 30%,
    rgb(255, 196, 196),
    red
  );
  border-radius: 50%;
  cursor: pointer;
  transition: transform 200ms ease;

  &:hover {
    transform: scale(1.1);
  }
}
</style>