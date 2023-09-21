import requests
import json
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from time import sleep

devices = ["B448E4","B44037","B44949"] # Liste des capteurs Sigfox
login = "6334446bbdcbd20e4daf92b4" 
password = "3806e9d6cead4f45803df27eee00994a"
authentication = (login, password) # creds pour Sigfox


while True: # toute les 10mins
    
    for device in devices:


        response = requests.get(f"https://backend.sigfox.com/api/v2/devices/{device}/messages",
        auth=authentication) # questionne l'API REST Sigfox

        jsonData = json.loads(response.text) # transforme le Str en JSON
        lastData = jsonData["data"][0] #prend la dernière valeurs


        my_hexdata = lastData['data'] # extrait le payload ( Hexa )


        scale = 16 ## nb caractère

        num_of_bits = len(my_hexdata)*4

        binData = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits) # hexa -> bin 


        """ Parcing payload avec information Sigfox """
        
        batterie = (int(binData[:5],2)* 0.05) + 2.7

        reserved = binData[5:8]
        dataType = binData[8:13]

        flag = binData[13:14]

        dataTmp = (int(binData[14:24],2)-200)/8

        dataHum = int(binData[24:32],2)/2
        

        bucket = "IUT_Devices" # Bucket influxDB
        token = "NZuKx9nuCgkreX6PJ7jd2IdEGNVAosqmxcJUnJi944WTODCL-XJ1WXcAEHcMwmpEbML20G4P60QEr99YiU-xcg==" # Token Bucket


        client = InfluxDBClient(url="http://51.158.110.29:8086", token=token, org="iutbeziers") # Login to Influx
        write_api = client.write_api(write_options=SYNCHRONOUS) # Write mode + synchronise

        t = Point("sensors").tag("device",device).field("temp",dataTmp) # create the influx point
        h = Point("sensors").tag("device",device).field("hum",dataHum) # create the influx point
        v = Point("sensors").tag("device",device).field("vdd",batterie)

        write_api.write(bucket=bucket, record=t) # write
        write_api.write(bucket=bucket, record=h) # write
        write_api.write(bucket=bucket, record=v) # write

        print(f"Data push : tmp = {dataTmp} | hum = {dataHum}")
        client.close() # ferme la connexion client

    

    sleep(60*10) # dors 10mins
