from paho.mqtt.client import *
from proto import message_pb2

print "MQTT CLIENT SCRIPT"


# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#
#     # Subscribing in on_connect() means that if we lose the connection and
#     # reconnect then subscriptions will be renewed.
#     client.subscribe("$SYS/#")
#
# # The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    if msg.topic == "test-topic":
        received_message = message_pb2.DeviceReading()
        print "A message was received from the test-topic"
        received_message.ParseFromString(msg.payload)
        print received_message

    if msg.topic == "online":
        print "LMAO"
        print msg.payload


#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
#
# client.connect("iot.eclipse.org", 1883, 60)
#
# # Blocking call that processes network traffic, dispatches callbacks and
# # handles reconnecting.
# # Other loop*() functions are available that give a threaded interface and a
# # manual interface.
# client.loop_forever()

client = Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")

host = "localhost"

client.connect(host, port=1883, keepalive=60, bind_address="")

client.on_message = on_message
client.loop_start()

client.subscribe("test-topic")
client.subscribe("online")

# -----
message = message_pb2.DeviceReading()
message.sensor_type = "temperature"
message.sensor_reading = 20
message.unit = "c"
message.serial_number = "1"
# -----

client.publish("test-topic", message.SerializeToString())
#client.publish("52:7d:e6:ef:2a:8b/remote_shutdown", "test")
