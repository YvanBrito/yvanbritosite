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
      this.updateDate = response.data.split(' ')[0]
      this.updateDate = this.updateDate.split('-')[2] + '-' + this.updateDate.split('-')[1] + '-' + this.updateDate.split('-')[0]

      this.updateTime = response.data.split(' ')[1]
      this.updateTime = this.updateTime.split(':')[0] + ':' + this.updateTime.split(':')[1]
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