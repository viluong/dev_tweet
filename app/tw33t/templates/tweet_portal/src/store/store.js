import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './actions'
import getter from './getter'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    tweets: [],
    result_count: 0,
    user: null
  },
  mutations: mutations,
  getters: getter,
  actions: actions
})
