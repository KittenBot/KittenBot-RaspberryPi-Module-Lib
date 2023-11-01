import RPi.GPIO as GPIO
import time

class Servo:
	def __init__(self,servoPIN):

		GPIO.setmode(GPIO.BCM)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(servoPIN, GPIO.OUT)

		self.p=GPIO.PWM(servoPIN,50)
		self.p.start(0)
	def setAngle(self,angle):
		angle = min(angle,176)
		try:
			self.p.ChangeDutyCycle(2.5+angle/360*20)
			time.sleep(0.2)
			self.p.ChangeDutyCycle(0)
			time.sleep(0.02)
		except KeyboardInterrupt:
			pass
