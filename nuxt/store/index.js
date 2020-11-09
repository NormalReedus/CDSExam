import data from '@/data/covid_19_output.json'

export const state = () => ({
  loading: true,
  covidMaxVals: data.tertiles,
  covidRecords: data.records,
  currentDataIndex: 0,
  geoSvgs: {}, // geoId props pointing to the svg dom element
  transitions: true,
  // colorblind: false,
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
  // setColorblind(state, val) {
  //   state.colorblind = val
  // },
  setCovidVariable(state, val) {
    state.covidVariable = val
  },
}

export const getters = {
  currentCovidData(state) {
    return state.covidRecords[state.currentDataIndex]
  },
}
