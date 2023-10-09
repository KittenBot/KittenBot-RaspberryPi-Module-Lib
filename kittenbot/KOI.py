import threading
import serial
import time

class KOI(threading.Thread):
    def __init__(self,serial_port='/dev/ttyS0', baud_rate=115200):
        threading.Thread.__init__(self)
        self.koi = serial.Serial(serial_port,baud_rate)
        self.running = True
        if not self.koi.isOpen():
            print("open filed")
        else:
            print("open success: ")
            print(self.koi)

        count = 0
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
    
    def run(self):
        while self.running:
            if self.koi.in_waiting:
                data = self.ser.read(self.ser.in_waiting)
                print('Received:', data)
                
    def stop(self):
        self.running = False
    
    def init_yolo_face():
        self.koi.write("K30\r\n".encode())
    
    def refresh_face_quantity():
        self.koi.write("K31\r\n".encode())
        
if __name__ == '__main__':
    st = KOI()
    st.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        st.stop()

