# python3.6

import paho.mqtt.client as mqtt
import ssl
from time import sleep
import json
version = '3' # or '3'
mytransport = 'tcp' # or 'tcp'

ttnToken:str="NNSXS.3BVJF3YWR6MKUSJUGRYSI4K665V3TVYZZD6CK7Y.PTPMIRWO4ORECVZLDRJOIOAU4EXQ4JTVC3QYTDZ7CUBH6YK6BR3Q"


if version == '5':
    client = mqtt.Client(client_id="myPy",
                         transport=mytransport,
                         protocol=mqtt.MQTTv5)
if version == '3':
    client = mqtt.Client(client_id="myPy",
                         transport=mytransport,
                         protocol=mqtt.MQTTv311,
                         clean_session=True)
    

client.username_pw_set('iutbiot51@ttn', password=ttnToken)
client.tls_set(certfile=None,
               keyfile=None,
               # If these arguments above are not None then they will
               # be used as client information for TLS based
               # authentication and authorization (depends on broker setup).
               cert_reqs=ssl.CERT_REQUIRED)
               # this makes it mandatory that the broker
               # has a valid certificate
               
               


broker = "eu1.cloud.thethings.network" # eg. choosen-name-xxxx.cedalo.cloud

myport = 8883
if version == '5':
    from paho.mqtt.properties import Properties
    from paho.mqtt.packettypes import PacketTypes 
    properties=Properties(PacketTypes.CONNECT)
    properties.SessionExpiryInterval=30*60 # in seconds
    client.connect(broker,
                   port=myport,
                   clean_start=mqtt.MQTT_CLEAN_START_FIRST_ONLY,
                   properties=properties,
                   keepalive=60);

if version == '3':
    client.connect(broker,port=myport,keepalive=60);

client.loop_start();


mytopic = "v3/iutbiot51@ttn/devices/+/up"
client.subscribe(mytopic,2);

def on_message(client, userdata, message):
    try:
        print(f"topic : {message.topic}\n")
        print(f"payload :")# {str(message.payload.decode('utf-8'))}\n\n")
        
        #pprint(message.payload.decode('utf-8'))
        
        jsonData = json.loads(message.payload.decode('utf-8'))
        print(jsonData.keys())
        print(jsonData.get('uplink_message').get('decoded_payload'))
    
    except TypeError:
        pass
        
        
listener = mqtt.Client()
listener._send_connect = print(f"listener ttn : trying to connect...") # SIN
listener.on_connect = print(f"listener ttn : Connected on {broker}:{myport}") # SIN ACK
listener.on_message = on_message # exec on_message when a message arrive
listener.subscribe(mytopic) # listen on the topic
listener.loop_start() # listen begin | Use a thread


while True:
    sleep(5000)
