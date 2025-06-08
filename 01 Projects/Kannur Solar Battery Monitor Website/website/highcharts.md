```JS

function createChart(containerId, title, yAxisTitle, seriesName) {
  return Highcharts.chart(containerId, {
    chart: {
      backgroundColor: "#3b4252",
      type: "line",
    },
    title: {
      text: title,
      style: {
        color: getComputedStyle(document.documentElement).getPropertyValue(
          "--nord4",
        ),
      },
    },
    xAxis: {
      type: "datetime",
      title: {
        text: "Time",
        style: {
          color: getComputedStyle(document.documentElement).getPropertyValue(
            "--nord4",
          ),
        },
      },
      labels: {
        style: {
          color: getComputedStyle(document.documentElement).getPropertyValue(
            "--nord4",
          ),
        },
      },
    },
    yAxis: {
      title: {
        text: yAxisTitle,
        style: {
          color: getComputedStyle(document.documentElement).getPropertyValue(
            "--nord4",
          ),
        },
      },
      labels: {
        style: {
          color: getComputedStyle(document.documentElement).getPropertyValue(
            "--nord4",
          ),
        },
      },
    },
    series: [
      {
        name: seriesName,
        data: [],
        color: getComputedStyle(document.documentElement).getPropertyValue(
          "--nord8",
        ),
      },
    ],
    legend: {
      itemStyle: {
        color: getComputedStyle(document.documentElement).getPropertyValue(
          "--nord4",
        ),
      },
    },
    credits: {
      enabled: false,
    },
  });
}
```