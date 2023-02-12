import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loading: false,
  },
  getters: {
    loading(state) {
      return state.loading
    }
  },
  mutations: {
    setLoading(state, payload) {
      state.loading = payload
    }
  },
  actions: {
    setLoading({ commit }, payload) {
      commit('setLoading', payload)
    }
  },
  modules: {
  }
})
