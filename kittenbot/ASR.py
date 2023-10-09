import serial
import time
import struct

instructions_input = {
	"asr100": "rouse",
	"asr200": "light_on",
	"asr201": "light_off",
	"asr202": "brighter",
	"asr203": "dimmer",
	"asr204": "red_light_on",
	"asr205": "green_light_on",
	"asr206": "yellow_light_on",
	"asr207": "blue_light_on",
	"asr208": "sitting_room_light_on",
	"asr209": "sitting_room_light_off",
	"asr210": "kitchen_light_on",
	"asr211": "kitchen_light_off",
	"asr212": "bedroom_light_on",
	"asr213": "bedroom_light_off",
	"asr214": "balcony_light_on",
	"asr215": "balcony_light_off",
	"asr216": "bathroom_light_on",
	"asr217": "bathroom_light_off",
	"asr218": "all_light_on",
	"asr219": "all_light_off",
	"asr300": "open_door",
	"asr301": "close_door",
	"asr302": "open_window",
	"asr303": "close_window",
	"asr304": "open_curtains",
	"asr305": "close_curtains",
	"asr306": "hanger_out",
	"asr307": "hanger_in_",
	"asr308": "fan_on",
	"asr309": "fan_off",
	"asr310": "speed_up",
	"asr311": "slow_down",
	"asr312": "air_conditioner_on",
	"asr313": "air_conditioner_off",
	"asr314": "music_on",
	"asr315": "music_off",
	"asr316": "pause",
	"asr317": "previous_song",
	"asr318": "next_song",
	"asr319": "volume_up",
	"asr320": "volume_down",
	"asr321": "robot_on",
	"asr322": "robot_off",
	"asr323": "robot_stop",
	"asr324": "move_forward",
	"asr325": "move_backward",
	"asr326": "turn_left",
	"asr327": "turn_right",
	"asr328": "lift_on",
	"asr329": "first_floor",
	"asr330": "second_floor",
	"asr331": "third_floor",
	"asr400": "check_temperature",
	"asr401": "check_humidity",
	"asr402": "check_weather",
	"asr403": "check_time",
	"asr404": "check_date",
	"asr405": "measure_distance",
	"asr406": "measure_temperature",
	"asr407": "measure_weight",
	"asr408": "measure_height",
	"asr901": "command_one",
	"asr902": "command_two",
	"asr903": "command_three",
	"asr904": "command_four",
	"asr905": "command_five",
	"asr906": "command_six",
	"asr907": "command_seven",
	"asr908": "command_eight",
	"asr909": "command_nine",
	"asr910": "command_ten"
}

instructions_output = {
	"temperature_is": b'\xAA\x55\x01\x55\xAA',
	"Humidity_is": b'\xAA\x55\x02\x55\xAA',
	"welcome": b'\xAA\x55\x05\x55\xAA',
	"distance_is": b'\xAA\x55\x06\x55\xAA',
	"millimeter": b'\xAA\x55\x07\x55\xAA',
	"centimeter": b'\xAA\x55\x08\x55\xAA',
	"meter": b'\xAA\x55\x09\x55\xAA',
	"body_temperature_is": b'\xAA\x55\x0A\x55\xAA',
	"weight_is": b'\xAA\x55\x0B\x55\xAA',
	"gram": b'\xAA\x55\x0C\x55\xAA',
	"kilogram": b'\xAA\x55\x0D\x55\xAA',
	"please_say_the_password": b'\xAA\x55\x0E\x55\xAA',
	"The_weather_is": b'\xAA\x55\x0F\x55\xAA',
	"sunny": b'\xAA\x55\x10\x55\xAA',
	"cloudy": b'\xAA\x55\x11\x55\xAA',
	"raining": b'\xAA\x55\x12\x55\xAA',
	"snowing": b'\xAA\x55\x13\x55\xAA',
	"haze": b'\xAA\x55\x14\x55\xAA',
	"big": b'\xAA\x55\x15\x55\xAA',
	"middle": b'\xAA\x55\x16\x55\xAA',
	"small": b'\xAA\x55\x17\x55\xAA',
	"which_floor_are_you_going_to": b'\xAA\x55\x18\x55\xAA',
	"yes": b'\xAA\x55\x19\x55\xAA',
	"no": b'\xAA\x55\x1A\x55\xAA',
	"percent": b'\xAA\x55\x1B\x55\xAA',
	"You_are_right": b'\xAA\x55\x1C\x55\xAA',
	"You_are_wrong": b'\xAA\x55\x1D\x55\xAA',
	"degrees": b'\xAA\x55\x1E\x55\xAA',
	"ok": b'\xAA\x55\x21\x55\xAA'
}
class SugarASR:
	def __init__(self):

		self.sugarASR = serial.Serial('/dev/ttyS0',115200)
		self.cmd = ""

		if not self.sugarASR.isOpen():
			print("open filed")
		else:
			print("open success: ")
			print(self.sugarASR)

	#获取指令，如果收到指令会返回True然后更新类属性cmd
	def detected(self):
		try:
			data = self.sugarASR.inWaiting()
			if data:
				self.cmd = instructions_input[self.sugarASR.read(data).decode()]
				return True
			else:
				return False
		except:
			return False
		finally:
			time.sleep(0.1)
	
	#播报内置语句
	def tts_words(self,text):
		self.sugarASR.write(instructions_output[text])

	#播报整数
	def tts_integer(self,num):
		data = [0xAA,0X55,0X20,0X00,0X00,0X00,0X00,0x55,0xAA]
		index = 0
		for i in range(3,7):
			data[i] = num >> index & 0xff
			index += 8
		self.sugarASR.write(bytearray(data))

	#播报小数
	def tts_double(self,f):
		data = [0xAA,0X55,0X1f,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0X00,0x55,0xAA]
		float_to_bytearray = struct.pack('d', f)
		index = 0
		for i in range(3,11):
			data[i] = float_to_bytearray[index]
			index += 1
		self.sugarASR.write(bytearray(data))

	#播报时间
	def tts_time(self,h,m):
		data = [0xAA,0X55,0X03,h,m,0x55,0xAA]
		self.sugarASR.write(bytearray(data))

	#播报日期
	def tts_date(self,y,m,d):
		data = [0xAA,0X55,0X04,0x00,0x00,0x00,0x00,0x00,0x00,0x55,0xAA]
		date_to_bytearray = struct.pack('<iBB',y,m,d)
		index = 0
		for i in range(3,9):
			data[i] = date_to_bytearray[index]
			index+=1
		self.sugarASR.write(bytearray(data))