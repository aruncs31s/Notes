```python
<!DOCTYPE html>

<html>

<head>

<title>Solar Battery Monitor</title>

<link rel="stylesheet" href="{{ url_for('static', filename='devices.css') }}">

</head>

<body>

<h1>Solar Battery Monitoring System</h1>

<h2> {{ title }} </h2>

<div class="dashboard">

<main>

<div class="current-values">

<h2>Live Readings</h2>

<p>Battery: <span id="battery">--</span>V</p>

</div>

<div id="chart-battery" class="chart-container"></div>

<div class="control-panel">

<button id="controlButton" class="control-button">Toggle Control</button>

<p class="button-status" id="buttonStatus">Status: Inactive</p>

</div>

<div class="device-status">

<h2>Device Status</h2>

<ul id="deviceList"></ul>

</div>

</div>

<h2>Devices</h2>

<ul>

{% for device in devices %}

<li>{{ device.name }} - Status: {{ device.status }} - IP: {{ device.ip }}</li>

{% endfor %}

</ul>

  

<script>

function createChart(containerId, title, yAxisTitle, seriesName) {

return Highcharts.chart(containerId, {

chart: { type: 'line' },

title: { text: title },

xAxis: {

type: 'datetime',

title: { text: 'Time' }

},

yAxis: {

title: { text: yAxisTitle }

},

series: [{

name: seriesName,

data: []

}]

});

}

  

// Initialize charts

const charts = {

battery: createChart('chart-battery', 'Battery Voltage', 'Voltage (V)', 'Battery')

};

  

const controlButton = document.getElementById('controlButton');

const buttonStatus = document.getElementById('buttonStatus');

let isActive = false;

  

controlButton.addEventListener('click', function() {

isActive = !isActive;

controlButton.classList.toggle('active');

fetch('/api/control', {

method: 'POST',

headers: {

'Content-Type': 'application/json',

},

body: JSON.stringify({

state: isActive

})

})

.then(response => response.json())

.then(data => {

buttonStatus.textContent = `Status: ${isActive ? 'Active' : 'Inactive'}`;

if (data.error) {

alert('Error: ' + data.error);

isActive = !isActive; // Revert state on error

controlButton.classList.toggle('active');

}

})

.catch(error => {

console.error('Error:', error);

alert('Failed to send command to ESP8266');

isActive = !isActive; // Revert state on error

controlButton.classList.toggle('active');

});

});

  

function updateDashboard() {

fetch('/api/data?timeframe=hour')

.then(response => response.json())

.then(data => {

if (data.length > 0) {

const latest = data[0];

// Update current values

document.getElementById('battery').textContent = latest.battery_voltage;

  

// Update charts

const chartData = data.reverse().map(reading => ({

battery: [new Date(reading.timestamp).getTime(), reading.battery_voltage]

}));

  

charts.battery.series[0].setData(chartData.map(d => d.battery));

}

})

.catch(error => console.error('Error fetching data:', error));

}

  

function updateDeviceStatus() {

fetch('/api/devices')

.then(response => response.json())

.then(devices => {

const deviceList = document.getElementById('deviceList');

deviceList.innerHTML = '';

devices.forEach(device => {

const li = document.createElement('li');

li.textContent = `${device.name} - ${device.status}`;

deviceList.appendChild(li);

});

})

.catch(error => console.error('Error fetching device status:', error));

}

  

// Update dashboard every 5 seconds

setInterval(updateDashboard, 5000);

updateDashboard(); // Initial update

  

// Update device status every 10 seconds

setInterval(updateDeviceStatus, 10000);

updateDeviceStatus(); // Initial update

</script>

</body>

</html>
```