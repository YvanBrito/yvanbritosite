<template>
    <svg id="my_dataviz" width="400" height="300"></svg>
</template>

<script>
import * as d3 from "d3"

export default {
    name: 'MapaMundi',
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
            loading: false,
            width: 0,
            height: 0,
            data: {}
        }
    },
    mounted() {
        // The svg
        var svg = d3.select("svg"),
            width = +svg.attr("width"),
            height = +svg.attr("height");

        // Map and projection
        var projection = d3.geoNaturalEarth()
            .scale(width / 1.3 / Math.PI)
            .translate([width / 2, height / 2])

        // Load external data and boot
        d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson", function(data){

            // Draw the map
            svg.append("g")
                .selectAll("path")
                .data(data.features)
                .enter().append("path")
                    .attr("fill", "#69b3a2")
                    .attr("d", d3.geoPath()
                        .projection(projection)
                    )
                    .style("stroke", "#fff")
        })
    }
}
</script>

<style>

</style>