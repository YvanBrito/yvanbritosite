<template>
  <div>
    <svg :id="name" :width="width" :height="height"></svg>
  </div>
</template>

<script>
import * as d3 from "d3";

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
        width: {
            type: Number,
            default: 200
        },
        height: {
            type: Number,
            default: 200
        }
    },
    mounted() {
        this.setChart()
    },
    methods: {
        setChart() {
            // set the dimensions and margins of the graph
            var margin = 40

            // The radius of the pieplot is half the this.width or half the this.height (smallest one). I subtract a bit of margin.
            var radius = Math.min(this.width, this.height) / 2 - margin

            // append the svg object to the div called 'my_dataviz'
            var svg = d3.select(`#${this.name}`)
            .append("g")
                .attr("transform", "translate(" + this.width / 2 + "," + this.height / 2 + ")");

            // Create dummy data
            var data = {a: 9, b: 20, c:30, d:8, e:12}

            // set the color scale
            var color = d3.scaleOrdinal()
            .domain(data)
            .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56"])

            // Compute the position of each group on the pie:
            var pie = d3.pie()
            .value(function(d) {return d.value; })
            var data_ready = pie(d3.entries(data))

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
            .attr('fill', function(d){ return(color(d.data.key)) })
            .attr("stroke", "black")
            .style("stroke-width", "2px")
            .style("opacity", 0.7)
        }
    }
}
</script>

<style>

</style>