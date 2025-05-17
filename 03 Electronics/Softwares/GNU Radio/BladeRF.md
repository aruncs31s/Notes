---
aliases: 
Date: 20-01-25
---
# BladeRF
modulate and demodulate 802.11 packets
run directly on the [bladeRF 2.0 micro xA9](https://www.nuand.com/product/bladerf-xa9/)’s FPGA
Linux mac80211

In IEEE 802.11, specifically there is a requirement that a receiving modem (be it a client STA, or access point AP) must acknowledge the successful reception of an incoming packet addressed to it by beginning to transmit an an ACK packet within 10 microseconds of the end of the incoming packet.^[https://www.nuand.com/bladeRF-wiphy/]

![](https://www.nuand.com/wp-content/uploads/2021/01/architecture-4.png)

## Resources
1. https://www.nuand.com/bladeRF-wiphy/
