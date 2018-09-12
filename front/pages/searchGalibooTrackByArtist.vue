<template lang="pug">

section.section
  .container
    label.label Enter artist
    .field.has-addons
      .control
        input.input(v-model="query", type='text')
      //- p.help This is a help text
      .control
        button.button.is-primary(@click="searchGalibooArtist") Submit
  hr
  b-loading(:is-full-page='isFullPage', :active.sync='loading')
  .columns.is-multiline.is-mobile
    .column.is-full-mobile.is-half-tablet.is-one-third-desktop.is-one-quarter-widescreen.is-one-fifth-fullhd.is-pulled-left(v-for="res in galibooResults")
      AudioCard(:artist="res.artist", :title="res.title", :src="res.audioUrl", :spotifyId="res.spotifyId", :id="res.id")

</template>

<script>
import AudioCard from '@/components/AudioCard'
export default {
  name: 'HomePage',
  components: {
    AudioCard
  },
  async fetch ({ store }) {},
  data() {
      return {
        isFullPage: true,
        query: ''
      }
  },
  computed: {
    loading() {
      return this.$store.getters.loading;
    },
    galibooResults() {
      return this.$store.getters.galibooResults;
    }
  },
  mounted() {
  },
  methods: {
    async searchGalibooArtist() {
      await this.$store.dispatch('searchGalibooTracksByArtist', this.query)
    }
  }
}
</script>

