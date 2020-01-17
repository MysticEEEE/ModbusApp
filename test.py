import serial
import serial.tools.list_ports
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

PORT = 'COM3'

def main():
    try:
        master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,
		        baudrate=9600,
		        bytesize=8,
		        parity='N',
		        stopbits=2,
		        xonxoff=0))
        
        master.set_timeout(5)
        master.set_verbose(True)
        
        print('connected')
        #read 方法
        print(master.execute(1,cst.READ_HOLDING_REGISTERS,80,2))#slaveAddr funCode startAddr regNum
        #write方法
        #print(master.execute(35, cst.WRITE_MULTIPLE_REGISTERS, 9, output_value=[1]))
    except modbus_tk.modbus_rtu.ModbusInvalidResponseError as err:
        print(err)

if __name__ == '__main__':
    main()