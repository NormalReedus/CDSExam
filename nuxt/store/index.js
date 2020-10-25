// Fuck yes:
import data from '@/data/covid_19_final.json'

export const state = () => ({
  covidMaxVals: {
    deaths: data.max_deaths,
    cases: data.max_cases,
    deathsPerPop: data.max_deaths_per_pop,
    casesPerPop: data.max_cases_per_pop,
  },
  covidRecords: data.records,
  currentDataIndex: 0,
  geoSvgs: {}, // geoId props pointing to the svg dom element
})

export const mutations = {
  setGeoSvgs(state, svgEls) {
    svgEls.forEach((el) => {
      state.geoSvgs[el.id] = el
    })
  },

  setCurrentDataIndex(state, index) {
    state.currentDataIndex = index
  },
}

export const getters = {
  currentCovidData(state) {
    return state.covidRecords[state.currentDataIndex]
  },
}
