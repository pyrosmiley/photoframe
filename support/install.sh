#!/usr/bin/env bash

#Does installing things, hopefully. WIP.

"""
In ~/.config/lxsession/LXDE-pi/autostart
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@point-rpi
#@/usr/bin/python /home/pi/Documents/photoframe/button_control.py
@/bin/bash /etc/init.d/button_service start

"""

#Test Network Connectivity:
case "$(curl -s --max-time 2 -I http://google.com | sed 's/^[^ ]*  *\([0-9]\).*/\1/; 1q')" in
  [23]) echo ">>>Successfully connected to the Internet!";;
  5) echo ">>>Blocked by proxy settings";;
  *) echo ">>>Network connection unsuccessful";;
esac

#Determine install location:

#Install system dependencies:
echo ">>>Checking for system dependencies"
sudo apt-get install python3 python3-setuptools libjpeg-dev zlib1g-dev libpng12-dev libfreetype6-dev
sudo apt-get install python3-pip
sudo apt-get install unclutter

#Install python dependencies:
sudo pip install pi3d
sudo pip3 install Pillow
sudo pip3 install PyUserInput
sudo pip3 install gpiozero
sudo pip3 install flickrapi
sudo pip3 install requests
sudo pip3 install psutil

#set up private keys.py file:
cp keys.sample.py keys.py

#make shell scripts executable:
sudo chmod u+x slideshow_start.sh slideshow_stop.sh

#System configuration:
sudo raspi-config # set gpu_mem=128
#disable autosleep

#Write data to LXDE-pi/autostart and copy file

#Write data to init.d and install service
echo ">>>Installing Button Input Daemon..."
chmod +x /etc/init.d/button_service
cp /photoframe/support/button_service /etc/init.d/button_service
echo ">>>Activating Button Service..."
update-rc.d button_service defaults
echo "Success"


#Add photo update to crontab:

#Initial Photo Download:
echo "Attempting initial photo download"



