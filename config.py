#!/usr/bin/env python

import gpiozero

### GPIO PIN LOCATIONS: ###
power_button = gpiozero.Button(3, bounce_time=0.1)
slideshow_button = gpiozero.Button(6, bounce_time=0.1)
update_button = gpiozero.Button(5, bounce_time=0.1)
help_button = gpiozero.Button(19, bounce_time=0.1)
screen_power = gpiozero.OutputDevice(22)

led = gpiozero.RGBLED(red=21,green=20,blue=16)
speed = 0.0025


if __name__ == '__main__':
    pass
