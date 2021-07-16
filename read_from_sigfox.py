# for more information read : https://support.sigfox.com/apidocs#
# import requests module
import requests
from requests.auth import HTTPBasicAuth
from sigfox_config import sigfox_c
import json
import datetime
import cbor2 as cbor
import binascii
from pymongo import MongoClient
import time 

device_id = sigfox_c["device_id"]
Login = sigfox_c["Login"]
Password = sigfox_c["Password"]


    
Device_retreive_a_list_of_message_url = "https://api.sigfox.com/v2/devices/"+device_id+"/messages"
last_epoch = 0
# Get the last message received
query_parameters = {"limit" :1} # the maximum number of items to return integer <int32> 100 by default



def insert_data_to_mongodb(time,temperature):
    # inserting data in MongoDB
    try:
        conn = MongoClient()
        print("Connected successfully!!!")
        # database
        db = conn.lopy
        # Created or Switched to collection names: bme
        collection = db.bme
        data = {
        "temprature":temperature,
        "time":time
        }
        # Insert Data
        rec_id = collection.insert_one(data)
    except:
        print("Could not connect to MongoDB")
    

# Making a get request
response = requests.get(Device_retreive_a_list_of_message_url,
            auth = HTTPBasicAuth(Login, Password),params=query_parameters)


# print request object
if (response != 200):
    exit

response = json.loads(response.text)['data'][0]

s=response["time"]
record_time = datetime.datetime.fromtimestamp(s/ 1000.0).strftime('%Y-%m-%d %H:%M:%S')
print(record_time)

print(cbor.loads(binascii.unhexlify(response["data"])))
temperatures= cbor.loads(binascii.unhexlify(response["data"]))
insert_data_to_mongodb(record_time,temperatures)

# check if we received data from the last time registred
time.sleep(10)


while True:
    if s > 0:
        query_parameters = {"since": s+1}
        response = requests.get(Device_retreive_a_list_of_message_url,
                    auth = HTTPBasicAuth(Login, Password),params=query_parameters)
        # print request object
        if (response != 200):
            exit
        response = json.loads(response.text)['data']
        for v in response:
            if s <response["time"]:
                s = response["time"]
            record_time = datetime.datetime.fromtimestamp(s/ 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            print(record_time)
            print(cbor.loads(binascii.unhexlify(response["data"])))
            temperatures = cbor.loads(binascii.unhexlify(response["data"]))
            # inserting data in MongoDB
            insert_data_to_mongodb(record_time,temperatures)
        time.sleep(60)
