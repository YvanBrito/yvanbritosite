<template>
  <v-container
    class="fill-height"
    fluid
  >
    <Panel :area="area"/>
    
    <v-row>
      <v-col 
        :lg="8"
        :md="8"
        :sm="12">
        <Card
          :title="'Número de Casos'">
        <LineChart
          :name='"mortespordia1"'
          :dataPath='area'
          :heightInitial='300'/>
      </Card>
      </v-col>
      <v-col
        :lg="4"
        :md="4"
        :sm="12">
        <Card :title="'Nº de casos por continente'">
          <PieChart
              :name='"mortespordia4"'
              :dataPath='area'
              :heightInitial='300'/>
        </Card>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        :lg="8"
        :md="8"
        :sm="12">
        <Card
          :title="'Top 10 número de Casos'">
          <BarChart
              :name='"mortespordia3"'
              :dataPath='area'
              :heightInitial='300'/>
        </Card>
      </v-col>
      <v-col
        :lg="4"
        :md="4"
        :sm="12">
        <Card :title="'Nº de casos por região'">
          
        </Card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Panel from './Panel'
import Card from './Card'
import LineChart from './Charts/LineChart'
import BarChart from './Charts/BarChart'
import PieChart from './Charts/PieChart'


export default {
  components: {
    Panel,
    Card,
    LineChart,
    BarChart,
    PieChart
  },
  props: {
    area: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
.dashboard {
  border: 1px solid rgba(98, 182, 255, 0.8);
  border-radius: 8px;
  padding: 10px;
  margin-bottom: 10px;
  margin-top: 70px;
  width: 90%;
  position: absolute;
  left: 50%;
  -ms-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
}
</style>