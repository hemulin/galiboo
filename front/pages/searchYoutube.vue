<template lang="pug">

section.section
  .container
    label.label Search youtube
    .field.has-addons
      .control
        input.input(v-model="query", type='text')
      //- p.help This is a help text
      .control
        button.button.is-primary(@click="searchYoutube") Submit
  hr
  .columns.is-multiline.is-mobile
    .column.is-full-mobile.is-half-tablet.is-one-third-desktop.is-one-quarter-widescreen.is-one-fifth-fullhd.is-pulled-left(v-for="res in youtubeResults")
      VideoCard(:title="res.title", :url="res.url", :thumbnail="res.thumbnail", :videoId="res.videoId")

</template>

<script>
import VideoCard from '@/components/VideoCard'
export default {
  name: 'HomePage',
  components: {
    VideoCard
  },
  async fetch ({ store }) {},
  data() {
      return {
        query: ''
    }
  },
  computed: {
    resp() {
      return this.$store.getters.resp;
    },
    youtubeResults() {
      return this.$store.getters.youtubeResults;
    }
  },
  mounted() {
  },
  methods: {
    async searchYoutube() {
      await this.$store.dispatch('searchYoutube', this.query)
    }
  }
}
</script>

