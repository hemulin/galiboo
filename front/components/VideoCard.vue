<template lang="pug">
.card
  .card-image
    //- figure.image.is-4by3
    figure
      iframe.ytplayer(type='text/html', :src="src", frameborder='0')
  .card-content
    .content
      p.title.is-size-4 {{ title }}
</template>
<script>
export default {
  props: {
    title: String,
    url: String,
    thumbnail: String,
    videoId: String
  },
  data () {
    return {
      src: `https://www.youtube.com/embed/${this.videoId}?autoplay=0`
    }
  }
}
</script>
<style lang="scss" scoped>
.ytplayer {
  width: 100%;
}
</style>
