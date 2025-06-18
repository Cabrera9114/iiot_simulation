import paho.mqtt.client as mqtt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = []

def on_message(client, userdata, message):
    payload = message.payload.decode("utf-8")
    print("📥 Raw MQTT:", payload)

    now = datetime.now().replace(microsecond=0)
    try:
        values = eval(payload)
        temperature = values["temperature"]
        humidity = values["humidity"]
        print(f"✅ Parsed at {now}: Temp={temperature}, Humidity={humidity}")

        data.append({
            "timestamp": now,
            "temperature": temperature,
            "humidity": humidity
        })
    except Exception as e:
        print("❌ Failed to parse payload:", e)
        return

    if len(data) > 100:
        data.pop(0)

    df = pd.DataFrame(data)

    # Force timestamp as string label for x-axis
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["label"] = df["timestamp"].dt.strftime("%H:%M:%S")

    plt.clf()
    plt.plot(df["label"], df["temperature"], label="Temperature", marker="o", color="red")
    plt.plot(df["label"], df["humidity"], label="Humidity", marker="o", color="blue")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)


client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensor/data")
client.on_message = on_message

plt.ion()
plt.figure()
client.loop_start()
plt.show(block=True)
input("Press Enter to stop...\n")
