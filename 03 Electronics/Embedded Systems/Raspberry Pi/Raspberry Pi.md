## Programs 
- [[Raspberry Pi ESP32 Communication]]
- [[I2C LCD Interfacing]]

#### Automatic Wifi Connect 
[Source](https://www.tech-sparks.com/raspberry-pi-auto-connect-to-wifi/#:~:text=Edit%20wpa_supplicant.,conf&text=When%20you%20need%20to%20connect,networks%20by%20modifying%20their%20details.)
1. need to edit the `wpa_supplicant.conf` placed at `/etc/`
```bash
update_config=1
ap_scan=1
network={
    ssid="Your_SSID_1"
    psk="Your_Password_1"
    key_mgmt=WPA-PSK
}
```
2. create the `/etc/systemd/system/wpa_supplicant.service` 
```bash
```javascript
[Unit]
Description=WPA supplicant
Wants=network.target
After=network.target
[Service]
Type=simple
ExecStartPre=/sbin/ifconfig wlan0 up
ExecStart=/sbin/wpa_supplicant -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf
RemainAfterExit=yes
[Install]
WantedBy=multi-user.target
```

##### Method 2 

Edit the `/etc/NetworkManager/system-connections/preconfigured.nmconnection`

