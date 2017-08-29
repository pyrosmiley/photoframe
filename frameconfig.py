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
power_button = gpiozero.Button(3)
slideshow = gpiozero.Button(6)
update_sys_button = gpiozero.Button(5)
help_button = gpiozero.Button(19)

#led = gpiozero.RGBLED(red=21,green=20,blue=16)
