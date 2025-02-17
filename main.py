from fullScreen import *
from socketComms import SocketComms
import urllib.error
import time


comms = SocketComms('127.0.0.1', 7500, 7501)
comms.start()
screenRun()
time.sleep(6)

import entryscreen
entryscreen.start(comms)


