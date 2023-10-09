from kittenbot.KOI import *

koi = KOI()
koi.screen_mode(2)
koi.color_cali("red")
time.sleep(10)

try:
    while True:
        print(koi.color_tracking("red"))
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()
