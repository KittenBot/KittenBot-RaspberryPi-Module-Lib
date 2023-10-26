#色块追踪
#现象描述：程序运行之后会进入校准阶段，请将想要学习的色块完全置于正方形中，
#        十秒钟之后结束校准同时进入最追踪模式，屏幕将会不断打印色块信息

#引入相关库
from kittenbot.KOI import *

koi = KOI()#初始化koi
koi.screen_mode(0)#设置屏幕为前置
koi.color_cali("red")##学习颜色
time.sleep(10)#等待十秒

try:
    #程序主循环
    while True:
        print(koi.color_tracking("red"))#打印色块信息
        time.sleep(0.1)#一定的延时
except KeyboardInterrupt:
    koi.stop()#捕获异常后停止模型
