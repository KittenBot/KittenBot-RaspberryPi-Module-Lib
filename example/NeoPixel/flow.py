from kittenbot.NeoPixel import *
import time

neopix = NeoPixel(18,60)

while True:
	for i in range(60):
		neopix.setColor(i,(255,255,255))
		neopix.display()
		time.sleep(0.1)

	for i in range(59,-1,-1):
		neopix.setColor(i,(0,0,0))
		neopix.display()
		time.sleep(0.1)

