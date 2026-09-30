# Practical 7: IoT Based Web Controlled Home Automation
# Raspberry Pi Relay Control
#
# Relay connection:
# Relay IN  -> Raspberry Pi Physical Pin 37
# Relay GND -> Raspberry Pi GND pin 6
# Relay VCC -> Appropriate supply for relay module pin 2
#
# Required package:
# sudo apt install python3-rpi.gpio
#
# Run:
# python3 practical_7_home_automation.py

import RPi.GPIO as GPIO
from time import sleep

relay_pin = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)

GPIO.output(relay_pin, 1)

try:
    while True:
        GPIO.output(relay_pin, 0)
        sleep(5)

        GPIO.output(relay_pin, 1)
        sleep(5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()