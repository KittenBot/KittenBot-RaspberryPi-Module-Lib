#特征分类
#现象描述：程序运行之后，会出现输入提示，如果输入id1或者id2则是分别对两个物体进行训练。输入start开始识别，识别到的信息回打印到终端。
from kittenbot.KOI import *#引入相关库

koi = KOI()#初始化KOI
koi.screen_mode(0)#设置屏幕方向为前置
koi.cls_init()#初始化特征分类

#程序主循环
try:
    while True:
        
        cmd = input("Enter id1 or id2 for training and enter start for identification:")#提示用户输入
        
        #根据输入内容进行对应处理
        if cmd == 'start':
            break#结束训练状态
        elif cmd == 'id1':
            koi.cls_add_tag("id1")#训练id1
        elif cmd == 'id2':
            koi.cls_add_tag("id2")#训练id2
        time.sleep(0.1)#一定的延时
        
    while True:
        print(koi.cls_run())#打印识别结果
        time.sleep(0.5)#一定的延时
        
except KeyboardInterrupt:
    koi.stop()#异常捕获，释放KOI模型
