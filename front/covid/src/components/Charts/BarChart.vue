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
            api.get('/toptenconfirmed')
            .then(response => {
                this.loading = false
                this.data = response.data
            })
        },
        setChart() {
            d3.select(`#${this.name}`).html("");
            let svg = d3.select(`#${this.name}`).append('svg'),
            margin = {
                top: 20,
                right: 20,
                bottom: 30,
                left: 50
            },
            width = this.width - margin.left - margin.right,
            height = this.height - margin.top - margin.bottom
            
            svg.attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
            
            let g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            let x = d3.scaleBand()
                .rangeRound([0, width])
                .padding(0.1);

            let y = d3.scaleLinear()
                .rangeRound([height, 0]);

            x.domain(this.data.map(function (d) {
                    return d.Country;
                }));
            y.domain([0, d3.max(this.data, function (d) {
                        return Number(d.value);
                    })]);

            g.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x))

            g.append("g")
            .call(d3.axisLeft(y))
            .append("text")
            .attr("fill", "#000")
            .attr("transform", "rotate(-90)")
            .attr("y", 6)
            .attr("dy", "0.71em")
            .attr("text-anchor", "end")
            .text("Speed");

            g.selectAll(".bar")
            .data(this.data)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("x", function (d) {
                return x(d.Country);
            })
            .attr("y", function (d) {
                return y(Number(d.value));
            })
            .attr("width", x.bandwidth())
            .attr("height", function (d) {
                return height - y(Number(d.value));
            });
        }
    }
}
</script>

<style>
.bar {
    fill: steelblue;
}

.bar:hover {
    fill: brown;
}
</style>