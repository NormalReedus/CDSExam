// Fuck yes:
import mock from '@/data/mock.json'

export const state = () => ({
  covidData: mock,
  currentDataIndex: 0,
  geoSvgs: {}, // geoId props pointing to the svg dom element
})

export const mutations = {
  setGeoSvgs(state, svgEls) {
    svgEls.forEach((el) => {
      state.geoSvgs[el.id] = el
    })
  },

  setCurrentCovidData(state, newData) {
    state.currentCovidData = newData
  },

  setCurrentDataIndex(state, index) {
    state.currentDataIndex = index
  },
}

export const getters = {
  currentCovidData(state) {
    return state.covidData[state.currentDataIndex]
  },
}
