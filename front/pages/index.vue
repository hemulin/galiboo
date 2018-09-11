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
      }
  },
  computed: {
    resp() {
      return this.$store.getters.resp;
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
      return getColor('ff715b', 'b9d653', this.val4/100);
    }
  }
}
</script>

