<template lang="pug">

section.section
  .columns.is-mobile
    .column(v-for='(feature, i) of features', :key='i')
      .card
        header.card-header
          p.card-header-title.has-text-grey {{ feature.title }}
        .card-content
          .content.has-text-centered
            b-icon(:icon='feature.icon', size='is-large', type='is-primary')
            b-icon(:icon='feature.icon', size='is-large', type='is-info')
            b-icon(:icon='feature.icon', size='is-large', type='is-success')
            b-icon(:icon='feature.icon', size='is-large', type='is-warning')
            b-icon(:icon='feature.icon', size='is-large', type='is-danger')
        footer.card-footer
          .card-footer-item(v-html='feature.content')
</template>

<script>
import BLogo from '@/components/Logo'

export default {
  name: 'HomePage',
  components: {BLogo},
  data() {
      return {
          features: [
              { icon: 'github-circle', title: 'Free', content: `<span>Open source on <a href="https://github.com/buefy/buefy"> GitHub</a></span>` },
              { icon: 'cellphone-link', title: 'Responsive', content: `<span><b class="has-text-grey">Every</b> component is responsive</span>` },
              { icon: 'alert-decagram', title: 'Modern', content: `<span>Built with <a href="https://vuejs.org/">Vue.js</a> and <a href="http://bulma.io/">Bulma</a></span>` },
              { icon: 'arrange-bring-to-front', title: 'Lightweight', content: `<span>No other internal dependency</span>` }
          ]
      }
  }
}
</script>

