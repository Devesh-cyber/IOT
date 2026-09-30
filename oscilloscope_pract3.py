# Practical 3: Raspberry Pi Based Oscilloscope
#
# Connection:
# ADS1115 VDD  -> Raspberry Pi Physical Pin 1 (3.3V)
# ADS1115 GND  -> Raspberry Pi Physical Pin 6 (GND)
# ADS1115 SDA  -> Raspberry Pi Physical Pin 3 (GPIO2 / SDA)
# ADS1115 SCL  -> Raspberry Pi Physical Pin 5 (GPIO3 / SCL)
# Signal       -> ADS1115 A0
#
# I2C Address: 0x48
#
# Setup:
# sudo raspi-config
# Enable I2C
#
# Required packages:
# pip install board --break-system-packages
# sudo pip install drawnow --break-system-packages
# sudo apt-get install -y i2c-tools python3-smbus
# python3 -m pip install --upgrade --no-cache-dir adafruit-blinka adafruit-circuitpython-busdevice adafruit-circuitpython-ads1x15 --break-system-packages

from collections import deque
import time
import board
import busio
import numpy as np
import matplotlib.pyplot as plt
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn
from matplotlib.animation import FuncAnimation


# ================= SETTINGS =================

DURATION = 10          # Seconds shown on screen
SAMPLE_RATE = 128     # ADS1115 sample rate
GAIN = 1              # ±4.096V
CHANNEL = 0           # ADS1115 A0
I2C_ADDRESS = 0x48

# ============================================


# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)


# ADC setup
ads = ADS1115(i2c, address=I2C_ADDRESS)
ads.data_rate = SAMPLE_RATE
ads.gain = GAIN
chan = AnalogIn(ads, CHANNEL)


# Buffer
num_samples = SAMPLE_RATE * DURATION

x = np.linspace(0, DURATION, num_samples)

y = deque(
    [0.0] * num_samples,
    maxlen=num_samples
)


# Plot
fig, ax = plt.subplots()

ax.set_xlim(0, DURATION)
ax.set_ylim(-4.2, 4.2)

ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")
ax.set_title("ADS1115 Software Oscilloscope")

ax.grid(True)

line, = ax.plot(x, y, lw=1)


# Update loop
def update(frame):

    try:
        voltage = chan.voltage

    except Exception:
        voltage = 0.0

    y.append(voltage)

    line.set_ydata(y)

    return line,


# Animation
ani = FuncAnimation(
    fig,
    update,
    interval=1000 / SAMPLE_RATE,
    blit=True
)


plt.show()