#语音识别（仅支持旧版本固件）
#现象描述：程序运行后，输入Train A：学习指令A，Train B：学习指令B，Identify：识别指令
from kittenbot.KOI import *#引入相关库

koi = KOI()#初始化KOI
koi.screen_mode(0)#设置后置摄像头
print("Please note the screen prompt to wait for the ambient noise calibration to complete")#显示在终端的提示信息
koi.audio_noisetap()#初始化语音识别

try:
    #程序主循环
    while True:
        cmd = input("Choose Train A, Train B, or Identify:\n")#等待用户输入
        if cmd == "Train A":
            koi.speech_add_tag("A")#学习指令A
        elif cmd == "Train B":
            koi.speech_add_tag("B")#学习指令B
        elif cmd == "Identify":
            print(koi.speech_run())#识别指令
        time.sleep(0.1)
except KeyboardInterrupt:
    koi.stop()#捕获异常停止KOI模型
