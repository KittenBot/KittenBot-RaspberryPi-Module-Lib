from kittenbot.ASR import *
import time

asr = SugarASR('/dev/ttyS0')

while True:
    if asr.detected():
        print(asr.cmd)
        if asr.cmd == "check_weather":
            asr.tts_date(2023,10,8)
        if asr.cmd == "check_temperature":
            asr.tts_words("temperature_is")
            time.sleep(1)
            asr.tts_double(22.56)
            time.sleep(3)
            asr.tts_words("degrees")
