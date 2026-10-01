# Raspberry Pi 4B — GPIO pin diagram

Top view of the 40-pin header, rotated so **pin 1 is at the top left**. The odd-numbered row faces the board interior; the even-numbered row faces the board edge. Pin 1 is at the end away from the USB/Ethernet ports.

Numbers beside the circles are **physical (BOARD) pins**. `GPIO` labels use **BCM numbering**.

```text
           Function / BCM    Physical    BCM / Function
                              ┌─────────┐
               3.3V power   │  1 ● ● 2│   5V power
        I2C1 SDA / GPIO 2   │  3 ● ● 4│   5V power
        I2C1 SCL / GPIO 3   │  5 ● ● 6│   Ground
                   GPIO 4   │  7 ● ● 8│   GPIO 14 / UART TX
                   Ground   │  9 ● ●10│   GPIO 15 / UART RX
                     GPIO 17  │ 11 ● ●12│   GPIO 18 / PWM0, PCM CLK
                     GPIO 27  │ 13 ● ●14│   Ground
                     GPIO 22  │ 15 ● ●16│   GPIO 23
                  3.3V power  │ 17 ● ●18│   GPIO 24
         SPI0 MOSI / GPIO 10  │ 19 ● ●20│   Ground
          SPI0 MISO / GPIO 9  │ 21 ● ●22│   GPIO 25
         SPI0 SCLK / GPIO 11  │ 23 ● ●24│   GPIO 8 / SPI0 CE0
                      Ground  │ 25 ● ●26│   GPIO 7 / SPI0 CE1
  HAT ID EEPROM SDA / GPIO 0  │ 27 ● ●28│   GPIO 1 / HAT ID EEPROM SCL
                      GPIO 5  │ 29 ● ●30│   Ground
                      GPIO 6  │ 31 ● ●32│   GPIO 12 / PWM0
              PWM1 / GPIO 13  │ 33 ● ●34│   Ground
      PWM1, PCM FS / GPIO 19  │ 35 ● ●36│   GPIO 16
                     GPIO 26  │ 37 ● ●38│   GPIO 20 / PCM DIN
                      Ground  │ 39 ● ●40│   GPIO 21 / PCM DOUT
                              └─────────┘
                         USB / Ethernet end
```

- **Power:** 3.3V on pins 1 and 17; 5V on pins 2 and 4.
- **Ground:** pins 6, 9, 14, 20, 25, 30, 34 and 39.
- **GPIO:** digital input/output at 3.3V logic; GPIO inputs are not 5V tolerant.
- **I2C:** SDA = data, SCL = clock.
- **SPI:** MOSI/MISO = data, SCLK = clock, CE = chip select.
- **UART:** TX = transmit, RX = receive.
- **PWM:** pulse-width modulation. **PCM:** digital audio.
- Alternate functions shown require configuration. Pins 27/28 are reserved for HAT identification.

**Numbering example:** `GPIO.BOARD` pin 16 is `GPIO.BCM` GPIO 23. For the TM1637 practical, BCM `clk=16, dio=18` means physical pins **36 and 12**; physical pins **16 and 18** require BCM `clk=23, dio=24`.

Sources: [Raspberry Pi 4B datasheet](https://pip-assets.raspberrypi.com/categories/545-raspberry-pi-4-model-b/documents/RP-008341-DS-1-raspberry-pi-4-datasheet.pdf), [Raspberry Pi GPIO documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio).
