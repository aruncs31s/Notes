---
id: Implementation
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
Date: "03-03-25"
dg-publish: true
---
# Implementation
- [[Reasearch]]
- [[BPSK Implementation]]
- [[QPSK Implementation]]
- [[Performance Analysis]]
- [[Ber Curve]]

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

# Transmitter

## Tx

#### 

First one im going to look out use FSK[^1] Modulation Scheme 
- It includes 

```python
class pkt_fsk_xmt(gr.top_block, Qt.QWidget):

```

Which inherits from both the `gr.top_block` and `Qt.QWidget` class. 

## Transmitter

```python
class pkt_fsk_xmt(gr.top_block, Qt.QWidget):
	def __init__(self, InFile='default'):
		gr.top_block.__init__(self, "pkt_fsk_xmt", catch_exceptions=True)
		Qt.QWidget.__init__(self)
		self.setWindowTitle("pkt_fsk_xmt")
		qtgui.util.check_set_qss()
		try:
			self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
		except BaseException as exc:
			print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
		self.top_scroll_layout = Qt.QVBoxLayout()
		self.setLayout(self.top_scroll_layout)
		self.top_scroll = Qt.QScrollArea()
		self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
		self.top_scroll_layout.addWidget(self.top_scroll)
		self.top_scroll.setWidgetResizable(True)
		self.top_widget = Qt.QWidget()
		self.top_scroll.setWidget(self.top_widget)
		self.top_layout = Qt.QVBoxLayout(self.top_widget)
		self.top_grid_layout = Qt.QGridLayout()
		self.top_layout.addLayout(self.top_grid_layout)

```

This initializes the flow graph and sets up the gui

```python
def __init__(self, InFile='default'):

```

- `InFile` is the file that the class might need to process or use during its operation.
- [ ] Find more about this 

## Receiver

[^1]: Frequency Shift Keying(FSK) is a modulation scheme which involves changing the carrier frequency to transmit digital data.

## Transmitting a file with qpsk
- `xxd -p` can be used to show the binary .

In my knowledge the the qpsk works like this 

```mermaid 
graph LR
binary --> |2 bits| QPSK | 

```

> Do i have to provide 2 binary bits to qpsk[^2] at a time 
> it does work with 2 bits at a time (dibits)

[^2]: 

