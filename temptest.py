#!/usr/bin/python
# Example to read i2c device on BBB using Adafruit's lib
# Lamprey 1.10 cape with MLX90614 IR temp device connected to bus 2 @0x20 addr
# JP 4/29/17

from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x20,2) #device addr, busnum
from time import sleep

tavg = 0
hot = 0

try:
  while 1:
    tobj1 = i2c.readU16(0x7)
    #print tobj1
    tobj1 = tobj1*0.02-273.15
    if tavg == 0:
        tavg = tobj1
    tavg = round(tavg * 0.9 + tobj1 * 0.1, 2)
    print tobj1 #, tavg

    #control the RGB led
    if tobj1 > 30 and hot == 0:
        hot = 1
        with open("RGB", "w") as tf:
            tf.write("100 0 0")
    if tobj1 < 30 and hot ==1:
        hot = 0
        with open("RGB", "w") as tf:
            tf.write("0 5 50")

    sleep(0.1)

except KeyboardInterrupt:
    print ""
    print "bye."
