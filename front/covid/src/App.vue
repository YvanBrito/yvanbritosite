<template>
  <v-app>
    <NavBar @areaSelected='changeArea'/>

    <v-content>
      <Dashboard :area="area"/>
    </v-content>

    <v-footer
      color="indigo"
    >
      <v-spacer></v-spacer>
      <span class="white--text">&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar.vue'
import Dashboard from './components/Dashboard.vue'

// https://covid.saude.gov.br/
// https://www.covid-19.pa.gov.br/
// https://github.com/CSSEGISandData/COVID-19
// https://github.com/tookit/vue-material-admin

// https://materialdesignicons.com/
export default {
  name: 'App',
  components: {
    NavBar,
    Dashboard
  },
  props: {
    source: String,
  },
  data() {
    return{
      area: 'global',
    }
  },
  methods: {
    changeArea(area){
      this.area = area
    }
  }
}
</script>

<style>

</style>
