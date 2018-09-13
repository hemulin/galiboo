<template lang="pug">
div
  circle-slider(
        v-model='value',
        :circle-width='16',
        :progress-width='20',
        :knob-radius='20',
        :progress-color="progrssColor()",
        :side="200")
  .value-display {{ value }}%
</template>
<script>
import Vue from 'vue'
import VueCircleSlider from 'vue-circle-slider'
Vue.use(VueCircleSlider)
export default {
  components: {
    circleslider: VueCircleSlider.VueCircleSlider
  },
  props: {
    // id: String,
    // spotifyId: String,
    // artist: String,
    // title: String,
    // src: String
  },
  data () {
    return {
      value: 0
    }
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
      return getColor('ff715b', 'b9d653', this.value/100);
    }
  }
}
</script>
<style lang="scss" scoped>
.value-display {
    margin: -8rem 0rem 0rem 5rem;
    font-size: 2rem;
    font-weight: 800;
}
</style>
