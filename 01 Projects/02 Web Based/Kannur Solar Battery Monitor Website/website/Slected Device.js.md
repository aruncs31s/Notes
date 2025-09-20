---
id: Slected_Devicejs
aliases: []
tags:
  - projects
  - web_based
  - kannur_solar_battery_monitor_website
  - website
dg-publish: true
---

```js
debug = 1;
timeOffset = -60000;

const current_node = document
  .getElementById("current-node")
  .innerHTML.split(":")
  .map((part) => part.trim())[1];
console.log("Curret node : " + current_node);

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

// Function to update the main dashboard elements and today's chart
function updateLiveChart() {
  fetch(`/api/data?device_id=${current_node}`) // Fetch today's data
    .then((response) => {
      console.log("Response from /api/data (today):", response);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      if (debug) {
        console.log("Inside get , data");
      }
      if (data.length > 0) {
        const latest = data[data.length - 1];
        // Update battery voltage display
        if (latest.hasOwnProperty("battery_voltage")) {
          const batteryElement = document.getElementById(
            "current-battery-value",
          );

          if (batteryElement) {
            batteryElement.textContent = latest.battery_voltage;
            if (debug == 1) {
              console.log("Battery Element Exists");
            }
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
      } else {
        console.log("No data available for today");
        // Optionally clear today's chart or show a message
        // charts.battery.series[0].setData([]);
        const batteryElement = document.getElementById("current-battery-value");
        if (batteryElement) {
          batteryElement.textContent = "N/A";
        }
      }
    })
    .catch((error) => console.error("Error fetching today's data:", error));
}

// New async Functions
async function updateOldChart_a(day, theChart) {
  try {
    const response = await fetch(`/api/data/old?device_id=${current_node}&day=${day}`);
    console.log(`Response from /api/data (prev_${day}):`, response);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    if (data.length > 0) {
      const chartData = data.map((reading) => [
        new Date(reading.timestamp).getTime() + new Date().getTimezoneOffset() * timeOffset,
        reading.battery_voltage,
      ]);
      theChart.series[0].setData(chartData);
    } else {
      console.log(`No data available for prev_${day}`);
      theChart.series[0].setData([]);
    }
  } catch (error) {
    console.error(`Error fetching data for prev_1:`, error);
  }
}

let lates_data = [];

async function get_latest_data() {
  try {
    const response = await fetch(`/api/data?device_id=${current_node}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    if (data.length > 0) {
      lates_data = data[data.length - 1];
      console.log("Latest data:", lates_data);
      return lates_data;
    } else {
      const liveResponse = await fetch(`/api/data/live?device_id=${current_node}`);
      if (!liveResponse.ok) {
        throw new Error(`HTTP error! status: ${liveResponse.status}`);
      }
      const liveData = await liveResponse.json();
      lates_data = liveData["battery_voltage"];
      if (lates_data) {
        console.log("Latest data from live:", lates_data);
        return lates_data;
      } else {
        console.log("No data available for latest");
        return null;
      }
    }
  } catch (error) {
    console.error("Error fetching latest data:", error);
    return null;
  }
}

// Fix setInterval for live updates
setInterval(async () => {
  const latest = await get_latest_data();
  if (latest && latest.hasOwnProperty("battery_voltage")) {
    const x = new Date(latest.timestamp).getTime() + timeOffset;
    const y = parseFloat(latest.battery_voltage);
    if (charts.battery.series[0].data.length > 4000) {
      charts.battery.series[0].addPoint([x, y], true, true, true);
    } else {
      charts.battery.series[0].addPoint([x, y], true, false, true);
    }

    const batteryElement = document.getElementById("battery");
    if (batteryElement) {
      batteryElement.textContent = latest.battery_voltage;
    }
  } else {
    console.log("No new data available for live update.");
  }
}, 5000);

// Remove redundant commented-out code

// Ensure updateAllOldCharts is called after defining updateOldChart
async function updateAllOldCharts() {
  // a_1 a_2 in the sense that these are async funtions , change later 
  // updateOldChart_a(day,Chart)
  await updateOldChart_a(1, charts.old_battery_1);
  await updateOldChart_a(2, charts.old_battery_2);
  await updateOldChart_a(3, charts.old_battery_3);
  await updateOldChart_a(4, charts.old_battery_4);
  await updateOldChart_a(5, charts.old_battery_5);  
  await updateOldChart_a(6, charts.old_battery_6);

}

// Initial call
updateAllOldCharts();
setInterval(updateLiveChart, 60000); 
setInterval(get_latest_data, 2000);

```