import paho.mqtt.client as mqtt
from multiprocessing import Process
from config import values_to_transmit
import config as cfg
import time
import json

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


topics = ["levFrontLeftDprValue", "levFrontRightDprValue", "levBackLeftDprValue", "levBackRightDprValue", "levLowPressure", "levHighPressure", "levFrontLeftDistance", "levFrontRightDistance", "levBackLeftDistance", "ecFirstDistance", "ecSecondDistance", "ecThirdDistance", "batteryTemperature", "batteryFirstVoltage", "batterySecondVoltage"]


class PubSub(Process):
    def __init__(self, queue_sub, queue_pub):
        super(PubSub, self).__init__()
        self.queue_sub = queue_sub
        self.queue_pub = queue_pub

    @staticmethod
    def _on_connect(client, userdata, rc):
        client.subscribe("levFrontLeftDprValue")
        print("Connected with result code "+str(rc))

    @staticmethod
    # The callback for when a PUBLISH message is received from the server.
    def _on_message(client, userdata, msg):
        self.queue_sub.put()
        print(msg.topic + " "+ str(msg.payload))

    @staticmethod
    def _on_publish(client, userdata, msg):
        #time.sleep(0.001)
        print(msg)

    def run(self):
        client = mqtt.Client()
        client.qos = 2
        client.on_connect = PubSub._on_connect
        client.on_message = PubSub._on_message
        client.on_publish = PubSub._on_publish

        client.connect(cfg.broker_addr, 1883, 60)
        client.loop_start()

        # Needed so sub can catch pubs from itself
        time.sleep(1)
        # Publishes values as they are added to the stack
        while True:
            if not self.queue_pub.empty():
                out_list = self.queue_pub.get()

                #for x in range(16):
                    #client.publish(topics[x], out_list[x])
