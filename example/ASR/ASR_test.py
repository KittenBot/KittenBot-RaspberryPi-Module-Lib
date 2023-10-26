#方糖语音识别
#程序现象：说出唤醒词之后，终端打印识别到的相关指令
#         识别到查询日期：播报2023年10月8日，识别到查询问题播报：22.56度

from kittenbot.ASR import *#引入相关库
asr = SugarASR('/dev/ttyS0')#初始化方糖语音模块

#程序主循环
while True:
    if asr.detected():#是否触发语音识别
        print(asr.cmd)#打印检测到的命令

        if asr.cmd == "check_weather":#当命令是查询日期时
            asr.tts_date(2023,10,8)#播报日期
        if asr.cmd == "check_temperature":#当命令是查询温度时
            #播报温度
            asr.tts_words("temperature_is")
            time.sleep(1)
            asr.tts_double(22.56)
            time.sleep(3)
            asr.tts_words("degrees")
