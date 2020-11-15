#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#define DHTPIN D2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
char hum[10];
char temp[10];
String data;

const char* wifi_network = "xender";
const char* wifi_pass = "CLFA56A210";
const char* mqtt_serv_address = "192.168.1.70"                                                                                                                                                                  ;
const int mqtt_port_number = 1883;

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup() {
Serial.begin(115200);
setup_wifi();
client.setServer(mqtt_serv_address, mqtt_port_number);
dht.begin();
}


void setup_wifi() {
delay(10);
// We start by connecting to a WiFi network
Serial.println();
Serial.print("Connecting to ");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
Serial.println(wifi_network);
WiFi.begin(wifi_network, wifi_pass);
while (WiFi.status() != WL_CONNECTED) {
WiFi.begin(wifi_network, wifi_pass);
Serial.print(".");
delay(5000);
}
Serial.println("");
Serial.println("WiFi connected");
Serial.println("IP address: ");
Serial.println(WiFi.localIP());
}
void reconnect() {
// Loop until we're reconnected
while (!client.connected()) {
Serial.print("Attempting MQTT connection...");
// Attempt to connect
if (client.connect("ESP8266Client"))
{
Serial.println("connected");




// Once connected, publish an announcement...
client.publish("fromEsp8266", "Hello world, I am ESP8266!");
} else {
Serial.print("failed, rc=");
Serial.print(client.state());
Serial.println(" try again in 5 seconds");
// Wait 5 seconds before retrying
delay(5000);

    }
  }
 }

void loop() {
if (!client.connected()) {
reconnect();
}

int h = dht.readHumidity();
int t = dht.readTemperature();
itoa(h, hum, 10);
itoa(t, temp, 10);
Serial.print("Humidity: ");
Serial.println(hum);
Serial.print("Temperature: ");
Serial.println(temp);
delay(1000);
client.loop();
data = String(hum) + ',' + String(temp);
Serial.println(data);
delay(1000);
long now = millis();
if (now - lastMsg> 2000) {
lastMsg = now;
++value;
Serial.print("Publish message: ");
Serial.println("hello, its connected");
client.publish("fromEsp8266", data.c_str());

}
}
