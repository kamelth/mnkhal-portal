# Simple mqtt Publisher

import paho.mqtt.client as paho
import sys
import json
import time

client = paho.Client()

if client.connect('localhost', 1883, 60) != 0:
    print('Couldn\'t connect to MQTT Broker!')
    sys.exit(-1)

for i in range(30):
    payload = {
        "weight": i*5,
        "vibration": i*10
    }
    client.publish('test/sensors', json.dumps(payload), 0)
    time.sleep(10)

client.disconnect()
