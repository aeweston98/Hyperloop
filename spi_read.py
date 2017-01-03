# code to read values off the wire

import paho.mqtt.client as mqtt
from multiprocessing import Process
from config import values_to_transmit
import config as cfg
import time
import serial

ser = serial.Serial("/dev/ttyS0" baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)

class spi(Process):
    def __init__(self, queue):
        super(spiRead, self).__init__()
        self.read_queue = read_queue
        self.write_queue = write_queue


    def run(self):

        while True:
        	data_out = self.write_queue.get()


        	check = ser.read(1)
        	
        	if check == '@':
            	data = read_ser.read()
            	#decode data
            	#data = float(data.decode(encoding="utf-8"))
            	self.read_queue.put(data)
                