from kittenbot.ENV import *
import time
env = ENV()

while True:
    time.sleep(1)
    print("temp:",env.update()[0],"°")
    print("hum:",env.update()[1],"%")