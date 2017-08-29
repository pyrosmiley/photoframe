#!/usr/bin/env python

#it may not be the most "proper" way but gpiozero is a very easy-to-use library. Importing RPi.GPIO just in case signal bouncing is noticed.
import gpiozero
import RPi.GPIO as GPIO
import subprocess
import psutil
from signal import pause
import os
from pykeyboard import PyKeyboard
import sys
from time import sleep

file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_dir)



path = "/home/pi/Documents/photoframe"
help_path = '/home/pi/Documents/photoframe/helpfiles' 

power_button = gpiozero.Button(3, bounce_time=0.1)
slideshow_button = gpiozero.Button(6, bounce_time=0.1)
update_button = gpiozero.Button(5, bounce_time=0.1)
help_button = gpiozero.Button(19, bounce_time=0.1)

#led = gpiozero.RGBLED(red=21,green=20,blue=16)

press_count = 0 

#use PyKeyboard module to simulate spacebar for help menu progression
try:
    key = PyKeyboard()
except:
    key = 0
#===============================================================================
# BUTTON FUNCTIONS:
# Script will listen for button presses 
# then call appropriate function for each.
# I'm trying to limit the amount of coding in this script 
# for changeability, since this service cannot be
# edited once deployed to the init.d folder.
#===============================================================================

def power_off():
    subprocess.call(['shutdown', '-h', 'now'], shell=False)
    
    
def sys_update() :    
    os.system("python frame_update.py")

def show_start():
    os.system(os.path.join(path, "./slideshow_start.sh"))
#    led.pulse(on_color=(0,0.75,0),n=3,background=True) 
    
    
def show_stop():
    os.system("./slideshow_stop.sh")
   
    
#As there are multiple python process running, need to determine if the slideshow is active or not. 
#If it is active, script will collect its PID and stop it. If not, it will start. 
def slide_toggle():
    global pid
    try:
        pid = subprocess.check_output(['pgrep', '-f', 'python pictureframe.py'], shell=False, stderr=subprocess.STDOUT)
        print("Checking for currently running slideshow process.")
    except subprocess.CalledProcessError as pid:
        pid = 0
        print(">>>No slideshow process found.")
    if pid > 0:
        show_stop()
        print(">>>Stopping slideshow. Process ID is {}.".format(pid))
    else:
        show_start ()
        print(">>>Starting show. PID value {} indicates no show running.".format(pid))      

#Help screens are image files found in path defined above. Use feh to present slides. Use PyKeyboard to simulate space bar 
#iff the feh process is currently running, and count the number of presses to restart the main show after help is exited.

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
            key.tap_key('space')    # DOES NOT WORK OVER SSH 
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
    subprocess.call(['python', '{}/download_flickr_set.py'.format(path), '1', '&'], shell=False)
    #download_flickr_set()


os.chdir(file_dir)
#show_start()

power_button.when_pressed = power_off 

slideshow_button.when_pressed = slide_toggle

help_button.when_pressed = show_help

#update_sys_button.when_pressed = sys_update

update_button.when_pressed = manual_update

pause()

