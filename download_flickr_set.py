#!/usr/bin/env python3

# download_flickr_set.py

"""Check specified Flickr album and synchronize with designated photos directory. All variables pull from config.py
and keys.py, so this WILL NOT WORK if not set properly over there. Also assumes usage of a common-anode RGB LED, which
is meant as an indicator for currently running process, but will flash ONLY if called manually via button push, or
with the argument '1' when called from command line."""

# Heavily modified but based very much on Jarvl's at https://gist.github.com/Jarvl/3799acac27283f80641d57804faac9ae
# ...which in turn is a fixed version of this instructable: http://www.instructables.com/id/Internet-Photo-Frame/

import flickrapi
import requests
import os
import sys
from re import match
from multiprocessing import Process, Event, Lock
import config
import keys
from time import sleep


p_dir = config.p_path

FLICKR_KEY = keys.F_API_KEY
FLICKR_SECRET = keys.F_SECRET
USER_ID = keys.F_USER_ID
SET_ID = keys.F_SET_ID

led = config.led

bright = config.bright  # LED brightness
blink = 1 if len(sys.argv) > 1 else 0


def connect():
    pass


def make_url(photo):
    # url_template = "http://farm{farm-id}.staticflickr.com/
    #                 {server-id}/{id}_{secret}_[mstzb].jpg"
    photo['filename'] = "%(id)s_%(secret)s_h.jpg" % photo
    url = ("http://farm%(farm)s.staticflickr.com/%(server)s/%(filename)s" % photo)
    return url, photo['filename']


def flash(vRed, vGreen, vBlue):
    if blink == 1:
        led.color = (vRed, vGreen, vBlue)
    else:
        pass


def main():
    flash(0, bright, bright)  # cyan

    print(" ---> Requesting photos...")
    flickr = flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET)
    photos = flickr.walk_set(SET_ID)

    count = 0
    update = False

    for photo in photos:
        count += 1

        url, filename = make_url(photo.attrib)
        path = "{}/{}".format(p_dir,filename)
    #check to see if file already exists
        try:
            os.stat(path)
            print(" ---> Already have {}".format(url))
            flash(bright, bright, 0)  # yellow
    #download content and save to new image file
        except:
            print(" ---> Downloading {}".format(url))
            flash(bright * 0.75, 0, bright)  # purple
            r = requests.get(url)
            with open("{}".format(path), 'wb') as imageFile:
                for chunk in r.iter_content(100000):
                    imageFile.write(chunk)
                update = True
                print(path)
        sleep(0.2)
    sleep(3)

    # check to see if it needs to remove photos from folder
    filelist = os.listdir(p_dir)
    if count < len(filelist):
        print(" ---> Removing photos")
        flash(bright, 0, 0)  # red
        for f in filelist:
            pics = flickr.walk_set(SET_ID)
            print(f)
            for pic in pics:
                url, filename = make_url(pic.attrib)
                matchObj = match(f, filename)
                if matchObj:
                    print(" ---> Found {}, matched {}".format(f, filename))
                    break
            else:
                print(" ---> Deleting {}".format(f))
                os.remove("{}/{}".format(p_dir,f))
                update = True
    sleep(0.5)

    # if it added or removed a photo, update slideshow
    print(">>>done")
    if update == True and blink == 1:
        print(" ---> Restarting slideshow")
        os.system("{}/slideshow_stop.sh".format(config.file_dir))
        os.system("{}/slideshow_start.sh".format(config.file_dir))
    else:
        print("~fin~")


if __name__ == '__main__':
    main()

    quit()
