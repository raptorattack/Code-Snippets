#https://pypi.python.org/pypi/PyUserInput/#downloads
#/usr/local/lib/python2.7/dist-packages/pykeyboard/x11.py

import time
from pykeyboard import PyKeyboard

k = PyKeyboard()

time.sleep(5)
while True:

    k.press_key('Control_L')
    k.tap_key('w')
    k.release_key('Control_L')


    time.sleep(6)
    k.press_key('Control_L')
    k.press_key('Shift_L')
    k.tap_key('t')
    k.release_key('Shift_L')
    k.release_key('Control_L')
    time.sleep(25)
    k.tap_key(k.function_keys[5])
    time.sleep(25)
    k.tap_key(k.function_keys[5])
    time.sleep(25)


