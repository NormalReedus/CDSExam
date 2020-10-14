// Fuck yes:
import mock from '@/data/mock.json'

export const state = () => ({
  covidData: mock,
  currentCovidData: mock[0], // Defaults to first entry
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
}
