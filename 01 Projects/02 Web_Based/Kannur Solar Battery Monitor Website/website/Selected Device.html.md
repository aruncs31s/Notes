```html
{% extends "base.html" %}

{% block title %} Device - {{ device_name }} {% endblock %}
{% block extra_js %}
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/networkgraph.js"></script>
<script src="https://code.highcharts.com/modules/accessibility.js"></script>
  
{% endblock %}

{% block extra_css %}
<!-- For Datepciker -->
<link rel="stylesheet" href="https://code.jquery.com/ui/1.14.1/themes/base/jquery-ui.css">
<!-- End Datepicker -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/selected_device.css') }}" />
{% endblock %}

{% block content %}

<div class="horizontal_layout">
  <div class="vert_layout single-style">
    <div id="chart-battery" class="chart-container"></div>
    <div class="device-control">
      <h3 id="current-node"> Device: {{ device_name }}</h3>
      <div class="control-panel">
        <button id="controlButton" class="control-button">
          Toggle Control
        </button>
        <p class="button-status" id="buttonStatus">Status: Inactive</p>
        <p>Battery: <span id="current-battery-value">--</span>V</p>
        <p>LED State: <span id="ledState">--</span></p>
        <!-- <form action="todo">
          <input type="text" placeholder="when to turn on " class="pad2m border2"> 
        </form> -->
        <!-- <button class="button-30" role="button">Toggle Timer</button> -->

      </div>
    </div>
  </div>
</div>

<div class="older_readings horizontal_layout">
  <h1>Older Readings</h2>


    <div class="vert_layout card-layout">
      <div class="card-chart-container">
        <div id="chart-battery_prev_1" class="chart-container-new"></div>
      </div>
      <div class="card-chart-container">
        <div id="chart-battery_prev_2" class="chart-container-new"></div>
      </div>
    </div>
    <div class="vert_layout card-layout">
      <div class="card-chart-container">
        <div id="chart-battery_prev_3" class="chart-container-new"></div>
      </div>
      <div class="card-chart-container">
        <div id="chart-battery_prev_4" class="chart-container-new"></div>
      </div>
    </div>
    <div class="vert_layout card-layout">
      <div class="card-chart-container">
        <div id="chart-battery_prev_5" class="chart-container-new"></div>
      </div>
      <div class="card-chart-container">
        <div id="chart-battery_prev_6" class="chart-container-new"></div>
      </div>
    </div>
</div>

<!-- <div class="dashboard"> -->




<!-- <div class="vert_layout"> -->
<!-- <div class="current-values"> -->
<!-- <div class="row"> -->
<!-- <div class="column-left"> -->
<!-- <p>Date: <input type="text" id="datepicker"></p> -->
<!-- <div id="chart-battery" class="chart-container"></div> -->
<!-- </div> -->
<!-- <div class="column-right"> -->
<!-- <h3 id="current-node" > Device: {{ device_name }}</h3> -->
<!-- <div class="control-panel"> -->
<!-- <button id="controlButton" class="control-button"> -->
<!-- Toggle Control -->
<!-- </button> -->
<!-- <p class="button-status" id="buttonStatus">Status: Inactive</p> -->
<!-- <p>Battery: <span id="battery">--</span>V</p> -->
<!-- <p>LED State: <span id="ledState">--</span></p> -->
<!-- </div> -->
<!-- </div> -->
<!-- </div> -->
<!-- </div> -->
<!-- </div> -->
<!-- </div> -->


<!-- <div class="related-devices"> -->
<!-- <div class="nearby-devices"> -->
<!-- <h2>Nearby Devices</h2> -->
<!-- <div id="graph-container" class="graph-container" ></div> -->

<!-- <div class="device-list" > -->
<!-- {% for device in nearby_devices %} -->
<!-- <li -->
<!-- class="{{ 'active-device' if device.status.lower() == 'active' else 'inactive-device' }}" -->
<!-- id="list" -->
<!-- > -->
<!-- <a -->
<!-- href="/device/{{ device.assigned_place }}" -->
<!-- onclick="sendDeviceInfo('{{ device.name }}')" -->
<!-- class="button-link"  -->
>
<!-- {{ device.assigned_place }} -->
<!-- </a> -->
<!-- <div> -->
<!-- <span> {{ device.status }} - IP: {{ device.ip }} </span> -->
<!-- </div> -->
<!-- </li> -->

<!-- {% endfor %} -->
<!-- </div> -->
<!-- </div> -->
<!-- <div class="device-under-main-node"> -->
<!-- <div class="device-list"> -->
<!-- <h2>Devices under Main Node</h2> -->
<!-- {% for device in devices_under_main_node %} -->
<!-- <li -->
<!-- class="{{ 'active-device' if device.status.lower() == 'active' else 'inactive-device' }}" -->
<!-- id="list" -->
<!-- > -->
<!-- <a -->
<!-- href="/device/{{ device.assigned_place }}" -->
<!-- onclick="sendDeviceInfo('{{ device.name }}')" -->
<!-- class="button-link" -->
<!-- > -->
<!-- {{ device.assigned_place }} -->
<!-- </a> -->
<!-- <div> -->
<!-- <span> {{ device.status }} - IP: {{ device.ip }} </span> -->
<!-- </div> -->
<!-- </li> -->
<!--  -->
<!-- {% endfor %} -->
<!-- </div> -->
<!-- </div> -->
<!-- </div> -->
<script src="{{ url_for('static', filename='js/chart_def.js') }}"></script>

<script src="{{ url_for('static', filename='js/selected_device.js') }}"></script>

<!-- For Datepicker -->
<!-- <script src="{{ url_for('static', filename='js/ui/datepicker.js') }}"></script> -->

<script src="https://code.jquery.com/jquery-3.7.1.js"></script>
<script src="https://code.jquery.com/ui/1.14.1/jquery-ui.js"></script>
<!-- <script>
  $(function () {
    $("#datepicker").datepicker();
  });
</script> -->

<!-- End Datepicker -->
{% endblock %}

```