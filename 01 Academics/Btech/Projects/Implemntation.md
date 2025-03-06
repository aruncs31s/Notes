---
aliases: 
Date: "04-03-25"
---
# Implemntation

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
