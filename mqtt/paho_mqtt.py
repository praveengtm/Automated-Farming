import paho.mqtt.client as mqtt
import sqlite3

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("fromEsp8266")
def on_message(client, userdata, msg):
	data_str = msg.payload.decode("utf-8")
	data_list = data_str.split(",")
	if len(data_list == 3):
		conn = sqlite3.connect('sensor.db')
		c = conn.cursor()
		c.execute("INSERT into sensors VALUES(?,?)",(data_list[0], data_list[1]))
		conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
	
client.connect("ip-address", 1883, 60)
client.loop_forever()
