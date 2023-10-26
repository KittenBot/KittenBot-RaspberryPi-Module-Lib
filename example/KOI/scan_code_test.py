from kittenbot.KOI import *

koi = KOI()
koi.screen_mode(2)

try:
    while True:
        cmd = input("Choose qrcode, barcode, or apriltag:\n")
        if cmd == "qrcode":
            print(koi.scan_qrcode())
        elif cmd == "barcode":
            print(koi.scan_barcode())
        elif cmd == "apriltag":
            print(koi.scan_apriltag())
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()