'''
import paho.mqtt.client as mqtt
from multiprocessing import Process
import config as cfg
import time


class Subscriber(Process):
    def __init__(self):
        super(Subscriber, self).__init__()

    @staticmethod
    def _on_connect(client, userdata, rc):
        # Leave the sending of data to another process
        print("Sub Initialised")
        client.subscribe("/Test")

    @staticmethod
    def _on_publish(client, userdata, msg):
        # Use another process to handle incoming data and reduce loads
        print(msg.resp)

    def run(self):
        client = mqtt.Client()
        client.qos = 0
        client.on_connect = Subscriber._on_connect
        client.on_publish = Subscriber._on_publish

        client.connect(cfg.broker_addr, 1883, 60)
        client.loop_forever()
'''