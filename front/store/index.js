import Vuex from 'vuex';

const createStore = () => {
  return new Vuex.Store({
    state: {
      counter: 0,
      pages: [],
      resp: ''
    },
    mutations: {
      increment(state) {
        state.counter++;
      },
      getPages(state, data) {
        state.pages = data;
      },
      updateResp: (state, resp) => {
        state.resp = resp;
      }
    },
    actions: {
      fetchData({ commit }) {
        commit('getPages', {
          1: { name: 'index' },
          2: { name: 'search' }
        });
      },
      async getResp({ commit }) {
        try {
          console.log('test2');
          let resp = await this.$axios.$get(`/hello`);
          commit('updateResp', resp);
        } catch (e) {
          // this.$log.error('getResp: backend call error', e);
          console.log('getResp: backend call error', e);
        }
      }
    },
    getters: {
      getPages(state) {
        return state.pages;
      },
      resp(state) {
        return state.resp;
      }
    }
  });
};

export default createStore;
