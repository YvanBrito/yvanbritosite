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
import * as d3 from "d3"
import api from '@/api'

export default {
    name: 'BarChart',
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
            var margin = {top: 20, right: 30, bottom: 40, left: 90},
                width = this.width - margin.left - margin.right,
                height = this.height - margin.top - margin.bottom;

            // append the svg object to the body of the page
            var svg = d3.select(`#${this.name}`)
            .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

            // Parse the Data
            var x = d3.scaleLinear()
                .domain([0, 2134000])
                .range([ 0, width]);
            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x))
                .selectAll("text")
                .attr("transform", "translate(-10,0)rotate(-45)")
                .style("text-anchor", "end");

            // Y axis
            var y = d3.scaleBand()
                .range([ 0, height ])
                .domain(this.data.map(function(d) { return d.Region; }))
                .padding(.1);
            svg.append("g")
                .call(d3.axisLeft(y))

            //Bars
            svg.selectAll("myRect")
                .data(this.data)
                .enter()
                .append("rect")
                .attr("x", x(0) )
                .attr("y", function(d) { return y(d.Region); })
                .attr("width", function(d) { return x(d.value); })
                .attr("height", y.bandwidth() )
                .attr("fill", "#69b3a2")
        }
    }
}
</script>

<style>

</style>