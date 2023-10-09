from kittenbot.KOI import *

koi = KOI()
koi.screen_mode(2)
koi.cls_init()

start = False
try:
    while True:
        if koi.get_btn_state()["btnA"] and koi.get_btn_state()["btnB"]:
            start = True
        elif koi.get_btn_state()["btnA"]:
            koi.cls_add_tag("id1")
        elif koi.get_btn_state()["btnB"]:
            koi.cls_add_tag("id2")
        while start:
            print(koi.cls_run())
            time.sleep(0.5)
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()
