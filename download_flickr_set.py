#!/usr/bin/env python

import flickrapi
import requests
import os
import sys
import re
from multiprocessing import Process, Event, Lock


from time import sleep
import frameconfig



FLICKR_KEY = frameconfig.F_API_KEY
FLICKR_SECRET = frameconfig.F_SECRET
USER_ID = frameconfig.F_USER_ID
SET_ID = frameconfig.F_SET_ID

#led = RGBLED(red=17,green=27,blue=22)

bright = 0.5 #LED brightness
blink = 1 if len(sys.argv) > 1 else 0


def connect():
    pass

def make_url(photo):
    # url_template = "http://farm{farm-id}.staticflickr.com/
    #                 {server-id}/{id}_{secret}_[mstzb].jpg"
    photo['filename'] = "%(id)s_%(secret)s_h.jpg" % photo
    url = ("http://farm%(farm)s.staticflickr.com/%(server)s/%(filename)s" % photo) 
    return url, photo['filename']

#def flash(vRed, vGreen, vBlue):
    if blink == 1:
        led.color = (vRed, vGreen, vBlue)
    else:
        pass
    

def main():     
#    flash (0, bright, bright)  #cyan
    
    print (" ---> Requesting photos...")
    flickr = flickrapi.FlickrAPI(FLICKR_KEY,FLICKR_SECRET)
    photos = flickr.walk_set(SET_ID)
    
    count = 0
    update = False
    
    for photo in photos:
        count += 1

        url, filename = make_url(photo.attrib)
        path = '/home/pi/Pictures/flickr/%s' % filename 
        try:
            os.stat(path)
            print(" ---> Already have {}".format(url))
 #           flash(bright, bright, 0) #yellow

        except:
            print(" ---> Downloading {}".format(url))
 #           flash(bright*0.75, 0, bright)  #purple
            r = requests.get(url)      
            with open("{}".format(path), 'w+') as image_file:
                image_file.write("{}".format(r.content))
                update = True
        sleep(0.2)
    sleep(3)

    #check to see if it needs to remove photos from folder
    filelist = os.listdir("/home/pi/Pictures/flickr")
    if count < len(filelist):
        print(" ---> Removing photos")
#        flash(bright,0,0)               #red
        for f in filelist:
            pics = flickr.walk_set(SET_ID)
            print(f)
            for pic in pics:
                url, filename = make_url(pic.attrib)
                matchObj = re.match(f, filename)
                if matchObj:
                    print(" ---> Found {}, matched {}".format(f,filename))
                    break
            else:
                print(" ---> Deleting {}".format(f))
                os.remove("/home/pi/Pictures/flickr/{}".format(f))
                update = True    
    sleep(0.5)

    #if it added or removed a photo, update slideshow
    print(">>>done")
    if update == True and blink == 1:
        print(" ---> Restarting slideshow")
        os.system("/home/pi/Documents/photoframe/slideshow_stop.sh")
        os.system("/home/pi/Documents/photoframe/slideshow_start.sh")
    else:
        print("~fin~")
    

if __name__ == '__main__':
    main()
    
    quit()
