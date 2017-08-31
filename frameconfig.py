#!/usr/bin/env python

from config_private import *
import gpiozero

#################
## FLICKR INFO ##
#################

F_API_KEY = config_private.F_API_KEY
F_SECRET = config_private.F_SECRET
F_USER_ID = "151931575@N06"
F_SET_ID = "72157682473955023"


### GPIO PIN LOCATIONS: ###
power_button = gpiozero.Button(3, bounce_time=0.1)
slideshow_button = gpiozero.Button(6, bounce_time=0.1)
update_button = gpiozero.Button(5, bounce_time=0.1)
help_button = gpiozero.Button(19, bounce_time=0.1)
screen_power = gpiozero.OutputDevice(22)

#led = gpiozero.RGBLED(red=21,green=20,blue=16)


if __name__ == '__main__':
    pass
