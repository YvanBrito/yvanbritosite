<template>
  <nav>
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link @click='selectArea("global")'>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Mundo</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click='selectArea("brasil")'>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Brasil</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click='selectArea("para")'>
          <v-list-item-action>
            <v-icon>mdi-contact-mail</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Para</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      app
      color="indigo"
      dark
      hide-on-scroll
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title style="cursor: pointer" @click="teste()">
        Yvan Brito
      </v-toolbar-title>
      <v-spacer></v-spacer>
      Atualizado em: {{ updateDate }} às {{ updateTime }}
    </v-app-bar>
  </nav>
</template>

<script>
import api from '@/api'

export default {
  name: 'NavBar',
  data() {
    return {
      drawer: false,
      updateDate: '',
      updateTime: ''
    }
  },
  created() {
    api.get('/updateDate')
    .then(response => {
      let date = new Date(response.data + ' UTC')

      this.updateDate = ("0" + date.getDate()).slice(-2) + '/' + ("0" + (date.getMonth() + 1)).slice(-2) + '/' + date.getFullYear()
      this.updateTime = ("0" + date.getHours()).slice(-2) + ':' + ("0" + date.getMinutes()).slice(-2)
    })
  },
  methods: {
    selectArea(area){
      this.$emit('areaSelected', area)
    },
    teste() {
      location.href='http://yvanbrito.com'
    }
  }
}
</script>

<style>
.home-link{
  text-decoration: none;
  color: white;
}
</style>