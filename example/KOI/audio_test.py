#录音和播放
##现象描述，运行程序之后终端会出现输入提示。输入record之后屏幕会出现对应提示此时请录制音频。输入play播放录制好的声音
from kittenbot.KOI import *#引入相关库

koi = KOI()#初始化KOI
koi.screen_mode(0)#设置屏幕方向为后置

try:
    while True:
        
        cmd = input("select record or play:\n")#等待用户终端输入
        
        #根据输入内容执行录制或者播放
        if cmd == "record":
            koi.display_text(0,0,2000,"record...")#屏幕显示录制提示
            koi.audio_record("test.wav")#录制音频
        elif cmd == "play":
            koi.display_text(0,0,2000,"play...")#屏幕显示播放提示
            koi.audio_play("test.wav")#播放音频
        
except KeyboardInterrupt:
    koi.stop()#异常捕获，释放KOI模型
