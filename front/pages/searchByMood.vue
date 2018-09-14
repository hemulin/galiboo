<template lang="pug">

section.section
  .columns.is-multiline.is-mobile
    .column
      CircularSlider(title="Acousticness")
    .column
      CircularSlider(title="Danceability")
    .column
      CircularSlider(title="Energy")
    .column
      CircularSlider(title="Instrumentalness")
    .column
      CircularSlider(title="Valence")

</template>

<script>
import CircularSlider from '@/components/CircularSlider'
export default {
  components: {
    CircularSlider,
  },
  async fetch ({ store }) {},
  data() {
    return {}
  },
  computed: {},
  mounted() {
  }
}
</script>

