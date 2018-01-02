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

#Install python dependencies:

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



