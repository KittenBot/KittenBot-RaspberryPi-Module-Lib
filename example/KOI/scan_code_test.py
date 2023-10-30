#扫码测试
#现象描述：程序启动之后，输入qrcdoe扫描二维码，barcode扫描条形码，apriltag扫描apriltag标签
from kittenbot.KOI import *#引入相关库

koi = KOI()#初始化KOI
koi.screen_mode(2)#设置为后置摄像头

try:
    #程序主循环
    while True:
        #print(koi.scan_qrcode())#识别二维么
        print(koi.scan_barcode())#识别条形码
        #print(koi.scan_apriltag())#识别apiiltag标签
except KeyboardInterrupt:
    koi.stop()#捕获异常，停止运行模型
