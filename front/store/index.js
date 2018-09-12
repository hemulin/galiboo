import Vuex from 'vuex';

const createStore = () => {
  return new Vuex.Store({
    state: {
      loading: false,
      pages: [],
      resp: '',
      galibooResults: [],
      youtubeResults: []
    },
    mutations: {
      toggleLoading(state) {
        state.loading = !state.loading;
      },
      getPages(state, data) {
        state.pages = data;
      },
      updateResp: (state, resp) => {
        state.resp = resp;
      },
      updateGalibooResults: (state, data) => {
        state.galibooResults = data;
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
      async searchGaliboo({ commit }, query) {
        try {
          commit('toggleLoading');
          commit('updateGalibooResults', []);
          let resp = await this.$axios.$get(`/search_galiboo_smart_search?q=${query}`);
          commit('updateGalibooResults', resp);
          commit('toggleLoading');
        } catch (e) {
          // this.$log.error('getResp: backend call error', e);
          console.log('searchGaliboo: backend call error', e);
        }
      },
      async searchGalibooTracks({ commit }, query) {
        try {
          commit('toggleLoading');
          commit('updateGalibooResults', []);
          let resp = await this.$axios.$get(`/search_galiboo_tracks?q=${query}`);
          commit('updateGalibooResults', resp);
          commit('toggleLoading');
        } catch (e) {
          // this.$log.error('getResp: backend call error', e);
          console.log('searchGaliboo: backend call error', e);
        }
      },
      async searchGalibooTracksByArtist({ commit }, query) {
        try {
          commit('toggleLoading');
          commit('updateGalibooResults', []);
          let resp = await this.$axios.$get(`/search_galiboo_tracks_by_artist?q=${query}`);
          commit('updateGalibooResults', resp);
          commit('toggleLoading');
        } catch (e) {
          // this.$log.error('getResp: backend call error', e);
          console.log('searchGaliboo: backend call error', e);
        }
      },
      async searchGalibooSimiliar({ commit }, track_id) {
        try {
          commit('toggleLoading');
          commit('updateGalibooResults', []);
          let resp = await this.$axios.$get(`/search_galiboo_similiar?track_id=${track_id}`);
          commit('updateGalibooResults', resp);
          commit('toggleLoading');
        } catch (e) {
          // this.$log.error('getResp: backend call error', e);
          console.log('searchGaliboo: backend call error', e);
        }
      },
      async searchYoutube({ commit }, query) {
        try {
          commit('toggleLoading');
          let resp = await this.$axios.$get(`/search_youtube?q=${query}`);
          commit('updateYoutubeResults', resp);
          commit('toggleLoading');
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
      loading(state) {
        return state.loading;
      },
      galibooResults(state) {
        return state.galibooResults;
      },
      youtubeResults(state) {
        return state.youtubeResults;
      }
    }
  });
};

export default createStore;
