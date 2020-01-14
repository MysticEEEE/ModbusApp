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

port = 'COM1'
logger = modbus_tk.utils.create_logger("console")

def main():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(
            port = port,
            baudrate= 9600,
            bytesize = 8,
            parity= 'O',
            stopbits = 1))

        master.set_timeout(5)
        master.set_verbose(True)

        print('Connected successfully')

        received = master.execute(1,cst.READ_HOLDING_REGISTERS,2,8)
        logger.info(received)
        print('received',received)

    except modbus.ModbusError as err:
        logger.error('Error')

if __name__ == '__main__':
    main()