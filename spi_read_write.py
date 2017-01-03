# code to read values off the wire

import paho.mqtt.client as mqtt
from multiprocessing import Process
from config import values_to_transmit
import config as cfg
import time
import serial

def start():
    ser = serial.Serial("/dev/cu.usbmodem0E218D01", baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)
    return ser

'''
	uint16_t levFrontLeftDprValue;
	uint16_t levFrontRightDprValue;
	uint16_t levBackLeftDprValue;
	uint16_t levBackRightDprValue;
	uint16_t levLowPressure;
	uint16_t levHighPressure;
	uint16_t levFrontLeftDistance;
	uint16_t levFrontRightDistance;
	uint16_t levBackLeftDistance;
	uint16_t levBackRightDistance;
	uint16_t ecFirstDistance;
	uint16_t ecSecondDistance;
	uint16_t ecThirdDistance;
	uint16_t batteryTemperature;
	uint16_t batteryFirstVoltage;
	uint16_t batterySecondVoltage;
'''



class spi(Process):
    def __init__(self, read_queue, write_queue, ser):
        super(spi, self).__init__()
        self.read_queue = read_queue
        self.write_queue = write_queue
        self.ser = ser


    def run(self):
        while True:
            values_in = []
            #check = self.ser.read(1)
            if 1 == 1:
                for x in range(16):
                    #data = self.ser.read(16)
                    #print(data)
                    #decode data
                    #data = float(data.decode(encoding="utf-8"))
                    values_in.append(x)
                    print(x)
        			# write data first 
                    #if not self.write_queue.empty():
                        #data_out = self.write_queue.get()
                        #self.ser.write(b'@')
                        #self.ser.write(data_out)  	  	
                self.read_queue.put(values_in)

