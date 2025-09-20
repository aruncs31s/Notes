---
id: Python_Simulation
aliases: []
tags:
  - academics
  - btech
  - projects
  - final_year_project
Date: 01-11-2024
dg-publish: true
---
# Python Simulation
- [[#BPSK]]
- [[#QPSK]]
- [[#AWGN Channel]]
**Requirements**

```bash
matplotlib==3.9.2
numpy==2.1.3
scipy==1.14.1

```

## Modulation

### BPSK

```python
def bpsk(_system):
    _number_of_constellaition_points = 2
    _possible_symbols = np.arange(0, _number_of_constellaition_points)
    _constellation = _system.properties.amplitude * np.cos(
        _possible_symbols / _number_of_constellaition_points * 2 * np.pi
    )
    _random_syms = np.random.randint(
        low=0,
        high=_number_of_constellaition_points,
        size=int(_system.properties.get_number_of_Symbols()),
    )
    _modulated = _constellation[_random_syms]
    return _modulated, _constellation

```

![[bpsk constellation.png]]

### QPSK

```python
def qpsk(_system):
    _number_of_constellaition_points = 4
    # Generate random symbols (two bits per symbol)
    _random_symbols = np.random.randint(
        0, _number_of_constellaition_points, int(_system.number_of_Symbols / 2)
    )
    # Normalize amplitude for QPSK
    _amplitude = _system.properties.amplitude / np.sqrt(2)

    # QPSK mapping (00, 01, 11, 10 to unique phase shifts)
    _constellations = _amplitude * (
        np.cos(np.pi / 4 * (1 + 2 * _random_symbols))
        + 1j * np.sin(np.pi / 4 * (1 + 2 * _random_symbols))
    )

```

## Channel
### AWGN Channel 

```python
class Channel:

    def __init__(self, channel_name, txData, _system, EbN0dBs):
        self.channel_name = channel_name
        self.txData = txData
        self.EbN0dBs = EbN0dBs
        ber_len = len(EbN0dBs)
        simulatedBer = np.zeros(ber_len)
        if channel_name == "AWGN":
            for j, EbN0dB in enumerate(EbN0dBs):
                noiseGamma = 10 ** (EbN0dB / 10)
                avgPower = np.mean(np.abs(txData) ** 2)
                #     avgPower = sum(abs(txData) ** 2) / len(txData)
                linear_noisePower = avgPower / noiseGamma
                #
                noise_vector = np.sqrt(
                    linear_noisePower / 2
                ) * np.random.standard_normal(txData.shape)
                # Add Noice to the tx data
                noisy_signal = txData + noise_vector
                rxData = noisy_signal >= 0
                rxData = rxData.astype(int)
                sourceData = (txData >= 0).astype(
                    int
                )  # convert the data back to 0 and 1

                simulatedBer[j] = np.sum(rxData != sourceData) / len(txData)
            self.rxData = rxData
            self.simulatedBER = simulatedBer

```

## Channel Coding

### Hamming Codes
- [[Hamming Codes]]

```python
# channel_coding.py

import numpy as np

class HammingCode:
    def __init__(self):
        # Define generator and parity check matrices for Hamming(7,4)
        self.G = np.array([
            [1, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 0, 1]
        ])
        
        self.H = np.array([
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1]
        ])
        
        # Syndrome table for error correction
        self.syndrome_table = {
            '000': 0,    # No error
            '111': 1,    # Error in bit 1
            '110': 2,    # Error in bit 2
            '011': 3,    # Error in bit 3
            '100': 4,    # Error in bit 4
            '101': 5,    # Error in bit 5
            '010': 6,    # Error in bit 6
            '001': 7     # Error in bit 7
        }

    def encode(self, data):
        """
        Encode data using Hamming(7,4) code
        Input: data bits in groups of 4
        Output: encoded data in groups of 7
        """
        # Reshape data into groups of 4 bits
        remainder = len(data) % 4
        if remainder != 0:
            # Pad with zeros if necessary
            padding = 4 - remainder
            data = np.append(data, np.zeros(padding))
        
        num_blocks = len(data) // 4
        data = data.reshape((num_blocks, 4))
        
        # Encode each block
        encoded = np.zeros((num_blocks, 7))
        for i in range(num_blocks):
            encoded[i] = np.mod(np.dot(data[i], self.G), 2)
            
        return encoded.flatten()

    def decode(self, received_data):
        """
        Decode received data using Hamming(7,4) code
        Input: received data in groups of 7
        Output: decoded data in groups of 4
        """
        num_blocks = len(received_data) // 7
        received_data = received_data.reshape((num_blocks, 7))
        decoded = np.zeros((num_blocks, 4))
        
        for i in range(num_blocks):
            # Calculate syndrome
            syndrome = np.mod(np.dot(self.H, received_data[i]), 2)
            syndrome_str = ''.join(syndrome.astype(int).astype(str))
            
            # Correct error if present
            error_pos = self.syndrome_table[syndrome_str]
            if error_pos > 0:
                received_data[i][error_pos-1] ^= 1
                
            # Extract data bits (positions 0,1,2,4)
            decoded[i] = received_data[i][[0,1,2,4]]
            
        return decoded.flatten()

    def calculate_ber(self, original, decoded):
        """Calculate Bit Error Rate"""
        return np.sum(original != decoded) / len(original)

```

```python
# main.py
# Modified main.py (key changes only)

# Add to imports
from channel_coding import HammingCode

# Modify the Properties class to include channel coding
class Properties:
    def __init__(self, frequency, number_of_Symbols, amplitude, channel_coding='none'):
        self.frequency = frequency
        self.number_of_Symbols = number_of_Symbols
        self.amplitude = amplitude
        self.channel_coding = channel_coding

# Modify Channel class to handle coded data
class Channel:
    def __init__(self, channel_name, txData, _system, EbN0dBs):
        self.channel_name = channel_name
        self.txData = txData
        self.EbN0dBs = EbN0dBs
        self.hamming = HammingCode() if _system.properties.channel_coding == 'hamming' else None
        
        ber_len = len(EbN0dBs)
        simulatedBer = np.zeros(ber_len)
        
        if channel_name == "AWGN":
            for j, EbN0dB in enumerate(EbN0dBs):
                noiseGamma = 10 ** (EbN0dB / 10)
                avgPower = np.mean(np.abs(txData) ** 2)
                linear_noisePower = avgPower / noiseGamma
                
                noise_vector = np.sqrt(linear_noisePower / 2) * np.random.standard_normal(txData.shape)
                noisy_signal = txData + noise_vector
                
                # Apply Hamming decoding if enabled
                if self.hamming:
                    rxData = (noisy_signal >= 0).astype(int)
                    rxData = self.hamming.decode(rxData)
                    sourceData = self.hamming.decode((txData >= 0).astype(int))
                else:
                    rxData = (noisy_signal >= 0).astype(int)
                    sourceData = (txData >= 0).astype(int)
                
                simulatedBer[j] = np.sum(rxData != sourceData) / len(sourceData)
                
            self.rxData = rxData
            self.simulatedBER = simulatedBer

# Modify modulation functions to handle coded data
def bpsk(_system):
    # Generate random bits
    random_bits = np.random.randint(2, size=int(_system.properties.get_number_of_Symbols()))
    
    # Apply Hamming encoding if enabled
    if _system.properties.channel_coding == 'hamming':
        hamming = HammingCode()
        random_bits = hamming.encode(random_bits)
    
    # BPSK modulation
    _constellation = _system.properties.amplitude * np.array([-1, 1])
    _modulated = _constellation[random_bits]
    
    return _modulated, _constellation

```

```python
# modulation_analyzer.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

class ModulationAnalyzer:
    def __init__(self, system):
        self.system = system
        self.metrics = {}
        
    def analyze_spectral_efficiency(self):
        """Calculate and compare spectral efficiency"""
        self.metrics['spectral_efficiency'] = {
            'bpsk': 1.0,  # 1 bit/s/Hz
            'qpsk': 2.0   # 2 bits/s/Hz
        }
        
    def analyze_power_efficiency(self, EbN0dBs):
        """Calculate power efficiency at different Eb/N0 values"""
        # Theoretical BER calculations
        bpsk_ber = 0.5 * erfc(np.sqrt(10 ** (EbN0dBs / 10)))
        qpsk_ber = erfc(np.sqrt(10 ** (EbN0dBs / 10))) * 0.5
        
        # Find minimum Eb/N0 required for BER = 10^-5
        target_ber = 1e-5
        bpsk_required_ebn0 = EbN0dBs[np.where(bpsk_ber < target_ber)[0][0]]
        qpsk_required_ebn0 = EbN0dBs[np.where(qpsk_ber < target_ber)[0][0]]
        
        self.metrics['power_efficiency'] = {
            'bpsk': {
                'required_ebn0': bpsk_required_ebn0,
                'ber_curve': bpsk_ber
            },
            'qpsk': {
                'required_ebn0': qpsk_required_ebn0,
                'ber_curve': qpsk_ber
            }
        }
        
    def analyze_implementation_complexity(self):
        """Compare implementation complexity"""
        self.metrics['complexity'] = {
            'bpsk': {
                'constellation_points': 2,
                'decision_regions': 1,
                'hardware_complexity': 'Low'
            },
            'qpsk': {
                'constellation_points': 4,
                'decision_regions': 2,
                'hardware_complexity': 'Moderate'
            }
        }
        
    def plot_comparison(self, EbN0dBs):
        """Generate comprehensive comparison plots"""
        fig = plt.figure(figsize=(15, 10))
        
        # BER Performance
        ax1 = fig.add_subplot(221)
        ax1.semilogy(EbN0dBs, self.metrics['power_efficiency']['bpsk']['ber_curve'], 
                    'b-', label='BPSK')
        ax1.semilogy(EbN0dBs, self.metrics['power_efficiency']['qpsk']['ber_curve'], 
                    'r--', label='QPSK')
        ax1.set_xlabel('Eb/N0 (dB)')
        ax1.set_ylabel('BER')
        ax1.grid(True)
        ax1.legend()
        ax1.set_title('BER Performance Comparison')
        
        # Spectral Efficiency
        ax2 = fig.add_subplot(222)
        schemes = ['bpsk', 'qpsk']
        efficiencies = [self.metrics['spectral_efficiency'][scheme] for scheme in schemes]
        ax2.bar(schemes, efficiencies)
        ax2.set_ylabel('bits/s/Hz')
        ax2.set_title('Spectral Efficiency')
        
        # Constellation Diagram
        ax3 = fig.add_subplot(223)
        # BPSK constellation
        ax3.plot([-1, 1], [0, 0], 'bo', label='BPSK')
        # QPSK constellation
        qpsk_real = [1/np.sqrt(2), -1/np.sqrt(2), -1/np.sqrt(2), 1/np.sqrt(2)]
        qpsk_imag = [1/np.sqrt(2), 1/np.sqrt(2), -1/np.sqrt(2), -1/np.sqrt(2)]
        ax3.plot(qpsk_real, qpsk_imag, 'ro', label='QPSK')
        ax3.grid(True)
        ax3.set_xlabel('In-Phase')
        ax3.set_ylabel('Quadrature')
        ax3.legend()
        ax3.set_title('Constellation Diagrams')
        
        # Required Eb/N0 for target BER
        ax4 = fig.add_subplot(224)
        required_ebn0 = [
            self.metrics['power_efficiency']['bpsk']['required_ebn0'],
            self.metrics['power_efficiency']['qpsk']['required_ebn0']
        ]
        ax4.bar(schemes, required_ebn0)
        ax4.set_ylabel('Required Eb/N0 (dB) for BER = 10^-5')
        ax4.set_title('Power Requirement Comparison')
        
        plt.tight_layout()
        return fig
    
    def generate_recommendation(self):
        """Generate a recommendation based on analysis"""
        recommendation = {
            'high_bandwidth_efficiency': 'QPSK',
            'power_constrained': 'BPSK',
            'simple_implementation': 'BPSK',
            'balanced_performance': 'QPSK'
        }
        
        return recommendation

def compare_modulation_schemes(system, EbN0dBs):
    """Main function to compare modulation schemes"""
    analyzer = ModulationAnalyzer(system)
    
    # Perform analysis
    analyzer.analyze_spectral_efficiency()
    analyzer.analyze_power_efficiency(EbN0dBs)
    analyzer.analyze_implementation_complexity()
    
    # Generate plots
    comparison_plot = analyzer.plot_comparison(EbN0dBs)
    
    # Get recommendations
    recommendations = analyzer.generate_recommendation()
    
    return analyzer.metrics, recommendations, comparison_plot

```