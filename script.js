// Define dimensions and margins for the chart
const width = 600;
const height = 600;
const margin = 50;
const radius = Math.min(width, height) / 2 - margin;

// Select the chart container
const svg = d3.select("#chart")
    .style("display", "flex") // Add this
    .style("justify-content", "center") // Add this
    .style("align-items", "center") // Add this
    .style("height", "70vh") // Add this
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", `translate(${width / 2}, ${height / 2})`);


// Read the CSV data
d3.csv("startup_funding.csv").then(function(data) {
    
    // Count occurrences of each industry vertical
    const counts = {};
    data.forEach(d => {
        counts[d.IndustryVertical] = (counts[d.IndustryVertical] || 0) + 1;
    });

    // Transform counts object into an array of objects
    const countsArray = Object.keys(counts).map(key => ({
        IndustryVertical: key,
        count: counts[key]
    }));

    // Sort industry verticals alphabetically
    countsArray.sort((a, b) => a.IndustryVertical.localeCompare(b.IndustryVertical));

    // Scale for the angles
    const x = d3.scaleBand()
        .range([0, 2 * Math.PI])
        .domain(countsArray.map(d => d.IndustryVertical))
        .padding(0.1);

    // Scale for the radius
    const y = d3.scaleLinear()
        .range([margin, radius])
        .domain([0, d3.max(countsArray, d => d.count)]);

    // Add bars
    svg.append("g")
        .selectAll("path")
        .data(countsArray)
        .enter()
        .append("path")
        .attr("fill", "#69b3a2")
        .attr("d", d3.arc()
            .innerRadius(y(0))
            .outerRadius(d => y(d.count))
            .startAngle(d => x(d.IndustryVertical))
            .endAngle(d => x(d.IndustryVertical) + x.bandwidth())
            .padAngle(0.01)
            .padRadius(radius));

    // Add the labels
    svg.append("g")
        .selectAll("g")
        .data(countsArray)
        .enter()
        .append("g")
        .attr("text-anchor", "middle")
        .attr("transform", d => `rotate(${(x(d.IndustryVertical) + x.bandwidth() / 2) * 180 / Math.PI - 90}) translate(${radius + 10},0)`)
        .append("text")
        .text(d => `${d.IndustryVertical} (${d.count})`)
        .attr("transform", d => (x(d.IndustryVertical) + x.bandwidth() / 2 + Math.PI / 2) % (2 * Math.PI) < Math.PI ? "rotate(90)" : "rotate(-90)")
        .style("font-size", "12px")
        .style("font-weight", "bold");

}).catch(function(error) {
    console.log(error);
});
