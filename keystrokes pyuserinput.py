#https://pypi.python.org/pypi/PyUserInput/#downloads

import time
from pykeyboard import PyKeyboard

k = PyKeyboard()

time.sleep(5)
k.press_key('H')
k.tap_key('e')
k.release_key('H')
print "works"
