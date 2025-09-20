---
id: Battery_Level
aliases: []
tags:
  - projects
  - electronics
  - inverter_gui_touch_screen
  - flutter_app
dg-publish: true
---
# Battery Level
- 12.8V

## Single Cell 

| Specs                                   | Value                 |
| --------------------------------------- | --------------------- |
| **Nominal Voltage**                     | **3.2V**              |
| **Max Charge Voltage**                  | **3.65V**             |
| **Discharge Cut Off Voltage**           | **2.5V**              |
| **Charging Current**                    | **1.2A-6A (0.2C-1C)** |
| **Max. Continuous Discharging Current** | **18A (3C)**          |
• 0.2C = 1.2 A (slow charge)  
• 1C = 6 A (fastest safe charge).
The maximum current you can continuously draw from the battery. If the capacity is 6Ah, then:  
• 3C = 18 A.

### Battery Level 
- **3.65 V** → 100% (fully charged)
- **3.40–3.45 V** → ~95–100% (nearly full)
- **3.30 V** → ~90%
- **3.20–3.25 V** → ~50% (midpoint)
- **3.10 V** → ~20%
- **2.90–3.00 V** → ~10%
- **2.50 V** → 0% (discharged cutoff)

## 12.8V Cell 
- **14.6 V** → ~100% (charge termination voltage)
- **13.8–13.6 V** → ~95–100%
- **13.2 V** → ~90%
- **12.8–12.9 V** → ~50%
- **12.4 V** → ~20–30%
- **11.6–11.8 V** → ~10%
- **10.0 V** → ~0% (cutoff; don’t go lower)

### Level Calculation

```dart
double lifepo4SocCell(double vCell) {
  // Voltage vs SoC map (approx, for one LiFePO4 cell at rest)
  final List<List<double>> points = [
    [2.50, 0],
    [2.90, 10],
    [3.10, 20],
    [3.20, 50],
    [3.30, 90],
    [3.40, 95],
    [3.45, 99],
    [3.65, 100],
  ];

  if (vCell <= points[0][0]) return 0.0;
  if (vCell >= points.last[0]) return 100.0;

  // Linear interpolation between points
  for (int i = 1; i < points.length; i++) {
    double v0 = points[i - 1][0];
    double s0 = points[i - 1][1];
    double v1 = points[i][0];
    double s1 = points[i][1];

    if (vCell >= v0 && vCell <= v1) {
      return s0 + (s1 - s0) * (vCell - v0) / (v1 - v0);
    }
  }

  return 0.0; // fallback
}

double lifepo4SocPack(double vPack, {int cellsInSeries = 4}) {
  double vCell = vPack / cellsInSeries;
  return lifepo4SocCell(vCell);
}

```