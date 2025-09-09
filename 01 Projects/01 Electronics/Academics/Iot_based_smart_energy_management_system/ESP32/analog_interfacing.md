---
id: analog_interfacing
aliases: []
tags:
  - projects
  - electronics
  - academics
  - iot_based_smart_energy_management_system
  - esp32
dg-publish: true
---
#### Analog Interfacing

- [Introduction](#introduction)
- [Sources](#sources)

#### Introduction

- ADC will have a defined resolution and a reference voltage which is usually the supply voltage
- Maximum Possible Value

$$
Max = 2^N -1
$$

_Where N = resolution_

- If resolution is `8 bit`

$$
Max = 255
$$

 <details>
<summary>Example</summary>
Thus, if the reference voltage is 5V and an 8−bit ADC is used, then 5V corresponds to a reading of 255, 1V corresponds to a reading of (255/5*1) = 51, 2V corresponds to a reading (255/5*2) = 102 and so on. If we had a 12 bit ADC, then 5V would correspond to a reading of 4095, 1V would correspond to a reading of (4095/5*1) = 819, and so on.
</details>

#CalculateResolution

- Static

```rust
fn main() {
// Define The Number of Resolution
	let N :isize = 8;
	let Max = 2isize.pow(N as u32) -1;
	println!("Maximaum Size = {}",Max);
}

```

- Dynamic
  - By Rust

```rust
fn main() {
    let mut N = String::new();
    println!("Enter The ADC bit value");

    std::io::stdin().read_line(&mut N).unwrap();
    // Attempt to parse the input as an integer
    let N: isize = match N.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a number.");
            return;
        }
    };
    // let N = std::io::stdin().read_line(&mut N).unwrap();
    let Max = 2isize.pow(N as u32) -1  ;
    println!("Maximaum Size = {}", Max);
}

```

- By Python

```python
N=int(input("Enter the ADC Value"))
print("Max Value = " ,2**N -1)

```

#ComputeVoltage

- Static

```rust
//Compute the voltage with obtained value of adc
fn main(){
let reference_voltage: f32= 5.0;
let obtained_adc_val = 512;
let N = 10;
let Max : f32= (2f32).powi(N) -1.0 ;
println!("Voltage = {}",(reference_voltage *obtained_adc_val as f32)/Max)
}

```

- Dynamic

```rust
fn main() {
    // Read The ADC Value form user
    let mut N = String::new();
    let mut obtained_adc_val = String::new();
    let mut reference_voltage = String::new();

    println!("Enter The ADC bit value");
    std::io::stdin().read_line(&mut N).unwrap();
    let N: isize = match N.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("invalid input. please enter a number.");
            return;
        }
    };

    println!("Enter the Refernce Voltage");
    std::io::stdin().read_line(&mut reference_voltage).unwrap();
    let reference_voltage: f32 = match reference_voltage.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("invalid input. please enter a number.");
            return;
        }
    };
    println!("Enter the obtained ADC Value");
    std::io::stdin().read_line(&mut obtained_adc_val).unwrap();

    let obtained_adc_val: isize = match obtained_adc_val.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a number.");
            return;
        }
    };
    let Max: f32 = (2f32).powf(N as f32) -1.0;
    println!(
        "Voltage = {}",
        (reference_voltage as f32 * obtained_adc_val as f32) / Max
    )
}

```

#### Finding Voltage

```python
Vmax=10 #V 
ADC_BIT = 2 
current_value = int(input("Enter current value"))
voltage = Vmax *((2 ** 2 - 1 ) / current_value );
print(f" Voltage =  {voltage}")

```

## Example

#### Connecting ADC Sensors With ESP32

- [Conecting LDR Sensor ]()

##### Connecting LDR Sensor

[[Projects/Iot_based_smart_energy_management_system/Sensors/LDR Sensor]]

![[Projects/Iot_based_smart_energy_management_system/Files/Images/Pasted image 20240328225646.png|300x250]]

`Credit` [Intercaing Code](https://github.com/yash-sanghvi/ESP32/blob/master/AnalogReadWithLDR/AnalogReadWithLDR.ino)

```c
const int LDR_PIN = 36;

void setup() {
   Serial.begin(9600);
   analogReadResolution(10); //default is 12. Can be set between 9-12.
}
void loop() {
   float LDR_Voltage = ((float)LDR_Reading*3.3/1023);
   Serial.print("Reading: ");Serial.print(LDR_Reading); Serial.print("\t");Serial.print("Voltage: ");Serial.println(LDR_Voltage);
}

```

#### Sources

- [Source1](<https://www.tutorialspoint.com/esp32_for_iot/interfacing_esp32_with_analog_sensors.htm#:~:text=In%20the%20image%20shown%20below,36%20(VN)%20of%20ESP32.>)
-
