#人脸检测
#现象描述：运行程序之后，屏幕将会启用前置摄像头。在检测到人脸时输出koi矩形左上角坐标，没有检测到时候输出-1
from kittenbot.KOI import *#引入相关库
koi = KOI()#初始化KOI
koi.screen_mode(2)#前置2，后置0
koi.face_yolo_init()#初始化，人脸模型

#程序主循环
while True:
	face_xy = koi.get_face_coord()#获取人脸坐标
	print("x:",face_xy['x'],"y:",face_xy['y'])#将坐标打印到控制台
	time.sleep(0.5)#设置一定延时

