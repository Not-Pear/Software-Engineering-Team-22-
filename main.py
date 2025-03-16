from fullScreen import FullScreen
from socketComms import SocketComms
import urllib.error
import time


comms = SocketComms('127.0.0.1', 7500, 7501)
comms.start()
fullscreen = FullScreen()
fullscreen.run()
time.sleep(3)

import entryscreen
entryscreen.start(comms)


