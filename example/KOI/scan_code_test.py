#扫码测试
#现象描述：程序启动之后，输入qrcdoe扫描二维码，barcode扫描条形码，apriltag扫描apriltag标签
from kittenbot.KOI import *#引入相关库

koi = KOI()#初始化KOI
koi.screen_mode(0)#设置为后置摄像头

try:
    #程序主循环
    while True:
        cmd = input("Choose qrcode, barcode, or apriltag:\n")#等待用户输入

        #根据输入内容进行对应操作
        if cmd == "qrcode":
            print(koi.scan_qrcode())#识别二维么
        elif cmd == "barcode":
            print(koi.scan_barcode())#识别条形码
        elif cmd == "apriltag":
            print(koi.scan_apriltag())#识别apiiltag标签
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()#捕获异常，停止运行模型
