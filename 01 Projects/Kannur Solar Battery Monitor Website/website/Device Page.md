---
aliases:
  - smart city device page
cssclasses:
  - wide-page
tags:
  - website
  - smartcity
dg-publish: true
---
>[!blank|right-small]+ Pages 
>There are mainly 4 pages , `Home` , `devices`,`info`, and `about`
>- [[Home Page]]
>- [[Device Page]]
>- [[main_page]]
>- [[APIs]]
>Others
>- [[database]]
> 
# Device Page

This page will contain the battery voltage graph and the relay button


![[Screenshot 2025-04-19 at 3.53.43 AM.png]]
[commit:: 2519b02]



![[Screenshot 2025-05-07 at 12.19.36 PM.png]]
![[Screenshot 2025-05-07 at 12.23.36 PM.png]]

---



## Voltage Vs Time Graph
The voltage graph now has as 75% of full with in `c9d809` 
```js
document.addEventListener("DOMContentLoaded", function () { other codes ...
}
```
This ensures the `DOM` is fully loaded. 

```js
if (document.getElementById("chart-battery")) {
    const charts = {
      battery: createChart(
        "chart-battery",
        "Battery Voltage Over Time",
        "Voltage (V)",
        "Battery Voltage"
      ),
    };
```
![[Screenshot 2025-05-02 at 12.53.14 AM.png]]

```js
let initialChartData = [];
function updateDashboard() {
  fetch("/api/data")
	.then((response) => response.json())
	.then((data) => {
	  if (data.length > 0) {
		const latest = data[data.length - 1];

		// Check if battery_voltage exists
		if (latest.hasOwnProperty("battery_voltage")) {
		  const batteryElement = document.getElementById("battery");
		  if (batteryElement) {
			batteryElement.textContent = latest.battery_voltage;
		  } else {
			console.error("Battery element not found in DOM.");
		  }
		} else {
		  console.error("battery_voltage property is missing in the latest data");
		}

		initialChartData = data.map((reading) => [
		  new Date(reading.timestamp).getTime() + new Date().getTimezoneOffset() * -60000,
		  reading.battery_voltage,
		]);

		charts.battery.series[0].setData(initialChartData);
	  } else {
		console.log("No data available");
	  }
	})
	.catch((error) => console.error("Error fetching data:", error));
}

```

### 30 Minuts fetching
```python
# Indexes
TIME_INDEX 2
VOLT_INDEX 3
```

```python
def get_30_min_interval_data(device_id):
    db.cursor.execute('''
    SELECT * FROM timeseries_data 
    WHERE device_id = ? AND strftime('%M', timestamp) IN ('00', '30')
    ''', (device_id,))
    rows = db.cursor.fetchall()
    result = []
    for row in rows:
        result.append({
            'timestamp': row[TIME_INDEX],
            'voltage': row[VOLT_INDEX]
        })
    return result

# Example usage
interval_data = get_30_min_interval_data(ip)
for data in interval_data:
    # print(data['timestamp'].time())
    # Filter to get only one value per 30-minute interval
    unique_interval_data = {}
    for data in interval_data:
        interval_key = data['timestamp'].replace(minute=0, second=0, microsecond=0) if data['timestamp'].minute < 30 else data['timestamp'].replace(minute=30, second=0, microsecond=0)
        if interval_key not in unique_interval_data:
            unique_interval_data[interval_key] = data

    # Print the filtered data
    for key, value in unique_interval_data.items():
        print(f"Interval: {key}, Voltage: {value['voltage']}")
```


## Unused



```html
<div class="vert_layout">
	<div class="related-devices">
		<div class="nearby-devices">
			<h2>Nearby Devices</h2>
				<!-- <div id="graph-container" class="graph-container"></div> -->
				<div class="device-list">
					{% for device in nearby_devices %}
						<li class="{{ 'active-device' if device.status.lower() == 'active' else 'inactive-device' }}" id="list">
							<a href="/device/{{ device.assigned_place }}" onclick="sendDeviceInfo('{{ device.name }}')"
							class="button-link">
								{{ device.assigned_place }}
							</a>
								<div>
									<span> {{ device.status }} - IP: {{ device.ip }} </span>
								</div>
						</li>
						{% endfor %}
					</div>
						<div class="device-under-main-node">
							<div class="device-list">
								<h2>Devices under Main Node</h2>
									{% for device in devices_under_main_node %}
									<li class="{{ 'active-device' if device.status.lower() == 'active' else 'inactive-device' }}" id="list">
										<a href="/device/{{ device.assigned_place }}" onclick="sendDeviceInfo('{{ device.name }}')"
			class="button-link">
			{{ device.assigned_place }}
						</a>
							<div>
								<span> {{ device.status }} - IP: {{ device.ip }} </span>
							</div>
						</li>
					{% endfor %}
				</div>
			</div>
		</div>
	</div>
</div>
```

## Network Graph

### CSS
### HTML
### Scripts
##### Getting Current node
```js
  const current_node = document
    .getElementById("current-node")
    .innerHTML.split(":")
    .map((part) => part.trim())[1];
  console.log(current_node);

```


```js 
// For Network Graph
// Declare a global variable to store the fetched data
let nearNodesData = [];
let nearAllNodesData = [];
// Use a configurable base URL for API calls
const API_BASE_URL = "http://localhost:5000"; // Replace with environment-specific value
// Function to fetch data and store in the global variable
function fetchNearNodes(current_node) {
	return fetch(`${API_BASE_URL}/device/get_near_nodes/${current_node}`)
	.then((response) => {
	// console.log("Response received:", response);
	return response.json();
	})
	.then((data) => {
	// console.log("Data received:", data);
	nearNodesData = data; // Store data in the global variable
	return data;
	})
	.catch((error) => {
	console.error("Error fetching data:", error);
	});
}
```

```js
function getTotalNearNodes(type) {
  if (type === "near_nodes") {
    return nearNodesData["total_near_nodes"];
  } else if (type === "all_nodes") {
    return nearAllNodesData[0]?.near_all_nodes?.length || 0;
  }
}

```

```js


document.addEventListener("DOMContentLoaded", async function () {
  // Thanks: https://www.highcharts.com/docs/chart-and-series-types/network-graph
   

  // await fetchNearNodes(current_node);
  await fetchAllNodes(current_node);
  const total_near_nodes = getTotalNearNodes("all_nodes");
  console.log("Total near nodes:", total_near_nodes);

  let near_node_arr = [];
  if (nearAllNodesData.length > 0 && nearAllNodesData[0]?.near_all_nodes) {
    for (let i = 0; i < total_near_nodes; i++) {
      near_node_arr.push([current_node, nearAllNodesData[0]["near_all_nodes"][i]]);
    }
  } else {
    console.error("near_all_nodes data is missing or not properly formatted");
  }
  console.log("nodes");
  console.log(near_node_arr);

  try {
    Highcharts.chart("graph-container", {
      chart: {
        type: "networkgraph",
        plotBorderWidth: 1,
        backgroundColor: "#3b4252",
      },
      credits: {
        enabled: false,
      },
      title: {
        text: null, // Disable the title
      },
      plotOptions: {
        networkgraph: {
          keys: ["from", "to"],
          marker: {
            radius: 7, // Set the default node size
          },
          events: {
            click: function (event) {
              const nodeName = event.point.name;
              console.log("Node clicked:", nodeName);
              window.location.href = "/device/" + nodeName;
            },
          },
        },
      },
      series: [
        {
          layoutAlgorithm: {
            enableSimulation: true,
            initialPositions: function () {
              const chart = this.series[0].chart,
                width = chart.plotWidth,
                height = chart.plotHeight;

              this.nodes.forEach(function (node) {
                // If initial positions were set previously, use that
                // positions. Otherwise use random position:
                node.plotX =
                  node.plotX === undefined ? Math.random() * width : node.plotX;
                node.plotY =
                  node.plotY === undefined ? Math.random() * height : node.plotY;
              });
            },
          },
          name: "K8",
          data: near_node_arr,
          nodes: [
            {
              id: current_node,
              color: "green", // Change the color to green
              marker: {
                radius: 14, // Increase the size of the current node
              },
            },
            {
              id: nearAllNodesData[0]?.main_node,
              color: "red", // Change the color to red
              marker: {
                radius: 10, // Set the size of the main node
              },
            },
          ],
          dataLabels: {
            enabled: true,
            linkFormat: "",
            style: {
              color: "white",
              textOutline: "none",
              fontWeight: "normal",
              fontSize: "14px",
              // color: getComputedStyle(document.documentElement).getPropertyValue('--nord8'),
            },
          },
        },
      ],
    });
    console.log("Highcharts chart initialized");
  } catch (error) {
    console.error("Error initializing Highcharts chart:", error);
  }
  updateDashboard(); // Only call once here
});

```

```js
// Update dashboard every 5 seconds
setInterval(updateDashboard, 5000);

function get_data() {
  console.log("date_requested to /api/data");
  const TIME_INDEX = 2;
  const BAT_INDEX = 3;
  const ip = "192.168.1.2";

  // Placeholder for db and datetime logic
  const raw_data = []; // Replace with actual db.get_data logic
  const top_data = raw_data[raw_data.length - 1] || {};
  const data = {
    time: top_data[TIME_INDEX]?.strftime?.("%H:%M:%S") || "N/A",
    battery_voltage: top_data[BAT_INDEX] || 0,
  };
  return jsonify(data), 200;
}
```

