#!/usr/bin/env python3

import os
import subprocess
from signal import pause
#import schedule

import psutil
from pykeyboard import PyKeyboard
import config
import display_control

path = config.file_dir
help_path = (path + "/helpfiles")

power_button = config.power_button
slideshow_button = config.slideshow_button
update_button = config.update_button
help_button = config.help_button
screen = config.screen_power

led = config.led

press_count = 0

# use PyKeyboard module to simulate spacebar for help menu progression
try:
    key = PyKeyboard()
except:
    key = 0


# ===============================================================================
# BUTTON FUNCTIONS:
# Script will listen for button presses 
# then call appropriate function for each.
# I'm trying to limit the amount of coding in this script 
# for changeability, since this service cannot be
# edited once deployed to the init.d folder.
# ===============================================================================


def power_off():
    #####
    display_control.toggle()
    #####
    os.system("/sbin/shutdown -h now")


def sys_update():
    os.system("python frame_update.py")


def show_start():
    os.system(os.path.join(path, "./slideshow_start.sh"))
    led.pulse(on_color=(0, 0.75, 0), n=3, background=True)


def show_stop():
    os.system("./slideshow_stop.sh")


# As there are multiple python process running, need to determine if the slideshow is active or not.
# If it is active, script will collect its PID and stop it. If not, it will start.
def slide_toggle():
    try:
        pid = int(subprocess.check_output(['pidof', 'python', 'pictureframe.py']).decode("utf-8"))
        print("Checking for currently running slideshow process.")
    except subprocess.CalledProcessError as e:
        pid = 0
        print(">>>No slideshow process found.")
    if pid > 0:
        show_stop()
        print(">>>Stopping slideshow. Process ID is {}.".format(pid))
    else:
        show_start()
        print(">>>Starting show. PID value {} indicates no show running.".format(pid))


# Help screens are image files found in path defined above. Use feh to present slides. Use PyKeyboard to simulate space bar
# iff the feh process is currently running, and count the number of presses to restart the main show after help is exited.

def show_help():
    global press_count
    num_slides = len(os.listdir(help_path))
    help_active = False

    for proc in psutil.process_iter():
        if proc.name() == "feh":
            help_active = True
        else:
            pass
    if help_active == True:
        if press_count < num_slides:
            key.tap_key('space')  # DOES NOT WORK OVER SSH
            press_count += 1
            print("slide count: {}    press count: {}".format(num_slides, press_count))
        else:
            key.tap_key('space')
            press_count = 0
            show_start()
    else:
        show_stop()
        os.system("./help_slides.sh")
        press_count += 1


def manual_update():
    subprocess.call(['python3', '{}/download_flickr_set.py'.format(path), '1', '&'], shell=False)
    # download_flickr_set()


#os.chdir(file_dir)

####----TEMP----####
#display_control.toggle()
####----TEMP----####

if __name__ == "__main__":

    if config.startup: show_start()

    power_button.when_pressed = power_off

    slideshow_button.when_pressed = slide_toggle

    help_button.when_pressed = show_help

    # update_sys_button.when_pressed = sys_update

    update_button.when_pressed = manual_update

    pause()
