import time, datetime
import os

os.system('fswebcam -r 1920x1080 -s focus=50 --list-controls --png 0  --save /home/pi/Desktop/%H%M%S.png')
whattime = datetime.date.today()
print whattime
