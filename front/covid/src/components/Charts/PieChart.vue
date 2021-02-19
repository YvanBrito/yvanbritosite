<template>
  <div :style="{height: height+'px'}">
    <div v-if='loading' class="lds-ripple">
        <div>
        </div>
        <div>
        </div>
    </div>
    <transition name="fade">
        <div v-show="!loading" :id="name"></div>
    </transition>
  </div>
</template>

<script>
import * as d3 from "d3";
import api from '@/api'

export default {
    name: 'PieChart',
    props: {
        name: {
            type: String,
            required: true
        },
        dataPath: {
            type: String,
            required: true
        },
        heightInitial: {
            type: Number,
            default: 200
        }
    },
    data() {
        return {
            loading: true,
            width: 0,
            height: 0,
            data: []
        }
    },
    watch: {
        dataPath() {
            let svg = d3.select(`#${this.name}`).append('svg')
            svg.html("");
            this.getData()
        }
    },
    created(){
        this.height = this.heightInitial
    },
    mounted() {
        this.getData()
        this.$nextTick(() => {
            window.addEventListener('resize', () => {
                this.width = 100
                this.setChart()
                this.width = parseFloat(d3.select(`#${this.name}`).style('width'))
                this.setChart()
                })
        })
    },
    updated() {
        this.width = parseFloat(d3.select(`#${this.name}`).style('width'))
        this.setChart()
    },
    beforeDestroy() {
        this.data = []
    },
    methods: {
        getData(){
            d3.select(`#${this.name}`).html("");
            api.get('/worldregions')
            .then(response => {
                this.loading = false
                this.data = response.data
            })
        },
        setChart() {
            d3.select(`#${this.name}`).html("");
            // set the dimensions and margins of the graph
            var margin = 40

            // The radius of the pieplot is half the this.width or half the this.height (smallest one). I subtract a bit of margin.
            let radius = Math.min(this.width, this.height) / 2 - margin

            // append the svg object to the div called 'my_dataviz'
            let svg = d3.select(`#${this.name}`).append("svg")
                .attr("width", this.width + margin)
                .attr("height", this.height + margin)
            .append("g")
                .attr("transform", "translate(" + this.width / 2 + "," + this.height / 2 + ")");

            // Create dummy data
            // var data = {a: 9, b: 20, c:30, d:8, e:12}
            // var data = [{"Region": "Americas", "value": 2416970}, {"Region": "Europe", "value": 1838914}, {"Region": "Asia", "value": 803588}, {"Region": "Africa", "value": 239593}, {"Region": "Oceania", "value": 10585}]

            // set the color scale
            let color = d3.scaleOrdinal()
            .domain(this.data.map(function(d) { return d.Region; }))
            .range(["#52D726", "#FFEC00", "#FF7300", "#FF0000", "#007ED6"])

            // Compute the position of each group on the pie:
            let pie = d3.pie()
            .value(function(d) { return d.value.value; })
            let data_ready = pie(d3.entries(this.data))

            // Build the pie chart: Basically, each part of the pie is a path that we build using the arc function.
            svg
            .selectAll('whatever')
            .data(data_ready)
            .enter()
            .append('path')
            .attr('d', d3.arc()
                .innerRadius(0)
                .outerRadius(radius)
            )
            .attr('fill', function(d){ return(color(d.data.value.Region)) })
            .style("opacity", 0.8)
            .on('mouseover', d => {
                console.log(d)
            })
            .on('mouseout', () => {
                console.log('teste2')
            })

            svg.append("g")
            .attr('id', 'legend')
            .selectAll()
            .data(data_ready)
            .enter()
            .append("circle")
            .attr("cx",120)
            .attr("cy",-140)
            .attr("r", 6)
            .style("fill", function(d){ return(color(d.data.value.Region)) })
            .append("text").text(function(d){ return(d.data.value.Region)})

            svg.select('#legend')
            .selectAll()
            .data(data_ready)
            .enter()

            // legend.append("circle").attr("cx",200).attr("cy",100).attr("r", 6).style("fill", "rgb(70, 130, 180)")
            // legend.append("circle").attr("cx",200).attr("cy",130).attr("r", 6).style("fill", "rgb(182, 63, 63)")
            // legend.append("circle").attr("cx",200).attr("cy",160).attr("r", 6).style("fill", "rgb(61, 235, 128)")
            // legend.append("text").attr("x", 220).attr("y", 100).text("Confirmados").style("font-size", "15px").attr("alignment-baseline","middle")
            // legend.append("text").attr("x", 220).attr("y", 130).text("Mortos").style("font-size", "15px").attr("alignment-baseline","middle")
            // legend.append("text").attr("x", 220).attr("y", 160).text("Recuperados").style("font-size", "15px").attr("alignment-baseline","middle")
        }
    }
}
</script>

<style>

</style>