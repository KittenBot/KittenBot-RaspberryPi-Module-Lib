import threading
import serial
import time

class KOI(threading.Thread):
    def __init__(self,serial_port='/dev/ttyS0', baud_rate=115200):
        threading.Thread.__init__(self)
        self.koi = serial.Serial(serial_port,baud_rate)

        if not self.koi.isOpen():
            print("open filed")
        else:
            print("open success: ")
            print(self.koi)

        self.running = False

        self.btn_state = {"btnA":0,"btnB":0}
        self.face_attributes = {"x":0,"y":0,"number":0}
        self.ip = ""
        self.cls_result = ""
        self.speech_result = ""
        self.qrcode_result = ""
        self.barcode_result = ""
        self.apriltag_result = ""
        self.color_attributes = {"x":0,"y":0,"w":0,"h":0}
        self.line_attributes = {"x1":0,"y1":0,"x2":0,"y2":0}
        self.rectangle_attributes = {"x":0,"y":0,"w":0,"h":0}
        self.circle_attributes = {"x":0,"y":0,"r":0}
        self.baiduAi_face_feature = ""

        count = 0
        data = ""
        while True:
            if count >= 10:
                print("Please restart KOI !")
            self.koi.write("K0\r\n".encode())
            time.sleep(1)
            bytes_to_read = self.koi.in_waiting
            if bytes_to_read:
                data = self.koi.read(bytes_to_read).decode()
                print(data)
            if "K0" in data:
                break
            count+=1
        print("init succeed")
        self.running = True
        self.start()
    
    def run(self):
        while self.running:
            if self.koi.in_waiting:
                try:
                    data = self.koi.read(self.koi.in_waiting).decode().strip().split()
                    print('Received:', data)
                    if data[0] == "K3":
                        self.btn_state["btnA"] = int(data[1])
                        self.btn_state["btnB"] = int(data[2])
                    elif data[0] == "K31":
                        if len(data) == 1:
                            self.face_attributes["x"] = -1
                            self.face_attributes["y"] = -1
                        else:
                            self.face_attributes["x"] = float(data[1])
                            self.face_attributes["y"] = float(data[2])
                    elif data[0] == "K32":
                        if len(data) == 1:
                            self.face_attributes["number"] = 0
                        else:
                            self.face_attributes["number"] = int(data[1])
                    elif data[0] == "K54":
                        self.ip = data[1]
                    elif data[0] == "K42":
                        self.cls_result = data[1]
                    elif data[0] == "K65":
                        self.speech_result = data[1]
                    elif data[0] == "K20":
                        self.qrcode_result = data[1]
                    elif data[0] == "K22":
                        self.barcode_result = data[1]
                    elif data[0] == "K23":
                        self.apriltag_result = data[1]
                    elif data[0] == "K15":
                        self.color_attributes["x"] = float(data[1])
                        self.color_attributes["y"] = float(data[2])
                        self.color_attributes["w"] = int(data[3])
                        self.color_attributes["h"] = int(data[4])
                    elif data[0] == "K12":
                        self.line_attributes["x1"] = float(data[1])
                        self.line_attributes["y2"] = float(data[2])
                        self.line_attributes["x2"] = float(data[3])
                        self.line_attributes["y2"] = float(data[4])
                    elif data[0] == "K11":
                        self.rectangle_attributes["x"] = float(data[1])
                        self.rectangle_attributes["y"] = float(data[2])
                        self.rectangle_attributes["w"] = int(data[3])
                        self.rectangle_attributes["h"] = int(data[4])
                    elif data[0] == "K10":
                        self.circle_attributes["x"] = int(data[1])
                        self.circle_attributes["y"] = int(data[2])
                        self.circle_attributes["r"] = int(data[3])
                except:
                    pass
            time.sleep(0.1)
                
    def stop(self):
        self.running = False
    
    def screen_mode(self,dir):
        self.koi.write("K6 {}\r\n".format(dir).encode())
        time.sleep(0.1)

    def display_text(self,x,y,delay,text):
        self.koi.write("K4 {} {} {} {}\r\n".format(x,y,delay,text).encode())
        time.sleep(0.1)

    def screen_save(self,pic_name):
        self.koi.write("K2 {}\r\n".format(pic_name).encode())
        time.sleep(0.1)

    def screen_show(self,pic_name):
        self.koi.write("K1 {}\r\n".format(pic_name).encode())
        time.sleep(0.1)
    
    def get_btn_state(self):
        self.koi.write("K3\r\n".encode())
        time.sleep(0.1)
        return self.btn_state
    
    def face_yolo_init(self):
        self.koi.write("K30\r\n".encode())
        time.sleep(0.1)
    
    def get_face_coord(self):
        self.koi.write("K31\r\n".encode())
        time.sleep(0.1)
        return self.face_attributes
    
    def get_face_number(self):
        self.koi.write("K32\r\n".encode())
        time.sleep(0.1)
        return self.face_attributes["number"]
    
    
    def connect_wifi(self,router,pwd):
        self.koi.write("K50 {} {}\r\n".format(router,pwd).encode())
        time.sleep(0.1)
    
    def get_ip(self):
        self.koi.write("K54\r\n".encode())
        time.sleep(2)
        return self.ip

    def cls_init(self):
        self.koi.write("K40\r\n".encode())
        time.sleep(0.1)
    
    def cls_add_tag(self,id):
        self.koi.write("K41 {}\r\n".format(id).encode())
        time.sleep(0.1)
    
    def cls_run(self):
        self.koi.write("K42\r\n".encode())
        time.sleep(0.2)
        return self.cls_result
    
    def cls_save_model(self,model):
        self.koi.write("K43 {}\r\n".format(model).encode())
        time.sleep(0.1)

    def cls_load_model(self,model):
        self.koi.write("K44 {}\r\n".format(model).encode())
        time.sleep(0.1)
    
    def audio_record(self,wav):
        self.koi.write("K61 {}\r\n".format(wav).encode())
        time.sleep(0.1)
    
    def audio_play(self,wav):
        self.koi.write("K62 {}\r\n".format(wav).encode())
        time.sleep(0.1)
        
    def audio_noisetap(self):
        self.koi.write("K63\r\n".encode())    
        time.sleep(0.1)
    
    def speech_add_tag(self,id):
        self.koi.write("K64 {}\r\n".format(id).encode())
        time.sleep(0.1)
    
    def speech_run(self):
        self.koi.write("K65\r\n".encode())
        time.sleep(0.1)
        return self.speech_result
    
    def speech_save_model(self,model):
        self.koi.write("K66 {}\r\n".format(model).encode())
        time.sleep(0.1)

    def speech_load_model(self,model):
        self.koi.write("K67 {}\r\n".format(model).encode())
        time.sleep(0.1)
    
    def scan_qrcode(self):
        self.koi.write("K20\r\n".encode())
        time.sleep(0.5)
        return self.qrcode_result

    def scan_barcode(self):
        self.koi.write("K22\r\n".encode())
        time.sleep(0.5)
        return self.barcode_result

    def scan_apriltag(self):
        self.koi.write("K23\r\n".encode())
        time.sleep(0.5)
        return self.apriltag_result

    def color_cali(self,name):
        self.koi.write("K16 {}\r\n".format(name).encode())
        time.sleep(0.1)
    
    def color_tracking(self,name):
        self.koi.write("K15 {}\r\n".format(name).encode())
        time.sleep(0.1)
        return self.color_attributes

    def line_tracking(self,name):
        self.koi.write("K12 {}\r\n".format(name).encode())
        time.sleep(0.1)
        return self.line_attributes
    
    def circle_detect(self,th=2000):
        self.koi.write("K10 {}".format(th).encode())
        time.sleep(0.5)
        return self.circle_attributes

    def rectangle_detect(self,th=2000):
        self.koi.write("K11 {}".format(th).encode())
        time.sleep(0.5)
        return self.rectangle_attributes
    
    def stop_kpu(self):
        self.koi.write("K98\r\n".encode())
        time.sleep(0.1)
    
    def reset(self):
        self.koi.write("K99\r\n".encode())
        time.sleep(0.15)

if __name__ == '__main__':

    koi = KOI()
    koi.screen_mode(2)
    try:
        while True:
            print(koi.circle_detect())
            time.sleep(0.1)
    except KeyboardInterrupt:
        koi.stop()


