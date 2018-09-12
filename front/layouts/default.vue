<template lang="pug">
div
  nav.navbar.header.has-shadow.is-primary(role='navigation', aria-label='main navigation')
    .navbar-brand
      a.navbar-item(href='/')
        h2 Galiboo
      .navbar-menu.is-hidden-desktop(:class="{ 'active': showNav }", @click='toggleMobileNav()')
        .navbar-start
          nuxt-link.navbar-item(v-for='(item, key) of items', :key='key',:to='item.to', exact-active-class='is-active')
            span.menu-link {{ item.title }}
      span.navbar-burger.burger(@click='toggleMobileNav()', :class="{ 'is-active': showNav }")
        span
        span
        span
  section.main-content.columns
    aside.column.is-2.section.is-hidden-touch
      ul.menu-list
        li(v-for='(item, key) of items', :key='key')
          nuxt-link(:to='item.to', exact-active-class='is-active')
            b-icon(:icon='item.icon')
            span.sidebar-title {{ item.title }}
    .column.is-10
      nuxt
</template>
<script>
export default {
  data() {
    return {
      showNav: false,
      items: [
        { title: 'Home', icon: 'home', to: { name: 'index' } },
        { title: 'Search by Mood', icon: 'lightbulb', to: { name: 'searchByMood' } },
        { title: 'Search by Similiar', icon: 'lightbulb', to: { name: 'searchSimiliar' } }
      ]
    }
  },
  mounted () {
  },
  methods: {
    toggleMobileNav () {
      this.showNav = !this.showNav
    },
    exampleLog() {
      this.$log.debug('foo')
      this.$log.info({foo: 'bar'})
      this.$log.warn('warning!')
      this.$log.error('Error', 500)
    }
  }
}
</script>
<style lang="scss" scoped>
@import '~@/assets/scss/style.scss';
@import '~@/assets/scss/mixins.scss';
.logo {
  margin-right: 10px;
}

.menu-link {
  // color: $link-invert;
}

.navbar {
  .container {
    @include mobile-landscape {
      display: flex;
    }
  }
}
.navbar-brand {
  position: relative;
  z-index: 11;
  .navbar-menu {
    @include mobile-landscape {
      height: 0;
      overflow: hidden;
      transition: height ease 0.5s;
      display: block;
      padding:0;
      position: absolute;
      top: 52px;
      width: 100%;
      &.active {
        height: 165px;
      }
    }
  }
}
.header-navbar {
  height: 4.5rem;

  @media screen and (max-width: 1023px) {
    height: initial;
  }
}

.issuer-logo {
  max-width: 100%;
  transition: transform 0.15s;
  transform: scale(1);

  &:hover {
    transition: transform 0.15s;
    transform: scale(1.1);
  }
}

a.navbar-item {
  // color: $text-opaque;
  // font-size: $text-large-size;
  text-decoration: none;

  &:hover {
      // color: #fff;
      text-decoration: none;
  }
}

// mobile menu
.navbar-burger.burger.is-active {
  span {
    // background-color: white;
  }
}

.navbar-burger {
  span {
    // background-color: white
  }
}

@media screen and (max-width: 1023px) {
  .navbar-end {
    display: flex;
    height: 52px;
    position: absolute;
    right: 0;
    top: 0;
  }
}

@media screen and (max-width: 768px) {
  .container {
    padding: 0;
  }
}

.sidebar-title {
  margin-left: .5rem;
}
</style>

