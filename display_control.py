#! /usr/bin/env python3

import schedule
import time
import config

controller = config.screen_power
# indicator = config.screen_sensor


def toggle():
    controller.on()
    time.sleep(0.1)
    controller.off()


if __name__ == "__main__":
    toggle()

    # eventually, this can be rewritten as a 'Display' class, which should allow for some more customization
    # having it as a class instead of just a library should let you define methods for {on, off, toggle}
    # This is all, of course, dependent on being able to find a way to detect the actual status of the display, and
    # capturing it as an InputDevice on a GPIO pin
