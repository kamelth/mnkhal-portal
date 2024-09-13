# Simple mqtt Subscriber

import paho.mqtt.client as paho
import sys


def onMessage(client, userData, msg):
    if msg.topic == 'test/weight':
        print(msg.topic + ': ' + msg.payload.decode())


client = paho.Client()
client.on_message = onMessage


if client.connect('172.19.0.2', 1883, 60) != 0:
    print('Couldn\'t connect to MQTT Broker!')
    sys.exit(-1)

client.subscribe('test/weight')

try:
    print('Press CTRL+C to exit...')
    client.loop_forever()
except:
    print('Disconnecting from Broker')


client.disconnect()
