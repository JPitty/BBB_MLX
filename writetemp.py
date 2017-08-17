#!/usr/bin/python
# Example to read i2c device on BBB using Adafruit's lib
# Lamprey 1.10 cape with MLX90614 IR temp device connected to bus 2 @0x20 addr
# JP 8/17/17

from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x20,1) #device addr, busnum
from time import sleep
import display, sys, time

counter = 0
samples = sys.argv[1]

def writetf(tfstr):
    with open("/root/BBB_MLX/RGB", "w") as tf:
        tf.write(str(tfstr))

#wakeup the led:
writetf('0 50 0')
sleep(1)
writetf('0 0 0')

try:
  with open("/root/BBB_MLX/data", "w") as data:
    while counter < int(samples):
      tobj1 = i2c.readU16(0x7)
      tobj1 = tobj1*0.02-273.15
      data.write(str(time.time())  + " " + str(tobj1) + "\n")
      counter += 1
      sleep(0.05)

except KeyboardInterrupt:
    print ""
    print "bye."
