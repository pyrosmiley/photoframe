#!/bin/bash

export DISPLAY=:0.0
XAUTHORITY=/home/pi/.Xauthority

#add -z for randomization
# -Z auto zoom
# -F fullscreen
# -Y hide mouse pointer
# -D [n] (--slideshow-delay) automatically progress slides after [n] seconds
# -f [FILE] read from file list, one file per line

# run slideshow with background process
feh -Z -F -Y --cycle-once /home/pi/Documents/photoframe/helpfiles/ &
