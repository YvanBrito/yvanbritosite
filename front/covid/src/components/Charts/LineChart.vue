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
    name: 'LineChart',
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
            data: {}
        }
    },
    watch: {
        dataPath() {
            let svg = d3.select(`#${this.name}`).append('svg-component')
                .attr("width", 0)
                .attr("height", 0)
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
        this.data = {}
    },
    methods: {
        getData(){
            this.loading = true
            d3.select(`#${this.name}`).html("");
            api.get(`/${this.dataPath}/`)
                .then(response => {
                    this.loading = false
                    this.data = response.data
                    
                    // parse the date / time
                    let parseTime = d3.timeParse("%m/%d/%y");
                    // format the data
                    this.data.forEach(function(d) {
                        d.date = parseTime(d.date);
                        d.confirmed = +d.confirmed;
                        d.deaths = +d.deaths;
                        d.recovered = +d.recovered;
                    });
                })
        },
        setChart() {
            d3.select(`#${this.name}`).html("");
            let margin = {top: 20, right: 20, bottom: 50, left: 70},
                width = this.width - margin.left - margin.right,
                height = this.height - margin.top - margin.bottom;

            // set the ranges
            let x = d3.scaleTime().range([0, width]);
            let y = d3.scaleLinear().range([height, 0]);
            //let y = d3.scaleSymlog().range([height, 0]);

            // define the line
            let valuelineConfirmed = d3.line()
                .x(function(d) { return x(d.date); })
                .y(function(d) { return y(d.confirmed); });
            
            let valuelineDeaths = d3.line()
                .x(function(d) { return x(d.date); })
                .y(function(d) { return y(d.deaths); });
            
            let valuelineRecovered = d3.line()
                .x(function(d) { return x(d.date); })
                .y(function(d) { return y(d.recovered); });

            // append the svg obgect to the body of the page
            // appends a 'group' element to 'svg'
            // moves the 'group' element to the top left margin
            let svg = d3.select(`#${this.name}`).append('svg')
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");
            
            

            // Scale the range of the data
            x.domain(d3.extent(this.data, function(d) { return d.date; }));
            y.domain([0, d3.max(this.data, function(d) { return d.confirmed; })]);
            
            // Add the valueline path.
            svg.append("path")
                .data([this.data])
                .attr("class", "confirmed")
                .attr("d", valuelineConfirmed);
            
            svg.append("path")
                .data([this.data])
                .attr("class", "deaths")
                .attr("d", valuelineDeaths);
            
            svg.append("path")
                .data([this.data])
                .attr("class", "recovered")
                .attr("d", valuelineRecovered);

            // Add the x Axis
            svg.append("g")
                .attr("transform", "translate(0," + height + ")")
                .call(d3.axisBottom(x))
                .selectAll("text")
                    .attr("transform", "translate(-10,10)rotate(-45)")
                    .style("text-anchor", "end");

            svg.append("text")             
                .attr("transform",
                        "translate(" + (width/2) + " ," + 
                                    (height + margin.top + 30) + ")")
                .style("text-anchor", "middle")
                .text("Data");

            // Add the y Axis
            svg.append("g")
                .call(d3.axisLeft(y)
                .tickFormat(function (d) {
                if ((d / 1000000) >= 1) {
                    d = d / 1000000 + "KK";
                } else if ((d / 1000) >= 1) {
                    d = d / 1000 + "K";
                }
                return d;
                }))

            svg.append("text")
                .attr("transform", "rotate(-90)")
                .attr("y",10 - margin.left)
                .attr("x",0 - (height / 2))
                .attr("dy", "1em")
                .style("text-anchor", "middle")
                .text("Casos");

            let legend = svg.append("g").attr("class", "legend")
            .attr("transform",
                        "translate(-170,-80)")
            legend.append("circle").attr("cx",200).attr("cy",100).attr("r", 6).style("fill", "rgb(70, 130, 180)")
            legend.append("circle").attr("cx",200).attr("cy",130).attr("r", 6).style("fill", "rgb(182, 63, 63)")
            legend.append("circle").attr("cx",200).attr("cy",160).attr("r", 6).style("fill", "rgb(61, 235, 128)")
            legend.append("text").attr("x", 220).attr("y", 100).text("Confirmados").style("font-size", "15px").attr("alignment-baseline","middle")
            legend.append("text").attr("x", 220).attr("y", 130).text("Mortos").style("font-size", "15px").attr("alignment-baseline","middle")
            legend.append("text").attr("x", 220).attr("y", 160).text("Recuperados").style("font-size", "15px").attr("alignment-baseline","middle")
        }
    }
}
</script>

<style>
/* Fade Animation */
.fade-enter {
    opacity: 0;
}
.fade-enter-active {
    transition: opacity 1s;
}

/* Chart */
.confirmed {
  fill: none;
  stroke: rgb(70, 130, 180);
  stroke-width: 4px;
}
.deaths {
  fill: none;
  stroke: rgb(182, 63, 63);
  stroke-width: 4px;
}
.recovered {
  fill: none;
  stroke: rgb(61, 235, 128);
  stroke-width: 4px;
}
.legend {
    border: 1px solid black;
}

/* Loader animated icon */
.lds-ripple {
  display: inline-block;
  position: relative;
  left: 45%;
  top: 30%;
  width: 80px;
  height: 80px;
}
.lds-ripple div {
  position: absolute;
  border: 4px solid #56a1c7;
  opacity: 1;
  border-radius: 50%;
  animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}
.lds-ripple div:nth-child(2) {
  animation-delay: -0.5s;
}
@keyframes lds-ripple {
  0% {
    top: 36px;
    left: 36px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0px;
    left: 0px;
    width: 72px;
    height: 72px;
    opacity: 0;
  }
}

</style>