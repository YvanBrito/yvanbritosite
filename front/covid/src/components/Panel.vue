<template>
  <v-row>
    <v-col>
      <Card 
        title='Confirmados' 
        :enableToolbar='false' 
        :isLoading="isLoading">
        <div v-if='isLoading' class="text--primary">
          Loading
        </div>
        <div v-else class="d-flex justify-space-between">
          <div>
            <p class="display-1 text--primary">
              {{ confirmed | formatNumber }}
            </p>
            <div class="text--primary">
              Confirmados
            </div>
          </div>
        </div>
      </Card>
    </v-col>
    <v-col>
      <Card title='Óbitos' :enableToolbar='false' :isLoading="isLoading">
        <div v-if='isLoading' class="text--primary">
          Loading
        </div>
        <div v-else class="d-flex justify-space-between">
          <div>
            <p class="display-1 text--primary">
              {{ deaths | formatNumber }}
            </p>
            <div class="text--primary">
              Óbitos
            </div>
          </div>
        </div>
      </Card>
    </v-col>
    <v-col>
      <Card title='Recuperados' :enableToolbar='false' :isLoading="isLoading">
        <div v-if='isLoading' class="text--primary">
          Loading
        </div>
        <div v-else class="d-flex justify-space-between">
          <div>
            <p class="display-1 text--primary">
              {{ recovered | formatNumber }}
            </p>
            <div class="text--primary">
              Recuperados
            </div>
          </div>
        </div>
      </Card>
    </v-col>
    <v-col>
      <Card title='Letalidade' :enableToolbar='false' :isLoading="isLoading">
        <div v-if='isLoading' class="text--primary">
          Loading
        </div>
        <div v-else class="d-flex justify-space-between">
          <div>
            <p class="display-1 text--primary">
              {{ letality | formatNumber }}%
            </p>
            <div class="text--primary">
              Taxa de Letalidade
            </div>
          </div>
        </div>
      </Card>
    </v-col>
  </v-row>
</template>

<script>
import Card from './Card'
import api from '@/api'

export default {
  name: 'Panel',
  components: {
    Card
  },
  props: {
    area: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      confirmed: 0,
      deaths: 0,
      recovered: 0,
      letality: 0,
      isLoading: true
    }
  },
  created() {
    this.getData()
  },
  watch: {
    area() {
      this.getData()
    }
  },
  filters: {
    formatNumber(num) {
      return num.toString().replace('.', ',').replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.')
    }
  },
  methods: {
    getData() {
      this.isLoading = true
      api.get(`/${this.area}`)
        .then(response => {
          this.isLoading = false
          this.confirmed = response.data[response.data.length-1].confirmed
          this.deaths = response.data[response.data.length-1].deaths
          this.recovered = response.data[response.data.length-1].recovered
          this.letality = Math.round(((this.deaths/this.confirmed)*100 + Number.EPSILON) * 100) / 100
        })
    }
  }
}
</script>

<style>
</style>