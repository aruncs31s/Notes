---
id: Full Code
aliases: []
tags: []
---

```javascript
document.addEventListener("DOMContentLoaded", function () {
  const current_node = document
    .getElementById("current-node")
    .innerHTML.split(":")
    .map((part) => part.trim())[1];
  console.log("Curret node : " + current_node);
  // Ensure the DOM is fully loaded before initializing charts
  if (document.getElementById("chart-battery")) {
    console.log("Initializing charts...");
    const charts = {
      battery: createChart(
        "chart-battery",
        "Battery Voltage (Today)", // Updated title
        "Voltage (V)",
        "Battery Voltage",
      ),
      old_battery_1: createChart(
        "chart-battery_prev_1",
        "Battery Voltage (Yesterday)", // Updated title
        "Voltage (V)",
        "Battery Voltage",
      ),
      old_battery_2: createChart(
        "chart-battery_prev_2",
        "Battery Voltage (2 Days Ago)", // Updated title
        "Voltage (V)",
        "Battery Voltage",
      ),
      old_battery_3: createChart(
        "chart-battery_prev_3",
        "Battery Voltage (3 Days Ago)", // Updated title
        "Voltage (V)",
        "Battery Voltage",
      ),
      old_battery_4: createChart(
        "chart-battery_prev_4",
        "Battery Voltage (4 Days Ago)", // Updated title
        "Voltage (V)",
        "Battery Voltage",
      ),
      old_battery_5: createChart(
        "chart-battery_prev_5",
        "Battery Voltage (5 Days Ago)", // Updated title
        "Voltage (V)",
        "Battery Voltage",
      ),
      old_battery_6: createChart(
        "chart-battery_prev_6",
        "Battery Voltage (6 Days Ago)", // Updated title
        "Voltage (V)",
        "Battery Voltage",
      ),
    };
    // For live graph data (current day)
    let initialChartData = [];

    function updateOldCharts() {
      for (let i = 1; i <= 6; i++) {
        fetch(`/api/data/old?device_id=${current_node}&day=${i}`)
          .then((response) => {
            console.log(`Response from /api/data for prev_${i}:`, response);
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
          })
          .then((data) => {
            if (data.length > 0) {
              const chartData = data.map((reading) => [
                new Date(reading.timestamp).getTime() +
                  new Date().getTimezoneOffset() * -60000,
                reading.battery_voltage,
              ]);
              const chartKey = `old_battery_${i}`;
              if (charts[chartKey]) {
                charts[chartKey].series[0].setData(chartData);
              } else {
                console.error(`Chart ${chartKey} not found.`);
              }
            } else {
              console.log(`No data available for prev_${i}`);
              // Optionally clear the chart or show a message
              const chartKey = `old_battery_${i}`;
              if (charts[chartKey]) {
                charts[chartKey].series[0].setData([]);
              }
            }
          })
          .catch((error) =>
            console.error(`Error fetching data for prev_${i}:`, error),
          );
      }
    }

    // Function to update the main dashboard elements and today's chart
    function updateDashboard() {
      fetch(`/api/data?device_id=${current_node}`) // Fetch today's data
        .then((response) => {
          console.log("Response from /api/data (today):", response);
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          return response.json();
        })
        .then((data) => {
          if (data.length > 0) {
            const latest = data[data.length - 1];
            // Update battery voltage display
            if (latest.hasOwnProperty("battery_voltage")) {
              const batteryElement = document.getElementById("battery");
              if (batteryElement) {
                batteryElement.textContent = latest.battery_voltage;
              } else {
                console.error("Battery element not found in DOM.");
              }
            } else {
              console.error(
                "battery_voltage property is missing in the latest data",
              );
            }

            // Prepare and set data for today's chart only
            initialChartData = data.map((reading) => [
              new Date(reading.timestamp).getTime() +
                new Date().getTimezoneOffset() * -60000,
              reading.battery_voltage,
            ]);
            charts.battery.series[0].setData(initialChartData);

            // Removed lines updating old charts here
          } else {
            console.log("No data available for today");
            // Optionally clear today's chart or show a message
            charts.battery.series[0].setData([]);
            const batteryElement = document.getElementById("battery");
            if (batteryElement) {
              batteryElement.textContent = "N/A";
            }
          }
        })
        .catch((error) => console.error("Error fetching today's data:", error));
    }

    // Live update interval for today's chart
    setInterval(() => {
      // Fetch only the latest data point for the current device
      fetch(`/api/data?device_id=${current_node}&latest=true`) // Assuming an endpoint for latest data point exists or adjust as needed
        .then((response) => response.json())
        .then((latest) => {
          // Assuming the endpoint returns a single latest object or an array with one item
          if (latest && latest.hasOwnProperty("battery_voltage")) {
            // Adjust check if response is an array
            const x =
              new Date(latest.timestamp).getTime() +
              new Date().getTimezoneOffset() * -60000; // Use timestamp from data
            const y = parseFloat(latest.battery_voltage);

            // Add point to the live chart (today's chart)
            if (charts.battery.series[0].data.length > 4000) {
              // Keep shift logic if needed
              charts.battery.series[0].addPoint([x, y], true, true, true);
            } else {
              charts.battery.series[0].addPoint([x, y], true, false, true);
            }

            // Update the displayed battery voltage
            const batteryElement = document.getElementById("battery");
            if (batteryElement) {
              batteryElement.textContent = latest.battery_voltage;
            }
          } else {
            console.log("No new data available for live update.");
          }
        })
        .catch((error) => console.error("Error fetching live data:", error));
    }, 15000); // Keep interval as 15 seconds

    // Initial calls
    updateDashboard(); // Fetch and display today's data initially
    updateOldCharts(); // Fetch and display historical data initially

    // Set interval for updating today's dashboard data (excluding live point adding)
    // This might be redundant if the live update handles the latest value display
    // Consider if you still need this separate interval
    setInterval(updateDashboard, 60000); // Update dashboard data every minute, for example

    // Optionally, set an interval to refresh historical data less frequently
    // setInterval(updateOldCharts, 3600000); // Refresh historical data every hour, for example
  } else {
    console.error("Chart container 'chart-battery' not found in DOM.");
  }
});

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
