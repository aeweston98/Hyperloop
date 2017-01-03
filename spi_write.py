# might need to merge send/recieve to a singe file

import paho.mqtt.client as mqtt
from multiprocessing import Process
from config import values_to_transmit
import config as cfg
import time
import serial

write_ser = serial.Serial("/dev/ttyS0" baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None)


class spiWrite(Process):
    def __init__(self, queue):
        super(spiWrite, self).__init__()
        self.queue = queue

    def run(self):

        while True:
            if not self.queue.empty():

                