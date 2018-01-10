#!/usr/bin/env python

import gpiozero
import os
import sys

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_dir)

### GPIO PIN LOCATIONS: ###

power_button = gpiozero.Button(3, bounce_time=0.1)
slideshow_button = gpiozero.Button(7, bounce_time=0.1)
update_button = gpiozero.Button(25, bounce_time=0.1)
help_button = gpiozero.Button(8, bounce_time=0.1)
screen_power = gpiozero.OutputDevice(5)

led = gpiozero.RGBLED(red=21,green=20,blue=16)

# rainbow LED speed
speed = 0.0025
# LED brightness (value should be 0.3-1)
bright = 0.5


#UPDATE INTERVAL:
interval = 15  #minutes

# Folder location for photos. To specify a folder *outside* of the "photoframe" directory, make sure to
# use the full file path, e.g. commented example below. DO NOT put a '/' at the end or things will break!
#p_path = "/home/pi/Pictures/flickr"
p_path = (file_dir + "/photos")


#SLIDESHOW SETTINGS:
startup = True   #start show automatically on startup? True or False
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
