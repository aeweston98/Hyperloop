# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 13:01:09 2016

@author: anthonyweston
"""

import time
import paho.mqtt.client as mqtt
from multiprocessing import Process
#import numpy as np

#to delay the publish requests use sleep(x), x in seconds


#the class for keeping track of the transmission data
class transmission_data:
    
    def __init__(self, pub_topics, sub_topics, iden):
        self.pub_topics = pub_topics
        self.sub_topics = sub_topics
        self.iden = iden
    
    sent = 0
    received = 0
    times = []
    failed = 0
    
#subscription topics for pub a/ sub b and pub b/ sub b
a_topics = ["test/topic1", "test/topic2", "test/topic3", "test/topic4", "test/topic5"]
b_topics = ["test/topic6", "test/topic7", "test/topic8", "test/topic9", "test/topic10"]

#define a data object for each transmission direction
a_to_b = transmission_data(a_topics, b_topics, "pub a to sub b")
b_to_a = transmission_data(b_topics, a_topics, "pub b to sub a")

#function to interpret the results of the test and print them to the console
def data_interp(t):
    time_sum = 0
    for x in range((t.received+t.failed)):
        time_sum += t.times[x]
        
    avg_time = (time_sum / (t.received + t.failed))*1000
    no_send = ((t.sent - t.received - t.failed) / t.sent)*100
    fail_send = (t.failed / t.sent) * 100
    correct_send = (t.received / t.sent) * 100
    
    print("For the transmission from " + t.iden + ":")
    print("The average time for transmission is " + str(avg_time) + " ms")
    print("The percentage of failed transmissions is " + str(no_send) + " %")
    print("The percentage of corrupted transmissions is " + str(fail_send) + " %")
    print("The percentage of successful transmissions is " + str(correct_send) + " %")



#get the user defined values for the program
test = str(input("What testing string do you want to use? "))

frequency = int(input("With what frequency would you like to publish your data (ms)? "))

num = int(input("How many iterations would you like to have? "))



#the code for the mqtt clients and target functions for multiprocessing (one for publishing, one for subscribing)
#this has to be hard coded into the file
hostname = "159.203.42.214:18083"

mqtta = mqtt.connect(hostname)
mqttb = mqtt.connect(hostname)

def publish_a(mqtto, t, test, n):
    for y in range(n):
        for x in range(5):
            cur = time.time()
            send = str(cur) + " " + str(test)
            mqtto.publish(t.pub_topics[x], payload = send)
            t.sent += 1;
            
def subscribe_a(mqtto, t, test, n):
    for y in range(n):
        for x in range(5):
            
            msg = mqtto.subscribe(t.sub_topics[x])
            
            end = time.time()

            data = msg.payload.split()
            elapsed = end - int(data[0])
            t.times.append(elapsed)            
            
            if data[1] == test:
                t.received += 1
            else:
                t.failed += 1
                
if __name__=='__main__':
    p1 = Process(target = publish_a(mqtta, a_to_b, test, num))
    p2 = Process(target = subscribe_a(mqttb, a_to_b, test, num))
    p3 = Process(target = publish_a(mqttb, b_to_a, test, num))
    p4 = Process(target = subscribe_a(mqtta, b_to_a, test, num))
    p1.start()
    p2.start()
    p3.start()
    p4.start()



#print the results of the test
data_interp(a_to_b)
data_interp(b_to_a)

