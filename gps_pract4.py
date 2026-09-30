# Practical 5: Raspberry Pi GPS Module Interfacing
#
# Serial Port: /dev/ttyAMA0
# Baud Rate: 9600
#
# Setup:
# sudo nano /boot/config.txt
#
# Add:
# dtparam=spi=on
# dtoverlay=pi3-disable-bt
# core_freq=250
# enable_uart=1
# force_turbo=1
#
# Then:
# sudo systemctl stop serial-getty@ttyS0.service
# sudo systemctl disable serial-getty@ttyS0.service
# sudo systemctl enable serial-getty@ttyAMA0.service
#
# Install:
# sudo apt-get install minicom
# sudo pip install pynmea2
#
# Run:
# python3 practical_5_gps.py

import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

port = "/dev/ttyAMA0"

# Create serial object
ser = serial.Serial(
    port,
    baudrate=9600,
    timeout=0.5
)

while True:
    try:
        data = ser.readline()
    except:
        print("loading")

    if data[0:6] == b'$GPGGA':
        msg = pynmea2.parse(data.decode(errors="ignore"))
        print(msg)
        time.sleep(2)