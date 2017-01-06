###   Idledale Weathercam REV1.0                   ###
###                                                ###
###   AUTHOR:   Emily Gomez                        ###
###   DATE:     1/5/2017                           ###
###   CONTACT:  emily.brockmeier@gmail.com         ###
###                                                ###
###   THIS CODE WAS DEVELOPED TO POST REGULAR      ###
###   PHOTOS OF THE WEATHER CONDITIONS IN          ###
###   IDLEDALE COLORADO.                           ###
###                                                ###
###   IT TAKES PHOTOS AND POSTS THEM TO A          ###
###   FACEBOOK PAGE AT                             ###
###   FACEBOOK.COM/PROFILE.PHO?ID=100014826400870  ###
###                                                ###


import os
import time
import glob
import sys
import dropbox

SLEEP = 3600 #time between updates (in seconds)

#START LOOP
while True:

#CAPTURE PHOTO
    os.system('fswebcam -r 1920x1080 --no-banner --png --save /home/pi/Pictures/weather.png')
#

# SECTION HERE THAT UPLOADS TO DROPBOX #
    client = dropbox.client.DropboxClient('***')
    #print ("linked account: ", client.account_info())

    f = open('/home/pi/Pictures/weather.png', 'rb')
    response = client.put_file('/home/pi/Pictures/weather.png', f)
    #print ('uploaded: ', response)

    folder_metadata = client.metadata('/')
    #print ('metadata: ', folder_metadata)

    f, metadata = client.get_file_and_metadata('/home/pi/Pictures/weather.png')
    out = open('response', 'wb')
    out.write(f.read())
    out.close()
    #print (metadata)
# SECTION HERE THAT UPLOADS TO DROPBOX #



#DELAY UNTIL NEXT PHOTO
    time.sleep(SLEEP) #set in start of code
#
