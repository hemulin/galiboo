<template lang="pug">
.card
  .card-content
    p.title.is-size-4 {{ artist }}
    p.subtitletitle.is-size-5  {{ title }}
  .card-content
    //- figure.image.is-4by3
    audio(controls='')
      source(:src='src', type='audio/mpeg')
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
export default {
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
