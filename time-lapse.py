import os
import time
from time import strftime

FRAMES = 10
TIMEBETWEEN = 6

frameCount = 0
while frameCount < FRAMES:
    imageNumber = str(frameCount).zfill(7)
    TIME = time.strftime("%m-%d-%Y--%H:%M:%S")
    os.system("raspistill -o /home/pi/Pictures/picture_%s.jpg"%(TIME))
    frameCount += 1;
    time.sleep(TIMEBETWEEN - 6)


raise SystemExit
