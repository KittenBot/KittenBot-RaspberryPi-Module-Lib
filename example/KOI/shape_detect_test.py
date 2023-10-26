#图形追踪
#现象描述：
from kittenbot.KOI import *#引入相关库

koi = KOI()#初始化koi
koi.screen_mode(0)#设置为后置摄像头
try:
    #程序主循环
    while True:
        print(koi.circle_detect())#检测圆形，反馈相关信息，通过注释启用或者关闭
        #print(rectangle_detect())#检测矩形，反馈相关信息，通过注释启用或者关闭
        time.sleep(0.1)#一定的延时
except KeyboardInterrupt:
    koi.stop()#捕获异常，停止koi模型
