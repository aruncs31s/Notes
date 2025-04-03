---
aliases:
Date: "03-03-25"
---

# Implementation
- [[Reasearch]]
```tasks
not done 
path includes Final Year Project/Implementation

```
## Packet Tx using BPSK
[Source 1](https://wiki.gnuradio.org/index.php?title=File_transfer_using_Packet_and_BPSK)
``` bash
cd ~/
git clone [https://github.com/duggabe/gr-control.git](https://github.com/duggabe/gr-control.git)
cd ~/gr-control
```
First im tring to send a text file  which will contain something like "MESSAGE FROM ACER LAPTOP"



### Transmitter




## Tx

```python
from gnuradio import gr, blocks, digital
import iio
SAMP_RATE = 1e6
CENTER_FREQ = 2.4e9
GAIN = 0
class PlutoTx(gr.top_block):
    def __init__(self, file_path):
    gr.top_block.__init__(self)
    self.samp_rate = SAMP_RATE
    self.center_freq = CENTER_FREQ
    self.gain = GAIN
    # Read file
    self.src = blocks.file_source(gr.sizeof_char, file_path, repeat=False)
    self.enc = digital.packet_encoder(samples_per_symbol=2)
    self.mod = digital.qpsk_mod()
    self.sink = iio.PlutoSDR_Sink("ip:192.168.2.1", self.samp_rate, self.center_freq, self.gain)
    self.connect(self.src, self.enc, self.mod, self.sink)
if __name__ == "__main__":
    tx = PlutoTx("test_file.txt")
    tx.run()
```
