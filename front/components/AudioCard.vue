<template lang="pug">
.card
  .card-content
    p.title.is-size-4 {{ artist }}
    p.subtitletitle.is-size-5  {{ title }}
  .card-content
    //- figure.image.is-4by3
    audio(controls='')
      source(:src='src', type='audio/mpeg')
    //- av-line(:line-width='2', line-color='lime', :audio-src='src')
  footer.card-footer
    p.card-footer-item
      span
        p Like
    p.card-footer-item
      span
        p Dislike
    p.card-footer-item
      span
        button.button.is-primary(@click="searchSimiliar") Search
</template>
<script>
import AudioVisual from 'vue-audio-visual'
import AvLine from '~/node_modules/vue-audio-visual/src/components/AvLine.js'
export default {
  components: {
    'av-line': AvLine
  },
  props: {
    id: String,
    spotifyId: String,
    artist: String,
    title: String,
    src: String
  },
  data () {
    return {}
  },
  methods: {
    async searchSimiliar() {
      await this.$store.dispatch('searchGalibooSimiliar', this.id)
    }
  }
}
</script>
<style lang="scss" scoped>
.ytplayer {
  width: 100%;
}
</style>
