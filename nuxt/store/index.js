import data from '@/data/covid_19_data.json'

export const state = () => ({
  loading: true,
  covidMaxVals: data.max_vals,
  covidRecords: data.records,
  currentDataIndex: 0,
  geoSvgs: {}, // geoId props pointing to the svg dom element
  transitions: true,
  altColorMode: false,
  covidVariable: 'cases', // 'deaths', 'deaths_per_cap', 'cases_per_cap'
  perDate: false,
  maxInfo: {
    country: null,
    max: null,
  },
  showMaxInfo: false,
})

export const mutations = {
  stopLoader(state) {
    state.loading = false
  },

  setGeoSvgs(state, svgEls) {
    svgEls.forEach((el) => {
      state.geoSvgs[el.id] = el
    })
  },
  setCurrentDataIndex(state, index) {
    state.currentDataIndex = index
  },
  setMaxInfo(state, { country, max }) {
    state.maxInfo = { country, max }
  },
  hideMaxInfo(state) {
    state.showMaxInfo = false
  },
  showMaxInfo(state) {
    state.showMaxInfo = true
  },
  setTransitions(state, val) {
    state.transitions = val
  },
  setColorMode(state, val) {
    state.altColorMode = val
  },
  setCovidVariable(state, val) {
    state.covidVariable = val
  },
}

export const getters = {
  currentCovidData(state) {
    return state.covidRecords[state.currentDataIndex]
  },
}
