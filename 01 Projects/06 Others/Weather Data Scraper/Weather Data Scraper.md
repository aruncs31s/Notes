---
id: project_template
aliases: []
tags: []
Created: "14-09-2024"
Starting Date: "14-09-2024"
Target Date: ""
---

# Weather Data Scraper

Designed to scrape 

- [x] scrape the `LiFePo` Battey level ✅ 2025-07-05

#code

```python
import time
from datetime import datetime

import requests as req

# Replace it with station ip addr
url = "http://172.16.32.8/data"

current_date = datetime.now().strftime("%Y-%m-%d")


def set_file(new_date):
    output_file = f"readings/normal/{new_date}_log.txt"
    output_file_csv = f"readings/csv/{new_date}_log.csv"
    get_reading(new_date, output_file, output_file_csv)


def get_reading(current_date, output_file, output_file_csv):
    try:
        with open(output_file_csv, "a") as f:
            f.write(
                f"Time,Temperature,Humidity,Wind_speed,Wind_direction,Rain Volume\n"
            )

        response = req.get(url)
        # Continuously read the data
        while True:
            # NOTE: This is a continues measurement so it should reset or save to new file every new day
            # TODO: Implement the above thing
            timestamp = datetime.now().strftime("%H:%M:%S")
            data_json = response.json()
            data = [
                data_json["temperature"],
                data_json["humidity"],
                data_json["wind_speed"],
                data_json["wind_direction"],
                data_json["rain_volume"],
            ]
            with open(output_file, "a") as f:
                f.write(
                    f"{timestamp}  Temperature {data[0]} , Humidity {data[1]} ,Wind_speed {data[2]} , Wind_direction {data[3]} , Rain Volume {data[4]}\n"
                )
            with open(output_file_csv, "a") as f:
                f.write(
                    f"{timestamp},{data[0]},{data[1]} ,{data[2]},{data[3]} , {data[4]}\n"
                )
            #
            print(
                f"{timestamp} Temperature {data[0]} , Humidity {data[1]} ,Wind_speed {data[2]} , Wind_direction {data[3]} , Rain Volume {data[4]}"
            )
            time.sleep(2)
            new_date = datetime.now().strftime("%Y-%m-%d")
            if current_date != new_date:
                set_file(new_date)
    except Exception as e:
        print(f"Error Getting Json {e}")
        time.sleep(10)
        current_date = datetime.now().strftime("%Y-%m-%d")
        set_file(current_date)


if __name__ == "__main__":
    set_file(current_date)

```
