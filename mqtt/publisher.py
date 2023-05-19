import paho.mqtt.client as mqtt


def on_connect(client_pub, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print("Failed to connect, return code: " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

broker_address = "localhost"
topic = "Reshmanth"

client.connect(broker_address, 1883, 60)

while True:
    message = input("Enter a message (or 'exit' to quit): ")
    client.publish(topic, message)
    if message == 'exit':
        break
    # client.publish(topic, message)

client.disconnect()
