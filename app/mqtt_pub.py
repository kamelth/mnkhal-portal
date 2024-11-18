import paho.mqtt.client as mqtt

# EC2 public IP and MQTT broker port (1883)
broker = "34.228.22.195"
port = 1883  # Default MQTT port

# Define the topic
topic = "test/sensors"

# Define the message
message = "Hello from Python!"

# Create a client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker, port, 60)

# Publish a message to the topic
client.publish(topic, message)

# Disconnect from the broker
client.disconnect()

print(f"Message '{message}' published to topic '{topic}'")
