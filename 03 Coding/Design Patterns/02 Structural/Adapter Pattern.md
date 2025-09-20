---
id: Adapter_Pattern
aliases: []
tags:
  - coding
  - design_patterns
  - structural
dg-publish: true
---
# Adapter Pattern 
*To make different implementation to work together* 

> Wrap it in an interface to make it compatible with the existing code.

```ts
// Consider a third party weather api interface
interface WeatherAPI {
  getTempC(): number;
  getHumidity(): number;
  getWindSpeedKPH(): number;
}
// what our app expects
interface Weather {
  getTempF(): number;
  getHumidity(): number;
  getWindSpeedMPH(): number;
}

```

**Without Adapter**: Directly using the third-party API would require changing our app's code whenever the API changes.

```ts
class ThirdPartyWeatherAPI implements WeatherAPI {
  getTempC(): number {
    // Fetch temperature in Celsius
    return 25; // Example value
  }
  getHumidity(): number {
    // Fetch humidity
    return 60; // Example value
  }
  getWindSpeedKPH(): number {
    // Fetch wind speed in KPH
    return 15; // Example value
  }
}
const weatherAPI = new ThirdPartyWeatherAPI();
console.log(`Temperature in F: ${weatherAPI.getTempC() * 9/5 + 32}`);
console.log(`Humidity: ${weatherAPI.getHumidity()}`);
console.log(`Wind Speed in MPH: ${weatherAPI.getWindSpeedKPH() * 0.621371}`);  

```

**With Adapter**: The adapter translates the third-party API's methods to the expected interface, allowing our app to remain unchanged.

```ts
// Adapter class
class WeatherAdapter implements Weather {
  constructor(private api: WeatherAPI) {}
  getTempF(): number {
    return this.api.getTempC() * 9/5 + 32;
  }
  getHumidity(): number {
    return this.api.getHumidity();
  }
  getWindSpeedMPH(): number {
    return this.api.getWindSpeedKPH() * 0.621371;
  }
}

// Using
const weatherAPI = new ThirdPartyWeatherAPI();
const weather = new WeatherAdapter(weatherAPI);
console.log(`Temperature in F: ${weather.getTempF()}`);
console.log(`Humidity: ${weather.getHumidity()}`);
console.log(`Wind Speed in MPH: ${weather.getWindSpeedMPH()}`);

```

## 📚 Used In 
- [[SOLID principle]]
- [[Design Pattern]]
- [[Structural Pattern]]
- [[Creational Pattern]]
---

