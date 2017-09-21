#!/usr/bin/env python3

from time import sleep
from signal import pause
from config import led, speed


def rainbow():
        for n in range(100):
            led.color = (n/100,(100-n)/100,0)
            sleep(speed)
        for n in range(100):
            led.color =  ((100-n)/100,0,n/100)
            sleep(speed)
        for n in range(100): 
            led.color = (0,n/100,(100-n)/100)
            sleep(speed)
    else:
        led.color = (0,0,0)




    
#pause()

"""
led.pulse(fade_in_time=2, fade_out_time=0, on_color=(1,0,0), off_color=(0,0,1),n=1,background=False)
led.pulse(fade_in_time=2, fade_out_time=0, on_color=(0,0,1), off_color=(0,1,0),n=1,background=False)
led.pulse(fade_in_time=2, fade_out_time=0, on_color=(0,1,0), off_color=(1,0,0),n=1,background=False)
"""



#===============================================================================
# led.red = 1  # full red
# sleep(x)
# 
# led.red = 0.5  # half red
# sleep(x)
# 
# led.blue = 0.5
# sleep(x)
# 
# led.color = (0, 1, 0)  # full green
# sleep(x)
# 
# led.color = (1, 0, 1)  # magenta
# sleep(x)
# 
# led.color = (1, 1, 0)  # yellow
# sleep(x)
# 
# led.color = (0, 1, 1)  # cyan
# sleep(x)
# 
# led.color = (1, 1, 1)  # white
# sleep(x)
# 
# 
# led.color = (0, 0, 0)  # off
# sleep(x)
#===============================================================================


