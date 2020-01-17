import serial
import time
import threading
import codecs
import modbus_tk as modstk
import string
import binascii


ser = serial.Serial(
    port="COM7",
    baudrate=9600,             # 115200,
    parity=serial.PARITY_NONE,
    stopbits=2,  # STOPBITS_TWO
    bytesize=serial.EIGHTBITS
    )      


def delayGather():
         # 选择串口，并设置波特率
    # n = ser.inWaiting()
    # if n:
    #     data = 
    if ser.is_open:
        print("port open success")
        # hex(16进制)转换为bytes(2进制)，应注意Python3.7与Python2.7此处转换的不同
        send_data = codecs.decode('A0038200DB','hex')    # 发送数据转换为b'\xff\x01\x00U\x00\x00V'
        ser.write(send_data)   # 发送命令
        # time.sleep(0.1)        # 延时，否则len_return_data将返回0，此处易忽视！！！
        #len_return_data = ser.inWaiting()  # 获取缓冲数据（接收数据）长度
        while ser.inWaiting()>0:
            send_data = codecs.decode('A0038200DB','hex')    # 发送数据转换为b'\xff\x01\x00U\x00\x00V'
            ser.write(send_data)
            received = ser.read(8)
            print(received)
            # return_data = ser.read(len_return_data)  # 读取缓冲数据
            # weight = str(return_data)
            # feedback_data = int(weight[2:8], 16)   # 修改x和y
            # print(feedback_data)
            # data = ser.readline(1)
            # print(data)
    else:
            print("port open failed")

    global timer
    timer = threading.Timer(1, delayGather)
    timer.start()

if __name__ == '__main__':
    #delayGather()
    
    if ser.is_open:
        #发送 
        d=bytes.fromhex('A0 03 82 00 DB') 
        ser.write(d)
        print("发送成功")
        #接收
        n=ser.inWaiting()
        if n: 
            data= str(binascii.b2a_hex(ser.read(n)))[2:-1]
            print(data)
        ser.close()



#print(received_MaoZhong,received_MaoZhong[1])
            #print(maoZhonglist)
            # if time.time()-startTime>=3:
            #     timer.cancel()
        #print(maoZhonglist)
        # if len(maoZhonglist)>60:
        #     return maoZhonglist
            #print(maoZhonglist)
        #print('received',received)



# time.sleep(0.007)
            # global timer
            # timer = threading.Timer(0.015, main)
            # timer.start()