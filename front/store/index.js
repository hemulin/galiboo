import Vuex from 'vuex';

const createStore = () => {
  return new Vuex.Store({
    state: {
      counter: 0,
      pages: []
    },
    mutations: {
      increment(state) {
        state.counter++;
      },
      getPages(state, data) {
        state.pages = data;
      }
    },
    actions: {
      fetchData({ commit }) {
        commit('getPages', {
          1: { name: 'index' },
          2: { name: 'search' }
        });
      }
    },
    getters: {
      getPages(state) {
        return state.pages;
      }
    }
  });
};

export default createStore;
