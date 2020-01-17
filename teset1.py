
import serial
import binascii
import time
ser = serial.Serial()
 
def port_open():
    ser.port = 'COM7'            #设置端口号
    ser.baudrate = 9600     #设置波特率
    ser.bytesize = 8        #设置数据位
    ser.stopbits = 2        #设置停止位
    ser.parity = "N"        #设置校验位
    ser.open()              #打开串口,要找到对的串口号才会成功
    if(ser.isOpen()):
        print("打开成功")
    else:
        print("打开失败")
 
def port_close():
    ser.close()
    if (ser.isOpen()):
        print("关闭失败")
    else:
        print("关闭成功")
 
def send(send_data):
    if (ser.isOpen()):
        #ser.write(send_data.encode('utf-8'))  #utf-8 编码发送
        #ser.write(binascii.a2b_hex(send_data))  #Hex发送
        ser.write(send_data)
        print("发送成功",send_data)
    else:
        print("发送失败")
 
def hexShow(argv):  
    result = ''  
    hLen = len(argv)  
    for i in range(hLen):  
        hvol = ord(argv[i])  
        hhex = '%02x'%hvol  
        result += hhex+' '  
    return result
 
if __name__ == "__main__":
    port_open()
    #port_close()
    a = 'A0068000010201D6'
    b = 'A0038200DB'
    d=bytes.fromhex('A0068000010201D6')
    c=bytes.fromhex('A0038200DB') 
    while True:
        send(c)
        time.sleep(1) 
        n = ser.inWaiting()
        if n: 
            # s = hexShow(n)
            # print(s)
            try:   #如果读取的不是十六进制数据--
                data= str(binascii.b2a_hex(t.read(num)))[2:-1] #十六进制显示方法2
                print(data)
            except: #--则将其作为字符串读取
                str = ser.read(n)  
#print(str)  
            # hexShow(str)
            print(str)  
        serial.Serial.close(ser)

