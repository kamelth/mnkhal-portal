import RPi.GPIO as GPIO
import time
import sys
import json
import paho.mqtt.client as paho
from hx711 import HX711

# MQTT Client Setup
def setup_mqtt():
    client = paho.Client()
    if client.connect('http://34.228.22.195/', 1883, 60) != 0:
        print('Couldn\'t connect to MQTT Broker!')
        sys.exit(-1)
    return client

# Vibration sensor setup
VIBRATION_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_PIN, GPIO.IN)

def pulse_in(pin, level, timeout=1000000):
    start_time = time.time()
    while GPIO.input(pin) != level:
        if (time.time() - start_time) > timeout / 1000000.0:
            return 0
    pulse_start = time.time()
    while GPIO.input(pin) == level:
        if (time.time() - start_time) > timeout / 1000000.0:
            return 0
    pulse_end = time.time()
    pulse_duration = (pulse_end - pulse_start) * 1000000
    return pulse_duration

def read_vibration():
    measurement = pulse_in(VIBRATION_PIN, GPIO.HIGH)
    return measurement

# Weight sensor setup
hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
referenceUnit = 114
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()
print("Tare done! Add weight now...")

def read_weight():
    val = hx.get_weight(5)
    hx.power_down()
    hx.power_up()
    return val

# Cleanup function for GPIO and HX711
def clean_and_exit():
    GPIO.cleanup()
    print("Cleaning up...")
    sys.exit()

# Main loop
if __name__ == "__main__":
    try:
        mqtt_client = setup_mqtt()

        while True:
            vibration_value = read_vibration()
            weight_value = read_weight()

            payload = {
                "weight": weight_value,
                "vibration": vibration_value
            }
            mqtt_client.publish('test/sensors', json.dumps(payload), 0)

            print(f"Published: {payload}")
            time.sleep(1)  # Publish data every second

    except (KeyboardInterrupt, SystemExit):
        clean_and_exit()
    finally:
        mqtt_client.disconnect()
