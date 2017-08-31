#! /usr/bin/env python

import schedule
import time
import frameconfig as config

screen = config.screen_power

def toggle():
    screen.on()
    time.sleep(0.1)
    screen.off()

toggle()