import paho.mqtt.client as mqtt
import sqlite3

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("fromEsp8266")
def on_message(client, userdata, msg):
	conn = sqlite3.connect('sensor.db')
	c = conn.cursor()
	c.execute("INSERT into sensors VALUES(?,?)",(msg.payload[0], msg.payload[1]))
	conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
	
client.connect("192.168.1.70", 1883, 60)
client.loop_forever()
