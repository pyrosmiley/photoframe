#!/usr/bin/env python

import gpiozero

### GPIO PIN LOCATIONS: ###

power_button = gpiozero.Button(3, bounce_time=0.1)
slideshow_button = gpiozero.Button(6, bounce_time=0.1)
update_button = gpiozero.Button(5, bounce_time=0.1)
help_button = gpiozero.Button(19, bounce_time=0.1)
screen_power = gpiozero.OutputDevice(22)

led = gpiozero.RGBLED(red=21,green=20,blue=16)

# rainbow LED speed
speed = 0.0025
# LED brightness (value should be 0.3-1)
bright = 0.5


#UPDATE INTERVAL:
interval = 15  #minutes


#SLIDESHOW SETTINGS:
display_time = 15.0   # seconds to display each photo
fade_time = 3   # transition length. must be shorter than 1/2 of the display time
shuffle = True   # shuffle photos?
framerate = 24    # frames per second for animations. Use lower number for less of a performance hit.
PPS = 1   # Pictures Per Shader: no. of photos to display before changing shaders (set to 1 if only using basic shader!)

#transitions:
fade = True
star = False
holes = False
false = False
burn = True


if __name__ == '__main__':
    pass
