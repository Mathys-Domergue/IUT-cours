import paho.mqtt.client as mqtt
from time import sleep
from rich import print as pprint
import json
import ssl

ttnToken:str="NNSXS.3BVJF3YWR6MKUSJUGRYSI4K665V3TVYZZD6CK7Y.PTPMIRWO4ORECVZLDRJOIOAU4EXQ4JTVC3QYTDZ7CUBH6YK6BR3Q"


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
    #influx.infoPush(message.topic,str(message.payload.decode("utf-8")))


brokerIp = "eu1.cloud.thethings.network" # Need to be a String
brokerPort = 8883    # Need to be a Int



topic = "v3/iutbiot51@ttn/devices/+/up"


listener = mqtt.Client()
listener.connect(brokerIp,brokerPort,60)
listener._send_connect = print(f"listener ttn : trying to connect...") # SIN
listener.on_connect = print(f"listener ttn : Connected on {brokerIp}:{brokerPort}") # SIN ACK
listener.on_message = on_message # exec on_message when a message arrive
listener.subscribe(topic) # listen on the topic
listener.loop_start() # listen begin | Use a thread


while True:
    sleep(5000)