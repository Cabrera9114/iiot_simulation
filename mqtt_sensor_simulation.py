
import paho.mqtt.client as mqtt
import random
import time

# MQTT broker details
broker = "localhost"
port = 1883
topic = "sensor/data"

def simulate_sensor_data():
    while True:
        temperature = round(random.uniform(20.0, 25.0), 2)
        humidity = round(random.uniform(30.0, 50.0), 2)
        payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'
        client.publish(topic, payload)
        print(f"Published: {payload}")
        time.sleep(1)

client = mqtt.Client()
client.connect(broker, port)
simulate_sensor_data()
