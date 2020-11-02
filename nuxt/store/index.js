// Fuck yes:
import data from '@/data/covid_19_output.json'

export const state = () => ({
  loading: true,
  covidMaxVals: {
    deaths: data.max_vals.deaths,
    cases: data.max_vals.cases,
    deaths_per_cap: data.max_vals.deaths_per_cap,
    cases_per_cap: data.max_vals.cases_per_cap,
  },
  covidRecords: data.records,
  currentDataIndex: 0,
  geoSvgs: {}, // geoId props pointing to the svg dom element
  transitions: true,
  covidVariable: 'cases', // 'deaths', 'deaths_per_cap', 'cases_per_cap'
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

  setTransitions(state, val) {
    state.transitions = val
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
