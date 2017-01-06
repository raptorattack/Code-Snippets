import time, datetime
import os

os.system('fswebcam -r 1920x1080 --no-banner --set \'Focus (absolute)\'=250 --png  --save /home/pi/Desktop/%H%M%S.png')
#whattime = datetime.date.today()
#print whattime
