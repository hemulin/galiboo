<template lang="pug">

section.section
  .columns.is-multiline.is-mobile
    .column
      CircularSlider
    .column
      CircularSlider
    .column
      CircularSlider
    .column
      CircularSlider
    .column
      CircularSlider

  .columns.is-multiline.is-mobile
    //- .column.is-full-mobile.is-half-tablet.is-one-third-desktop.is-one-quarter-widescreen.is-one-fifth-fullhd.is-pulled-left(v-for="res in youtubeResults")
      VideoCard(:title="res.title", :url="res.url", :thumbnail="res.thumbnail", :videoId="res.videoId")

</template>

<script>
import CircularSlider from '@/components/CircularSlider'
import VideoCard from '@/components/VideoCard'
export default {
  name: 'HomePage',
  components: {
    CircularSlider,
    VideoCard
  },
  async fetch ({ store }) {},
  data() {
    return {
      youtubeResults: []
    }
  },
  computed: {
    // youtubeResults() {
    //   // return this.$store.getters.youtubeResults
    //   return [];
    // }
  },
  mounted() {
  }
}
</script>

