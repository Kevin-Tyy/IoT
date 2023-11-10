import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/coderz")

def on_message(client, userdata, msg):
    data = str(msg.payload.decode())
    name, ms = data.split(":")
    print(f"{name}: {ms}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("82.165.97.169", 1883, 60)
# Start the network loop
client.loop_start()
name = "The Freak"

while True:
    message = input("")
    client.publish("/coderz", name+":"+message)