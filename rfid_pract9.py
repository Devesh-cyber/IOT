# Practical 9: Raspberry Pi with RFID Module
#
# Connections:
# RFID PN532 -> Raspberry Pi
# GND -> Physical Pin 6
# VCC -> Physical Pin 2
# SDA -> Physical Pin 3
# SCL -> Physical Pin 5
#
# I2C Channel:
# Channel 1 -> ON
# Channel 2 -> OFF
#
# Setup:
# sudo raspi-config
# Enable I2C
#
# Install:
# pip3 install adafruit-circuitpython-pn532 --break-system-packages
#
# Run:
# python3 practical_9_rfid.py

import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize PN532
pn532 = PN532_I2C(i2c)

# Check firmware
ic, ver, rev, support = pn532.firmware_version

print(f"Success! Found PN532 with Firmware: {ver}.{rev}")
print("Place your card on the reader...")

# Read RFID card UID
while True:
    uid = pn532.read_passive_target(timeout=0.5)

    if uid is not None:
        print(f"Found Tag! ID is: {[hex(i) for i in uid]}")