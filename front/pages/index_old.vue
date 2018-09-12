<template lang="pug">

section.section
  .columns
    .column
      h2 Get resp: {{ resp }}
  .columns
    .column
      circle-slider(
        v-model='val4',
        :circle-width='16',
        :progress-width='20',
        :knob-radius='20',
        :progress-color="progrssColor()",
        :side="200")
</template>

<script>
import Vue from 'vue'
import VueCircleSlider from 'vue-circle-slider'
Vue.use(VueCircleSlider)
export default {
  name: 'HomePage',
  components: {
    circleslider: VueCircleSlider.VueCircleSlider},
  async fetch ({ store }) {
    await store.dispatch('getResp')
  },
  data() {
      return {
          val4: 50,
          player: null
      }
  },
  computed: {
    resp() {
      return this.$store.getters.resp;
    }
  },
  mounted() {
    let spotifyScript = document.createElement('script')
    spotifyScript.setAttribute('src', 'https://sdk.scdn.co/spotify-player.js')
    spotifyScript.async = true
    document.head.appendChild(spotifyScript)
    // this.initSpotify()
    window.onSpotifyWebPlaybackSDKReady = () => {}
    this.initiatePlayer()
  },
  methods: {
    progrssColor() {
      function getColor(hex1, hex2, val) {
        var hex = function(x) {
            x = x.toString(16);
            return (x.length == 1) ? '0' + x : x;
        };
        var r = Math.ceil(parseInt(hex1.substring(0,2), 16) * val + parseInt(hex2.substring(0,2), 16) * (1-val));
        var g = Math.ceil(parseInt(hex1.substring(2,4), 16) * val + parseInt(hex2.substring(2,4), 16) * (1-val));
        var b = Math.ceil(parseInt(hex1.substring(4,6), 16) * val + parseInt(hex2.substring(4,6), 16) * (1-val));

        var middle = hex(r) + hex(g) + hex(b);
        return '#'+middle;
      }
      return getColor('ff715b', 'b9d653', this.val4/100);
    },
    async initSpotify() {
      window.onSpotifyWebPlaybackSDKReady = () => {
        const token = 'BQDRU_gPnV9Whh9VimxWyGbqDkYj1VTjVqgOl9dymu_WOI-FA23GO2su-K_c9Ly0Mkut_ir3vstxn6zOVhBJGOnVFP8en5OMW5ppm3teRTT9ActuKBrxyW7AwxdLEPKVacaXb7DRguXfMMPzHEFgKMOJ54n6I1Ji42Lm';
        this.player = new Spotify.Player({
          name: 'Web Playback SDK Quick Start Player',
          getOAuthToken: cb => { cb(token); }
        });

        // Error handling
        this.player.addListener('initialization_error', ({ message }) => { console.error(message); });
        this.player.addListener('authentication_error', ({ message }) => { console.error(message); });
        this.player.addListener('account_error', ({ message }) => { console.error(message); });
        this.player.addListener('playback_error', ({ message }) => { console.error(message); });

        // Playback status updates
        this.player.addListener('player_state_changed', state => { console.log(state); });

        // Ready
        this.player.addListener('ready', ({ device_id }) => {
          console.log('Ready with Device ID', device_id);
        });

        // Not Ready
        this.player.addListener('not_ready', ({ device_id }) => {
          console.log('Device ID has gone offline', device_id);
        });

        // Connect to the player!
        this.player.connect();
        this.$log.info(this.player);
      };
    },
    waitForSpotifyWebPlaybackSDKToLoad: async function () {
        return new Promise(resolve => {
            if (window.Spotify) {
                resolve(window.Spotify)
            } else {
                window.onSpotifyWebPlaybackSDKReady = () => {
                    resolve(window.Spotify)
                }
            }
        })
    },
    initiatePlayer: async function () {
        const { Player } = await this.waitForSpotifyWebPlaybackSDKToLoad()
        const token = 'BQDRU_gPnV9Whh9VimxWyGbqDkYj1VTjVqgOl9dymu_WOI-FA23GO2su-K_c9Ly0Mkut_ir3vstxn6zOVhBJGOnVFP8en5OMW5ppm3teRTT9ActuKBrxyW7AwxdLEPKVacaXb7DRguXfMMPzHEFgKMOJ54n6I1Ji42Lm';
        const sdk = new Player({
            name: 'Test Web Playback SDK',
            volume: 1.0,
            getOAuthToken: callback => { callback(token) }
        })
        console.log(JSON.stringify(sdk))
        // Error handling
        sdk.addListener('initialization_error', ({ message }) => { console.log('Initialization_error: ' + message) })
        sdk.addListener('authentication_error', ({ message }) => { console.log('Authentication_error: ' + message) })
        sdk.addListener('account_error', ({ message }) => { console.log('Account_error: ' + message) })
        sdk.addListener('playback_error', ({ message }) => { console.log('Playback_error: ' + message) })
        // Playback status updates
        sdk.addListener('player_state_changed', state => {
            // Update UI information on player state changed
        })
        // Ready
        sdk.addListener('ready', ({ deviceId }) => {
            console.log('Ready with Device Id: ', deviceId)
        })
        // Not Ready
        sdk.addListener('not_ready', ({ deviceId }) => {
            console.log('Not ready with device Id: ', deviceId)
        })
        sdk.connect()
    }
  }
}
</script>

