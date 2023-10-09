from kittenbot.KOI import *

koi = KOI()
koi.screen_mode(2)

try:
    while True:
        cmd = input("select record or play:\n")
        if cmd == "record":
            koi.audio_record("test.wav")
        elif cmd == "play":
            koi.audio_play("test.wav")
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()