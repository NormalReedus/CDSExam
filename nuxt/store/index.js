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
  setColorMode(state, val) {
    state.altColorMode = val
  },
  setCovidVariable(state, val) {
    state.covidVariable = val
  },
  dataTrimmer(state) {
    const covidRecords = state.covidRecords
    // const geoIds = Object.keys(state.geoSvgs)
    for (const record of covidRecords) {
      for (const countryData of record.data) {
        if (!state.geoSvgs[countryData.geoId]) console.log(countryData.geoId)
      }
      // record.data = record.data.filter(e => geoIds.includes(e.geoId))
    }
  },
}

export const getters = {
  currentCovidData(state) {
    return state.covidRecords[state.currentDataIndex]
  },
}
