from kittenbot.KOI import *

koi = KOI()
koi.screen_mode(2)
try:
    while True:
        print(koi.circle_detect())
        #print(rectangle_detect())
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()
