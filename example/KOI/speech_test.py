from kittenbot.KOI import *

koi = KOI()
koi.screen_mode(2)
print("Please note the screen prompt to wait for the ambient noise calibration to complete")
koi.audio_noisetap()

try:
    while True:
        cmd = input("Choose Train A, Train B, or Identify:\n")
        if cmd == "Train A":
            koi.speech_add_tag("A")
        elif cmd == "Train B":
            koi.speech_add_tag("B")
        elif cmd == "Identify":
            print(koi.speech_run())
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()
