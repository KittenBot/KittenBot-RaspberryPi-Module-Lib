from rpi_ws281x import PixelStrip, Color


class NeoPixel():
	def __init__(self,pin,count):
		self.LED_COUNT = count
		LED_PIN = pin
		LED_BRIGHTNESS = 255
		LED_FREQ_HZ = 800000
		LED_DMA = 10
		LED_INVERT = False
		LED_CHANNEL = 0		
		self.strip = PixelStrip(self.LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
		self.strip.begin()
		
	def setColor(self,id,color):
		self.strip.setPixelColor(id,Color(color[0],color[1],color[2]))
	
	def setAllColor(self,color):
		for i in range(self.LED_COUNT):
			self.strip.setPixelColor(i,Color(color[0],color[1],color[2]))
	
	def display(self):
		self.strip.show()
	
