import Vuex from 'vuex';

const createStore = () => {
  return new Vuex.Store({
    state: {
      counter: 0,
      pages: [],
      resp: '',
      youtubeResults: []
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
      },
      updateYoutubeResults: (state, data) => {
        state.youtubeResults = data;
      }
    },
    actions: {
      fetchData({ commit }) {
        commit('getPages', {
          1: { name: 'index' },
          2: { name: 'search' }
        });
      },
      async searchYoutube({ commit }, query) {
        try {
          let resp = await this.$axios.$get(`/search_youtube?q=${query}`);
          commit('updateYoutubeResults', resp);
        } catch (e) {
          // this.$log.error('getResp: backend call error', e);
          console.log('searchYoutube: backend call error', e);
        }
      },
      async getResp({ commit }) {
        try {
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
      },
      youtubeResults(state) {
        return state.youtubeResults;
      }
    }
  });
};

export default createStore;
