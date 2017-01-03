'''
import paho.mqtt.client as mqtt
from multiprocessing import Process
import config as cfg
import time


class Publisher(Process):
    def __init__(self):
        super(Publisher, self).__init__()

    # The callback for when the client receives a CONNACK response from the server.
    @staticmethod
    def __on_connect(client, userdata, rc):
        client.subscribe("/Test")
        print("Pub Connected with result code "+str(rc))
        for j in range(1, 1000):
            # Arguments are stream to publish to, and string to publish
            client.publish("/Test", str(j))

    # The callback for when a PUBLISH message is received from the server.
    @staticmethod
    def __on_publish(client, userdata, msg):
        # Use another process to handle incoming data and reduce loads
        print(msg)

    def run(self):
        client = mqtt.Client()
        client.qos = 0
        client.on_connect = Publisher.__on_connect
        client.on_publish = Publisher.__on_publish

        client.connect(cfg.broker_addr, 1883, 60)
        client.loop_forever()
'''