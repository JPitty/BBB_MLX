#!/usr/bin/env python

import Adafruit_BBIO.PWM as PWM
import time, pyinotify
 
red = "P8_13"
green = "P9_16"
blue = "P9_14"
 
PWM.start(red, 10)
PWM.start(blue, 10)
PWM.start(green, 10)

wm = pyinotify.WatchManager()
mask = pyinotify.IN_MODIFY

def fade(colorA, colorB, ignore_color):
    PWM.set_duty_cycle(ignore_color, 100)
    for i in range(0, 100):
	    PWM.set_duty_cycle(colorA, i)
	    PWM.set_duty_cycle(colorB, 100-i)
	    time.sleep(0.03)

def combo(r, g, b):
    PWM.set_duty_cycle(red, float(r))
    PWM.set_duty_cycle(green, float(g))
    PWM.set_duty_cycle(blue, float(b))

def blinkit(r, g, b, t):
    combo(0, 0, 0)
    time.sleep(t)
    combo(r, g, b)

class EventHandler (pyinotify.ProcessEvent):
 def process_IN_MODIFY(self, event):
   f=open("/root/RGB",'r')
   req=str.strip(f.read())
   f.close()
   
   if req == 'fade':
    fade(red, green, blue)
    fade(green, blue, red)
    fade(blue, red, green)
    combo(0,0,0)
   elif req == 'blink':
    blinkit (0, 40, 0, 0.1)
   elif len(str.split(req)) == 3:
    c=str.split(req)
    combo(c[0], c[1], c[2])
   else:
    combo(0,0,0)

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch('/root/RGB', mask)
notifier.loop()
