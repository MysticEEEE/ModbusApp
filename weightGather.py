import serial
import sys
import logging
import modbus_tk
import modbus_tk.utils as ut
import modbus_tk.defines as cst
import modbus_tk.modbus as modbus
import modbus_tk.modbus_rtu as modbus_rtu
import time
import threading
import os
import pandas as pd



logger = modbus_tk.utils.create_logger("console")
logger.disabled = False

maoZhonglist = []
jingZhonglist = []
port = 'COM7'

path = os.getcwd()

ser = serial.Serial(
            port = port,
            baudrate= 9600,
            bytesize = 8,
            parity= 'N',
            stopbits = 2,
            xonxoff=0)
#master = modbus_rtu.RtuMaster(ser)
#master.execute(slave=1,function_code=16,starting_address=54,quantity_of_x=2,output_value=100)
startTime = time.time()

def maoZhong():
    while time.time()-startTime<=3:
        try:
            master = modbus_rtu.RtuMaster(ser)
            master.set_timeout(0.5)
            master.set_verbose(True)
    
            #print('Connected successfully')
            received_MaoZhong = master.execute(1,cst.READ_HOLDING_REGISTERS,80,2)
            #master.execute(slave=1,function_code=3,starting_address=80,quantity_of_x=2)
            maoZhonglist.append(received_MaoZhong[1])
            
        except modbus.ModbusError as err:
            logger.error("%s- Code=%d", err, err.get_exception_code())
            #print('Error')
    return maoZhonglist 

def jingZhong():
    while time.time()-startTime<=3:
        try:
            master = modbus_rtu.RtuMaster(ser)
            master.set_timeout(0.5)
            master.set_verbose(True)
    
            #print('Connected successfully')
            received_jinZhong = master.execute(1,cst.READ_HOLDING_REGISTERS,82,2)
            jingZhonglist.append(received_jinZhong[1])
            
        except modbus.ModbusError as err:
            logger.error("%s- Code=%d", err, err.get_exception_code())
            #print('Error')
    return jingZhonglist

def piZhong():
    try:
        master = modbus_rtu.RtuMaster(ser)
        master.set_timeout(0.5)
        master.set_verbose(True)
        logger.info(master.execute(1,cst.WRITE_MULTIPLE_REGISTERS,84,output_value=[0,50])) #写入皮重
    except modbus.ModbusError as err:
        logger.error("%s- Code=%d", err, err.get_exception_code())

def write(slave,address,value):
    try:
        master = modbus_rtu.RtuMaster(ser)
        master.set_timeout(0.5)
        master.set_verbose(True)
        logger.info(master.execute(slave,cst.WRITE_MULTIPLE_REGISTERS,address,output_value=value)) #写入皮重
    except modbus.ModbusError as err:
        logger.error("%s- Code=%d", err, err.get_exception_code())
def read(slave,address,quantity):
    try:
        master = modbus_rtu.RtuMaster(ser)
        master.set_timeout(0.5)
        master.set_verbose(True)
        logger.info(master.execute(slave,cst.READ_HOLDING_REGISTERS,address,quantity)) #写入皮重
    except modbus.ModbusError as err:
        logger.error("%s- Code=%d", err, err.get_exception_code())

def save(path):
    data = jingZhong()
    newData = pd.DataFrame(data)
    newData.columns=['Weight']
    # newData = newData[order]
    newData.to_excel(path+'\\'+'test.xlsx')
    print('Save Suceessfully!')
    
#写入存储，净重，皮重，去皮

if __name__ == '__main__':

    logger = modbus_tk.utils.create_logger("console")
    master = modbus_rtu.RtuMaster(ser)
    master.set_timeout(0.5)
    master.set_verbose(True)

    # master = modbus_rtu.RtuMaster(ser)
    # master.set_timeout(0.5)
    # master.set_verbose(True)
    # #logger.info(master.execute(1,cst.WRITE_MULTIPLE_REGISTERS,84,output_value=[0,50])) #写入皮重
    # logger.info(master.execute(1,cst.WRITE_MULTIPLE_REGISTERS,93,output_value=[1]))
    # logger.info(master.execute(1,cst.READ_HOLDING_REGISTERS,42,2))
    # #print(main())
    # path = os.getcwd()
    # save(path)
    read(2,2,1)
    # read(1,36,10)